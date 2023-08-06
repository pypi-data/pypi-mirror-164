# coding=utf-8
""" Contains objects related to workspaces.

Classes in the workspace file help manage the folders
where the application inputs and outputs are located.
They also help abstract the gis processing library
(arcpy) from the application processing logic.
"""

# import logging

from copy import deepcopy
from os import path
from sqlalchemy import create_engine, Table as AlchemyTable, Column, MetaData, Integer
from sqlalchemy.engine.reflection import Inspector

from src.oogeo.functions.constants import METADATA_TABLES
from src.oogeo.functions.conversions import upgrade_shapely_geometry
from src.oogeo.functions.database import create_in_clause
from src.oogeo.objects.layer import Layer
from src.oogeo.objects.table import Table
from geoalchemy2 import Geometry, WKTElement


def create_database_functions(workspace):
    """ Creates required functions in the specified workspace.

    :param workspace: The workspace object connected to the database where the functions will be created.
    :return: None
    """

    sql = "CREATE OR REPLACE FUNCTION shares_a_segment(analysis_geometry geometry, edge_buffer_geometry geometry) " \
          "RETURNS boolean AS $$ " \
          "DECLARE " \
          "shares_a_segment boolean := FALSE; " \
          "point RECORD; " \
          "last_point RECORD; " \
          "line_segment geometry; " \
          "point_cursor CURSOR(analysis_geometry geometry) FOR SELECT temp_table.geom FROM (SELECT (ST_Dump(ST_Points(analysis_geometry))).geom AS geom) AS temp_table; " \
          "BEGIN " \
          "IF ST_Disjoint(analysis_geometry, edge_buffer_geometry) THEN " \
          "RETURN FALSE; " \
          "END IF; " \
          "OPEN point_cursor(analysis_geometry); " \
          "LOOP " \
          "FETCH point_cursor INTO point; " \
          "EXIT WHEN NOT FOUND; " \
          "IF last_point IS NULL THEN " \
          "last_point := point; " \
          "CONTINUE; " \
          "END IF; " \
          "line_segment := ST_MakeLine(last_point.geom, point.geom); " \
          "IF ST_Within(line_segment, edge_buffer_geometry) THEN " \
          "shares_a_segment := TRUE; " \
          "EXIT; " \
          "END IF; " \
          "last_point := point; " \
          "END LOOP; " \
          "CLOSE point_cursor; " \
          "RETURN shares_a_segment; " \
          "END; $$ " \
          "LANGUAGE PLPGSQL;"
    workspace.execute_simple_sql(sql, use_transaction=False)


