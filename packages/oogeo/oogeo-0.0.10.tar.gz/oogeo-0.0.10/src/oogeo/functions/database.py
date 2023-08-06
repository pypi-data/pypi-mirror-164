"""
Common functions for creating database queries
"""

from shapely.wkb import loads as wkb_to_geom
from shapely.geometry import Polygon as ShapelyPolygon, LineString, MultiPolygon, MultiLineString

import src.oogeo.objects.line
import src.oogeo.objects.point
import src.oogeo.objects.polygon

from src.oogeo.functions.conversions import upgrade_shapely_geometry
from src.oogeo.objects.polygon import correct_invalid_polygon
from src.oogeo.objects.line import correct_invalid_line

from geoalchemy2 import Geometry, WKBElement


def geodataframe_to_layer(geodataframe, workspace, output_schema, output_layer_name, oid_field, shape_field):
    """ Converts a geodataframe to a geodatabase layer.

    :param geodataframe: The geodataframe to be stored in the database.
    :param workspace: The workspace containing the connection to the database where the geodataframe should be stored.
    :param output_layer_name: The name of the table to be created in the geodatabase.
    :param oid_field: The field representing the primary key for the table.
    :param shape_field: The field representing the shape field for the table.
    :return: A `Layer()` object representing the geodatabase table that was created.
    """

    # get the spatial reference in epsg format
    epsg = int(geodataframe.crs.to_epsg())

    # upgrade geometries to multis
    geodataframe.geometry = geodataframe.geometry.apply(upgrade_shapely_geometry)

    # get the layer's geometry type
    geometry_type = str(geodataframe.geom_type.tolist()[0]).upper()

    # correct invalid geometries if necessary
    if geometry_type == 'MULTIPOLYGON':
        geodataframe.geometry = geodataframe.geometry.apply(correct_invalid_polygon)
        geodataframe.drop(geodataframe[geodataframe.geometry.isnull()].index, inplace=True)

    elif geometry_type == 'MULTILINESTRING':
        geodataframe.geometry = geodataframe.geometry.apply(correct_invalid_line)

        # delete rows with null geometries
        geodataframe.drop(geodataframe[geodataframe.geometry.isnull()].index, inplace=True)

    # translate the geometries to geoalchemy (makes them storable in the db)
    geodataframe['temp_shape'] = geodataframe.geometry.apply(lambda x: WKBElement(x.wkb, srid=epsg))

    # delete the current geometry field and rename the new one properly
    geodataframe.drop(geodataframe.geometry.name, axis=1, inplace=True)
    geodataframe = geodataframe.rename(columns={'temp_shape': shape_field})

    # drop the edge_buffers column if it exists
    if 'edge_buffers' in list(geodataframe.columns.values):
        geodataframe.drop('edge_buffers', 1, inplace=True)
    if 'EDGE_BUFFERS' in list(geodataframe.columns.values):
        geodataframe.drop('EDGE_BUFFERS', 1, inplace=True)

    # drop the centroid column if it exists
    if 'centroid' in list(geodataframe.columns.values):
        geodataframe.drop('centroid', 1, inplace=True)
    if 'CENTROID' in list(geodataframe.columns.values):
        geodataframe.drop('CENTROID', 1, inplace=True)

    # drop the midpoint column if it exists
    if 'midpoint' in list(geodataframe.columns.values):
        geodataframe.drop('midpoint', 1, inplace=True)
    if 'MIDPOINT' in list(geodataframe.columns.values):
        geodataframe.drop('MIDPOINT', 1, inplace=True)

    # store the layer in the db
    workspace.create_schema(output_schema)
    geodataframe.to_sql(output_layer_name, workspace.alchemy_engine, if_exists='fail', index_label=oid_field, schema=output_schema,
        dtype={shape_field: Geometry(geometry_type, srid=epsg)})

    # set the object id as the primary key
    workspace.execute_simple_sql('ALTER TABLE "{}"."{}" ADD PRIMARY KEY ("{}");'.format(output_schema, output_layer_name, oid_field),
        use_transaction=False)

    # create a sequence for the table
    workspace.create_sequence(output_layer_name, oid_field, schema=output_schema)

    return_layer = oogeo.objects.layer.Layer(output_layer_name, workspace, schema=output_schema)
    return return_layer


