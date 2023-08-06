"""
Unit tests for the supporting utility functions in the 'utils' directory. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""

import unittest

from src.oogeo.functions.database import create_in_clause
from src.oogeo.functions.conversions import string_to_units, parse_expression


class TableMock(object):

    def __init__(self, table_name):
        self.table_name = table_name
        self.oid = 'id'
        self.shape = 'geom'

    def get_field_type(self, field_name):
        if field_name == 'string_field':
            return 'VARCHAR 100'
        return 'DOUBLE PRECISION'


class UtilsUnitTests(unittest.TestCase):

    def test_create_in_clause(self):
        in_clause = create_in_clause([1, 2])
        self.assertEqual(in_clause, ' IN (1,2)')

        in_clause = create_in_clause([1, 2], use_quotes=True)
        self.assertEqual(in_clause, " IN ('1','2')")

        in_clause = create_in_clause(['1', '2'])
        self.assertEqual(in_clause, ' IN (1,2)')

        in_clause = create_in_clause(['1', '2'], use_quotes=True)
        self.assertEqual(in_clause, " IN ('1','2')")

        in_clause = create_in_clause([1, 2], field_name='field')
        self.assertEqual(in_clause, '"field" IN (1,2)')

        in_clause = create_in_clause([1, 2], field_name='field', not_operator=True)
        self.assertEqual(in_clause, '"field" NOT IN (1,2)')

        in_clause = create_in_clause([1, 2], field_name='field', use_quotes=True)
        self.assertEqual(in_clause, "\"field\" IN ('1','2')")

        in_clause = create_in_clause([1, 2], field_name='field', use_quotes=True, not_operator=True)
        self.assertEqual(in_clause, "\"field\" NOT IN ('1','2')")

    def test_string_to_units(self):
        self.assertEqual(string_to_units('100 FEET', 'FEET'), 100)
        self.assertEqual(string_to_units('1 FOOT', 'FEET'), 1)
        self.assertEqual(string_to_units('100 METERS', 'METERS'), 100)
        self.assertEqual(string_to_units('1 METER', 'METERS'), 1)
        self.assertAlmostEqual(string_to_units('100 FEET', 'METERS'), 30.48, 2)
        self.assertAlmostEqual(string_to_units('1 FOOT', 'METERS'), 0.3048, 4)
        self.assertAlmostEqual(string_to_units('100 METERS', 'FEET'), 328.08, 2)
        self.assertAlmostEqual(string_to_units('1 METER', 'FEET'), 3.2808, 4)

    def test_parse_expression(self):
        table_mock = TableMock('TABLE_NAME')
        self.assertEqual(parse_expression(table_mock, 'int_field', 0), 0)
        self.assertEqual(parse_expression(table_mock, 'double_field', 1.1), 1.1)
        self.assertEqual(parse_expression(table_mock, 'double_field', 1.1), 1.1)
        self.assertEqual(parse_expression(table_mock, 'id', 'id = 1'), 'id = 1')
        self.assertEqual(parse_expression(table_mock, 'id', 'id != 1'), 'id != 1')
        self.assertEqual(parse_expression(table_mock, 'string_field', "'1'"), "'1'")
        self.assertEqual(parse_expression(table_mock, 'string_field', "'string value'"), "'string value'")
        self.assertEqual(parse_expression(table_mock, 'string_field', "1"), "'1'")
        self.assertEqual(parse_expression(table_mock, 'string_field', "string value"), "'string value'")
        self.assertEqual(parse_expression(table_mock, 'string_field', "string's value's"), "'string''s value''s'")
        self.assertEqual(parse_expression(table_mock, 'string_field', "'string's value's'"), "'string''s value''s'")
        self.assertEqual(parse_expression(table_mock, 'string_field', "!FIELD_NAME!"), '"FIELD_NAME"')
        self.assertEqual(parse_expression(table_mock, 'string_field', 'NULL'), 'NULL')
        self.assertEqual(parse_expression(table_mock, 'int_field', 'NULL'), 'NULL')
        self.assertEqual(parse_expression(table_mock, 'string_field', None), 'NULL')
        self.assertEqual(parse_expression(table_mock, 'int_field', None), 'NULL')
        self.assertEqual(parse_expression(table_mock, 'int_field', "!FIELD_NAME!"), '"FIELD_NAME"')
        self.assertEqual(parse_expression(table_mock, 'string_field', "!FIELD_NAME! = 'string_value'"), '"FIELD_NAME" = \'string_value\'')
        self.assertEqual(parse_expression(table_mock, 'int_field', "!FIELD_NAME! = 'string_value'"), '"FIELD_NAME" = \'string_value\'')
        self.assertEqual(parse_expression(table_mock, 'int_field', "!FIELD_NAME! = 1"), '"FIELD_NAME" = 1')
        self.assertEqual(parse_expression(table_mock, 'string_field', "!FIELD_NAME! = 1"), '"FIELD_NAME" = 1')
        self.assertEqual(parse_expression(table_mock, 'string_field', "!FIELD_NAME! != 1"), '"FIELD_NAME" != 1')
        self.assertEqual(parse_expression(table_mock, 'int_field', "!FIELD_NAME! != 1"), '"FIELD_NAME" != 1')
        self.assertEqual(parse_expression(table_mock, 'int_field', "SUM(!FIELD_NAME!) + 1"), 'SUM("FIELD_NAME") + 1')
        self.assertEqual(parse_expression(table_mock, 'string_field', "SUM(!FIELD_NAME!) + 1"), 'SUM("FIELD_NAME") + 1')
        self.assertEqual(parse_expression(table_mock, 'string_field', "!SHAPE.AREA@SQUAREFEET!"), 'ST_Area("geom")')
        self.assertEqual(parse_expression(table_mock, 'int_field', "!SHAPE.AREA@SQUAREFEET!"), 'ST_Area("geom")')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UtilsUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
