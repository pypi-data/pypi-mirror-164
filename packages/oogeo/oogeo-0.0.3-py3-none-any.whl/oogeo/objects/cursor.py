# coding=utf-8
""" Contains objects related to cursors.

"""

from src.oogeo.objects.selectionset import SelectionSet
from src.oogeo.functions.database import convert_feature_to_row


class SearchCursor(SelectionSet):
    """ Provides iterable for walking through table query results

    """

    def __init__(self, table, field_names, query_string, sql_clause, allow_invalid=False):
        """ Initializes the search cursor object.

        :param table: The table that the search cursor is based on.
        :param field_names: The list of field names to return in the cursor.
        :param query_string: The query string to define the contents of the cursor.
        :param sql_clause: Any SQL pre/post clauses to be applied.
        :param allow_invalid: If true, errors for invalid geometries will be ignored. Set this
            flag to true when loading datasets where you expect to encounter invalid geometries.
        """
        super(SearchCursor, self).__init__(table, field_names, query_string, sql_clause, allow_invalid)
        self.current_feature = None

    def __iter__(self):
        return self

    def __next__(self):
        """ Iterates over the rows in the cursor.

        :return: The next row in the cursor as a list of field values.
        """
        self.current_feature = next(self.results)

        if self.current_feature is None:
            raise StopIteration

        if '*' in self.field_names:
            self.field_names = self.source_table.field_names + [self.source_table.oid]
            self.field_names = self.field_names + [self.source_table.shape] if hasattr(self.source_table, 'shape') else self.field_names

        return convert_feature_to_row(self.source_table, self.current_feature, self.field_names, self.allow_invalid)

    def __exit__(self, exc_type, exc_value, traceback):
        """ Destroys the results layer after iteration is complete.

        """
        self.current_feature = None
        super(SearchCursor, self).__exit__(exc_type, exc_value, traceback)

    def __len__(self):
        """ Returns the number of features in the cursor.

        :return: The number of features in the cursor
        """
        return self.results.rowcount


class InsertCursor(object):
    """ Provides cursor for inserting rows into a table.

    """

    def __init__(self, layer, field_names):
        """ Initializes the `InsertCursor()` object.

        :param layer: The layer that the cursor will insert rows into.
        :param field_names: The field names to be altered.
        """
        self.layer = layer

        # validate field names
        if isinstance(field_names, str):
            field_names = layer.field_names if field_names == '*' else [field_names]
        self.field_names_to_write = field_names

    def insert_row(self, row):
        """ Inserts a row into the table.

        :param row: The row to be inserted.
        """

        # map field names to values
        insert_fields = {}
        geometry_columns = [column.lower() for column in self.layer.get_geometry_field_names(include_hidden=True)] if hasattr(self.layer, 'get_geometry_field_names') else []
        for field_name, value in row.items():
            if field_name.lower() in geometry_columns + ['shape@']:
                field_name = self.layer.shape if field_name.lower() == 'shape@' else field_name
                insert_fields[field_name] = value.to_postgis() if hasattr(value, 'to_postgis') else value
            elif field_name.lower() == 'oid@' or field_name.lower() == self.layer.oid.lower():
                continue
            elif field_name in self.layer.field_names:
                insert_fields[field_name] = value
            else:
                raise KeyError('Could not find field {}'.format(field_name))

        insert_statement = self.layer.alchemy_table.insert().values(**insert_fields)
        self.layer.workspace.execute_simple_sql(insert_statement)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return


class UpdateCursor(SearchCursor):
    """ Provides a cursor for updating rows in the database.

    """
    def __init__(self, table, field_names, query_string, sql_clause, allow_invalid=False):
        """ Initializes the update cursor object.

        :param table: The table that the search cursor is based on.
        :param field_names: The list of field names to return in the cursor.
        :param query_string: The query string to define the contents of the cursor.
        :param sql_clause: Any SQL pre/post clauses to be applied.
        :param allow_invalid: If true, errors for invalid geometries will be ignored. Set this
            flag to true when loading datasets where you expect to encounter invalid geometries.
        """
        super(UpdateCursor, self).__init__(table, field_names, query_string, sql_clause, allow_invalid)

    def update_row(self, row):
        """ Updates the database with the values in the specified row.

        :param row: The row object to be updated.
        """
        row_id = self.current_feature['table_oid']
        update_fields = {}
        for field_name, value in row.items():
            if field_name.lower() == 'shape@' or \
                    (hasattr(self.source_table, 'shape') and field_name.lower() == self.source_table.shape.lower()):
                update_fields[self.source_table.shape] = value.to_postgis()
            elif 'shape@' not in field_name.lower() and 'oid@' not in field_name.lower() and field_name.lower() != self.source_table.oid.lower():
                update_fields[field_name] = value

        self.source_table.workspace.execute_simple_sql(
            self.source_table.alchemy_table.update().where(getattr(self.source_table.alchemy_table.c, self.source_table.oid) == row_id).values(**update_fields)
        )

    def delete_row(self):
        """ Deletes the current row.

        :return: None
        """
        row_id = self.current_feature['table_oid']
        self.source_table.workspace.execute_simple_sql(
            self.source_table.alchemy_table.delete().where(getattr(self.source_table.alchemy_table.c, self.source_table.oid) == row_id)
        )