def create_in_clause(inclusion_list, use_quotes=False, field_name=None, not_operator=False):
    """
    Creates an SQL "IN" clause base on the data in the provided list.

    :param inclusion_list: The list of ids to convert into an IN clause.
    :param use_quotes: If True, single-quotes will be added around each value
    :param field_name: A field name to append to the query.
    :param not_operator: Adds the NOT operator to reverse the results of the in clause.
    :return: A string with the complete in clause.
    """
    if len(inclusion_list) == 0:
        inclusion_list.add(-1)
    quote_mark = "'" if use_quotes else ''
    not_operator = ' NOT' if not_operator else ''
    return_string = ''
    # get the list of values in a comma-separated list
    for item in inclusion_list:
        # append a comma if the list has already been started
        if not return_string == '':
            return_string = '{},'.format(return_string)
        # append current record
        return_string = '{}{}{}{}'.format(return_string, quote_mark, item, quote_mark)

    # create the final output and return
    field_name = '' if field_name is None else '"{}"'.format(field_name) if '.' not in field_name else field_name
    return '{}{} IN ({})'.format(field_name, not_operator, return_string)


def prepare_query(table, field_names, query_string, sql_clause, use_raw_fields=False):
    """ Prepares a complete SQL statement based on the inputs provided.

    :param table: The table that the query will be based on.
    :param field_names: The list of field names to be included in the query.
    :param query_string: The FROM clause to apply to the query.
    :param sql_clause: A tuple representing the prefix and postfix to be applied to the query.
        Typically the prefix is used to apply a COUNT or DISTINCT clause, and the postfix is
        used to apply an ORDER BY clause.
    :return: A complete SQL statement based on the provided inputs.
    """
    query = {}

    # Build up the correct WHERE clause. If the function call did not have one as a parameter,
    # we default to using the current layer selection (both attribute and location). If neither
    # exists, we omit the WHERE clause entirely.
    if not query_string:
        query['from_clause'] = f'"{table.schema}"."{table.table_name}"'
        query['where_clause'] = ""
    elif isinstance(query_string, int):
        query['from_clause'] = f'"{table.schema}"."{table.table_name}"'
        query['where_clause'] = 'WHERE "{}" = {}'.format(table.oid, query_string)
    elif isinstance(query_string, str):
        query['from_clause'] = table.from_clause
        query['where_clause'] = "WHERE {}".format(query_string)
    else:
        raise ValueError('Need valid query_string')

    # prepare field names
    if isinstance(field_names, str):
        field_names = [field_names]

    if '*' in field_names:
        field_names = [table.shape, table.oid] + table.field_names \
            if hasattr(table, 'shape') else [table.oid] + table.field_names

    table_oid_sql = '"{}" AS table_oid'.format(table.oid) if not use_raw_fields else '"{}"'.format(table.oid)
    shape_field_names = [name.lower() for name in table.get_geometry_field_names(include_hidden=True)] \
        if hasattr(table, 'get_geometry_field_names') else []
    column_names = {
        table_oid_sql if name.lower() == 'oid@' or name.lower() == table.oid.lower() else
        'ST_AsEWKB("{0}") as "{0}"'.format(table.shape) if not use_raw_fields and ('shape@' in name.lower() or (hasattr(table, 'shape') and name.lower() == table.shape.lower())) else
        'ST_AsEWKB("{0}") as "{0}"'.format(name) if not use_raw_fields and name.lower() in shape_field_names else
        '"{}"'.format(name)
        for name in field_names
    }
    if table_oid_sql not in column_names:
        column_names.add(table_oid_sql)

    query['columns'] = ", ".join(column_names)

    # Build up prefix and postfix clauses, if provided.
    if (sql_clause is None or sql_clause[0] is None) and table.from_clause != f'"{table.schema}"."{table.table_name}"':
        # this is a spatial join - we need to add a distinct clause here
        if not sql_clause:
            sql_clause = ('DISTINCT', None)
        elif not sql_clause[0] and (not sql_clause[1] or not sql_clause[1].upper().startswith('ORDER BY')):
            sql_clause = ('DISTINCT', sql_clause[1])

    query['prefix'] = sql_clause[0] if sql_clause and sql_clause[0] else ""
    query['postfix'] = sql_clause[1] if sql_clause and sql_clause[1] else ""

    return "SELECT {prefix} {columns} FROM {from_clause} {where_clause} {postfix}".format(**query)


