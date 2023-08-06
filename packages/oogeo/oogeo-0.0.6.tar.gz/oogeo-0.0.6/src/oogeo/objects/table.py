# coding=utf-8
""" Contains objects related to tables.

Classes in the table file help manage the tables
that are used by the application.
"""

# import logging
import re
from abc import ABC as abstract_base
from geoalchemy2 import Geometry
from sqlalchemy import Table as AlchemyTable, Column, MetaData
from src.oogeo.objects.cursor import SearchCursor, InsertCursor, UpdateCursor
from src.oogeo.objects.selectionset import SelectionSet
from src.oogeo.functions.database import build_query_string, build_update_clause, create_insert_row
from src.oogeo.functions.conversions import parse_expression


def load_alchemy_table(workspace, table_name, schema=None):
    """

    :param workspace:
    :param table_name:
    :return:
    """
    # set proper schema
    if not schema:
        schema = workspace.schema

    # reload the alchemy table to include the new field
    geometry_columns = workspace.get_geometry_columns(table_name, schema=schema)
    if geometry_columns:
        columns = [Column(geometry_column['name'], Geometry(geometry_column['type'], srid=geometry_column['srid'])) for geometry_column in geometry_columns]

        return AlchemyTable(table_name, MetaData(), *columns,
            autoload=True, autoload_with=workspace.alchemy_engine, schema=schema)
    else:
        return AlchemyTable(table_name, MetaData(), autoload=True, autoload_with=workspace.alchemy_engine, schema=schema)


