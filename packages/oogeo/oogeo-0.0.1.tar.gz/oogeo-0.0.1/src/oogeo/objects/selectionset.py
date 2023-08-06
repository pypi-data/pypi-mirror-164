""" Class containing methods related to selection sets.

"""

from src.oogeo.functions.database import prepare_query, format_query_string


class SelectionSet(object):
    """ Class containing methods related to selection sets.

    """

    def __init__(self, table, field_names=None, query_string='', sql_clause='', allow_invalid=False):
        """ Initializes the selection set object.

        """
        self.source_table = table
        self.allow_invalid = allow_invalid
        self.field_names = table.field_names + [table.shape] if field_names is None else [field_names] \
            if isinstance(field_names, str) else field_names
        self.full_query = prepare_query(table, self.field_names, format_query_string(table, query_string), sql_clause)
        self.results = self.source_table.workspace.execute_simple_sql(self.full_query)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Destroys the results layer after iteration is complete.

        """
        return