def convert_feature_to_row(source_table, feature, field_names, allow_invalid):
    """ Converts the provided feature into a list representing the row.

    :param source_table: The source table that the features came from.
    :param feature: The feature to be converted.
    :param field_names: The names of the fields in the feature.
    :return: A List representing the values in the row, ordered by the provided list of field names.
    """
    row = {}

    # iterate through field names and assemble row
    for field_name in field_names:
        lcase_field_name = field_name.lower()
        if 'oid@' in lcase_field_name or source_table.oid == field_name:
            row[field_name] = feature['table_oid']
            continue
        geometry_fields = [name.lower() for name in source_table.get_geometry_field_names(include_hidden=True)] if hasattr(source_table, 'get_geometry_field_names') else []
        if lcase_field_name not in ['shape@', 'shape@wkt', 'shape@xy', 'shape@length'] + geometry_fields:
            # check to see if the row is a boolean
            if source_table.get_field(field_name).type == 'BOOLEAN':
                row[field_name] = bool(feature[field_name])
            else:
                row[field_name] = feature[field_name]
            continue

        # Cache the geometry
        shape_field = field_name if lcase_field_name in geometry_fields else source_table.shape
        load_invalid = True if lcase_field_name in ['edge_buffers', 'centroid', 'midpoint'] else allow_invalid
        shapely_geometry = wkb_to_geom(feature[shape_field].tobytes())
        try:
            if isinstance(shapely_geometry, ShapelyPolygon) or isinstance(shapely_geometry, MultiPolygon):
                geometry = src.oogeo.objects.polygon.Polygon(shapely_geometry, source_table.spatial_reference, allow_invalid=load_invalid)
            elif isinstance(shapely_geometry, LineString) or isinstance(shapely_geometry, MultiLineString):
                geometry = src.oogeo.objects.line.Line(shapely_geometry, source_table.spatial_reference, allow_invalid=load_invalid)
            else:
                geometry = src.oogeo.objects.point.Point(shapely_geometry, source_table.spatial_reference, allow_invalid=load_invalid)
        except ValueError as e:
            raise ValueError('Invalid geometry in layer {}: {}'.format(source_table.table_name, shapely_geometry.wkt))

        # Lookup geometry fields
        if lcase_field_name in ['shape@'] + geometry_fields:
            row[field_name] = geometry
        elif lcase_field_name == 'shape@wkt':
            row[field_name] = geometry.wkt
        elif lcase_field_name == 'shape@length':
            if isinstance(geometry, src.oogeo.objects.point.Point):
                row[field_name] = 0
            else:
                row[field_name] = geometry.length
        elif lcase_field_name == 'shape@xy':
            if isinstance(geometry, src.oogeo.objects.point.Point):
                row[field_name] = geometry
            else:
                row[field_name] = geometry.centroid
        else:
            row[field_name] = None
    return row


def convert_features_to_rows(source_table, result_layer, field_names, allow_invalid):
    """ Converts the features in a query result table to a list of rows

    :param source_table: The table that spawned the query.
    :param result_layer: The result layer returned from the query.
    :param field_names: The field names to extract from the features.
    :return: A list of values representing the rows in the result layer.
    """

    results = []
    for current_feature in result_layer:
        results.append(convert_feature_to_row(source_table, current_feature, field_names, allow_invalid))
    return results