class TableBase(abstract_base):
    """ Abstract baseclass for supporting table objects.

    The `TableBase` class should never be initialized directly, but should be accessed through its inheritors,
    the `Table` class and the `Layer` class. The `Table` class acts as an initializer to properly initialize tables
    in ArcPy. The `Layer` class will initialize a layer instance in ArcPy, and also extends the basic table
    functionality with additional methods specific to layer manipulation.

    """

    def __init__(self, table, workspace, schema=None):
        """ Initializes the table base object.

        :param table_name: The name of the table as it is stored in SQLite.
        :param workspace: The workspace where the table is located.
        """
        self.alchemy_table = table if isinstance(table, AlchemyTable) else load_alchemy_table(workspace, table, schema=schema)
        self.table_name = self.alchemy_table.name
        self.schema = self.alchemy_table.schema
        self.deleted = False
        self._cached_oid_field = None
        self.workspace = workspace
        self._selections = []
        self._cached_query_string = None
        self._cached_update_clause = None


    def __enter__(self):
        """ Initialized the table if necessary and returns a reference to itself.

        :return: self
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Cleans up table files when exiting a `with` statement.

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.delete()

    # SELECTION METHODS
    def select_layer_by_attribute(self, query_string, selection_type='NEW_SELECTION'):
        """ Creates a selection set in the table based on an attribute query.

        This method selects records in the table based on the query string provided.
        The query string is in the form of an SQL WHERE clause.

        :param selection_type: Indicates how results from the query should be handled
        by the selection set. Options are:
            NEW_SELECTION - The resulting selection replaces the current selection. This is the default.
            ADD_TO_SELECTION - The resulting selection is added to the current selection if one exists. If no selection
                exists, this is the same as the new selection option.
            REMOVE_FROM_SELECTION - The resulting selection is removed from the current selection. If no selection
                exists, this option has no effect.
            SUBSET_SELECTION - The resulting selection is combined with the current selection. Only records that are
                common to both remain selected.
            SWITCH_SELECTION - Switches the selection. All records that were selected are removed from the current
                selection; all records that were not selected are added to the current selection. The expression
                parameter is ignored when this option is specified.
            CLEAR_SELECTION - Clears or removes any selection. The expression parameter is ignored when this option is
                specified.
        :param query_string: An SQL expression used to select a subset of records.
        """
        # if an int is provided as a query string, assume it's to query the oid
        if isinstance(query_string, int):
            query_string = '"{}" = {}'.format(self.oid, query_string)

        # bust the currently cached query string
        self._cached_query_string = None
        self._cached_update_clause = None

        # clear the selections list if this is a new query
        if selection_type == 'NEW_SELECTION':
            self.clear_selection()

        # wrap field names in parens
        query_string = ' {}'.format(query_string)
        for field_name in self.field_names:
            query_string = re.sub(' {} '.format(field_name), ' "{}" '.format(field_name), query_string)
        query_string = query_string.strip()

        # add selection to list
        self._selections.append({
            'selection_type': selection_type,
            'query': query_string,
            'update_clause': query_string,
            'overlap_type': 'ATTRIBUTE',
            'from_tables': [f'"{self.schema}"."{self.table_name}"'],
            'search_objects': []
        })

    def get_selection_count(self):
        """ Gets the number of selected records in the table.

        If features are selected in the table, the function will return the number of selected. features. If no
        features are selected, the function will return the total number of features in the table.

        :return: The number of selected features in the table, or the total number of features in the table if there
        are no records selected.
        """
        # go ahead and retrieve the where clause (this forces
        # the execution of any spatial queries and insures
        # that our from clause is correct
        where_clause = self.where_clause
        query_string = 'SELECT count(distinct("{}")) as count FROM {} {}'.format(self.oid, self.from_clause, where_clause)

        query_result = self.workspace.execute_simple_sql(query_string)
        count = next(query_result)['count']

        return count

    def get_selection_set(self, field_names=None):
        """ Gets the selected features in the table in a SelectionSet object.

        :return: A `SelectionSet()` object containing the selected objects in the table.
        """
        field_names = self.field_names if field_names is None else field_names
        return SelectionSet(self, field_names, self.query_string())

    def switch_selection(self):
        """ Switches the selected records in the table.

        If records are selected in the table, this function will deselect the features that are currently selected,
        and will select the features that were previously unselected.
        """
        self.select_layer_by_attribute('', selection_type='SWITCH_SELECTION')

    def clear_selection(self):
        """ Clears the selected features in the table.

        Clears the table of any selected features.
        """
        # bust the currently cached query string
        self._cached_query_string = None
        self._cached_update_clause = None

        # reset the selection list
        self._selections = []

    def clone_selections(self):
        """ Returns a copy of the current selection set which can be reapplied to the layer using the
        `apply_selections()` method.

        :return: A list containing a copy of the current selections.
        """
        return self._selections[:]

    def apply_selections(self, selections):
        """ Applies the provided list of selections to the layer. Can be used with the `clone_selections()`
        method to back-up and reapply selections to the layer.

        :param selections: The list of selections to apply to the layer.
        :return: None.
        """
        # bust the currently cached query string
        self._cached_query_string = None
        self._cached_update_clause = None
        # copy the provided set of selections to the layer's container
        self._selections = selections[:]

    # SCHEMA MANAGEMENT METHODS
    def add_field(self, field, field_type='TEXT',
        default_value=None,
        field_length=50,
        geometry_type=None,
        spatial_reference=None,
        add_index=False):
        """ Adds a new field to the table.
        This method will add a new field to an existing table.
        :param field: The name of the new field or an ogr field object.
        :param field_type: The type of field. Valid values are:
            TEXT - Any string of characters.
            FLOAT - Fractional numbers between -3.4E38 and 1.2E38.
            DOUBLE - Fractional numbers between -2.2E308 and 1.8E308.
            SHORT - Whole numbers between -32,768 and 32,767.
            INTEGER - Whole numbers between -2,147,483,648 and 2,147,483,647.
            LONG - Whole numbers between -9.2E18 to 9.2E18.
            DATE - Date and/or time.
            BLOB - (not currently implemented) Long sequence of binary numbers. You need a custom loader or viewer
                or a third-party application to load items into a BLOB field or view the contents of a BLOB field.
            RASTER - (not currently implemented) Raster images. All ArcGIS software-supported raster dataset formats
                can be stored, but it is highly recommended that only small images be used.
            GUID - Globally unique identifier.
        :param default_value: The default value to set the field to after creating it. If not provided no value will
            be set.
        :param field_length: The field length when creating TEXT fields. This value has no effect when creating fields
            of other data types. If not specified when creating a TEXT field, the value will revert to the sde default
            (50 characters for most DBMS systems). (not currently implemented)
        """
        # if the field already exists simply return
        if field in self.field_names:
            return

        # translate the Postgresql data type
        if not field_type == 'GEOMETRY':
            if field_type == 'TEXT':
                field_length = 50 if field_length == 0 else field_length
                field_type = 'VARCHAR({})'.format(field_length)
            elif field_type == 'FLOAT' or field_type == 'DOUBLE':
                field_type = 'FLOAT8'
            elif field_type == 'SHORT':
                field_type = 'SMALLINT'
            elif field_type == 'INTEGER':
                field_type = 'INT'
            elif field_type == 'LONG':
                field_type = 'BIGINT'
            elif field_type == 'DATE':
                field_type = 'TIMESTAMP'
            elif field_type == 'GUID':
                field_type = 'UUID'
            alter_statement = f'ALTER TABLE "{self.schema}"."{self.table_name}" ADD COLUMN "{field}" {field_type}'
            self.workspace.execute_simple_sql(alter_statement, use_transaction=False)
        else:
            self.workspace.create_geometry_column(self.table_name, field, geometry_type, spatial_reference, schema=self.schema)
            self._cached_shape_field = None
            self._cached_geometry_columns = None
            self._cached_geometry_columns_reduced = None

        # reload the table
        self.alchemy_table = load_alchemy_table(self.workspace, self.table_name, schema=self.schema)

        if default_value is not None:
            self.calculate_field(field, default_value)

        if add_index and not field_type == 'GEOMETRY':
            self.add_index(field)

    def add_index(self, field_name):
        """ Adds an index to the specified attribute.

        :param field_name: A list of field names to be included in the index.
        :return: None
        """

        self.workspace.create_index(self.table_name, field_name, schema=self.schema)

    def list_indexes(self):
        """ List the names of the indexes associated with the table.

        :return: A list of index names.
        """
        return self.workspace.list_indexes(self.table_name, schema=self.schema)

    def delete_field(self, field_name):
        """ Deletes the specified field from the table.

        Deletes the specified field from the table. Any data contained in the deleted field will be lost.

        :param field_name: The field to be deleted.
        """
        field_names = [field_name] if isinstance(field_name, str) else field_name

        for field_name in field_names:
            shape_fields = self.get_geometry_field_names(include_hidden=True) if hasattr(self, 'get_geometry_field_names') else []
            assert field_name in self.field_names + shape_fields, 'Field does not exists'
            sql = f'ALTER TABLE "{self.schema}"."{self.table_name}" DROP COLUMN IF EXISTS "{field_name}"'
            self.workspace.execute_simple_sql(sql, use_transaction=False)

        # reload the table
        self.alchemy_table = load_alchemy_table(self.workspace, self.table_name, schema=self.schema)

    def delete_other_fields(self, preserve_fields):
        """
        Deletes all of the fields in the table except those specified in the `preserve_fields` set. Fields
        required by all shapefiles (FID, Shape, etc.) will be preserved automatically.

        :param preserve_fields: A set of fields not to be deleted.
        :return: List of fields that were deleted.
        """
        # if the field is a string make it a list
        if isinstance(preserve_fields, str):
            preserve_fields = [preserve_fields]

        #  add shapefile required fields to list of fields to preserve
        # preserve_fields_set = set(preserve_fields + constants.SHAPEFILE_NECESSARY_FIELDS + [self.oid])
        preserve_fields_set = set(preserve_fields + [self.oid])

        # get the list of fields in the table
        existing_fields = set(self.field_names)

        # get the list of fields to delete
        delete_fields = list(existing_fields - preserve_fields_set)

        # delete the fields in the table that are not in the preserve list
        for field_name in delete_fields:
            self.delete_field(field_name)
        return delete_fields

    def rename_field(self, field_name, new_field_name):
        """ Renames the selected field.

        :param field_name: The current name of the field to be renamed.
        :param new_field_name: The new name for the field.
        """
        existing_field_names = self.field_names

        assert field_name in existing_field_names, 'Could not find field {0}'.format(field_name)

        sql = f'ALTER TABLE "{self.schema}"."{self.table_name}" RENAME COLUMN "{field_name}" TO "{new_field_name}"'
        self.workspace.execute_simple_sql(sql, use_transaction=False)
        self.alchemy_table = load_alchemy_table(self.workspace, self.table_name, schema=self.schema)

    def trim_field(self, field):
        """ Trims the string values in the specified field.

        :param field: The name of the field to be trimmed.
        """
        assert field in self.field_names, 'Specified field must exists in the table.'
        self.calculate_field(field, 'TRIM ("{}")'.format(field))

    def delete(self):
        """ Deletes the underlying table.

        This method removes the table from ArcMap's tables list and deletes the underlying shapefile. Once delete has
        been called the table can no longer be accessed.

        """
        # do not process if table has already been deleted
        if self.deleted:
            return

        self.workspace.drop_table(self.table_name, schema=self.schema, cascade=True)
        self.deleted = True

    def get_field(self, field_name):
        """ Returns the field definition for the specified field name.

        :param field_name: The name of the field to be retrieved.
        :return: The field definition for the specified field.
        """

        for field in self.fields:
            if field.name == field_name:
                return field

    def list_fields(self, type='ALL'):
        """ Gets a list of fields in the table.

        This method will return a collection of field objects representing the fields that are in the current table.

        :return: An array of field objects representing the fields in the table.
        """
        return_list = []
        if type.upper() == 'ALL':
            for column in self.alchemy_table.columns:
                if column.name.lower() in ['edge_buffers', 'centroid', 'midpoint']:
                    continue
                return_list.append(column)
            return return_list

        for column in self.alchemy_table.columns:
            if (hasattr(self, 'get_geometry_field_names') and column.name in self.get_geometry_field_names(include_hidden=True)) or not hasattr(column.type, 'python_type'):
                continue
            if column.type.python_type == str and type.upper() == 'STRING':
                return_list.append(column)
            elif column.type.python_type == int and type.upper() == 'INTEGER':
                return_list.append(column)
            elif column.type.python_type == float and type.upper() == 'FLOAT':
                return_list.append(column)
        return return_list

    def list_field_names(self):
        """ Gets a list of field names in the table as strings. The list does *not* include the oid or shape
        field names (these can be accessed through the `Table.oid` and `Layer.shape` properties.

        :return: An array of strings representing the names of the fields in the table.
        """
        shape_fields = self.get_geometry_field_names(include_hidden=True) if hasattr(self, 'get_geometry_field_names') else []
        return [field.name for field in self.list_fields() if field.name != self.oid and field.name not in shape_fields]

    def get_oid_field(self):
        """ Gets the name of the OID field for this table or layer.

        The "OID" field is the primary key field in an Esri table or feature class. Typically,
        the name of the OID field in shapefiles is "FID" and the OID field in geodatabase tables
        and feature classes is called "OBJECTID".

        This method will dynamically determine the proper name of the field to be used in
        database queries, etc.

        :return: A string with the name of the OID field for this table or layer.
        """
        # if we've already determined the OID field name, just return it
        if self._cached_oid_field is not None:
            return self._cached_oid_field

        self._cached_oid_field = self.alchemy_table.primary_key.columns.items()[0][0]
        return self._cached_oid_field

    def get_unique_field_values(self, field,
        query_string=None):
        """ Gets a set of unique values found in the selected features' field.

        :param field: The field name to look up.
        :param query_string: An SQL expression used to select a subset of records.
        :return: A set of field values.
        """
        with self.get_search_cursor(field, query_string, sql_clause=('DISTINCT', None)) as cursor:
            return set([row[field] for row in cursor])

    def get_distinct_field_values(self, fields):
        """ Gets a set of unique values found in the selected features' field.

        :param fields: The field names to look up.
        :return: A set of field values.
        """
        if isinstance(fields, str):
            fields = [fields]
        field_string = ','.join(['"{}"'.format(field) for field in fields])
        sql = f'SELECT DISTINCT {field_string} FROM "{self.schema}"."{self.table_name}" {self.where_clause}'
        results = self.workspace.execute_simple_sql(sql)

        return_results = []
        for row in results:
            result = {}
            for field in fields:
                result[field] = row[field]
            return_results.append(result)
        return return_results

    def vacuum(self):
        """ Cleans up any data files produced by the table. Can be used to manage hard-drive space when
        doing large update operations.

        :return: None
        """

        self.workspace.vacuum(self.table_name, schema=self.schema)

    # CURSOR METHODS
    def get_search_cursor(self,
        field_names='*',
        query_string=None,
        sql_clause=(None, None),
        allow_invalid=False):
        """ Gets a fast read-only cursor for looping through features in the table.

        The cursor allows for row-by-row access to the features in the table. This cursor is optimized for reading and
        should not be used to update features. Use the get_update_cursor method to get a cursor that allows write-access
        to the features in the table.

        :param field_names: The field or list of fields to be returned in the cursor.
        :param query_string: An SQL expression used to select a subset of records.
        :param sql_clause: An optional pair of SQL prefix and postfix clauses organized in a list or tuple.

            An SQL prefix supports None, DISTINCT, and TOP. SQL postfix supports None, ORDER BY, and GROUP BY. An SQL
            prefix clause is positioned in the first position and will be inserted between the SELECT keyword and
            the SELECT COLUMN LIST. The SQL prefix clause is most commonly used for clauses such as DISTINCT or ALL.

            An SQL postfix clause is positioned in the second position and will be appended to the SELECT statement,
            following the where clause. The SQL postfix clause is most commonly used for clauses such as ORDER BY.

            The default value is (None, None)
        :return: A cursor that can be iterated over to review features in the table.
        """
        if query_string is None:
            query_string = self.query_string(allow_invalid=allow_invalid)
        return SearchCursor(self, field_names, query_string, sql_clause, allow_invalid)

    def get_insert_cursor(self, field_names='*'):
        """ Gets a fast cursor for adding features to the table.

        :param field_names: The field or list of fields to be returned in the cursor.
        :return: A cursor that can write new features to the table.
        """
        return InsertCursor(self, field_names)

    def get_update_cursor(self,
        field_names=None,
        query_string=None,
        sql_clause=(None, None),
        allow_invalid=False):
        """ Gets a cursor that allows for updating the features in the table.

        The update cursor allows the features in the cursor to be updated. If you simply need to loop through the
        features in the table but do not need to update them, use the get_search_cursor method.

        :param field_names: The field or list of fields to be returned in the cursor.
        :param query_string: An SQL expression used to select a subset of records.
        :param sql_clause: An optional pair of SQL prefix and postfix clauses organized in a list or tuple.

            An SQL prefix supports None, DISTINCT, and TOP. SQL postfix supports None, ORDER BY, and GROUP BY. An SQL
            prefix clause is positioned in the first position and will be inserted between the SELECT keyword and
            the SELECT COLUMN LIST. The SQL prefix clause is most commonly used for clauses such as DISTINCT or ALL.

            An SQL postfix clause is positioned in the second position and will be appended to the SELECT statement,
            following the where clause. The SQL postfix clause is most commonly used for clauses such as ORDER BY.

            The default value is (None, None)
        :return: A cursor that can be used to update features in the table.
        """
        if query_string is None:
            query_string = self.query_string(allow_invalid)
        return UpdateCursor(self, field_names, query_string, sql_clause, allow_invalid)

    # DATA MANIPULATION METHODS
    def calculate_field(self, field, expression):
        """ Populates a field in the table with calculated values.

        This method will calculate a value for each feature in the table and place that value in the specified field.
        The entry can be as simple as a static value that will be the same for all features, or it can be calculated
        individually based on values in each feature.

        :param field: The field where the output of the expression will be written.
        :param expression: The expression used to calculate the value.
        """
        query_string = f'UPDATE "{self.schema}"."{self.table_name}" SET "{field}" = {parse_expression(self, field, expression)} {self.update_clause}'

        self.workspace.execute_simple_sql(query_string)

    def calculate_fields(self, values):
        """ Updates multiple attributes for the selected set of records.

        :param values: A dictionary with keys representing the field names to update and values representing
            the updated values.
        :return: None
        """
        fields_string = ','.join(['"{}" = {}'.format(key, value) for key, value in values.items()])

        query_string = f'UPDATE "{self.schema}"."{self.table_name}" SET {fields_string} {self.update_clause}'

        self.workspace.execute_simple_sql(query_string)

    def copy_field_values(self, source_field, target_field):
        """ Copies the values of one field to another field.

        The copy_field_values method will copy the values from the field specified in the source_field parameter into
        the field specified in the target_field parameter. The value from the source field will be converted to a
        string, so the target field must be of type TEXT.
        :param source_field: The name of the field containing the source values.
        :param target_field: The name of the field that the values will be copied into. This field must be of type TEXT.
        """
        sql = f'UPDATE "{self.schema}"."{self.table_name}" SET "{target_field}" = "{source_field}" {self.where_clause};'
        self.workspace.execute_simple_sql(sql)

    def change_data_type(self, field, data_type, field_length=None):
        """ Changes the data type of the specified field to the specified data type, and cast the data within
        the field to that data type.

        :param field: The name of the field to be changed.
        :param data_type: The type of field to convert to. Valid values are:
            TEXT - Any string of characters.
            FLOAT - Fractional numbers between -3.4E38 and 1.2E38.
            DOUBLE - Fractional numbers between -2.2E308 and 1.8E308.
            SHORT - Whole numbers between -32,768 and 32,767.
            INTEGER - Whole numbers between -2,147,483,648 and 2,147,483,647.
            LONG - Whole numbers between -9.2E18 to 9.2E18.
            DATE - Date and/or time.
            BLOB - (not currently implemented) Long sequence of binary numbers. You need a custom loader or viewer
                or a third-party application to load items into a BLOB field or view the contents of a BLOB field.
            RASTER - (not currently implemented) Raster images. All ArcGIS software-supported raster dataset formats
                can be stored, but it is highly recommended that only small images be used.
            GUID - Globally unique identifier.
        :param field_length: If specified, text fields will be of the specified length. Default length is 50 if a length
            is not provided. This parameter is ignored for data types that do not require a length specification.
        """
        temp_field_name = '{}_old'.format(field)
        if data_type == 'TEXT':
            field_length = 50 if not field_length else field_length
            conversion_func = 'VARCHAR({})'.format(field_length)
        elif data_type == 'FLOAT' or data_type == 'DOUBLE':
            conversion_func = 'FLOAT8'
        elif data_type == 'SHORT':
            conversion_func = 'SMALLINT'
        elif data_type == 'INTEGER':
            conversion_func = 'INT'
        elif data_type == 'LONG':
            conversion_func = 'BIGINT'
        elif data_type == 'DATE':
            conversion_func = 'TIMESTAMP'
        elif data_type == 'GUID':
            conversion_func = 'UUID'
        else:
            conversion_func = data_type

        self.rename_field(field, temp_field_name)
        self.add_field(field, data_type,
                       field_length=field_length)
        self.calculate_field(field, 'CAST("{}" AS {})'.format(temp_field_name, conversion_func))
        self.delete_field(temp_field_name)

    def add_rows(self, rows):
        """ Add new rows to the table using an insert cursor.

        :param rows: A list of dictionaries where each dictionary represents a row to be added. The dictionary
            objects should have field names as keys with the corresponding data as dictionary values.
        :return: None
        """
        # if this is a single row, convert it to a list
        if isinstance(rows, dict):
            rows = [rows]

        # if an empty list is provided, just return
        if len(rows) == 0:
            return

        # get insertable rows for each provided row
        insertable_rows = [create_insert_row(self, row) for row in rows]

        with self.workspace.alchemy_engine.connect() as connection:
            connection.execute(self.alchemy_table.insert(), insertable_rows)

    def duplicate_table(self, output_table_name,
        output_workspace=None, output_schema=None):
        """
        Duplicates the layer's schema as a new empty shapefile. The data in the source shapefile is *not*
        copied to the new shapefile. Use the `copy_to_new_table` method if you wish to copy the source
        data into a new layer.

        :param output_table_name: The name of the new layer.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: The new empty layer
        """
        # set the workspace and schema if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace
        output_schema = self.workspace.schema if not output_schema else output_schema
        output_workspace.create_schema(output_schema)

        field_defs = []
        for field in self.fields:
            if field.name.lower() == self.oid.lower():
                field_def = Column(field.name, field.type, primary_key=True, autoincrement=True)
            else:
                field_def = Column(field.name, field.type)
            field_defs.append(field_def)

        alchemy_table = AlchemyTable(output_table_name, MetaData(), schema=output_schema, *field_defs)
        alchemy_table.create(output_workspace.alchemy_engine)

        return Table(output_table_name, output_workspace, schema=output_schema)

    def copy_to_new_table(self, output_table_name,
        output_workspace=None, output_schema=None):
        """ Copies selected rows to a new table.

        :param output_table_name: The name of the geodatabase table to write to.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: The Table object interface to the newly created table.
        """

        # set the workspace if necessary
        db_transfer = False
        if output_workspace is None:
            output_workspace = self.workspace
        else:
            db_transfer = self.workspace.connection_info['host'] != output_workspace.connection_info['host'] or \
                        self.workspace.connection_info['port'] != output_workspace.connection_info['port'] or \
                        self.workspace.connection_info['database'] != output_workspace.connection_info['database']

        # set the output schema if necessary
        output_schema = self.workspace.schema if not output_schema else output_schema

        self.duplicate_table(output_table_name, output_workspace, output_schema=output_schema)

        # go ahead and retrieve the where clause (this forces
        # the execution of any spatial queries and insures
        # that our from clause is correct
        where_clause = self.where_clause

        # copy fields
        if not db_transfer:
            query_string = 'INSERT INTO "{output_schema_name}"."{output_table_name}" ({output_field_names}) \
                SELECT {field_names} FROM {from_clause} {where_clause}'\
                .format(
                output_schema_name=output_schema,
                output_table_name=output_table_name,
                output_field_names=','.join(['"{}"'.format(field_name) for field_name in self.field_names]),
                field_names=','.join(['"{}"'.format(field_name) for field_name in self.field_names]),
                from_clause=self.from_clause,
                where_clause=where_clause)
        else:
            # because where clause in this case is in a string it must be formatted
            where_clause = where_clause.replace("'", "''")
            query_string = "INSERT INTO \"{output_schema_name}\".\"{output_table_name}\" ({output_field_names}) \
                SELECT {field_names} FROM dblink('host={host} port={port} dbname={database} \
                user={user} password={password} options=-csearch_path=', 'select {field_names} from {from_clause} {where_clause}') \
                as link_table({field_definitions})"\
                .format(
                output_schema_name=output_schema,
                output_table_name=output_table_name,
                output_field_names=','.join(['"{}"'.format(field_name) for field_name in self.field_names]),
                field_names=','.join(['"{}"'.format(field_name) for field_name in self.field_names]),
                from_clause=self.from_clause,
                where_clause=where_clause,
                host=self.workspace.connection_info['host'],
                database=self.workspace.connection_info['database'],
                port=self.workspace.connection_info['port'],
                user=self.workspace.connection_info['user'],
                password=self.workspace.connection_info['password'],
                field_definitions=','.join(['"{}" {}'.format(field_name, self.get_field_type(field_name)) for field_name in self.field_names]))

        output_workspace.execute_simple_sql(query_string)

        return Table(output_table_name, output_workspace, schema=output_schema)

    def truncate(self):
        """
        Deletes the selected records in the table.
        :return: None
        """
        query_string = 'TRUNCATE TABLE  "{}"."{}"'.format(self.schema, self.table_name)

        self.workspace.execute_simple_sql(query_string)
        self.clear_selection()

    def delete_selected_rows(self):
        """
        Truncates the table.
        :return: None
        """
        query_string = 'DELETE FROM "{}"."{}" {}'.format(self.schema, self.table_name, self.where_clause)

        self.workspace.execute_simple_sql(query_string)
        self.clear_selection()

    def delete_duplicates(self, fields):
        """ Deletes duplicate records in the table.

        This method deletes duplicate records in the table based on the list of fields provided. If the field Shape is
        selected, feature geometries are compared.

        :param fields: The fields to be compared.
        """
        query_string = 'DELETE FROM "{schema_name}"."{table_name}" WHERE "{oid}" NOT IN \
                        (SELECT min("{oid}") AS OID FROM {table_name} GROUP BY {group_fields})'\
                        .format(
            oid=self.oid,
            schema_name=self.schema,
            table_name=self.table_name,
            group_fields=','.join(['"{}"'.format(field) for field in fields]),
        )

        self.workspace.execute_simple_sql(query_string)

    def _assert_matching_fields(self, other_table):
        """ Insures that the field names between this table and the other table match

        :param other_table: The table to be compared to this table.
        :return: None. Assertion errors will raise if the fields do not match.
        """
        source_field_names = [field_name.lower() for field_name in self.field_names]
        input_field_names = [field_name.lower() for field_name in other_table.field_names]
        for field_name in input_field_names:
            assert field_name in source_field_names

    def append(self, add_tables, schema_type='TEST'):
        """ Appends features from one or more tables to this table. This mutates the table.

        :param add_tables: A list of tables with features to append to this table.
        :param schema_type: A string specifying if the schema of the tables should match. Valid options are:
            TEST - Schema must match, otherwise throw error.
            NO_TEST - Schema do not have to match.
        """
        if not isinstance(add_tables, list):
            add_tables = [add_tables]
        if schema_type == 'TEST':
            for table in add_tables:
                self._assert_matching_fields(table)
        shape_field = self.shape if hasattr(self, 'shape') else None
        fields_to_copy = [name for name in self.field_names if name != self.oid]
        if shape_field is not None:
            fields_to_copy.append(shape_field)
        with self.get_insert_cursor(fields_to_copy) as insert_cursor:
            for add_table in add_tables:
                with add_table.get_search_cursor(fields_to_copy) as search_cursor:
                    for row in search_cursor:
                        insert_cursor.insert_row(row)

    def to_csv(self, path, attributes):
        """ Writes table contents to csv file.

        :param path: Path and filename of csv file to write to.
        :param attributes: The attributes (columns) to include in the csv.
        """
        with open(path, 'w') as output:
            output.write(','.join(attributes) + '\n')
            with self.get_search_cursor(attributes) as cursor:
                output.write('\n'.join(
                    [','.join([str(row[field]) for field in row])
                    for row in cursor]))

    def get_field_type(self, field_name):
        """ Gets the data type for the specified field.

        :param field_name: The name of the field to inspect.
        :return: The data type for the field. Valid values are:
            Blob - Blob
            Date - Date
            Double - Double
            Geometry - Geometry
            GlobalID - Global ID
            Guid - Guid
            Integer - Integer (Long Integer)
            OID - Object ID
            Raster - Raster
            Single - Single (Float)
            SmallInteger - Small Integer (Short Integer)
            String - String (Text)
        """
        shape_fields = self.get_geometry_field_names(include_hidden=True) if hasattr(self,
                                                                                     'get_geometry_field_names') else []
        field_names = self.field_names + shape_fields
        if field_name not in field_names:
            raise ValueError('Field not found - {}'.format(field_name))
        field_def = self.get_field(field_name)

        field_type = str(field_def.type)
        return field_type.replace('_', ' ')

    @property
    def max_oid(self):
        """ Returns the highest value in the designated `oid` field.

        :return: An integer representing the maximum value of the `oid` field.
        """
        result = self.workspace.execute_simple_sql('SELECT MAX("{}") as max_oid FROM "{}"."{}"'.format(self.oid, self.schema, self.table_name))
        row = next(result)
        return int(row['max_oid']) if row is not None and row['max_oid'] is not None else 0

    def query_string(self, allow_invalid=False):
        """ The query string for the selection set applied to the table.

        :return: A string representing the WHERE clause of the selection set applied to the table.
        """
        # return cached string if available
        if self._cached_query_string:
            return self._cached_query_string

        # cache new query string and return it
        self._cached_query_string = build_query_string(self, self._selections, allow_invalid=allow_invalid)
        return self._cached_query_string

    @property
    def update_clause(self):
        """ Returns the WHERE clause required to update the data in the table.

        :return: A string representing the WHERE clause required to update the table.
        """
        if self._cached_update_clause:
            return self._cached_update_clause

        # make sure the main query string has been cached (required for the update clause to work correctly)
        self._cached_query_string = build_query_string(self, self._selections)

        self._cached_update_clause = build_update_clause(self, self._selections)
        return self._cached_update_clause

    @property
    def from_clause(self):
        """ Properly formats FROM clause for SQL queries using the layer's selection filters.

        :return: String.
        """
        if len(self._selections) == 0:
            return f'"{self.schema}"."{self.table_name}"'

        last_selection = self._selections[-1]
        if 'result_query_string' in last_selection:
            return ", ".join(last_selection['from_tables'])

        from_tables = set()
        for selection in self._selections:
            from_tables.update(selection['from_tables'])
        return ", ".join(from_tables)

    @property
    def where_clause(self):
        """ Properly formats WHERE clause for SQL queries using the layer's selection filters.

        :return: String, a clause to append to end of SQL query.
        """
        return "WHERE {}".format(self.query_string(allow_invalid=True)) if len(self._selections) > 0 else ""

    def get_field_length(self, field_name):
        """ Gets the field length for the specified field.

        :param field_name: The name of the field to inspect.
        :return: The length of the field.
        """
        sql = "SELECT character_maximum_length FROM information_schema.COLUMNS WHERE table_schema = '{}' AND table_name = '{}' AND column_name = '{}';".format(self.schema, self.table_name, field_name)

        result = self.workspace.execute_simple_sql(sql)
        row = next(result)
        return int(row['character_maximum_length']) if row is not None and row['character_maximum_length'] is not None else 0

    # properties and support methods
    count = property(fget=get_selection_count)
    fields = property(fget=list_fields)
    oid = property(fget=get_oid_field)
    field_names = property(fget=list_field_names)


class Table(TableBase):
    """
    The table class manages table names and the association
    with its underlying shapefile. It also provides access
    to most geoprocessing tools that take tables as inputs.
    """

    def __init__(self, table, workspace, schema=None):
        """ Initializes the table object.

        All "Table" functions are actually housed in the `TableBase` class. The `Table` class is a helper class
        that allows a Table object to be initialized correctly in ArcPy.

        :param table_name: The name of the table as it will be displayed in the ArcMap table control (this is the
            internal name of the table)
        :param workspace: The workspace where the table is located.
        :param file_path: The path to the underlying dbf that stores the data for this table, if not in a geodatabase.
        """
        super(Table, self).__init__(table, workspace, schema=schema)

    @staticmethod
    def merge_tables_to_table(tables, output_table_name, output_workspace):
        """ Merges the specified tables into a new table.

        :param tables: The table objects to be merged.
        :param output_table_name: The name of the output table that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be located.
        :return: A new table object that represents the table containing the results of the process.
        """
        first_table = tables.pop()
        first_table.clear_selection()
        return_table = first_table.copy_to_new_table(output_table_name, output_workspace)

        for next_table in tables:
            return_table.append(next_table)

        return return_table
