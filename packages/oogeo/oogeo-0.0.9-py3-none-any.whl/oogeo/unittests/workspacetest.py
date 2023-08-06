"""
Unit tests for the Workspace class. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""


import unittest

from src.oogeo.unittests.databasetest import DatabaseTest
from src.oogeo.objects.layer import Layer
from src.oogeo.objects.table import Table
from src.oogeo.objects.workspace import Workspace


class WorkspaceClassUnitTests(DatabaseTest):

    def test_initialize_workspace(self):
        # verify we can initialize a workspace object without failure
        test_workspace = Workspace(self._databases['testing_inputs'])
        self.assertIsInstance(test_workspace, Workspace)

    def test_is_gdb(self):
        # load a gdb workspace and verify the is_gdb property
        test_workspace = Workspace(self._databases['testing_inputs'])
        self.assertTrue(test_workspace.is_gdb)

    def test_list_featureclasses(self):
        # get the list of feature classes from the test gdb (there is only 1)
        test_workspace = Workspace(self._databases['testing_inputs'])
        feature_classes = test_workspace.list_feature_classes()
        self.assertEqual(len(feature_classes), 4)
        self.assertEqual(feature_classes[0], 'adjacent_shapes')
        self.assertEqual(feature_classes[1], 'physical_blocks')
        self.assertEqual(feature_classes[2], 'snap_targets')
        self.assertEqual(feature_classes[3], 'zoning_districts')

        # test filter function
        feature_classes = test_workspace.list_feature_classes(wildcards='zon*')
        self.assertEqual(len(feature_classes), 1)
        self.assertEqual(feature_classes[0], 'zoning_districts')
        feature_classes = test_workspace.list_feature_classes(wildcards='zoning_districts*')
        self.assertEqual(len(feature_classes), 1)
        self.assertEqual(feature_classes[0], 'zoning_districts')
        feature_classes = test_workspace.list_feature_classes(wildcards='zoning_districts')
        self.assertEqual(len(feature_classes), 1)
        self.assertEqual(feature_classes[0], 'zoning_districts')
        feature_classes = test_workspace.list_feature_classes(wildcards=['zoning_districts*'])
        self.assertEqual(len(feature_classes), 1)
        self.assertEqual(feature_classes[0], 'zoning_districts')
        feature_classes = test_workspace.list_feature_classes(wildcards=['zoning_districts*', '*zoning_districts'])
        self.assertEqual(len(feature_classes), 1)
        self.assertEqual(feature_classes[0], 'zoning_districts')

    def test_create_featureclasses(self):
        # create a feature class and then delete it
        test_workspace = Workspace(self._databases['testing_inputs'])
        feature_class = test_workspace.create_feature_class('create_point_test', 'Point')
        feature_classes = test_workspace.list_feature_classes()
        self.assertIsInstance(feature_class, Layer)
        self.assertEqual(len(feature_classes), 5)
        self.assertIn('create_point_test', feature_classes)
        feature_class.delete()

        feature_class = test_workspace.create_feature_class('create_line_test', 'Polyline')
        feature_classes = test_workspace.list_feature_classes()
        self.assertIsInstance(feature_class, Layer)
        self.assertEqual(len(feature_classes), 5)
        self.assertIn('create_line_test', feature_classes)
        feature_class.delete()

        feature_class = test_workspace.create_feature_class('create_polygon_test', 'Polygon')
        feature_classes = test_workspace.list_feature_classes()
        self.assertIsInstance(feature_class, Layer)
        self.assertEqual(len(feature_classes), 5)
        self.assertIn('create_polygon_test', feature_classes)
        feature_class.delete()

        feature_classes = test_workspace.list_feature_classes()
        self.assertEqual(len(feature_classes), 4)
        self.assertNotIn('create_point_test', feature_classes)
        self.assertNotIn('create_line_test', feature_classes)
        self.assertNotIn('create_polygon_test', feature_classes)

    def test_list_tables(self):
        # get the list of tables from the test gdb (there is only `)
        test_workspace = Workspace(self._databases['testing_inputs'])
        tables = test_workspace.list_tables()
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0], 'adjacent_lots')
        tables = test_workspace.list_tables('a*')
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0], 'adjacent_lots')
        tables = test_workspace.list_tables('*s')
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0], 'adjacent_lots')
        tables = test_workspace.list_tables(['a*', '*s'])
        self.assertEqual(len(tables), 1)
        self.assertEqual(tables[0], 'adjacent_lots')
        tables = test_workspace.list_tables('xy*')
        self.assertEqual(len(tables), 0)
        tables = test_workspace.list_tables('*xy')
        self.assertEqual(len(tables), 0)

    def test_load(self):
        test_workspace = Workspace(self._databases['testing_inputs'])
        test_table = test_workspace.load('adjacent_lots')
        self.assertIsInstance(test_table, Table)
        test_layer = test_workspace.load('physical_blocks')
        self.assertIsInstance(test_layer, Layer)

    def test_create_table(self):
        # create a table and then delete it
        test_workspace = Workspace(self._databases['testing_inputs'])
        table = test_workspace.create_table('create_table_test')
        tables = test_workspace.list_tables()
        self.assertIsInstance(table, Table)
        self.assertEqual(len(tables), 2)
        self.assertIn('create_table_test', tables)
        table.delete()
        tables = test_workspace.list_tables()
        self.assertEqual(len(tables), 1)
        self.assertNotIn('create_table_test', tables)

    def test_create_geodatabase(self):
        # create a new database
        dbless_connection = self._databases['testing_inputs'].copy()
        dbless_connection['database'] = None
        temp_workspace = Workspace.create_geodatabase(dbless_connection, 'test_geodatabase')
        self.assertIsInstance(temp_workspace, Workspace)
        self.assertIn('test_geodatabase', temp_workspace.list_databases())

        # copy tables and layers from one db to another
        inputs_workspace = Workspace(self._databases['testing_inputs'])
        test_table = Table('adjacent_lots', inputs_workspace)
        test_layer = Layer('adjacent_shapes', inputs_workspace)
        test_table.copy_to_new_table(test_table.table_name, temp_workspace)
        test_layer.copy_to_new_table(test_layer.table_name, temp_workspace)
        self.assertIn(test_table.table_name, temp_workspace.list_tables())
        self.assertNotIn(test_table.table_name, temp_workspace.list_feature_classes())
        self.assertIn(test_layer.table_name, temp_workspace.list_feature_classes())
        self.assertNotIn(test_layer.table_name, temp_workspace.list_tables())

        # delete the temp database
        temp_workspace.disconnect()
        Workspace.drop_geodatabase(dbless_connection, 'test_geodatabase')
        self.assertNotIn('test_geodatabase', inputs_workspace.list_databases())

    def test_schema_operations(self):
        test_workspace = Workspace(self._databases['testing_inputs'])
        self.assertFalse(test_workspace.has_schema('testing'))
        schema_names = test_workspace.list_schemas()
        self.assertEqual(len(schema_names), 1)
        self.assertIn('public', schema_names)
        new_workspace = test_workspace.create_schema('testing')
        self.assertTrue(test_workspace.has_schema('testing'))
        self.assertTrue(new_workspace.has_schema('testing'))
        self.assertEqual(test_workspace.schema, 'public')
        self.assertEqual(new_workspace.schema, 'testing')
        self.assertEqual(len(new_workspace.list_tables_and_layers()), 0)
        schema_names = test_workspace.list_schemas()
        self.assertEqual(len(schema_names), 2)
        self.assertIn('public', schema_names)
        self.assertIn('testing', schema_names)
        new_workspace.drop_schema('testing')
        self.assertFalse(test_workspace.has_schema('testing'))
        self.assertFalse(new_workspace.has_schema('testing'))
        schema_names = test_workspace.list_schemas()
        self.assertEqual(len(schema_names), 1)
        self.assertIn('public', schema_names)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WorkspaceClassUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
