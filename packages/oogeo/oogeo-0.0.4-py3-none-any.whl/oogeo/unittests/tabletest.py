"""
Unit tests for the Table class. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""

import unittest

from src.oogeo.unittests.databasetest import DatabaseTest
from src.oogeo.objects.table import Table
from src.oogeo.objects.workspace import Workspace


class TableClassUnitTests(DatabaseTest):

    def setUp(self):
        # load the test table
        if not hasattr(self, 'test_table'):
            self.workspace = Workspace(self._databases['testing_inputs'])
            self.test_table = Table('adjacent_lots', self.workspace)

    def test_create_table_from_workspace(self):
        # verify that tables created by the workspace object function correctly
        with self.workspace.create_table('create_table_test', schema='testing') as table:
            table.add_field('test_str', 'TEXT')
            table.add_field('test_int', 'SHORT')
            table.add_field('test_dbl', 'DOUBLE')
            table.add_field('test_bool', 'BOOLEAN')
            rows = [
                {
                    'test_str': 'A',
                    'test_int': 1,
                    'test_dbl': 1.1,
                    'test_bool': True,
                },
                {
                    'test_str': 'B',
                    'test_int': 2,
                    'test_dbl': 2.2,
                    'test_bool': False,
                },
            ]
            table.add_rows(rows)
            self.assertEqual(table.count, 2)

            table.select_layer_by_attribute('test_int = 1')
            with table.get_search_cursor(['test_str', 'test_dbl', 'test_bool']) as cursor:
                row = next(cursor)
            self.assertEqual(row['test_str'], 'A')
            self.assertEqual(row['test_dbl'], 1.1)
            self.assertTrue(row['test_bool'])

            table.select_layer_by_attribute('test_int = 2')
            with table.get_search_cursor(['test_str', 'test_dbl', 'test_bool']) as cursor:
                row = next(cursor)
            self.assertEqual(row['test_str'], 'B')
            self.assertEqual(row['test_dbl'], 2.2)
            self.assertFalse(row['test_bool'])
        self.workspace.drop_schema('testing')

    def test_initialize_layer(self):
        # verify we can initialize a layer object without failure
        self.assertIsInstance(self.test_table, Table)

    def test_select_layer_by_attribute(self):
        # get the total rows in the table
        with self.test_table.copy_to_new_table(self.test_table.table_name, output_schema='testing') as local_table:
            total_rows = local_table.count

            # make a selection in the layer and test it
            local_table.select_layer_by_attribute('OBJECTID = 1')
            self.assertEqual(local_table.get_selection_count(), 1)
            self.assertEqual(local_table.count, 1)

            # select two more to test the add to selection function
            local_table.select_layer_by_attribute('OBJECTID = 2 OR OBJECTID = 3', selection_type='ADD_TO_SELECTION')
            self.assertEqual(local_table.get_selection_count(), 3)
            self.assertEqual(local_table.count, 3)

            # remove one from the selection set with the subset selection option
            local_table.select_layer_by_attribute('OBJECTID = 2 OR OBJECTID = 3', selection_type='SUBSET_SELECTION')
            self.assertEqual(local_table.get_selection_count(), 2)
            self.assertEqual(local_table.count, 2)

            # remove one from the selection set with the remove from option
            local_table.select_layer_by_attribute('OBJECTID = 2', selection_type='REMOVE_FROM_SELECTION')
            self.assertEqual(local_table.get_selection_count(), 1)
            self.assertEqual(local_table.count, 1)

            # switch the selection
            local_table.select_layer_by_attribute('OBJECTID = 2', selection_type='SWITCH_SELECTION')
            self.assertEqual(local_table.get_selection_count(), total_rows - 1)
            self.assertEqual(local_table.count, total_rows - 1)

            local_table.select_layer_by_attribute('OBJECTID = 1')
            self.assertEqual(local_table.get_selection_count(), 1)
            self.assertEqual(local_table.count, 1)

            # clear the selection
            local_table.clear_selection()
            self.assertEqual(local_table.get_selection_count(), total_rows)
            self.assertEqual(local_table.count, total_rows)

        # clean up testing schema
        self.workspace.drop_schema('testing')

    def test_oid_property(self):

        # test the oid property
        self.assertEqual(self.test_table.oid, 'OBJECTID')

    def test_max_oid(self):
        self.assertEqual(self.test_table.max_oid, 5)

    def test_field_names_property(self):
        self.assertIn('CBBL', self.test_table.field_names)
        self.assertIn('nbr_CBBL', self.test_table.field_names)
        self.assertIn('NODE_COUNT', self.test_table.field_names)
        self.assertIn('LENGTH', self.test_table.field_names)
        self.assertNotIn('OBJECTID', self.test_table.field_names)
        self.assertNotIn('SHAPE', self.test_table.field_names)

    def test_duplicate_table(self):
        with self.test_table.duplicate_table('duplicated_table_test', output_schema='testing') as duplicate_table:
            self.assertIsInstance(duplicate_table, Table)
            self.assertEqual(duplicate_table.count, 0)
            for field in self.test_table.field_names:
                self.assertIn(field, duplicate_table.field_names)
        self.workspace.drop_schema('testing')

    def test_fields_property(self):

        # test the field property
        fields = [field.name for field in self.test_table.fields]
        self.assertIn('CBBL', fields)

    def test_switch_and_clear_selection(self):

        # get the total rows in the table
        total_rows = self.test_table.count

        # make a selection in the layer, switch the selection, and test it
        self.test_table.select_layer_by_attribute('OBJECTID = 1')
        self.test_table.switch_selection()
        self.assertEqual(self.test_table.count, total_rows - 1)

        # clear the selection and test that
        self.test_table.clear_selection()
        self.assertEqual(self.test_table.count, total_rows)

    def test_field_functions(self):
        # add a new field to the table
        with self.test_table.copy_to_new_table('field_test', output_schema='testing') as test_table:
            test_table.add_field('test', 'TEXT')

            # test that the new field is in the list of fields
            fields = test_table.field_names
            self.assertIn('test', fields)

            # calculate a value into the field
            test_table.calculate_field('test', "'Test Text'")

            # add a second new field with a precalculated value
            test_table.add_field('TEST_2', 'TEXT',
                default_value="'Test Text'")

            # select a row in the table and verify calculated field
            with test_table.get_search_cursor(['test', 'TEST_2'],
                query_string='OBJECTID = 1') as cursor:
                for row in cursor:
                    self.assertEqual(row['test'], 'Test Text')
                    self.assertEqual(row['TEST_2'], 'Test Text')

            # delete one of the columns and verify
            test_table.delete_field('test')

            # rename the test_2 field to test_3
            test_table.rename_field('TEST_2', 'TEST_3')
            fields = test_table.field_names
            self.assertIn('TEST_3', fields)
            self.assertNotIn('TEST_2', fields)

            # add a new field and test the copy field values function
            test_table.add_field('test_4', 'TEXT')
            test_table.copy_field_values('TEST_3', 'test_4')

            # add a new field and test copying with the calculate field function
            test_table.add_field('test_5', 'TEXT')
            test_table.add_field('test_6', 'LONG')
            test_table.add_field('test_7', 'LONG')
            test_table.calculate_field('test_5', '!test_4!')
            test_table.calculate_field('test_6', '!{}!'.format(test_table.oid))
            test_table.calculate_field('test_7', '!test_6! * 2')
            # verify that the values in test 3 were copied to test 4
            with test_table.get_search_cursor(['TEST_3', 'test_4', 'test_5', 'test_6', 'test_7'],
                query_string='OBJECTID = 1') as cursor:
                for row in cursor:
                    self.assertEqual(row['TEST_3'], row['test_4'])
                    self.assertEqual(row['test_4'], row['test_5'])
                    self.assertEqual(row['test_6'], 1)
                    self.assertEqual(row['test_7'], 2)

            # delete the other field indirectly using the delete other fields method and test
            test_table.delete_other_fields(['nbr_CBBL', 'LENGTH', 'NODE_COUNT', 'CBBL'])

            # test that the new field is not in the list of fields
            fields = test_table.field_names
            self.assertIn('nbr_CBBL', fields)
            self.assertIn('LENGTH', fields)
            self.assertIn('NODE_COUNT', fields)
            self.assertIn('CBBL', fields)
            self.assertNotIn('TEST_3', fields)
            self.assertNotIn('test_4', fields)
            self.assertNotIn('test_5', fields)
            self.assertNotIn('test_6', fields)
        self.workspace.drop_schema('testing')

    def test_get_field_type(self):
        # verify the field types in the test table
        self.assertEqual(self.test_table.get_field_type('CBBL'), 'VARCHAR(255)')
        self.assertEqual(self.test_table.get_field_type('NODE_COUNT'), 'INTEGER')
        self.assertEqual(self.test_table.get_field_type('LENGTH'), 'DOUBLE PRECISION')

    def test_get_unique_field_values(self):
        # get the list of distinct node_count values and test it (there is only 1 value in the table - 0)
        node_counts = self.test_table.get_unique_field_values('NODE_COUNT')
        self.assertEqual(len(node_counts), 1)
        for node_count in node_counts:
            self.assertEqual(node_count, 0)
        cbbls = self.test_table.get_unique_field_values('CBBL')
        self.assertEqual(len(cbbls), 4)
        self.assertIn('NY-MN-10-15', cbbls)
        self.assertIn('NY-MN-10-16', cbbls)
        self.assertIn('NY-MN-10-1', cbbls)
        self.assertIn('NY-MN-10-14', cbbls)

    def test_get_distinct_field_values(self):
        single_field = self.test_table.get_distinct_field_values('NODE_COUNT')
        self.assertEqual(len(single_field), 1)
        self.assertIn({'NODE_COUNT': 0}, single_field)

        multi_fields = self.test_table.get_distinct_field_values(['NODE_COUNT', 'CBBL'])
        self.assertEqual(len(multi_fields), 4)
        self.assertIn({'NODE_COUNT': 0, 'CBBL': 'NY-MN-10-15'}, multi_fields)
        self.assertIn({'NODE_COUNT': 0, 'CBBL': 'NY-MN-10-16'}, multi_fields)
        self.assertIn({'NODE_COUNT': 0, 'CBBL': 'NY-MN-10-1'}, multi_fields)
        self.assertIn({'NODE_COUNT': 0, 'CBBL': 'NY-MN-10-14'}, multi_fields)

    def test_row_manipulation_methods(self):
        with self.test_table.copy_to_new_table(self.test_table.table_name, output_schema='testing') as local_table:
            # get a baseline count of the number of rows in the table
            base_count = local_table.count

            # insert a row into the table
            new_rows = [
                {'CBBL': 'test-cbbl-value', 'nbr_CBBL': 'test-nbr-cbbl-value', 'LENGTH': 0.1, 'NODE_COUNT': 0}
            ]
            local_table.add_rows(new_rows)

            # verify that the new row has been added
            self.assertEqual(local_table.count, base_count + 1)

            # get the new row with an update cursor and update it (the new row will have an oid > 5)
            with local_table.get_update_cursor('NODE_COUNT', 'OBJECTID > 5') as cursor:
                for row in cursor:
                    row['NODE_COUNT'] = 1
                    cursor.update_row(row)

            # query the new row back out with a search cursor and verify the update
            with local_table.get_search_cursor('NODE_COUNT', 'OBJECTID > 5') as cursor:
                for row in cursor:
                    self.assertEqual(row['NODE_COUNT'], 1)

            # delete the new row and verify that it's gone
            local_table.select_layer_by_attribute('OBJECTID > 5')
            local_table.delete_selected_rows()
            local_table.clear_selection()
            self.assertEqual(local_table.count, base_count)
        self.workspace.drop_schema('testing')

    def test_copy_to_new_table_and_delete_table(self):
        # select a few rows and copy them to a new table
        self.test_table.select_layer_by_attribute('OBJECTID > 3')
        copy_table = self.test_table.copy_to_new_table('copy_table_test')
        self.test_table.clear_selection()

        # verify the table has been added
        table_list = self.workspace.list_tables()
        self.assertEqual(len(table_list), 2)
        self.assertIn('copy_table_test', table_list)

        # verify the fields in the tables match
        base_fields = [field.name for field in self.test_table.fields]
        copy_fields = [field.name for field in copy_table.fields]
        self.assertListEqual(base_fields, copy_fields)

        # test adding an index to the table
        copy_table.add_index('CBBL')
        self.assertIn('idx_copy_table_test_CBBL', copy_table.list_indexes())

        # verify there are 2 rows in the new table
        self.assertEqual(copy_table.count, 2)

        # delete the new table and verify it's gone
        copy_table.delete()
        table_list = self.workspace.list_tables()
        self.assertEqual(len(table_list), 1)
        self.assertNotIn('copy_table', table_list)

    def test_append(self):
        # select a few rows and copy them to a new table
        self.test_table.select_layer_by_attribute('OBJECTID > 3')
        copy_table = self.test_table.copy_to_new_table('copy_table_test')
        self.test_table.clear_selection()

        # append the test table to the copy table and verify the row count
        combined_count = self.test_table.count + copy_table.count
        copy_table.append(self.test_table, 'TEST')
        self.assertEqual(copy_table.count, combined_count)

        # delete the new table
        copy_table.delete()

    def test_delete_duplicates(self):
        # get a baseline count of the number of rows in the table
        base_count = self.test_table.count

        # duplicate a row in the table
        new_rows = []
        with self.test_table.get_search_cursor(['CBBL', 'nbr_CBBL', 'LENGTH', 'NODE_COUNT'],
            query_string='OBJECTID = 1') as cursor:
            for row in cursor:
                # insert a row into the table
                new_rows.append({'CBBL': row['CBBL'], 'nbr_CBBL': row['nbr_CBBL'], 'LENGTH': row['LENGTH'], 'NODE_COUNT': row['NODE_COUNT']})
        self.test_table.add_rows(new_rows)
        # verify that the new row has been added
        self.assertEqual(self.test_table.count, base_count + 1)

        # delete duplicate rows
        self.test_table.delete_duplicates(['CBBL', 'nbr_CBBL', 'LENGTH', 'NODE_COUNT'])

        # verify that one row is gone
        self.assertEqual(self.test_table.count, base_count)

    def test_list_fields(self):
        fields = self.test_table.list_fields()
        self.assertEqual(len(fields), 5)
        fields = self.test_table.list_fields(type='String')
        self.assertEqual(len(fields), 2)
        fields = self.test_table.list_fields(type='Integer')
        self.assertEqual(len(fields), 2)
        fields = self.test_table.list_fields(type='Float')
        self.assertEqual(len(fields), 1)

    def test_delete_rows(self):
        # get a baseline count of the number of rows in the table
        base_count = self.test_table.count

        # duplicate a row in the table
        new_rows = []
        with self.test_table.get_search_cursor(['CBBL', 'nbr_CBBL', 'LENGTH', 'NODE_COUNT'],
            query_string='OBJECTID = 1') as cursor:
            for row in cursor:
                # insert a row into the table
                new_rows.append({'CBBL': row['CBBL'], 'nbr_CBBL': row['nbr_CBBL'], 'LENGTH': row['LENGTH'], 'NODE_COUNT': row['NODE_COUNT']})
        self.test_table.add_rows(new_rows)
        # verify that the new row has been added
        self.assertEqual(self.test_table.count, base_count + 1)

        # delete the new row
        self.test_table.select_layer_by_attribute('{} > 5'.format(self.test_table.oid))
        self.test_table.delete_selected_rows()

        # verify that one row is gone
        self.assertEqual(self.test_table.count, base_count)

    # def test_to_csv(self):
    #     # get a baseline count of the number of rows in the table
    #     base_count = self.test_table.count
    #
    #     # find the export path
    #     unittest_root = path.abspath(path.dirname(__file__))
    #     code_root = path.dirname(unittest_root)
    #     package_root = path.dirname(code_root)
    #     working_directory = path.join(package_root, self._configurations.get('WorkingDirectories', 'working_directory'))
    #
    #     # export the table to csv
    #     csv_fields = ['OBJECTID', 'CBBL', 'nbr_CBBL', 'LENGTH', 'NODE_COUNT']
    #     csv_file = path.join(working_directory, 'test_export.csv')
    #     self.test_table.to_csv(csv_file, csv_fields)
    #
    #     # read the exported csv file and make sure it's correct
    #     with open(csv_file, 'r') as file_reader:
    #         csv_reader = csv.reader(file_reader)
    #         csv_records = [
    #             {'OBJECTID': row[0], 'CBBL': row[1], 'nbr_CBBL': row[2], 'LENGTH': row[3], 'NODE_COUNT': row[4]}
    #             for row in csv_reader]
    #
    #     # verify that there is one more record in the csv file than in the table (this is the header row)
    #     self.assertEqual(len(csv_records), base_count + 1)
    #
    #     # verify that all of the fields are in the csv
    #     output_fields = sorted([value for value in csv_records[0]])
    #     csv_fields = sorted(csv_fields)
    #     self.assertListEqual(output_fields, csv_fields)
    #
    #     # delete the test file
    #     remove(csv_file)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableClassUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