class Workspace(object):
    """ Controls the workspace used by the application

    The workspace class tracks the input and output directories
    used by the application.
    """

    def __init__(self, connection_info, schema='public'):
        """ Initializes the workspace object.

        """
        assert connection_info, 'A database connection must be specified.'
        assert 'user' in connection_info, 'A database username must be specified.'
        assert 'password' in connection_info, 'A database password must be specified.'
        assert 'host' in connection_info, 'A database host must be specified (use "localhost" for local geodatabases).'
        assert 'port' in connection_info, 'A database port must be specified (default is 5432).'
        self.alchemy_engine = None
        self.connection_info = deepcopy(connection_info)
        self.connect()

        self.database_name = connection_info['database'] if 'database' in connection_info else None
        self.pandas_connection = None
        self.is_gdb = True
        self.schema = schema

    def open_pandas_connection(self):
        """

        :return:
        """
        self.connect()
        self.pandas_connection = self.alchemy_engine

    def close_pandas_connection(self):
        """

        :return:
        """
        if self.pandas_connection is None:
            return
        self.pandas_connection = None

    def delete_feature_classes(self, feature_classes, schema=None):
        """ Deletes feature classes in the geodatabase without requiring a `Layer()` object.

        :param feature_classes: The list of feature classes to be deleted.
        :return: None
        """

        if isinstance(feature_classes, str):
            feature_classes = [feature_classes]

        if not schema:
            schema = self.schema
        for feature_class in feature_classes:
            self.execute_simple_sql(f'DROP TABLE IF EXISTS "{schema}"."{feature_class}"', use_transaction=False)
            self.execute_simple_sql(f'DROP SEQUENCE IF EXISTS "{schema}"."{feature_class}_seq"', use_transaction=False)
            self.execute_simple_sql(f'DROP FUNCTION IF EXISTS "{schema}"."edge_buffers_{feature_class}"', use_transaction=False)

    def import_shapefile(self, shapefile_path, layer_name,
        projection=None, schema=None):
        """ Imports the specified shapefile into the geodatabase as the specified layer name

        :param shapefile_path: The fully-qualified path to the shapefile to be imported.
        :param layer_name: The name of the layer in the geodatabase.
        :param projection: If a WKID is provided, the shapefile will be projected into the
            specified projection before importing.
        :return: A new `Layer()` object representing the new layer in the geodatabase.
        """

        try:
            import geopandas
        except Exception as e:
            raise ValueError('Geopandas is not installed')

        assert self.is_gdb, 'Shapefiles can only be imported into geodatabase workspaces.'
        assert path.isfile(shapefile_path), 'A shapefile must be specified.'

        # logging.info('Importing layer %s from %s', layer_name, shapefile_path)

        # load the shapefile and get it's projection
        # logging.info('Loading the shapefile into geopandas')
        shapefile_gdf = geopandas.read_file(shapefile_path)
        epsg = int(shapefile_gdf.crs.to_epsg())

        # project the shapefile if necessary
        if projection and projection != epsg:
            shapefile_gdf.to_crs(epsg=projection)
            epsg = projection

        if not schema:
            schema = self.schema

        # upgrade geometries to multis
        shapefile_gdf.geometry = shapefile_gdf.geometry.apply(upgrade_shapely_geometry)

        # get the layer's geometry type
        geometry_type = shapefile_gdf.geometry.geom_type[0].upper()

        # translate the geometries to geoalchemy (makes them storable in the db)
        if epsg == 102718:
            epsg = 2263
        shapefile_gdf['geom'] = shapefile_gdf.geometry.apply(lambda x: WKTElement(x.wkt, srid=epsg))
        shapefile_gdf.drop(shapefile_gdf.geometry.name, 1, inplace=True)

        # save the file into the geodatabase
        shapefile_gdf.to_sql(layer_name, self.alchemy_engine, if_exists='fail', index_label='id', schema=schema,
            dtype={'geom': Geometry(geometry_type, srid=epsg)})

        # set the object id as the primary key
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{layer_name}" ADD PRIMARY KEY ("id");', use_transaction=False)

        # create a sequence for the table
        self.create_sequence(layer_name, 'id', schema=schema)

        return Layer(layer_name, self)

    def create_sequence(self, table_name, oid_field, schema=None):
        """

        :param table_name:
        :param oid_field:
        :return:
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        # get the highest oid value and use it to create a sequence for the table
        result = self.execute_simple_sql(f'SELECT MAX("{oid_field}") as max_oid FROM "{schema}"."{table_name}"')
        row = next(result)
        start_oid = int(row['max_oid']) + 1 if row is not None and row['max_oid'] is not None else 1
        sequence_name = f'"{schema}"."{table_name}_{oid_field}_seq"'
        sql = f'CREATE SEQUENCE IF NOT EXISTS {sequence_name} START WITH {start_oid}'
        self.execute_simple_sql(sql)
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{table_name}" ALTER COLUMN "{oid_field}" SET DEFAULT nextval(\'{sequence_name}\');', use_transaction=False)
        self.execute_simple_sql(f'ALTER SEQUENCE {sequence_name} OWNED BY "{schema}"."{table_name}"."{oid_field}"', use_transaction=False)

        return sequence_name

    def list_feature_classes(self, wildcards=None, feature_type='All', schema=None):
        """ Lists the feature classes in the workspace, limited by name and feature type.

        :param wildcards: String filter on the results returned. If no wildcard is specified, all values are returned.
        :param feature_type: Feature type to be returned. Valid options are: Annotation, Arc, Dimension, Edge,
            Junction, Label, Line, Multipatch, Node, Point, Polygon, Polyline, Region, Route, Tic, All (default).
        :return: If input_path is a geodatabase, a list of feature class names; if shapefiles, a list of file paths.
        """

        # validate wildcards param
        if not wildcards:
            wildcards = []
        if isinstance(wildcards, str):
            wildcards = [wildcards]

        # set the proper schema
        if not schema:
            schema = self.schema


        # create basic where clause
        where_clause = f"WHERE f_table_schema = '{schema}'"
        # set up wildcard search if necessary
        for wildcard in wildcards:
            wildcard = wildcard.replace('*', '%%')
            where_clause = f"{where_clause} AND f_table_name LIKE '{wildcard}'"

        with self.alchemy_engine.connect() as connection:
            sql = f'SELECT DISTINCT f_table_name FROM geometry_columns {where_clause};'
            # logging.debug('List feature classes sql: %s', sql)
            table_names = connection.execute(sql)
        return [row['f_table_name'] for row in table_names]

    def list_tables(self, wildcards=None, schema=None):
        """ Lists the tables in the workspace, limited by name and table type.

        :param wildcard: String filter on the results returned. If no wildcard is specified, all values are returned.
        :param table_type: Feature type to be returned. Valid options are: dBASE, INFO, All (default).
        :return: A list of table names.
        """
        # validate wildcards param
        if not wildcards:
            wildcards = []
        if isinstance(wildcards, str):
            wildcards = [wildcards]

        # set the proper schema
        if not schema:
            schema = self.schema

        # create basic where clause
        not_in_clause = create_in_clause(METADATA_TABLES, use_quotes=True, field_name='tablename', not_operator=True)
        where_clause = f"WHERE schemaname = '{schema}' AND {not_in_clause}"
        # set up wildcard search if necessary
        for wildcard in wildcards:
            wildcard = wildcard.replace('*', '%%')
            where_clause = f"{where_clause} AND tablename LIKE '{wildcard}'"

        with self.alchemy_engine.connect() as connection:
            sql = "SELECT DISTINCT tablename FROM pg_catalog.pg_tables {};".format(where_clause)
            table_name_results = connection.execute(sql)

        table_names = [row['tablename'] for row in table_name_results]
        feature_classes = self.list_feature_classes(schema=schema)
        return [row for row in filter(lambda x: x not in feature_classes, table_names)]

    def load(self, table, schema=None):
        """

        """
        if table in self.list_tables(schema=schema):
            return Table(table, self, schema=schema)
        if table in self.list_feature_classes(schema=schema):
            return Layer(table, self, schema=schema)
        raise ValueError('Could not load specified table.')

    def list_tables_and_layers(self, schema=None):
        """ List both the tables and layers in a geodatabase.

        """
        # set the proper schema
        if not schema:
            schema = self.schema

        input_features = self.list_feature_classes(schema=schema)
        input_tables = self.list_tables(schema=schema)
        return input_features + input_tables

    def create_spatial_index(self, feature_class_name, shape_field_name, schema=None):
        """ Creates a spatial index on the specified shape field.

        :param feature_class_name: The name of the feature class to be altered.
        :param shape_field_name: The name of the shape field to be indexed.
        :return: None
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        spatial_index_name = f'idx_{feature_class_name}_{shape_field_name}'
        self.execute_simple_sql(f'DROP INDEX IF EXISTS "{schema}"."{spatial_index_name}";')
        self.execute_simple_sql(f'CREATE INDEX "{spatial_index_name}" ON "{schema}"."{feature_class_name}" USING GIST ("{shape_field_name}");', use_transaction=False)

    def create_index(self, table_name, field_name, schema=None):
        """ Creates an index on a field

        :param table_name: The name of the table to be modified.
        :param field_name: The name of the field to be indexed.
        :return: None
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        index_name = 'idx_{0}_{1}'.format(table_name, field_name)
        self.execute_simple_sql(f'CREATE INDEX IF NOT EXISTS "{index_name}" ON "{schema}".{table_name} ("{field_name}");', use_transaction=False)

    def list_indexes(self, table_name, schema=None):
        """ Lists the names of the indexes on the specified table

        :param table_name: The name of the table to be analyzed.
        :return: A list of index names assofiated with the table.
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        with self.alchemy_engine.connect() as connection:
            index_names = connection.execute(
                f"SELECT indexname FROM pg_indexes WHERE schemaname = '{schema}' AND tablename = '{table_name}';")
        return [row['indexname'] for row in index_names]

    def create_geometry_column(self, table_name, field_name, field_type, spatial_reference=2263, schema=None, three_d=False):
        """ Adds a geometry column to the specified table.

        """
        # standardize geometry type
        geometry_type = field_type.upper()
        if geometry_type == 'POLYGON':
            geometry_type = 'MULTIPOLYGON'
        elif geometry_type == 'POLYLINE' or geometry_type == 'LINESTRING':
            geometry_type = 'MULTILINESTRING'

        # set the proper schema
        if not schema:
            schema = self.schema

        # set 2D/3D
        dimensions = '2' if not three_d else '3'

        # create the geometry column
        self.execute_simple_sql(
            f"SELECT AddGeometryColumn('{schema}', '{table_name}', '{field_name}', {spatial_reference}, '{geometry_type}', {dimensions});", use_transaction=False)

    def has_geometry_search_column(self, feature_class_name, schema=None):
        """ Indicates if a feature class has an 'edge_buffers' column (used for querying edges).

        :param feature_class_name: The name of the feature class to be analyzed.
        :return: True if the table has a geometry search column, otherwise False.
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        with self.alchemy_engine.connect() as connection:
            column_infos = connection.execute(
                f"SELECT f_geometry_column as name, type, srid FROM geometry_columns WHERE f_table_schema = '{schema}' AND f_table_name = '{feature_class_name}' AND LOWER(f_geometry_column) = 'edge_buffers';")
            if column_infos.rowcount > 0:
                return True
        return False

    def drop_geometry_search_column(self, feature_class_name, schema=None):
        """

        :param feature_class_name:
        :return:
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        # do not create if column already exists
        if not self.has_geometry_search_column(feature_class_name, schema=schema):
            return

        # drop column if it exists
        trigger_name = 'edge_buffers_{}'.format(feature_class_name)
        ucase_trigger_name = 'EDGE_BUFFERS_{}'.format(feature_class_name)

        # drop the trigger itself
        self.execute_simple_sql(f'DROP TRIGGER IF EXISTS "{trigger_name}" ON "{schema}"."{feature_class_name}"', use_transaction=False)
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "edge_buffers"')

        self.execute_simple_sql(f'DROP TRIGGER IF EXISTS "{ucase_trigger_name}" ON "{schema}"."{feature_class_name}"', use_transaction=False)
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "EDGE_BUFFERS"')

    def create_geometry_search_column(self, feature_class_name, geometry_type, shape_field_name, spatial_reference=2263, schema=None):
        """ Creates an 'edge_buffers' column on a feature class (used for querying edges).

        :param feature_class_name: The feature class to be modified.
        :return: None
        """
        # standardize geometry type
        geometry_type = geometry_type.upper()
        if geometry_type == 'POLYGON':
            geometry_type = 'MULTIPOLYGON'
        elif geometry_type == 'POLYLINE' or geometry_type == 'LINESTRING':
            geometry_type = 'MULTILINESTRING'

        # do not create search columns on point layers
        if geometry_type == 'POINT':
            return

        # set the proper schema
        if not schema:
            schema = self.schema

        # do not create if column already exists
        if self.has_geometry_search_column(feature_class_name, schema=schema):
            return

        # drop column if it exists
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "edge_buffers"')

        # create the edge_buffers geometry column
        self.create_geometry_column(feature_class_name, 'edge_buffers', 'MULTIPOLYGON', spatial_reference, schema=schema)

        # populate the edge_buffers column for existing rows
        spatial_sql = 'ST_Boundary("{}")'.format(shape_field_name) if geometry_type == 'MULTIPOLYGON' else '"{}"'.format(shape_field_name)
        spatial_sql = 'ST_Multi(ST_Buffer({}, 0.001, \'endcap=square join=mitre\'))'.format(spatial_sql)
        self.execute_simple_sql(f'UPDATE "{schema}"."{feature_class_name}" SET "edge_buffers" = {spatial_sql}')

        # add a spatial index to the column
        self.create_spatial_index(feature_class_name, 'edge_buffers', schema=schema)

        # create the trigger function to populate the edge buffers column
        trigger_name = 'edge_buffers_{}'.format(feature_class_name)
        if geometry_type == 'MULTILINESTRING':
            self.execute_simple_sql('CREATE OR REPLACE FUNCTION "{schema}"."{trigger_name}"() RETURNS trigger AS ${trigger_name}$ '
                                    'BEGIN '
                                    'NEW."edge_buffers" := ST_Multi(ST_Buffer(NEW."{shape_field_name}", 0.001, \'endcap=square join=mitre\')); '
                                    'RETURN NEW; '
                                    'END; ${trigger_name}$ LANGUAGE plpgsql;'.format(trigger_name=trigger_name, shape_field_name=shape_field_name, schema=schema), use_transaction=False)

        if geometry_type == 'MULTIPOLYGON':
            self.execute_simple_sql('CREATE OR REPLACE FUNCTION "{schema}"."{trigger_name}"() RETURNS trigger AS ${trigger_name}$ '
                                    'BEGIN '
                                    'NEW."edge_buffers" := ST_Multi(ST_Buffer(ST_Boundary(NEW."{shape_field_name}"), 0.001, \'endcap=square join=mitre\')); '
                                    'RETURN NEW; '
                                    'END; ${trigger_name}$ LANGUAGE plpgsql;'.format(trigger_name=trigger_name, shape_field_name=shape_field_name, schema=schema), use_transaction=False)

        # create the trigger itself
        self.execute_simple_sql('CREATE TRIGGER "{trigger_name}" BEFORE INSERT OR UPDATE ON "{schema}"."{feature_class_name}" '
                                'FOR EACH ROW EXECUTE PROCEDURE {schema}.{trigger_name}();'.format(trigger_name=trigger_name, feature_class_name=feature_class_name, schema=schema), use_transaction=False)

    def has_centroid_column(self, feature_class_name, schema=None):
        """ Indicates if a feature class has an 'centroid' column (used for querying).

        :param feature_class_name: The name of the feature class to be analyzed.
        :return: True if the table has a centroid column, otherwise False.
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        with self.alchemy_engine.connect() as connection:
            column_infos = connection.execute(
                "SELECT f_geometry_column as name, type, srid FROM public.geometry_columns "
                "WHERE f_table_schema = '{}' AND f_table_name = '{}' AND LOWER(f_geometry_column) = 'centroid';".format(schema, feature_class_name))
            if column_infos.rowcount > 0:
                return True
        return False

    def drop_centroid_column(self, feature_class_name, schema=None):
        """

        :param feature_class_name:
        :return:
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        # do not create if column already exists
        if not self.has_centroid_column(feature_class_name, schema=schema):
            return

        # drop column if it exists
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "centroid"')
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "CENTROID"')

    def create_centroid_columm(self, feature_class_name, shape_field_name, spatial_reference=2263, inside=False, schema=None):
        """

        :param feature_class_name:
        :param shape_field_name:
        :param spatial_reference:
        :return:
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        # do not create if column already exists
        create = not self.has_centroid_column(feature_class_name, schema=schema)
        if create:
            # create the centroid geometry column
            self.create_geometry_column(feature_class_name, 'centroid', 'POINT', spatial_reference, schema=schema)

        # populate the centroid column for existing rows
        if not inside:
            spatial_sql = f'ST_Centroid("{shape_field_name}")'
        else:
            spatial_sql = f'ST_PointOnSurface("{shape_field_name}")'
        self.execute_simple_sql(f'UPDATE "{schema}"."{feature_class_name}" SET "centroid" = {spatial_sql}')

        # create an index on the centroid column
        if create:
            self.create_spatial_index(feature_class_name, 'centroid', schema=schema)
        else:
            self.vacuum(feature_class_name, schema=schema)


    def has_midpoint_column(self, feature_class_name, schema=None):
        """ Indicates if a feature class has an 'midpoint' column (used for querying).

        :param feature_class_name: The name of the feature class to be analyzed.
        :return: True if the table has a midpoint column, otherwise False.
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        with self.alchemy_engine.connect() as connection:
            column_infos = connection.execute(
                "SELECT f_geometry_column as name, type, srid FROM public.geometry_columns "
                "WHERE f_table_schema = '{}' AND f_table_name = '{}' AND LOWER(f_geometry_column) = 'midpoint';".format(schema, feature_class_name))
            if column_infos.rowcount > 0:
                return True
        return False

    def drop_midpoint_column(self, feature_class_name, schema=None):
        """ Drops the `midpoint` column from the specified feature class.

        :param feature_class_name: The name of the feature class to be altered.
        :return: None
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        # do not create if column already exists
        if not self.has_midpoint_column(feature_class_name, schema=schema):
            return

        # drop column if it exists
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "midpoint"')
        self.execute_simple_sql(f'ALTER TABLE "{schema}"."{feature_class_name}" DROP COLUMN IF EXISTS "MIDPOINT"')

    def create_midpoint_columm(self, feature_class_name, shape_field_name, spatial_reference=2263, schema=None):
        """

        :param feature_class_name:
        :param shape_field_name:
        :param spatial_reference:
        :return:
        """

        # set the proper schema
        if not schema:
            schema = self.schema

        # do not create if column already exists
        if self.has_midpoint_column(feature_class_name, schema=schema):
            return

        # create the midpoint geometry column
        self.create_geometry_column(feature_class_name, 'midpoint', 'POINT', spatial_reference, schema=schema)

        # populate the midpoint column for existing rows
        spatial_sql = f'ST_LineInterpolatePoint(ST_LineMerge("{shape_field_name}"), 0.5)'
        self.execute_simple_sql(f'UPDATE "{schema}"."{feature_class_name}" SET "midpoint" = {spatial_sql}')

        # create a spatial index on the midpoint column
        self.create_spatial_index(feature_class_name, 'midpoint', schema=schema)

    def unlog_table(self, table_name, schema=None):
        """ Sets a table to be "unlogged", which will make the table perform faster, but data
        will not be recoverable is the database crashes.

        :param table_name: The name of the table to be set to "unlogged".
        :return: None
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        sql = f'ALTER TABLE "{schema}"."{table_name}" SET UNLOGGED;'
        self.execute_simple_sql(sql, use_transaction=False)

    def vacuum(self, table_name=None, analyze=True, schema=None):
        """ Cleans up any data files produced by the table. Can be used to manage hard-drive space when
        doing large update operations.

        :param table_name: The table to be vacuumed.
        :param analyze: If True, the `ANALYZE` command will also be issues to reanalyze the statistics
            for the table or database.
        :return: None
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        if table_name:
            if analyze:
                sql = f'VACUUM ANALYZE "{schema}"."{table_name}";'
            else:
                sql = f'VACUUM "{schema}"."{table_name}";'
        else:
            if analyze:
                sql = 'VACUUM ANALYZE;'
            else:
                sql = 'VACUUM;'
        self.execute_simple_sql(sql, use_transaction=False)

    def create_feature_class(self, feature_class_name, geometry_type, spatial_reference=2263, schema=None):
        """ Creates a new feature class in the workspace.

        :param feature_class_name: The name of the feature class to be created.
        :param geometry_type: The geometry type of the feature class. Valid values are:
            "POINT", "MULTIPOINT", "POLYGON", and "POLYLINE"
        :param spatial_reference: The WKID of the spatial reference for the new feature class. The default
            is 2263 (New York State Plane)
        :return: A `Layer` object representing the new feature class.
        """
        geometry_type = geometry_type.upper()
        if geometry_type == 'POLYGON':
            geometry_type = 'MULTIPOLYGON'
        elif geometry_type == 'POLYLINE' or geometry_type == 'LINESTRING':
            geometry_type = 'MULTILINESTRING'

        # set the proper schema
        if not schema:
            schema = self.schema
        self.create_schema(schema)

        alchemy_table = AlchemyTable(feature_class_name, MetaData(),
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('geom', Geometry(geometry_type, srid=spatial_reference)),
                                    schema=schema
        )

        alchemy_table.create(self.alchemy_engine)

        # add spatial index
        self.create_spatial_index(feature_class_name, 'geom', schema=schema)

        return Layer(alchemy_table, self, schema=schema)

    def create_table(self, table_name, schema=None):
        """ Creates a new table in the geodatabase.

        :param table_name: The name of the new table
        :return: A `Table()` object representing the new table.
        """
        # set the proper schema
        if not schema:
            schema = self.schema
        self.create_schema(schema)

        # create a new table with a primary key
        alchemy_table = AlchemyTable(table_name, MetaData(),
            Column('id', Integer, primary_key=True, autoincrement=True),
                                     schema=schema
        )
        alchemy_table.create(self.alchemy_engine)

        return Table(alchemy_table, self, schema=schema)

    def create_view(self, view_name, view_query, schema=None):
        """ Creates a view based on the specified sql query.

        :param view_name: The name to be given to the view.
        :param view_query: The SQL `SELECT` statement to be used to create the view.
        """
        # set the proper schema
        if not schema:
            schema = self.schema
        self.create_schema(schema)

        sql = f'CREATE OR REPLACE VIEW "{schema}"."{view_name}" AS {view_query};'
        # logging.debug('Create view sql: {}'.format(sql))
        self.execute_simple_sql(sql)

        sql = f'ALTER TABLE "{schema}"."{view_name}" OWNER TO postgres;'
        self.execute_simple_sql(sql)

    def drop_view(self, view_name, schema=None, cascade=False):
        """ Drops a view if it exists in the database.

        :param view_name: The name of the view to drop.
        :param cascade: If `True` a cascading drop will be performed.
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        sql = f'DROP VIEW IF EXISTS "{schema}"."{view_name}"'
        if cascade:
            sql = f'{sql} CASCADE'
        sql = f'{sql};'
        # logging.debug('Drop view sql: {}'.format(sql))
        self.execute_simple_sql(sql)

    def drop_table(self, table_name, schema=None, cascade=False):
        """

        :param table_name:
        :param cascade: If `True` a cascading drop will be performed.
        :return:
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        if self.has_geometry_search_column(table_name, schema=schema):
            self.drop_geometry_search_column(table_name, schema=schema)
        sql = f'DROP TABLE IF EXISTS "{schema}"."{table_name}"'
        if cascade:
            sql = f'{sql} CASCADE'
        sql = f'{sql};'

        self.execute_simple_sql(sql)

    def has_schema(self, schema):
        """ Indicates if the database has the specified schema.

        :param schema: The name of the schema to be checked.
        :return: `True` if the specified schema exists, else `False`.
        """
        sql = f"SELECT COUNT(*) AS \"count\" FROM information_schema.schemata WHERE schema_name = '{schema}';"
        scalar = self.execute_simple_sql(sql, use_transaction=False)
        row = next(scalar)
        return True if int(row['count']) > 0 else False

    def list_schemas(self, include_hidden=False):
        """ List the names of the schemas in the workspace.

        :param include_hidden: If `True`, the list will include schemas usually hidden from view, such as
            "pg_catalog" and "information_schema".
        :return: A list of schema names currently in the workspace.
        """
        sql = "SELECT schema_name FROM information_schema.schemata"
        if not include_hidden:
            sql = f"{sql} WHERE schema_name NOT IN ('pg_toast', 'pg_catalog', 'information_schema')"
        with self.alchemy_engine.connect() as connection:
            schema_names = connection.execute(sql)
        return [row['schema_name'] for row in schema_names]


    def create_schema(self, schema):
        """ Creates a new schema in the workspace.

        :param schema: The schema name to be created.
        :return: A `Workspace` object with the default schema set to the new schema name.
        """
        sql = f'CREATE SCHEMA IF NOT EXISTS {schema};'
        self.execute_simple_sql(sql, use_transaction=False)
        return Workspace(self.connection_info, schema=schema)

    def drop_schema(self, schema, cascade=False):
        """ Drops the specified schema.

        :param schema: The schema name to be dropped.
        :param cascade: If `True` a cascading drop will be performed.
        :return: None.
        """
        sql = f'DROP SCHEMA IF EXISTS {schema}'
        if cascade:
            sql = f'{sql} CASCADE'
        sql = f'{sql};'
        self.execute_simple_sql(sql, use_transaction=False)

    def get_geometry_columns(self, table_name, include_hidden=False, schema=None):
        """ Finds the geometry column for the specified table.

        :param table_name: The table to find.
        :param include_hidden: If true, columns that are otherwise hidden such as edge_buffers, midpoint, and centroid
            will be included in the results.
        :return: A dict representing the attributes of the geometry column ('name', 'type', and 'srid') or None
            if the table does not have a geometry column.
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        # find the name of the table's geometry column
        with self.alchemy_engine.connect() as connection:
            sql = "SELECT f_geometry_column as name, type, srid FROM public.geometry_columns " \
                  "WHERE f_table_schema = '{}' AND f_table_name = '{}'".format(schema, table_name)
            if not include_hidden:
                sql = '{} {}'.format(sql, "AND LOWER(f_geometry_column) NOT IN ('edge_buffers', 'centroid', 'midpoint')")
            sql = f'{sql};'

            column_infos = connection.execute(sql)
            if column_infos.rowcount == 0:
                return None

            return [info for info in column_infos]

    def get_oid_column(self, table_name, schema=None):
        """

        :param table_name:
        :return:
        """
        # set the proper schema
        if not schema:
            schema = self.schema

        inspector = Inspector(self.alchemy_engine)
        primary_keys = inspector.get_pk_constraint(table_name, schema=schema)
        return primary_keys['constrained_columns'][0]

    def connect(self):
        """ Opens the SqlAlchemy connection to the geodatabase.

        :return: None
        """
        if self.alchemy_engine is not None:
            return
        connection_string = f"postgresql://{self.connection_info['user']}:{self.connection_info['password']}@{self.connection_info['host']}:{self.connection_info['port']}"
        if 'database' in self.connection_info and self.connection_info['database'] is not None:
            connection_string = f"{connection_string}/{self.connection_info['database']}"
        self.alchemy_engine = create_engine(connection_string)

    def disconnect(self):
        """ Closes the SqlAlchemy connection to the geodatabase.

        :return: None
        """
        if self.alchemy_engine is None:
            return
        self.alchemy_engine.dispose()
        self.alchemy_engine = None

    def list_databases(self):
        """ Returns a list of databases in the PostGIS instance.

        :return: A list of databases in the PostGIS instance.
        """
        with self.alchemy_engine.connect() as connection:
            database_names = connection.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname NOT IN ('template0', 'template1');")
        return [row['datname'] for row in database_names]

    def execute_simple_sql(self, query_string, use_transaction=True):
        """ Executes a simple SQL statement and returns the results.

        :param query_string: The SQL statement to execute.
        :param use_transaction: If True the execution of the statement will be wrapped in a transaction. If
            False the statement will be executed outside of a transaction (required when altering the database
            schema).
        :return: The results of the database query.
        """
        if use_transaction:
            with self.alchemy_engine.connect() as connection:
                return connection.execute(query_string)

        # to execute without a transaction, get an open connection and
        # commit the current transaction before executing the actual sql statement
        connection = self.alchemy_engine.connect()
        connection.execute('COMMIT;')
        results = connection.execute(query_string)
        connection.close()
        return results

    @staticmethod
    def create_geodatabase(connection_info, database_name):
        """ Creates a file geodatabase, if it doesn't exist.

        :param file_path: File path to the folder that will contain the geodatabase.
        :param database_name: File name of the geodatabase (should end with .gdb).
        :return: A workspace object that is connected to the new geodatabase.
        """
        # logging.info('Creating geodatabase %s', database_name)
        connection_info = {
            'host': connection_info['host'],
            'port': connection_info['port'],
            'user': connection_info['user'],
            'password': connection_info['password']
        }
        workspace = Workspace(connection_info)
        sql = "CREATE DATABASE {} WITH  OWNER = postgres ENCODING = 'UTF8' " \
                           "TABLESPACE = pg_default CONNECTION LIMIT = -1;".format(database_name)
        workspace.execute_simple_sql(sql, use_transaction=False)
        workspace.disconnect()
        new_connection_info = connection_info.copy()
        new_connection_info['database'] = database_name
        new_workspace = Workspace(new_connection_info)
        new_workspace.execute_simple_sql('CREATE EXTENSION IF NOT EXISTS postgis', use_transaction=False)
        new_workspace.execute_simple_sql('CREATE EXTENSION IF NOT EXISTS dblink', use_transaction=False)
        create_database_functions(new_workspace)
        return new_workspace

    @staticmethod
    def drop_geodatabase(connection_info, database_name):
        """ Drops the specified database from the host server.

        :param connection_info: A dictionary containing database connection settings.
        :param database_name: The name of the database to be dropped.
        :return: None.
        """
        connection_info = {
            'host': connection_info['host'],
            'port': connection_info['port'],
            'user': connection_info['user'],
            'password': connection_info['password']
        }
        workspace = Workspace(connection_info)
        workspace.execute_simple_sql("DROP DATABASE IF EXISTS {}".format(database_name), use_transaction=False)