def filter_query_results(selection, current_filtered_oids, unfiltered_results, oid_field, shape_field):
    """ Manually filters query results based on geometry analysis.

    :param selection: A dictionary containing the selection criteria.
    :param current_filtered_oids: The list of currently selected oids from previous queries.
    :param unfiltered_results: A list of unfiltered results from the database.
    :return: A list of object ids representing the items to include in the final result set.
    """
    filtered_oids = current_filtered_oids.copy() \
        if not (selection['selection_type'] == 'SUBSET_SELECTION'
                or selection['selection_type'] == 'SWITCH_SELECTION') else set()

    # iterate through results and filter them manually
    result_oid = -1
    for row in unfiltered_results:
        test_oid = row[oid_field]
        result_geometry = row[shape_field]
        # handle custom geometry searches here based on overlap type
        if selection['overlap_type'] == 'SHARE_A_LINE_SEGMENT_WITH':
            result_lines = result_geometry.to_lines() if isinstance(result_geometry, src.oogeo.objects.polygon.Polygon) else [
                result_geometry]
            # filter results based on overlap type and collect oids
            for geometry in selection['search_objects']:
                geometry_lines = geometry.to_lines() if isinstance(geometry, src.oogeo.objects.polygon.Polygon) else [geometry]
                for result_line in result_lines:
                    for geometry_line in geometry_lines:
                        if result_line.shares_a_segment(geometry_line):
                            result_oid = test_oid
                            break
                    if result_oid >= 0:
                        break
                if result_oid >= 0:
                    break
        elif selection['overlap_type'] == 'BOUNDARY_TOUCHES':
            for geometry in selection['search_objects']:
                if result_geometry.touches(geometry):
                    result_oid = test_oid
                    break
        elif selection['overlap_type'] == 'CROSSED_BY_THE_OUTLINE_OF':
            for geometry in selection['search_objects']:
                if isinstance(result_geometry, src.oogeo.objects.polygon.Polygon):
                    lines = result_geometry.to_lines()
                    for line in lines:
                        if line.crosses(geometry):
                            result_oid = test_oid
                            break
                else:
                    if result_geometry.crosses(geometry):
                        result_oid = test_oid
                        break
        else:
            result_oid = row[oid_field]

        # if we found a result oid, handle it in our list
        if result_oid >= 0:
            if selection['selection_type'] == 'REMOVE_FROM_SELECTION':
                if result_oid in filtered_oids:
                    filtered_oids.remove(result_oid)
            elif selection['selection_type'] == 'SUBSET_SELECTION':
                if result_oid in current_filtered_oids:
                    filtered_oids.add(result_oid)
            else:
                filtered_oids.add(result_oid)

    return filtered_oids


def append_query_string(selection_type, current_query_string, new_query_string):
    """ Appends the new query string to the current string based on selection type.

    :param selection_type: The selection type, which will determine how the queries are joined.
    :param current_query_string: The current query string.
    :param new_query_string: The new query string to be appended to the current string.
    :return: The appended query string.
    """
    if selection_type == 'NEW_SELECTION':
        return new_query_string
    if selection_type == 'ADD_TO_SELECTION':
        return "({}) OR {}".format(current_query_string, new_query_string)
    if selection_type == 'REMOVE_FROM_SELECTION':
        return "({}) AND NOT {}".format(current_query_string, new_query_string)
    if selection_type == 'SUBSET_SELECTION':
        return "({}) AND {}".format(current_query_string, new_query_string)
    # handle final case - 'SWITCH_SELECTION'
    return "NOT ({})".format(current_query_string)


def execute_immediate(selections):
    """ Determines if each query needs to be executed and filtered individually or if a query string can be created.
    Only selection sets that are entirely attribute queries can use an accumulated query string. Selection sets
    that contain geometry queries must be executed individually.

    :param selections: The list of selections in the seleciton set.
    :return: True if each selection should be queried immediately, otherwise False.
    """
    for selection in selections:
        # determine if we can need to run the query now or if it can wait
        # if selection['overlap_type'] in ['SHARE_A_LINE_SEGMENT_WITH', 'BOUNDARY_TOUCHES', 'CROSSED_BY_THE_OUTLINE_OF']:
        if selection['overlap_type'] != 'ATTRIBUTE':
            return True
    return False


def format_query_string(table, query_string):
    """

    :param query_string:
    :return:
    """
    if isinstance(query_string, int):
        return query_string
    shape_field = table.shape if hasattr(table, 'shape') else ''
    query_string = ' {}'.format(query_string)
    for field_name in table.field_names + [table.oid, shape_field]:
        query_string = query_string.replace(' {} '.format(field_name), ' "{}" '.format(field_name))
    query_string = query_string.replace('%', '%%')
    return query_string.strip()


