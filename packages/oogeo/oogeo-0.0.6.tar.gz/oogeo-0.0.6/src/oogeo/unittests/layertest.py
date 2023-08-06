"""
Unit tests for the Layer class. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""

from src.oogeo.unittests.databasetest import DatabaseTest
from src.oogeo.objects.layer import Layer
from src.oogeo.objects.line import Line
from src.oogeo.objects.point import Point
from src.oogeo.objects.polygon import Polygon
from src.oogeo.objects.table import Table
from src.oogeo.objects.workspace import Workspace


class LayerClassUnitTests(DatabaseTest):
    def setUp(self):
        # load the test layer
        if not hasattr(self, 'test_layer'):
            self.workspace = Workspace(self._databases['testing_inputs'])
            self.test_layer = Layer('physical_blocks', self.workspace)
            self.overlay_layer = Layer('zoning_districts', self.workspace)
            self.adjacent_layer = Layer('adjacent_shapes', self.workspace)
            self.snap_targets_layer = Layer('snap_targets', self.workspace)

    def test_initialize_layer(self):
        # verify we can initialize a layer object without failure
        self.assertIsInstance(self.test_layer, Layer)

    def test_calculate_field(self):
        with self.test_layer.copy_to_new_table('layer_calc_field_test', output_schema='testing') as test_layer:
            test_point = Point((982609, 206224), self.test_layer.spatial_reference)
            test_layer.select_layer_by_location('CONTAINS', test_point)
            self.assertEqual(test_layer.count, 1)
            test_layer.calculate_field('borough', "'XX'")
            test_layer.select_layer_by_attribute("borough = 'XX'")
            self.assertEqual(test_layer.count, 1)
            test_layer.calculate_field('borough', "'MN'")

            # test shares a line segment with
            test_layer.select_layer_by_attribute(1)
            with test_layer.get_search_cursor([test_layer.shape]) as cursor:
                shared_polygon = next(cursor)[test_layer.shape]
            shared_line = shared_polygon.to_lines()[0]
            test_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', shared_line)
            self.assertEqual(test_layer.count, 1)
            test_layer.calculate_field('borough', "'XX'")
            test_layer.select_layer_by_attribute("borough = 'XX'")
            self.assertEqual(test_layer.count, 1)
            test_layer.calculate_field('borough', "'MN'")
            self.assertEqual(test_layer.count, 0)

            test_layer.select_layer_by_location('CONTAINS', test_point)
            test_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', shared_line, selection_type='ADD_TO_SELECTION')
            self.assertEqual(test_layer.get_selection_count(), 2)
            test_layer.calculate_field('borough', "'XX'")
            test_layer.select_layer_by_attribute("borough = 'XX'")
            self.assertEqual(test_layer.count, 2)
            test_layer.calculate_field('borough', "'MN'")
            self.assertEqual(test_layer.count, 0)

            # test cases for https://github.com/envelopecity/osgis/issues/158
            # add a few new polygons to the test layer
            left_polygon = Polygon([
                {'x': 0, 'y': 0},
                {'x': 2, 'y': 0},
                {'x': 2, 'y': 2},
                {'x': 0, 'y': 2},
                {'x': 0, 'y': 0},
            ], 2263)
            right_polygon = Polygon([
                {'x': 2, 'y': 0},
                {'x': 4, 'y': 0},
                {'x': 4, 'y': 2},
                {'x': 2, 'y': 2},
                {'x': 2, 'y': 0},
            ], 2263)

            test_layer.clear_selection()
            test_layer.add_rows([
                {'borough': 'XX', test_layer.shape: left_polygon},
                {'borough': 'XX', test_layer.shape: right_polygon}
            ])

            contained_polygon = Polygon([
                {'x': 0.5, 'y': 0.5},
                {'x': 1.5, 'y': 0.5},
                {'x': 1.5, 'y': 1.5},
                {'x': 0.5, 'y': 1.5},
                {'x': 0.5, 'y': 0.5},
            ], 2263)
            test_layer.select_layer_by_location('CONTAINS', contained_polygon)
            test_layer.calculate_field('borough', "'YY'")
            test_layer.select_layer_by_attribute("borough = 'YY'")
            self.assertEqual(test_layer.count, 1)
            test_layer.calculate_field('borough', "'XX'")

            crossing_polygon = Polygon([
                {'x': 1.5, 'y': 0.5},
                {'x': 2.5, 'y': 0.5},
                {'x': 2.5, 'y': 1.5},
                {'x': 1.5, 'y': 1.5},
                {'x': 1.5, 'y': 0.5},
            ], 2263)
            test_layer.select_layer_by_location('CONTAINS', crossing_polygon)
            test_layer.calculate_field('borough', "'YY'")
            test_layer.select_layer_by_attribute("borough = 'YY'")
            self.assertEqual(test_layer.count, 0)
            test_layer.calculate_field('borough', "'XX'")

            test_layer.select_layer_by_location('CROSSES', crossing_polygon)
            test_layer.calculate_field('borough', "'YY'")
            test_layer.select_layer_by_attribute("borough = 'YY'")
            self.assertEqual(test_layer.count, 2)
            test_layer.calculate_field('borough', "'XX'")

            test_layer.select_layer_by_attribute("borough = 'XX'")
            with self.workspace.create_feature_class('layer_calc_field_test_2', 'POLYGON', 2263, schema='testing_2') as query_layer:
                query_layer.add_field('attr_field')
                query_layer.add_rows([
                    {'attr_field': 'XX', query_layer.shape: crossing_polygon},
                    {'attr_field': 'XX', query_layer.shape: contained_polygon},
                ])
                self.assertEqual(query_layer.count, 2)
                query_layer.select_layer_by_location('WITHIN', test_layer)
                query_layer.calculate_field('attr_field', "'YY'")
                query_layer.select_layer_by_attribute("attr_field = 'YY'")
                self.assertEqual(query_layer.count, 1)

                # test setting string values w/out single quotes
                query_layer.select_layer_by_location('WITHIN', test_layer)
                query_layer.calculate_field('attr_field', "ZZ")
                query_layer.select_layer_by_attribute("attr_field = 'ZZ'")
                self.assertEqual(query_layer.count, 1)

                query_layer.select_layer_by_location('WITHIN', test_layer)
                query_layer.calculate_field('attr_field', "Z'Z")
                query_layer.select_layer_by_attribute("attr_field = 'Z''Z'")
                self.assertEqual(query_layer.count, 1)

                query_layer.select_layer_by_location('WITHIN', test_layer)
                query_layer.calculate_field('attr_field', "'Z'Z'")
                query_layer.select_layer_by_attribute("attr_field = 'Z''Z'")
                self.assertEqual(query_layer.count, 1)
        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_select_layer_by_location(self):
        # create a point at a known location and select features there
        test_point = Point((982609, 206224), self.test_layer.spatial_reference)
        with self.test_layer.copy_to_new_table('select_test', output_schema='testing') as local_layer:
            local_layer.select_layer_by_location('CONTAINS', test_point)
            self.assertEqual(local_layer.get_selection_count(), 1)

            # create a test point outside of any shape and make sure nothing is selected
            test_point = Point((990126, 222502), local_layer.spatial_reference)
            local_layer.select_layer_by_location('CONTAINS', test_point)
            self.assertEqual(local_layer.get_selection_count(), 0)

            # create a polygon that contains exactly 2 features and test "WITHIN"
            within_polygon = Polygon([
                {'x': 989997, 'y': 222253},
                {'x': 990267, 'y': 222751},
                {'x': 991041, 'y': 222319},
                {'x': 990763, 'y': 221830},
            ], local_layer.spatial_reference)

            # create a polygon that crosses one block and envelopes another
            crossing_polygon = Polygon([
                {'x': 990203, 'y': 222156},
                {'x': 990469, 'y': 222648},
                {'x': 991041, 'y': 222316},
                {'x': 990773, 'y': 221837},
            ], local_layer.spatial_reference)

            # create a polygon that does not touch any others in the layer
            non_touching_polygon = Polygon([
                {'x': 986686, 'y': 206427},
                {'x': 986699, 'y': 206445},
                {'x': 986731, 'y': 206414},
            ], local_layer.spatial_reference)

            local_layer.select_layer_by_location('WITHIN', non_touching_polygon)
            self.assertEqual(local_layer.get_selection_count(), 0)

            local_layer.select_layer_by_location('CONTAINS', non_touching_polygon)
            self.assertEqual(local_layer.get_selection_count(), 0)

            local_layer.select_layer_by_location('WITHIN', within_polygon)
            self.assertEqual(local_layer.get_selection_count(), 2)

            # test additive functions
            test_point = Point((982609, 206224), local_layer.spatial_reference)
            local_layer.select_layer_by_location('CONTAINS', test_point, selection_type='ADD_TO_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 3)

            # test remove function
            local_layer.select_layer_by_location('WITHIN', within_polygon, selection_type='REMOVE_FROM_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 1)

            # test subset selection
            test_point = Point((990229, 222253), local_layer.spatial_reference)
            local_layer.select_layer_by_location('WITHIN', within_polygon)
            self.assertEqual(local_layer.get_selection_count(), 2)
            local_layer.select_layer_by_location('CONTAINS', test_point, selection_type='SUBSET_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 1)

            # test with crossing polygon
            local_layer.select_layer_by_location('WITHIN', crossing_polygon)
            self.assertEqual(local_layer.get_selection_count(), 0)

            # test with non-touching polygon
            local_layer.select_layer_by_location('WITHIN', non_touching_polygon)
            self.assertEqual(local_layer.get_selection_count(), 0)

            # test shares a line segment with
            local_layer.select_layer_by_attribute(1)
            with local_layer.get_search_cursor([local_layer.shape]) as cursor:
                shared_polygon = next(cursor)[local_layer.shape]
            shared_line = shared_polygon.to_lines()[0]
            local_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', shared_line)
            self.assertEqual(local_layer.get_selection_count(), 1)
            touching_line = Line([
                {'x': 987037.6, 'y': 206401.9},
                {'x': 986994.130654663, 'y': 206413.056383729},
            ], local_layer.spatial_reference)
            local_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', touching_line)
            self.assertEqual(local_layer.get_selection_count(), 0)

            # test boundary touches
            # local_layer.select_layer_by_location('BOUNDARY_TOUCHES', touching_line)
            # self.assertEqual(local_layer.get_selection_count(), 1)

            # test crossed by the outline of
            local_layer.select_layer_by_location('CROSSED_BY_THE_OUTLINE_OF', touching_line)
            self.assertEqual(local_layer.get_selection_count(), 0)
            crossing_line = Line([
                {'x': 986777.1, 'y': 206428.7},
                {'x': 986734.4, 'y': 206478.4},
            ], local_layer.spatial_reference)
            local_layer.select_layer_by_location('CROSSED_BY_THE_OUTLINE_OF', crossing_line)
            self.assertEqual(local_layer.get_selection_count(), 1)
            local_layer.select_layer_by_location('CROSSED_BY_THE_OUTLINE_OF', crossing_polygon)
            self.assertEqual(local_layer.get_selection_count(), 2)
            local_layer.select_layer_by_location('CROSSED_BY_THE_OUTLINE_OF', non_touching_polygon)
            self.assertEqual(local_layer.get_selection_count(), 0)

            # test have their centers in
            local_layer.select_layer_by_location('HAVE_THEIR_CENTER_IN', crossing_polygon)
            self.assertEqual(local_layer.get_selection_count(), 2)
            local_layer.select_layer_by_location('HAVE_THEIR_CENTER_IN', within_polygon)
            self.assertEqual(local_layer.get_selection_count(), 2)
            local_layer.select_layer_by_location('HAVE_THEIR_CENTER_IN', non_touching_polygon)
            self.assertEqual(local_layer.get_selection_count(), 0)

            # test within a distance
            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', non_touching_polygon, search_distance=100)
            self.assertEqual(local_layer.get_selection_count(), 4)
            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', non_touching_polygon, search_distance='30 METERS')
            self.assertEqual(local_layer.get_selection_count(), 4)

            # test layer selections
            local_layer.clear_selection()
            self.adjacent_layer.select_layer_by_location('WITHIN', local_layer)
            self.assertEqual(self.adjacent_layer.get_selection_count(), 6)
            self.adjacent_layer.clear_selection()

            local_layer.select_layer_by_location('CONTAINS', self.adjacent_layer)
            self.assertEqual(local_layer.get_selection_count(), 1)

            local_layer.select_layer_by_attribute(1)
            with local_layer.copy_to_new_table('single_shape_test') as single_shape_layer:
                local_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', single_shape_layer)
                self.assertEqual(local_layer.get_selection_count(), 1)
                local_layer.clear_selection()

            self.adjacent_layer.select_layer_by_location('HAVE_THEIR_CENTER_IN', local_layer)
            self.assertEqual(self.adjacent_layer.get_selection_count(), 6)
            self.adjacent_layer.clear_selection()

            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', self.adjacent_layer, search_distance=200)
            self.assertEqual(local_layer.get_selection_count(), 9)

            local_layer.select_layer_by_location('INTERSECT', self.adjacent_layer, invert_spatial_relationship='INVERT')
            self.assertEqual(local_layer.get_selection_count(), 2878)

            # complex scenario #1
            # first search returns 4 records, the attribute search adds a fifth
            # and the within search adds two more, for a total of 7
            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', non_touching_polygon, search_distance=100)
            local_layer.select_layer_by_attribute('{} = 1'.format(local_layer.oid), selection_type='ADD_TO_SELECTION')
            local_layer.select_layer_by_location('WITHIN', within_polygon, selection_type='ADD_TO_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 7)

            # remove 4 items from the previous selection
            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', non_touching_polygon, search_distance=100, selection_type='REMOVE_FROM_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 3)

            # perform an attribute subselection
            local_layer.select_layer_by_attribute('{} = 1'.format(local_layer.oid), selection_type='SUBSET_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 1)

            # complex scenario #2
            local_layer.select_layer_by_attribute('{} = 1'.format(local_layer.oid))
            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', non_touching_polygon, search_distance=100, selection_type='ADD_TO_SELECTION')
            local_layer.select_layer_by_location('WITHIN', within_polygon, selection_type='ADD_TO_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 7)
            local_layer.switch_selection()
            self.assertEqual(local_layer.get_selection_count(), 2872)

            # complex scenario #3
            local_layer.select_layer_by_attribute('{} = 1'.format(local_layer.oid))
            local_layer.select_layer_by_location('WITHIN_A_DISTANCE', non_touching_polygon, search_distance=100, selection_type='ADD_TO_SELECTION')
            local_layer.select_layer_by_attribute('{} = 2'.format(local_layer.oid), selection_type='ADD_TO_SELECTION')
            local_layer.select_layer_by_location('WITHIN', within_polygon, selection_type='ADD_TO_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 8)
            local_layer.select_layer_by_location('WITHIN', within_polygon, selection_type='REMOVE_FROM_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 6)
            local_layer.select_layer_by_attribute('{0} = 1 OR {0} = 2'.format(local_layer.oid), selection_type='SUBSET_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 2)
            local_layer.switch_selection()
            self.assertEqual(local_layer.get_selection_count(), 2877)
            local_layer.select_layer_by_location('WITHIN', within_polygon, selection_type='REMOVE_FROM_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 2875)
            local_layer.select_layer_by_attribute('{} = 2'.format(local_layer.oid), selection_type='ADD_TO_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 2876)
            local_layer.select_layer_by_attribute('{0} = 1 OR {0} = 2'.format(local_layer.oid), selection_type='SUBSET_SELECTION')
            self.assertEqual(local_layer.get_selection_count(), 1)

            # special share a line segment test
            with self.adjacent_layer.split_lines_to_layer('lines_selection_test_1') as line_layer_1, \
                line_layer_1.copy_to_new_table('lines_selection_test_2') as line_layer_2:
                line_layer_2.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', line_layer_1)
                self.assertEqual(line_layer_1.count, line_layer_2.count)

                # use line layers to test MIDPOINT_NEAR option
                line_layer_2.select_layer_by_location('MIDPOINT_NEAR', line_layer_1)
                self.assertEqual(line_layer_1.count, line_layer_2.count)


            # test shares a line segment database function
            local_layer.select_layer_by_attribute(1)
            with local_layer.get_search_cursor([local_layer.shape]) as cursor:
                shared_polygon = next(cursor)[local_layer.shape]
            shared_line = shared_polygon.to_lines()[0]
            local_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', shared_line)
            self.assertEqual(local_layer.get_selection_count(), 1)
            touching_line = Line([
                {'x': 987037.6, 'y': 206401.9},
                {'x': 986994.130654663, 'y': 206413.056383729},
            ], local_layer.spatial_reference)
            local_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', touching_line)
            self.assertEqual(local_layer.get_selection_count(), 0)

            with self.adjacent_layer.split_lines_to_layer('lines_selection_test_1') as line_layer_1, \
                line_layer_1.copy_to_new_table('lines_selection_test_2') as line_layer_2:
                line_layer_2.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', line_layer_1)
                self.assertEqual(line_layer_1.count, line_layer_2.count)

            local_layer.select_layer_by_attribute(1)
            with local_layer.copy_to_new_table('single_shape_test') as single_shape_layer:
                local_layer.select_layer_by_location('SHARE_A_LINE_SEGMENT_WITH', single_shape_layer)
                self.assertEqual(local_layer.get_selection_count(), 1)
                local_layer.clear_selection()

            # clear selections before exit
            local_layer.clear_selection()
            self.adjacent_layer.clear_selection()

        self.workspace.drop_schema('testing', cascade=True)

    def test_add_field(self):
        self.adjacent_layer.select_layer_by_attribute('{} <= 2'.format(self.adjacent_layer.oid))
        with self.adjacent_layer.copy_to_new_table('add_column_test', output_schema='testing') as test_layer:
            self.adjacent_layer.clear_selection()

            test_layer.add_field('CBBL_2')
            test_layer.copy_field_values('cbbl', 'CBBL_2')
            with test_layer.get_search_cursor(['cbbl', 'CBBL_2']) as cursor:
                for row in cursor:
                    self.assertEqual(row['cbbl'], row['CBBL_2'])
        self.workspace.drop_schema('testing', cascade=True)

    def test_duplicate_layer(self):
        # copy the test layer
        with self.test_layer.duplicate_layer('duplicated_layer_test') as duplicated_layer:
            # verify there are now 5 layers in the db
            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(layers), 5)
            self.assertEqual(duplicated_layer.count, 0)
            for field_name in self.test_layer.field_names:
                self.assertIn(field_name, duplicated_layer.field_names)

    def test_delete_other_fields(self):
        with self.test_layer.copy_to_new_table('test_copy') as test_layer:
            test_layer.add_field('POINT_COUNT', 'SHORT')

            self.assertIn('POINT_COUNT', test_layer.field_names)

            # delete fields other than blocks and BLOCK_ID
            test_layer.delete_other_fields(['blocks', 'borough', 'phyblockid', 'cbb'])
            self.assertNotIn('POINT_COUNT', test_layer.field_names)
            self.assertIn('blocks', test_layer.field_names)
            self.assertIn('borough', test_layer.field_names)
            self.assertIn('phyblockid', test_layer.field_names)
            self.assertIn('cbb', test_layer.field_names)

    def test_shape_property(self):
        # test the shape property
        self.assertEqual(self.test_layer.shape, 'SHAPE')

    def test_oid_property(self):
        # test the oid property
        self.assertEqual(self.test_layer.oid, 'OBJECTID')

    def test_get_geometries(self):
        geometries = self.test_layer.get_geometries()
        self.assertIsInstance(geometries, list)
        self.assertGreater(len(geometries), 0)
        self.assertIsInstance(geometries[0], Polygon)

    def test_get_lines(self):
        self.test_layer.select_layer_by_attribute('OBJECTID < 11')
        lines = self.test_layer.get_lines()
        self.assertIsInstance(lines, list)
        self.assertGreater(len(lines), 0)
        self.assertIsInstance(lines[0], Line)
        self.test_layer.clear_selection()

    def test_field_names_property(self):
        self.assertIn('blocks', self.test_layer.field_names)
        self.assertIn('borough', self.test_layer.field_names)
        self.assertIn('phyblockid', self.test_layer.field_names)
        self.assertIn('cbb', self.test_layer.field_names)
        self.assertNotIn('OBJECTID', self.test_layer.field_names)
        self.assertNotIn('SHAPE', self.test_layer.field_names)

    def test_get_geodataframe(self):
        df = self.test_layer.get_geodataframe()
        self.assertEqual(len(df.index), 2879)
        self.assertEqual(df.index.name, self.test_layer.oid)

    def test_identity_to_layer(self):
        # select 1 block and one zd whose geometries overlap
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        self.overlay_layer.select_layer_by_attribute('OBJECTID = 327')
        with self.test_layer.identity_to_layer(self.overlay_layer, 'identity_test', output_schema='testing') as overlay_results_layer:

            # verify there is now 1 feature class in the schema
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)

            # verify that a layer object was returned and that it contains 2 features
            self.assertIsInstance(overlay_results_layer, Layer)
            self.assertEqual(overlay_results_layer.count, 2)
            self.assertIn('ZONEDIST', overlay_results_layer.field_names)
            overlay_results_layer.select_layer_by_attribute("ZONEDIST = 'C6-4.5'")
            self.assertEqual(overlay_results_layer.count, 1)
            overlay_results_layer.select_layer_by_attribute('ZONEDIST IS NULL')
            self.assertEqual(overlay_results_layer.count, 1)


        # select 1 block and 3 zds whose geometries overlap
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        self.overlay_layer.select_layer_by_attribute('OBJECTID IN (327, 465, 358)')
        with self.test_layer.copy_to_new_table('identity_inputs_test', output_schema='testing') as test_layer, \
                test_layer.identity_to_layer(self.overlay_layer, 'identity_test', output_schema='testing') as overlay_results_layer:

            # verify there are now 2 feature classes in the schema
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 2)

            # verify that a layer object was returned and that it contains 3 features
            self.assertIsInstance(overlay_results_layer, Layer)
            self.assertEqual(overlay_results_layer.count, 3)
            self.assertIn('ZONEDIST', overlay_results_layer.field_names)
            overlay_results_layer.select_layer_by_attribute("ZONEDIST = 'C6-4.5'")
            self.assertEqual(overlay_results_layer.count, 1)
            overlay_results_layer.select_layer_by_attribute("ZONEDIST = 'C6-6'")
            self.assertEqual(overlay_results_layer.count, 1)
            overlay_results_layer.select_layer_by_attribute("ZONEDIST = 'C5-3'")
            self.assertEqual(overlay_results_layer.count, 1)


        # clear selection and delete overlay results layer
        self.test_layer.clear_selection()
        self.overlay_layer.clear_selection()
        self.workspace.drop_schema('testing', cascade=True)

    def test_intersect_to_layer(self):
        # select 1 block and one zd whose geometries overlap
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        self.overlay_layer.select_layer_by_attribute('OBJECTID = 327')
        with self.test_layer.intersect_to_layer(self.overlay_layer, 'intersect_test', output_schema='testing') as overlay_results_layer:
            # verify there is now 1 layer in the db schema
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)

            # verify that a layer object was returned and that it contains  feature
            self.assertIsInstance(overlay_results_layer, Layer)
            self.assertEqual(overlay_results_layer.count, 1)
            self.assertEqual(overlay_results_layer.geometry_type, 'Polygon')
            self.assertIn('ZONEDIST', overlay_results_layer.field_names)
            with overlay_results_layer.get_search_cursor('ZONEDIST') as cursor:
                zonedist = next(cursor)['ZONEDIST']
                self.assertEqual(zonedist, 'C6-4.5')

        # with self.test_layer.intersect_to_layer(self.overlay_layer, 'intersect_point_test', output_type='POINT', output_schema='testing') as overlay_results_layer:
        #     self.assertIsInstance(overlay_results_layer, Layer)
        #     self.assertEqual(overlay_results_layer.geometry_type, 'Point')
        #     self.assertEqual(overlay_results_layer.count, 23)
        #     self.assertIn('ZONEDIST', overlay_results_layer.field_names)
        #
        # with self.overlay_layer.split_lines_to_layer('intersect_line_test', output_schema='testing_2') as line_layer, \
        #         self.test_layer.intersect_to_layer(line_layer, 'intersect_point_test_2', output_type='POINT', output_schema='testing') as overlay_results_layer:
        #     self.assertIsInstance(overlay_results_layer, Layer)
        #     self.assertEqual(overlay_results_layer.geometry_type, 'Point')
        #     self.assertEqual(overlay_results_layer.count, 2)

        # clear selection and delete overlay results layer
        self.test_layer.clear_selection()
        self.overlay_layer.clear_selection()
        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_clip_to_layer(self):
        self.overlay_layer.select_layer_by_attribute('OBJECTID = 168')
        with self.overlay_layer.clip_to_layer(self.adjacent_layer, 'clipped_layer_test', output_schema='testing') as clip_layer:
            self.overlay_layer.clear_selection()
            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(layers), 4)
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)
            self.assertIsInstance(clip_layer, Layer)
            self.assertEqual(clip_layer.count, 1)
        self.workspace.drop_schema('testing', cascade=True)

    def test_feature_vertices_to_points_layer(self):
        # select 1 block
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        with self.test_layer.feature_vertices_to_points_layer('vertices_to_points_test', output_schema='testing') as results_layer:

            # verify that a layer object was returned and that it contains 4 features
            self.assertIsInstance(results_layer, Layer)
            self.assertEqual(results_layer.count, 19)
            self.assertEqual(results_layer.geometry_type, 'Point')
            self.assertIn('blocks', results_layer.field_names)
            self.assertIn('borough', results_layer.field_names)
            self.assertIn('phyblockid', results_layer.field_names)
            self.assertIn('cbb', results_layer.field_names)

        # clear selection and delete overlay results layer
        self.test_layer.clear_selection()
        self.workspace.drop_schema('testing')

    def test_feature_to_point_layer(self):
        # select 1 block
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        with self.test_layer.feature_to_point_layer('feature_to_points_test', output_schema='testing') as results_layer:
            # verify that a layer object was returned and that it contains 1 feature
            self.assertIsInstance(results_layer, Layer)
            self.assertEqual(results_layer.count, 1)
            self.assertEqual(results_layer.geometry_type, 'Point')
            self.assertIn('blocks', results_layer.field_names)
            self.assertIn('borough', results_layer.field_names)
            self.assertIn('phyblockid', results_layer.field_names)
            self.assertIn('cbb', results_layer.field_names)

        with self.test_layer.feature_to_point_layer('feature_to_points_inside_test', point_location='INSIDE', output_schema='testing') as results_layer:
            # verify that a layer object was returned and that it contains 1 feature
            self.assertIsInstance(results_layer, Layer)
            self.assertEqual(results_layer.count, 1)
            self.assertEqual(results_layer.geometry_type, 'Point')
            self.assertIn('blocks', results_layer.field_names)
            self.assertIn('borough', results_layer.field_names)
            self.assertIn('phyblockid', results_layer.field_names)
            self.assertIn('cbb', results_layer.field_names)

        # clear selection and delete overlay results layer
        self.test_layer.clear_selection()
        self.workspace.drop_schema('testing')

    def test_copy_to_new_table(self):
        # select a single feature and create a copy of the polygon layer
        self.test_layer.select_layer_by_attribute(1)
        copy_layer = self.test_layer.copy_to_new_table('copy_layer_test')
        self.test_layer.clear_selection()

        # verify there are now 5 layers in the db and there is only one record in the output table
        layers = self.workspace.list_feature_classes()
        self.assertEqual(len(layers), 5)
        self.assertEqual(copy_layer.count, 1)

        # delete test layer
        copy_layer.delete()

    def test_select_to_layer(self):
        # create a layer from the polygon layer
        with self.test_layer.select_to_layer('copy_layer_test', 'OBJECTID = 1', output_schema='testing') as select_layer:

            # verify there are now 5 layers in the db
            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(layers), 4)
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)

            self.assertEqual(select_layer.count, 1)

            # verify there is only one record in the new layer
            self.assertEqual(select_layer.get_selection_count(), 1)

        self.workspace.drop_schema('testing', cascade=True)

    def test_convert_to_table(self):
        with self.test_layer.convert_to_table('converted_table_test', output_schema='testing') as test_table:
            self.assertIsInstance(test_table, Table)

            tables = self.workspace.list_tables()
            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(tables), 1)
            self.assertEqual(len(layers), 4)

            tables = self.workspace.list_tables(schema='testing')
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(tables), 1)
            self.assertEqual(len(layers), 0)

            self.assertIn(test_table.table_name, tables)
            self.assertNotIn(test_table.table_name, layers)
            self.assertEqual(self.test_layer.count, test_table.count)

        self.workspace.drop_schema('testing', cascade=True)

    def test_geometry_type(self):
        self.assertEqual(self.test_layer.geometry_type, 'Polygon')

    def test_spatial_reference(self):
        self.assertEqual(self.test_layer.spatial_reference, 2263)

    def test_get_geometry_columns(self):
        geometry_columns = self.test_layer.get_geometry_columns()
        self.assertEqual(len(geometry_columns), 1)
        self.assertEqual(geometry_columns[0]['name'], 'SHAPE')

        geometry_columns = self.test_layer.get_geometry_columns(include_hidden=True)
        self.assertEqual(len(geometry_columns), 2)
        names = [geom_col['name'] for geom_col in geometry_columns]
        self.assertIn('SHAPE', names)
        # self.assertIn('edge_buffers', names)
        self.assertIn('EDGE_BUFFERS', names)

    def test_mbr_to_layer(self):
        # create an mbr layer from the polygon layer
        with self.test_layer.minimum_bounding_geometry_to_layer('mbr_layer_test', output_schema='testing') as mbr_layer:
            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(layers), 4)
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)

            # verify that there are the same number of rows as the
            # source table, and that there is an "orig_fid" field
            self.assertEqual(self.test_layer.count, mbr_layer.count)
            self.assertIn('orig_fid', mbr_layer.field_names)

        # create an mbr layer from the polygon layer using field options
        with self.test_layer.minimum_bounding_geometry_to_layer('mbr_layer_2_test',
            geometry_type='CONVEX_HULL',
            omit_field_options='MBG_FIELDS',
            output_schema='testing') as mbr_layer:

            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(layers), 4)
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)

            # verify that there are the same number of rows as the
            # source table, and that there is an "orig_fid" field as well as the MBG fields
            self.assertEqual(self.test_layer.count, mbr_layer.count)
            self.assertIn('orig_fid', mbr_layer.field_names)
            self.assertIn('mbg_length', mbr_layer.field_names)
            self.assertIn('mbg_width', mbr_layer.field_names)

        self.workspace.drop_schema('testing', cascade=True)

    def test_buffer_to_layer(self):
        # create a buffer layer from the polygon layer
        with self.test_layer.buffer_to_layer('buffer_layer_test', 100, output_schema='testing') as buffer_layer:
            layers = self.workspace.list_feature_classes()
            self.assertEqual(len(layers), 4)
            layers = self.workspace.list_feature_classes(schema='testing')
            self.assertEqual(len(layers), 1)
        self.workspace.drop_schema('testing')

    def test_dissolve_to_layer(self):
        # dissolve the adjacent polygons layer by cbb
        with self.adjacent_layer.dissolve_to_layer('dissolve_layer_test', ['cbb'], output_schema='testing') as dissolve_layer:
            self.assertEqual(dissolve_layer.count, 1)
            self.assertNotIn('cbbl', dissolve_layer.field_names)
            self.assertIn('cbb', dissolve_layer.field_names)

        # dissolve the adjacent polygons layer by cbbl (should not dissolve)
        with self.adjacent_layer.dissolve_to_layer('dissolve_layer_2_test', ['cbbl'], output_schema='testing') as dissolve_layer_2:
            self.assertEqual(dissolve_layer_2.count, 6)
            self.assertIn('cbbl', dissolve_layer_2.field_names)
            self.assertNotIn('cbb', dissolve_layer_2.field_names)

        # test multi-part versus single-part
        with self.adjacent_layer.dissolve_to_layer('dissolve_layer_3_test', ['canbuild'], output_schema='testing') as dissolve_layer_3:
            self.assertEqual(dissolve_layer_3.count, 2)
            self.assertIn('canbuild', dissolve_layer_3.field_names)
            self.assertNotIn('cbb', dissolve_layer_3.field_names)

        with self.adjacent_layer.dissolve_to_layer('dissolve_layer_4_test', ['canbuild'], multi_part=False, output_schema='testing') as dissolve_layer_4:
            self.assertEqual(dissolve_layer_4.count, 3)
            self.assertIn('canbuild', dissolve_layer_4.field_names)
            self.assertNotIn('cbb', dissolve_layer_4.field_names)

        # test dissolving on multiple fields
        with self.adjacent_layer.dissolve_to_layer('dissolve_layer_5_test', ['canbuild', 'corner'], output_schema='testing') as dissolve_layer_5:
            self.assertEqual(dissolve_layer_5.count, 3)
            self.assertIn('canbuild', dissolve_layer_5.field_names)
            self.assertIn('corner', dissolve_layer_5.field_names)
            self.assertNotIn('cbb', dissolve_layer_5.field_names)

        with self.adjacent_layer.dissolve_to_layer('dissolve_layer_6_test', ['canbuild', 'corner'], multi_part=False, output_schema='testing') as dissolve_layer_6:
            self.assertEqual(dissolve_layer_6.count, 5)
            self.assertIn('canbuild', dissolve_layer_6.field_names)
            self.assertIn('corner', dissolve_layer_6.field_names)
            self.assertNotIn('cbb', dissolve_layer_6.field_names)

        # test dissolving line layers
        self.adjacent_layer.select_layer_by_attribute(1)
        with self.adjacent_layer.split_lines_to_layer('temp_lines_test', output_schema='testing_2') as line_layer:
            self.adjacent_layer.clear_selection()
            with line_layer.dissolve_to_layer('temp_lines_dissolved_test', output_schema='testing') as dissolve_layer_7:
                self.assertLess(dissolve_layer_7.count, line_layer.count)

        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_split_and_unsplit_lines_to_layer(self):
        # export polygon edges to lines
        with self.adjacent_layer.split_lines_to_layer('split_lines_test', output_schema='testing') as lines_layer:
            self.assertEqual(lines_layer.geometry_type, 'Polyline')
            self.assertEqual(lines_layer.count, 45)

            # merge the lines back together
            with lines_layer.unsplit_lines_to_layer('unsplit_lines_test') as unsplit_lines:
                self.assertEqual(unsplit_lines.geometry_type, 'Polyline')
                self.assertEqual(unsplit_lines.count, 41)
                self.assertEqual(unsplit_lines.schema, 'testing')

            with lines_layer.unsplit_lines_to_layer('dissolve_lines_test', dissolve_fields='cbbl', output_schema='testing_2') as dissolve_lines:
                self.assertEqual(dissolve_lines.geometry_type, 'Polyline')
                self.assertEqual(dissolve_lines.count, 6)
                self.assertEqual(dissolve_lines.schema, 'testing_2')

        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_near(self):
        # select the 9 blocks around the adjacent lots layer
        self.test_layer.select_layer_by_location('WITHIN_A_DISTANCE', self.adjacent_layer, search_distance=200)
        with self.test_layer.copy_to_new_table('near_layer_test', output_schema='testing') as near_layer:
            self.test_layer.clear_selection()

            # use the near function to measure the distances of the 9 selected polygons from the adjacent lots layer
            near_layer.near(self.adjacent_layer)

            # verify that all rows in the near table have a near_fid value
            near_layer.select_layer_by_attribute('near_fid >= 0')
            self.assertEqual(near_layer.count, 9)

            # verify that 8 records have a near distance and one has the value 0
            near_layer.select_layer_by_attribute('near_dist > 0')
            self.assertEqual(near_layer.count, 8)
            near_layer.select_layer_by_attribute('near_dist = 0')
            self.assertEqual(near_layer.count, 1)
            near_layer.clear_selection()

            # test with a selection set on the near layer
            near_layer.select_layer_by_location('INTERSECT', self.adjacent_layer)
            near_layer.switch_selection()

            # measure the distance to the adjacent lot polygons
            near_layer.near(self.adjacent_layer)

            # verify that all rows but one have a near_fid value (one row should be excluded
            near_layer.select_layer_by_attribute('near_fid >= 0')
            self.assertEqual(near_layer.count, 8)
            near_layer.select_layer_by_attribute('near_fid = -1')
            self.assertEqual(near_layer.count, 1)

            # verify that 8 records have a near distance and one has the value -1
            near_layer.select_layer_by_attribute('near_dist > 0')
            self.assertEqual(near_layer.count, 8)
            near_layer.select_layer_by_attribute('near_dist = -1')
            self.assertEqual(near_layer.count, 1)

            # test with a selection set on both layers
            near_layer.select_layer_by_location('INTERSECT', self.adjacent_layer)
            near_layer.switch_selection()
            self.adjacent_layer.select_layer_by_attribute('{} = 1'.format(self.adjacent_layer.oid))

            # measure the distance to the adjacent lot polygons
            near_layer.near(self.adjacent_layer)

            # verify that all rows but one have a near_fid value (one row should be excluded
            near_layer.select_layer_by_attribute('near_fid = 1')
            self.assertEqual(near_layer.count, 8)
            near_layer.select_layer_by_attribute('near_fid = -1')
            self.assertEqual(near_layer.count, 1)

            # verify that 8 records have a near distance and one has the value -1
            near_layer.select_layer_by_attribute('near_dist > 0')
            self.assertEqual(near_layer.count, 8)
            near_layer.select_layer_by_attribute('near_dist = -1')
            self.assertEqual(near_layer.count, 1)

            self.adjacent_layer.clear_selection()

        self.workspace.drop_schema('testing', cascade=True)

    def test_snap(self):
        # snap the vertices of the adjacent lots layer to the main test layer (physical blocks)
        with self.snap_targets_layer.copy_to_new_table('snap_targets_test', output_schema='testing') as temp_snap_targets:
            temp_snap_targets.snap([[self.test_layer, 'VERTEX', '1 FOOT']])
            self.test_layer.select_layer_by_location('INTERSECT', self.adjacent_layer)
            with self.test_layer.split_lines_to_layer('snap_lines_test', output_schema='testing_2') as snap_lines_layer:
                self.test_layer.clear_selection()
                temp_snap_targets.snap([[snap_lines_layer, 'EDGE', '2 FEET']])
                temp_snap_targets.snap([[snap_lines_layer, 'END', '4 FEET']])

            # compare the first shape in the adjacent and target layers - they should now almost match
            self.adjacent_layer.select_layer_by_attribute('{} = 1'.format(self.adjacent_layer.oid))
            with self.adjacent_layer.get_search_cursor([self.adjacent_layer.shape]) as cursor:
                adjacent_geometry = next(cursor)[self.adjacent_layer.shape]
            self.adjacent_layer.clear_selection()
            temp_snap_targets.select_layer_by_location('INTERSECT', adjacent_geometry.centroid)
            with temp_snap_targets.get_search_cursor([temp_snap_targets.shape]) as cursor:
                snapped_geometry = next(cursor)[temp_snap_targets.shape]
            temp_snap_targets.clear_selection()
            self.assertAlmostEqual(adjacent_geometry.area, snapped_geometry.area, 4)

        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_split_line_at_points_to_layer(self):
        # export polygon edges to lines
        with self.adjacent_layer.split_lines_to_layer('lines_to_split_test', output_schema='testing') as lines_layer, \
            self.adjacent_layer.feature_vertices_to_points_layer('split_points_test', output_schema='testing_2') as points_layer:
            # merge the lines back together so we can split them with the points
            with lines_layer.unsplit_lines_to_layer('dissolve_lines_test') as dissolve_lines:
                self.assertEqual(dissolve_lines.schema, 'testing')
                # split the lines at points - should result in 45 lines
                with dissolve_lines.split_lines_at_points_to_layer(points_layer, 'lines_split_at_points_test', output_schema='testing_2') as split_lines:
                    self.assertEqual(split_lines.geometry_type, 'Polyline')
                    self.assertEqual(split_lines.count, 45)
                    self.assertEqual(split_lines.schema, 'testing_2')

        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_merge_layers(self):
        # select a single feature and create a copy of the polygon layer
        self.test_layer.select_layer_by_attribute('{} = 1'.format(self.test_layer.oid))
        with self.test_layer.copy_to_new_table('copy_layer_test', output_schema='testing') as copy_layer:
            self.test_layer.clear_selection()

            # merge the copied layer into the test layer
            merged_layer = self.test_layer.merge_to_layer(copy_layer, 'merged_layer_test')
            self.assertEqual(self.test_layer.count, merged_layer.count - 1)
            self.assertEqual(merged_layer.schema, 'public')
            merged_layer.delete()

            merged_layer = self.test_layer.merge_to_layer(copy_layer, 'merged_layer_2_test', output_schema='testing')
            self.assertEqual(self.test_layer.count, merged_layer.count - 1)
            self.assertEqual(merged_layer.schema, 'testing')
            merged_layer.delete()

        self.workspace.drop_schema('testing', cascade=True)

    def test_merge_layers_to_layer(self):
        # select a single feature and create a copy of the polygon layer
        self.test_layer.select_layer_by_attribute('OBJECTID = 1')
        with self.test_layer.copy_to_new_table('merge_copy_layer_test', output_schema='testing') as copy_layer:
            self.test_layer.clear_selection()

            # merge the copied layer into the test layer
            merged_layer = Layer.merge_layers_to_layer([copy_layer, self.test_layer], 'merged_layers_to_layer_test', self.workspace)
            self.assertEqual(merged_layer.schema, 'public')
            self.assertEqual(self.test_layer.count, merged_layer.count - 1)
            merged_layer.delete()

            # merge the copied layer into the test layer
            merged_layer = Layer.merge_layers_to_layer([copy_layer, self.test_layer], 'merged_layers_to_layer_test',
                                                       self.workspace, output_schema='testing_2')

            self.assertEqual(merged_layer.schema, 'testing_2')
            self.assertEqual(self.test_layer.count, merged_layer.count - 1)
            merged_layer.delete()

        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)

    def test_union_geometries(self):
        # union the geometries in the adjacent layer
        geometry = self.adjacent_layer.union_geometries()
        self.assertIsInstance(geometry, Polygon)

    def test_single_part_layer(self):

        with self.test_layer.to_single_part_layer('single_part_layer_test', output_schema='testing') as single_part_layer:
            self.assertEqual(single_part_layer.geometry_type, 'Polygon')
            self.assertEqual(self.test_layer.count, single_part_layer.count)
            self.assertEqual(single_part_layer.schema, 'testing')

        self.workspace.drop_schema('testing', cascade=True)

    def test_multi_part_layer(self):

        with self.test_layer.to_multi_part_layer('multi_part_layer_test', 'borough', output_schema='testing') as multi_part_layer:
            self.assertEqual(multi_part_layer.geometry_type, 'Polygon')
            self.assertEqual(multi_part_layer.count, 1)
            self.assertEqual(multi_part_layer.schema, 'testing')

        self.workspace.drop_schema('testing', cascade=True)

    def test_feature_to_polygon_layer(self):
        # create a point layer from the polygon layer
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        with self.test_layer.split_lines_to_layer('lines_layer_test', output_schema='testing') as lines_layer:
            self.test_layer.clear_selection()
            with self.test_layer.feature_to_point_layer('label_centroids_test', output_schema='testing_2') as points_layer:
                points_layer.delete_other_fields(['cbb'])

                # re-merge lines together as polygons
                with lines_layer.feature_to_polygon_layer('remade_polygon_layer_test', attributes_layer=points_layer, output_schema='testing_3') as polygon_layer:
                    # verify that the output is a polygon layer
                    self.assertEqual(polygon_layer.geometry_type, 'Polygon')
        self.workspace.drop_schema('testing', cascade=True)
        self.workspace.drop_schema('testing_2', cascade=True)
        self.workspace.drop_schema('testing_3', cascade=True)

    def test_generate_adjacency_table(self):
        # generate adjacency table from layer
        with self.adjacent_layer.generate_adjacency_table('adjacency_table_test', id_field='cbbl', output_schema='testing') as adjacency_table:
            # verify there is now 1 layer and 2 tables in the db and that adjacency table is of type "Table"
            tables = self.workspace.list_tables(schema='testing')
            self.assertEqual(len(tables), 1)
            self.assertIn('adjacency_table_test', tables)
            self.assertIsInstance(adjacency_table, Table)
            self.assertEqual(adjacency_table.count, 16)

        self.workspace.drop_schema('testing', cascade=True)

    def test_copy_to_schema(self):
        output_layer = self.test_layer.copy_to_new_table(self.test_layer.table_name, output_schema='testing')
        self.assertIsInstance(output_layer, Layer)
        layer_list = self.workspace.list_tables_and_layers(schema='testing')
        self.assertEqual(len(layer_list), 1)
        self.assertIn('physical_blocks', layer_list)
        output_layer.delete()
        layer_list = self.workspace.list_tables_and_layers(schema='testing')
        self.assertEqual(len(layer_list), 0)
        self.workspace.drop_schema('testing')

    def test_reproject_to_layer(self):
        self.test_layer.select_layer_by_attribute('OBJECTID = 1092')
        with self.test_layer.reproject_to_layer('reproject_test', 4326) as reprojected_layer:
            self.assertEqual(reprojected_layer.count, 1)
            self.assertEqual(reprojected_layer.spatial_reference, 4326)
            with reprojected_layer.get_search_cursor(reprojected_layer.shape) as cursor:
                geometry = next(cursor)[reprojected_layer.shape]
                self.assertEqual(geometry.spatial_reference, 4326)
                self.assertEqual(geometry.wkt, 'MULTIPOLYGON (((-73.98480133968964 40.74839358146502, -73.98514584121077 40.74791901190429, -73.98672799859544 40.748579010476696, -73.98680181748703 40.748609824374135, -73.98701632340045 40.74869932394527, -73.9870826384487 40.74872702556731, -73.98728315983132 40.74881069409462, -73.98742412455863 40.7488694865071, -73.98789395158482 40.7490652636495, -73.98782153208903 40.749457490345264, -73.98771225610628 40.749608230654204, -73.98707955145927 40.74934409792781, -73.98700047942175 40.74931107467757, -73.9868422775547 40.74924506042546, -73.98676317970046 40.749212046914415, -73.9866840902161 40.749179018041396, -73.98654170588975 40.74911960140967, -73.98614617388499 40.74895458539953, -73.98480133968964 40.74839358146502)))')