def build_update_clause(table, selections):
    """

    :param table:
    :param selections:
    :return:
    """
    update_clause = ''
    for selection in selections:
        if 'result_query_string' in selection:
            update_clause = selection['result_query_string']
        else:
            update_clause = append_query_string(selection['selection_type'], update_clause, format_query_string(table, selection['update_clause']))
    return 'WHERE {}'.format(update_clause) if update_clause != '' else update_clause


def build_query_string(table, selections, allow_invalid=False):
    """ Builds a query string (WHERE clause) for the provided table based on the list of provided selections.

    :param table: The table to be queried.
    :param selections: The list of dictionaries representing the selections to be made on the table.
    :return: A query string representing the WHERE clause that will return the selected results from the table.
    """

    # loop through selections and build up selection results
    query_string = ''
    from_tables = set()
    filtered_oids = set()
    execute = execute_immediate(selections)
    previous_query_string = None
    for selection in selections:

        # if this portion of the query has already been executed, pull
        # the result query string and move to the next selection object
        if 'result_query_string' in selection:
            previous_query_string = selection['result_query_string']
            query_string = selection['result_query_string']
            filtered_oids = selection['result_object_ids']
            from_tables = set()
            continue

        # begin building up query
        formatted_query = format_query_string(table, selection['query'])
        query_string = append_query_string(selection['selection_type'], query_string, formatted_query) \
            if not execute else formatted_query if not selection['selection_type'] == 'SWITCH_SELECTION' \
            else create_in_clause(filtered_oids, field_name=table.oid, not_operator=True)
        from_tables.update(selection['from_tables'])

        # this is a geometry query - we will need to execute the
        # query and manually filter the results
        if execute:
            sql_clause = ('DISTINCT', None) if selection['overlap_type'] != 'ATTRIBUTE' else (None, None)
            full_query = prepare_query(table, [table.oid, table.shape], query_string, sql_clause)

            # if this is a subset or add to selection, attach the previous results to the query to make it faster
            if previous_query_string:
                full_query = '{} AND ({})'.format(full_query, previous_query_string) \
                    if selection['selection_type'] == 'SUBSET_SELECTION' \
                    else '{} AND NOT ({})'.format(full_query, previous_query_string) \
                    if selection['selection_type'] == 'ADD_TO_SELECTION' else full_query

            # execute the query
            result_layer = table.workspace.execute_simple_sql(full_query)

            # get a list of features to filter
            unfiltered_results = convert_features_to_rows(table, result_layer, [table.oid, table.shape], allow_invalid)

            # filter the features based on their geometries
            filtered_oids = filter_query_results(selection, filtered_oids, unfiltered_results, table.oid, table.shape)

            # replace the current sql statement with an IN clause
            # selecting the oids of the required features, and reset
            # the list of tables (it will be repopulated on the next loop)
            query_string = create_in_clause(filtered_oids, field_name='{}."{}"'.format(table.table_name, table.oid))
            from_tables = set()

            # cache the resulting IN clause and filtered oids for re-use later
            selection['result_query_string'] = query_string
            selection['update_clause'] = query_string
            selection['result_object_ids'] = filtered_oids
            selection['from_tables'] = {f'"{table.schema}"."{table.table_name}"'}
    # return complete query string when complete
    return query_string


def create_insert_row(table, row):
    """ Creates a row that can be inserted into the provided table.

    """
    # map field names to values
    insert_fields = {}
    geometry_columns = [column.lower() for column in
                        table.get_geometry_field_names(include_hidden=True)] if hasattr(table, 'get_geometry_field_names') else []
    for field_name, value in row.items():
        if field_name.lower() in geometry_columns + ['shape@']:
            field_name = table.shape if field_name.lower() == 'shape@' else field_name
            insert_fields[field_name] = value.to_postgis() if hasattr(value, 'to_postgis') else value
        elif field_name.lower() == 'oid@' or field_name.lower() == table.oid.lower():
            continue
        elif field_name in table.field_names:
            insert_fields[field_name] = value
        else:
            raise KeyError('Could not find field {}'.format(field_name))
    return insert_fields

