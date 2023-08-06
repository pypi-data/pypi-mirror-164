"""
Unit tests for the Polygon class. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""

import unittest

from shapely.geometry import MultiPolygon
from shapely.wkt import loads as wkt_to_geom

from src.oogeo.objects.line import Line
from src.oogeo.objects.point import Point
from src.oogeo.objects.polygon import Polygon, correct_invalid_polygon
from src.oogeo.unittests.utilities import verify_edges


def create_multi_polygon(polygons):
    """ Creates a multi-polygon from the provided list of polygon coordinates.

    :param polygons: A list of polygon coordinates to be added to the multi-polygon
    :return: A `Polygon()` object that is multi-polygon.
    """

    polygons = [Polygon(polygon, 2263).geometry.geoms[0] for polygon in polygons]
    return Polygon(MultiPolygon(polygons), 2263)


class PolygonClassUnitTests(unittest.TestCase):

    def test_initialize_single_point(self):
        # try to create a polygon with a single point - this should error
        self.assertRaises(AssertionError, Polygon, {'x': 0, 'y': 0}, 2263)

    def test_has_duplicate_vertices(self):
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertFalse(test_polygon.has_duplicate_vertices())

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_polygon.has_duplicate_vertices())

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_polygon.has_duplicate_vertices())

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_polygon.has_duplicate_vertices())

    def test_remove_duplicate_vertices(self):

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_polygon.has_duplicate_vertices())
        test_polygon = test_polygon.remove_duplicate_vertices()
        self.assertFalse(test_polygon.has_duplicate_vertices())

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_polygon.has_duplicate_vertices())
        test_polygon = test_polygon.remove_duplicate_vertices()
        self.assertFalse(test_polygon.has_duplicate_vertices())

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_polygon.has_duplicate_vertices())
        test_polygon = test_polygon.remove_duplicate_vertices()
        self.assertFalse(test_polygon.has_duplicate_vertices())

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0.0000000001},
            {'x': 0, 'y': 0},
        ], 2263, allow_invalid=True)
        self.assertTrue(test_polygon.has_duplicate_vertices(tolerance=0.0000001))
        test_polygon = test_polygon.remove_duplicate_vertices(tolerance=0.0000001)
        self.assertFalse(test_polygon.has_duplicate_vertices(tolerance=0.0000001))

    def test_is_sliver(self):
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 10, 'y': 0},
            {'x': 10, 'y': 1},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertFalse(test_polygon.is_sliver(0.5))
        self.assertTrue(test_polygon.is_sliver(1.5))

        sliver_shapely = wkt_to_geom('MULTIPOLYGON (((1003303.815226838 183793.65247567, 1003323.777457252 183792.2719010115, 1003343.735422596 183790.8916544169, 1003363.685513929 183789.5120640099, 1003383.612967506 183788.1354263425, 1003383.571629003 183787.586871013, 1003283.809361339 183794.5556890815, 1003283.849059418 183795.0330503434, 1003303.815226838 183793.65247567)))')
        test_polygon = Polygon(sliver_shapely, 2263)
        self.assertTrue(test_polygon.is_sliver(0.6))
        self.assertTrue(test_polygon.is_sliver(0.5 * 1.15))

    def test_is_panhandle(self):
        panhandle_polygon = wkt_to_geom('MultiPolygon (((994594.96486242115497589 185083.88709992170333862, 994547.98201675713062286 185096.67972525954246521, 994507.40073308348655701 185090.08689066767692566, 994507.52901367843151093 185090.31523667275905609, 994600.82803967595100403 185105.30241142213344574, 994594.96486242115497589 185083.88709992170333862)))')
        test_polygon = Polygon(panhandle_polygon, 2263)
        self.assertTrue(test_polygon.is_panhandle(0.5))

    def test_correct_invalid_polygon(self):
        # load invalid polygon from wkt
        invalid_polygon = wkt_to_geom('MULTIPOLYGON (((998181.7384430777 220383.8550229302, 998180.6830846 220381.9595482, 998179.6265369284 220380.0619636702, 998093.9603617619 220427.6571546682, 998121.9975065 220478.0125057, 998096.0716202535 220431.4490230435, 998096.1525602558 220431.4040550667, 998181.7384430777 220383.8550229302)))')
        self.assertFalse(invalid_polygon.is_valid)

        corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        self.assertTrue(corrected_polygon.is_valid)

        # load invalid polygon from wkt
        invalid_polygon = wkt_to_geom('MULTIPOLYGON (((1004093.695416474 255146.4858733474, 1004130.4851614 255180.4493343, 1004180.541656191 255125.3147045502, 1004173.188124135 255118.5903592171, 1004173.575158629 255118.1671104975, 1004162.518394119 255107.9626296158, 1004112.065100317 255163.4443502591, 1004093.695416474 255146.4858733474)))')
        self.assertFalse(invalid_polygon.is_valid)

        corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        self.assertTrue(corrected_polygon.is_valid)

        invalid_polygon = wkt_to_geom('MultiPolygon (((1001594.17527340003289282 233573.72811210001236759, 1001518.41521386301610619 233615.62428152089705691, 1001550.42009844095446169 233597.92521852179197595, 1001598.88708802999462932 233685.30362714719376527, 1001642.64236800000071526 233661.10621820000233129, 1001594.17527340003289282 233573.72811210001236759)))')

        corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        self.assertTrue(corrected_polygon.is_valid)

        invalid_polygon = wkt_to_geom('MultiPolygon (((920024.0722319291671738 125942.31172181050351355, 920013.83220084011554718 125938.51228067280317191, 920008.50239960080944002 125958.98859780450584367, 920019.64771340775769204 125962.46235728080500849, 919998.12185300013516098 126060.49783032959385309, 920024.0722319291671738 125942.31172181050351355)))')
        corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        self.assertTrue(corrected_polygon.is_valid)

        invalid_polygon = wkt_to_geom('MultiPolygon (((920046.35380502487532794 125840.28926518819935154, 920046.35380502487532794 125840.28926518819935154, 920028.7601323863491416 125920.91399536149401683, 919932.91429717803839594 125891.09317277259833645, 919929.39142483472824097 125907.23708075280592311, 920013.83220084011554718 125938.51228067280317191, 920024.0722319291671738 125942.31172181050351355, 920027.0646324553526938 125928.68339775850472506, 920027.09228860423900187 125928.55705304880393669, 920046.35380502487532794 125840.28926518819935154)))')
        corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        self.assertTrue(corrected_polygon.is_valid)

        # no longer testing these cases - this function is depreciated
        # invalid_polygon = wkt_to_geom('MULTIPOLYGON (((989908.1861252695 227122.8884342581, 989859.5917872 227035.4849551, 989750.2156936 227096.0287972, 989837.7063758497 227047.5993655299, 989886.2855789515 227135.0069759444, 989886.9753203362 227136.2480141334, 989935.5545232634 227223.6556242336, 989886.2855789515 227135.0069759444, 989903.6674612078 227125.3854407433, 989903.6693415458 227125.3888374274, 989908.1861252695 227122.8884342581)), ((989798.7948967018 227183.4364076145, 989848.0639231 227272.0852036, 989799.4847201387 227184.6775934383, 989798.7948967018 227183.4364076145)))')
        # corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        # self.assertTrue(corrected_polygon.is_valid)
        #
        # invalid_polygon = wkt_to_geom('MultiPolygon (((989649.02891724265646189 213535.52197094840812497, 989661.1169990838970989 213557.40546854041167535, 989690.47960790770594031 213541.03879328790935688, 989690.48415919148828834 213541.04695851169526577, 989709.7101341406814754 213530.33278379120747559, 989709.71157897997181863 213530.33537647291086614, 989748.15011850453447551 213508.91599551049876027, 989748.15706968470476568 213508.92846987731172703, 989773.81029188085813075 213494.62748081600875594, 989726.65702365338802338 213409.26520982378860936, 989726.65701814508065581 213409.2651977218920365, 989726.65693923644721508 213409.26524169990443625, 989761.72206663258839399 213472.74405685419333167, 989757.8240749699762091 213474.91708352908608504, 989757.81931785575579852 213474.90854656320880167, 989719.38013015000615269 213496.3282887160894461, 989719.37832410086411983 213496.32504786399658769, 989700.15030773938633502 213507.04036021459614858, 989700.14461863471660763 213507.03015368490014225, 989649.02891724265646189 213535.52197094840812497)))')
        #
        # corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        # self.assertTrue(corrected_polygon.is_valid)
        #
        # invalid_polygon = wkt_to_geom('MultiPolygon (((996024.90885291993618011 163162.32398775219917297, 995894.1118704229593277 163143.14817309379577637, 995892.94619034230709076 163149.60977433621883392, 995887.32874751091003418 163182.31640183925628662, 995887.32874751091003418 163182.31640183925628662, 996019.24088525772094727 163201.82620534300804138, 996024.90885291993618011 163162.32398775219917297)))')
        # corrected_polygon = correct_invalid_polygon(invalid_polygon, 2263)
        # self.assertTrue(corrected_polygon.is_valid)

    def test_initialize_tuple(self):
        # initialize the polygon using a list of points
        point_array = [(0, 0), (0, 1), (1, 1), (1, 0)]
        Polygon(point_array, 2263)

    def test_initialize_dict(self):
        # initialize the polygon using a list of dict points
        point_array = [{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 0}]
        Polygon(point_array, 2263)

    def test_initialize_rings(self):
        # initialize the polygon using a list rings
        # exterior_array = [{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}]
        ring_array = [{'x': 2, 'y': 2}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}]
        poly = Polygon([{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}, ring_array], 2263)
        self.assertFalse(poly.is_multipart)
        self.assertTrue(poly.is_valid)

    def test_initialize_multipart(self):
        array_1 = [{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}]
        array_2 = [{'x': 10, 'y': 10}, {'x': 10, 'y': 15}, {'x': 15, 'y': 15}, {'x': 15, 'y': 10}]
        poly = Polygon([array_1, array_2], 2263)
        self.assertTrue(poly.is_multipart)
        self.assertTrue(poly.is_valid)


    def test_centroid(self):
        # create a new 2 x 2 polygon (centroid should be 1,1)
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertEqual(test_polygon.centroid.x, 1)
        self.assertEqual(test_polygon.centroid.y, 1)

    def test_boundary(self):
        # create a square and verify it's boundary has 4 turns and it's length is 8
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        test_boundary = test_polygon.boundary
        self.assertEqual(test_boundary.turn_count, 4)
        self.assertEqual(test_boundary.length, 8)

    def test_area(self):
        # create a polygon of area 4
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        self.assertEqual(test_polygon.area, 4)

    def test_mbr(self):
        # create a polygon with a concave edge
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 2, 'y': 3},
            {'x': 2, 'y': 0},
        ], 2263)

        # verify the MBR is a rectangle
        lines = test_polygon.mbr.to_lines()
        self.assertEqual(len(lines), 4)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 3},
            {'x': 2, 'y': 3},
            {'x': 2, 'y': 0},
        ]
        self.assertEqual(verify_edges(lines, target_points), 4)

        # create a polygon with a "point" (similar to a roof-shape)
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 3, 'y': 1},
            {'x': 3, 'y': 0},
        ], 2263)

        # verify that the MBR is a rectangle
        lines = test_polygon.mbr.to_lines()
        self.assertEqual(len(lines), 4)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 3, 'y': 2},
            {'x': 3, 'y': 0},
        ]
        self.assertEqual(verify_edges(lines, target_points), 4)

    def test_convex_hull(self):
        # create a polygon with a concave edge
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 2, 'y': 3},
            {'x': 2, 'y': 0},
        ], 2263)

        # verify that the hull is a rectangle
        lines = test_polygon.convex_hull.to_lines()
        self.assertEqual(len(lines), 4)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 3},
            {'x': 2, 'y': 3},
            {'x': 2, 'y': 0},
        ]
        self.assertEqual(verify_edges(lines, target_points), 4)

        # create a polygon with a "point" (similar to a roof-shape)
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 3, 'y': 1},
            {'x': 3, 'y': 0},
        ], 2263)

        # verify that the convex hull is the same as the original polygon
        lines = test_polygon.convex_hull.to_lines()
        self.assertEqual(len(lines), 5)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 3, 'y': 1},
            {'x': 3, 'y': 0},
        ]
        self.assertEqual(verify_edges(lines, target_points), 5)

    def test_union(self):
        # create 2 adjacent polygons and union them together
        polygon_1 = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 0},
        ], 2263)
        polygon_2 = Polygon([
            {'x': 1, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 1},
            {'x': 2, 'y': 0},
        ], 2263)

        test_polygon = polygon_1.union(polygon_2)
        lines = test_polygon.to_lines()
        self.assertEqual(len(lines), 6)

        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 1},
            {'x': 2, 'y': 0},
            {'x': 1, 'y': 0},
        ]
        self.assertEqual(verify_edges(lines, target_points), 6)

    def test_to_lines(self):
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 0},
        ], 2263)
        lines = test_polygon.to_lines()
        self.assertEqual(len(lines), 4)

        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 0},
        ]
        self.assertEqual(verify_edges(lines, target_points), 4)

    def test_touches(self):
        # create four polygons, one that touches, one that crosses, and one that does not touch the test polygon
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        touching_polygon = Polygon([
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)
        crossing_polygon = Polygon([
            {'x': 1, 'y': 0},
            {'x': 1, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 3, 'y': 0},
            {'x': 3, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)

        self.assertTrue(test_polygon.touches(touching_polygon))
        self.assertFalse(test_polygon.touches(crossing_polygon))
        self.assertFalse(test_polygon.touches(non_touching_polygon))

        # create 4 points (one interior, two touching, and one exterior) and test
        interior_point = Point({'x': 1, 'y': 1}, 2263)
        touching_vertex_point = Point({'x': 2, 'y': 2}, 2263)
        touching_edge_point = Point({'x': 2, 'y': 1}, 2263)
        exterior_point = Point({'x': 3, 'y': 3}, 2263)

        self.assertTrue(test_polygon.touches(touching_vertex_point))
        self.assertTrue(test_polygon.touches(touching_edge_point))
        self.assertFalse(test_polygon.touches(interior_point))
        self.assertFalse(test_polygon.touches(exterior_point))

    def test_distance_to(self):
        # create 2 polygons 1 unit apart and measure the distance between them
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 3, 'y': 0},
            {'x': 3, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)
        self.assertEqual(test_polygon.distance_to(non_touching_polygon), 1)

    def test_disjoint(self):
        # create four polygons, one that touches, one that crosses, and one that does not touch the test polygon
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        touching_polygon = Polygon([
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)
        crossing_polygon = Polygon([
            {'x': 1, 'y': 0},
            {'x': 1, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 3, 'y': 0},
            {'x': 3, 'y': 2},
            {'x': 4, 'y': 2},
            {'x': 4, 'y': 0},
        ], 2263)

        self.assertFalse(test_polygon.disjoint(touching_polygon))
        self.assertFalse(test_polygon.disjoint(crossing_polygon))
        self.assertTrue(test_polygon.disjoint(non_touching_polygon))

    def test_contains(self):
        # create four polygons, one that touches, one that crosses, and one that does not touch the test polygon
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)
        inner_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 1},
        ], 2263)

        crossing_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 6},
            {'x': 2, 'y': 6},
            {'x': 2, 'y': 1},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 5},
        ], 2263)

        self.assertTrue(test_polygon.contains(inner_polygon))
        self.assertFalse(test_polygon.contains(crossing_polygon))
        self.assertFalse(test_polygon.contains(non_touching_polygon))

    def test_within(self):
        # create four polygons, one that touches, one that crosses, and one that does not touch the test polygon
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)
        inner_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 1},
        ], 2263)

        outer_polygon = Polygon([
            {'x': -1, 'y': -1},
            {'x': -1, 'y': 5},
            {'x': 5, 'y': 5},
            {'x': 5, 'y': -1},
        ], 2263)
        crossing_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 6},
            {'x': 2, 'y': 6},
            {'x': 2, 'y': 1},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 5},
        ], 2263)

        self.assertFalse(test_polygon.within(inner_polygon))
        self.assertFalse(test_polygon.within(crossing_polygon))
        self.assertFalse(test_polygon.within(non_touching_polygon))
        self.assertTrue(test_polygon.within(outer_polygon))

    def test_buffer(self):
        # create a small polygon and buffer around it
        test_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 1},
        ], 2263)
        buffer_polygon = test_polygon.buffer(1, end_style='SQUARE', join_style='MITRE')
        self.assertIsInstance(buffer_polygon, Polygon)

    def test_snap_point(self):
        # create a line and a point, and snap the point to the line
        square = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        snap_point = Point(
            {'x': 3, 'y': 1}, 2263
        )

        snapped_point = square.snap_point(snap_point)

        self.assertEqual(snapped_point.x, 2)
        self.assertEqual(snapped_point.y, 1)

    def test_nearest_point(self):
        # create two polygons and find the nearest points between them
        polygon_1 = Polygon([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ], 2263)
        polygon_2 = Polygon([
            {'x': 3, 'y': 3},
            {'x': 5, 'y': 3},
            {'x': 5, 'y': 5},
            {'x': 3, 'y': 5}
        ], 2263)
        nearest_point = polygon_1.nearest_point(polygon_2)
        self.assertEqual(nearest_point.x, 2)
        self.assertEqual(nearest_point.y, 2)

        nearest_point = polygon_2.nearest_point(polygon_1)
        self.assertEqual(nearest_point.x, 3)
        self.assertEqual(nearest_point.y, 3)

    def test_add_point(self):
        polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ], 2263)

        new_polygon = polygon.add_point(Point({'x': 1, 'y': 3}, 2263))

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]
        self.assertTrue(new_polygon.is_valid)
        self.assertEqual(verify_edges(new_polygon.to_lines(), target_points), 5)

        new_polygon = new_polygon.add_point(Point({'x': 1, 'y': 0}, 2263))
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]

        self.assertTrue(new_polygon.is_valid)
        self.assertEqual(verify_edges(new_polygon.to_lines(), target_points), 6)

    def test_replace_point(self):
        polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ], 2263)

        new_polygon = polygon.replace_point(Point({'x': 2, 'y': 0}, 2263), Point({'x': 3, 'y': 0}, 2263))

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 3, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]
        self.assertTrue(new_polygon.is_valid)
        self.assertEqual(verify_edges(new_polygon.to_lines(), target_points), 4)

        new_polygon = polygon.replace_point(Point({'x': 2, 'y': 0}, 2263), Point({'x': 2, 'y': 2}, 2263))

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]
        self.assertTrue(new_polygon.is_valid)
        self.assertEqual(verify_edges(new_polygon.to_lines(), target_points), 3)

        # verify it works on polygons with interior rings
        # exterior_array = [{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}]
        ring_array = [{'x': 2, 'y': 2}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}]
        polygon = Polygon([{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}, ring_array], 2263)

        new_polygon = polygon.replace_point(Point({'x': 2, 'y': 2}, 2263), Point({'x': 1, 'y': 1}, 2263))
        self.assertTrue(new_polygon.is_valid)

    def test_replace_points(self):

        # verify it works on polygons with interior rings
        # exterior_array = [{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}]
        ring_array = [{'x': 2, 'y': 2}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}]
        polygon = Polygon([{'x': 0, 'y': 0}, {'x': 0, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 0}, ring_array], 2263)

        point_map = [
            {
                'original_point': Point({'x': 2, 'y': 2}, 2263),
                'new_point': Point({'x': 1, 'y': 1}, 2263)
            },
            {
                'original_point': Point({'x': 5, 'y': 5}, 2263),
                'new_point': Point({'x': 6, 'y': 6}, 2263)
            }
        ]

        new_polygon = polygon.replace_points(point_map)
        self.assertTrue(new_polygon.is_valid)

    def test_snap_to_vertex(self):
        # create a square and set of snap targets to snap the square to
        square = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        snap_point = Point(
            {'x': 3, 'y': 0}, 2263
        )

        result = square.snap_to_vertex(snap_point, 2)
        self.assertIsInstance(result, Polygon)
        self.assertEqual(result.point_count, 5)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 0}
        ]
        self.assertEqual(verify_edges(result.to_lines(), target_points), 4)

        # test snap to line
        snap_line = Line([
            {'x': 3, 'y': 0},
            {'x': 6, 'y': 0}
        ], 2263)

        result = square.snap_to_vertex(snap_line, 2)
        self.assertIsInstance(result, Polygon)
        self.assertEqual(result.point_count, 5)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 0}
        ]
        self.assertEqual(verify_edges(result.to_lines(), target_points), 4)

        # test snap to polygon
        snap_polygon = Polygon([
            {'x': 3, 'y': 0},
            {'x': 6, 'y': 0},
            {'x': 6, 'y': 1},
        ], 2263)

        result = square.snap_to_vertex(snap_polygon, 2)
        self.assertIsInstance(result, Polygon)
        self.assertEqual(result.point_count, 5)

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 0}
        ]
        self.assertEqual(verify_edges(result.to_lines(), target_points), 4)

    def test_snap_to_edge(self):
        # create a square and a line to snap to
        line = Line([
            {'x': 0, 'y': 3},
            {'x': 6, 'y': 3},
            {'x': 12, 'y': 3},
        ], 2263)
        square = Polygon([
            {'x': 3, 'y': 0},
            {'x': 3, 'y': 2},
            {'x': 9, 'y': 2},
            {'x': 9, 'y': 0},
        ], 2263)

        result = square.snap_to_edge(line, 1.1)
        self.assertIsInstance(result, Polygon)
        self.assertEqual(result.point_count, 5)

        # verify each edge is correct
        target_points = [
            {'x': 3, 'y': 0},
            {'x': 3, 'y': 3},
            {'x': 9, 'y': 3},
            {'x': 9, 'y': 0},
        ]
        self.assertEqual(verify_edges(result.to_lines(), target_points), 4)

        # test densify option
        result = square.snap_to_edge(line, 1.1, densify=True)
        self.assertIsInstance(result, Polygon)
        self.assertEqual(result.point_count, 6)

        # verify each edge is correct
        target_points = [
            {'x': 3, 'y': 0},
            {'x': 3, 'y': 3},
            {'x': 6, 'y': 3},
            {'x': 9, 'y': 3},
            {'x': 9, 'y': 0},
        ]
        self.assertEqual(verify_edges(result.to_lines(), target_points), 5)

    def test_contains_point(self):
        # set up a test polygon and point
        square = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        point = Point(
            {'x': 3, 'y': 0},
            2263)
        self.assertFalse(square.contains_point(point))
        point = Point(
            {'x': 2, 'y': 2},
            2263)
        self.assertTrue(square.contains_point(point))

    def test_cut(self):
        # create a 4x4 polygon and cut it into 2 4x2 polygons
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)

        cut_line = Line([{'x': 0, 'y': 2}, {'x': 4, 'y': 2}], 2263)

        polygons = test_polygon.cut(cut_line)
        self.assertEqual(len(polygons), 2)
        self.assertEqual(polygons[0].area, 8)
        self.assertEqual(polygons[1].area, 8)

    def test_intersects(self):
        # create test polygon and one that touches,
        # one that crosses, and one that does not intersect the test polygon
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)
        inner_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 1},
        ], 2263)

        crossing_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 6},
            {'x': 2, 'y': 6},
            {'x': 2, 'y': 1},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 5},
        ], 2263)

        self.assertTrue(test_polygon.intersects(inner_polygon))
        self.assertTrue(test_polygon.intersects(crossing_polygon))
        self.assertFalse(test_polygon.intersects(non_touching_polygon))

        # test polygons that do not intersect but cross each others bounding boxes

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 5},
            {'x': 1, 'y': 5},
            {'x': 1, 'y': 1},
            {'x': 6, 'y': 1},
            {'x': 6, 'y': 0},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 2},
        ], 2263)
        self.assertFalse(test_polygon.intersects(non_touching_polygon))

        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 5},
            {'x': 1, 'y': 5},
            {'x': 1, 'y': 1},
            {'x': 6, 'y': 1},
            {'x': 6, 'y': 0},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 4},
            {'x': 7, 'y': 4},
            {'x': 7, 'y': 2},
        ], 2263)
        self.assertFalse(test_polygon.intersects(non_touching_polygon))

    def test_is_multipart(self):
        # create a single-part polygon and a multi-part and verify their properties
        single_part_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)

        multi_part_points = [
            [
                {'x': 0, 'y': 0},
                {'x': 0, 'y': 4},
                {'x': 4, 'y': 4},
                {'x': 4, 'y': 0},
            ],
            [
                {'x': 5, 'y': 5},
                {'x': 5, 'y': 8},
                {'x': 8, 'y': 8},
                {'x': 8, 'y': 5},
            ],
        ]
        multi_part_polygon = create_multi_polygon(multi_part_points)
        self.assertTrue(multi_part_polygon.is_multipart)
        self.assertFalse(single_part_polygon.is_multipart)

    def test_to_singlepart(self):
        # create a single-part polygon and a multi-part and verify their properties
        single_part_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)

        sub_poly_1 = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)

        sub_poly_2 = Polygon([
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 8},
            {'x': 8, 'y': 8},
            {'x': 8, 'y': 5},
        ], 2263)

        multi_part_points = [
            [
                {'x': 0, 'y': 0},
                {'x': 0, 'y': 4},
                {'x': 4, 'y': 4},
                {'x': 4, 'y': 0},
            ],
            [
                {'x': 5, 'y': 5},
                {'x': 5, 'y': 8},
                {'x': 8, 'y': 8},
                {'x': 8, 'y': 5},
            ],
        ]
        multi_part_polygon = create_multi_polygon(multi_part_points)

        # test single part polygon
        single_parts = single_part_polygon.to_singlepart()
        self.assertEqual(len(single_parts), 1)
        self.assertTrue(single_parts[0].equals(single_part_polygon))

        # test multi part polygon
        single_parts = multi_part_polygon.to_singlepart()
        self.assertEqual(len(single_parts), 2)
        self.assertTrue(single_parts[0].equals(sub_poly_1))
        self.assertTrue(single_parts[1].equals(sub_poly_2))

    def test_generalize(self):
        # create a polygon with unnecessary points and generalize it
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)
        simplified_polygon = test_polygon.generalize()
        self.assertIsInstance(simplified_polygon, Polygon)
        self.assertEqual(len(simplified_polygon.points), 5)

    def test_point_properties(self):
        # create a polygon with and tests it's point properties
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)
        self.assertEqual(test_polygon.point_count, 8)
        self.assertEqual(len(test_polygon.points), 8)

    def test_intersection(self):
        # create test polygon and one that touches, on that shares and edge with,
        # one that crosses, and one that does not intersect the test polygon
        test_polygon = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
        ], 2263)
        inner_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 1},
        ], 2263)

        boundary_polygon = Polygon([
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 0},
            {'x': 6, 'y': 0},
            {'x': 6, 'y': 4},
        ], 2263)

        touching_polygon = Polygon([
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 4},
        ], 2263)

        crossing_polygon = Polygon([
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 6},
            {'x': 2, 'y': 6},
            {'x': 2, 'y': 1},
        ], 2263)
        non_touching_polygon = Polygon([
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 6},
            {'x': 6, 'y': 6},
            {'x': 6, 'y': 5},
        ], 2263)

        inner_intersection = test_polygon.intersection(inner_polygon)
        self.assertIsInstance(inner_intersection, Polygon)
        boundary_intersection = test_polygon.intersection(boundary_polygon)
        self.assertIsInstance(boundary_intersection, Line)
        touching_intersection = test_polygon.intersection(touching_polygon)
        self.assertIsInstance(touching_intersection, Point)
        crossing_intersection = test_polygon.intersection(crossing_polygon)
        self.assertIsInstance(crossing_intersection, Polygon)
        non_touching_intersection = test_polygon.intersection(non_touching_polygon)
        self.assertIsNone(non_touching_intersection)

        test_polygon = Polygon('MultiPolygon (((988461.2379566878080368 211936.98201566934585571, 988365.81295062601566315 211764.06471055746078491, 987927.38994300365447998 212004.45300932228565216, 987906.93460333347320557 212015.67641207575798035, 987847.49476160109043121 212048.27510015666484833, 987829.11881403625011444 212058.3649749755859375, 987773.55429266393184662 212088.83997964859008789, 987734.49301908910274506 212110.25430689752101898, 987604.30463117361068726 212181.56387557089328766, 987624.35052284598350525 212324.46746115386486053, 987654.6204753965139389 212379.3912358433008194, 987829.94099090993404388 212283.18440724909305573, 987851.85170821845531464 212271.15621607005596161, 987895.68921899795532227 212247.11164474487304688, 987917.60715411603450775 212235.08706247806549072, 987939.52279271185398102 212223.05690284073352814, 987978.97743822634220123 212201.4155418872833252, 988088.57958120107650757 212141.31198757886886597, 988461.2379566878080368 211936.98201566934585571)))', 2263)
        test_line = Line('MultiLineString ((987791.84831440448760986 212078.80631513893604279, 987806.41291718184947968 212182.63517116010189056))', 2263)
        intersection = test_polygon.intersection(test_line)
        self.assertIsNotNone(intersection)
        self.assertIsInstance(intersection, Line)

        boundary = test_polygon.boundary
        intersection = boundary.intersection(test_line)
        self.assertIsNotNone(intersection)
        self.assertIsInstance(intersection, Point)

    def test_project(self):
        poly = Polygon('MultiPolygon (((-73.97893923520638282 40.69087290659831524, -73.97888466526673312 40.69047789895636669, -73.97889209583466652 40.69047740896701271, -73.97950339533063868 40.69046128666730056, -73.97943255520712569 40.68995809392075813, -73.97960914426312229 40.6899634823513523, -73.97998753927181781 40.68997693040562069, -73.9805256982288455 40.68999625421174926, -73.98060953033899523 40.69062534716058366, -73.98061474108125424 40.69062477827019109, -73.98133150948108039 40.69056294700607879, -73.9813325177215404 40.69056318567115937, -73.98151452811831064 40.69184084192470152, -73.98148382582000693 40.6918786248591644, -73.98023562784088369 40.69183301688332932, -73.98020310750368367 40.69158464485556692, -73.98006239645094695 40.69140241786742962, -73.98000979899762797 40.69105388277225899, -73.97994232965082517 40.69105870778071221, -73.979931100702359 40.69098758174454389, -73.97971518178567862 40.69100551359824891, -73.9797040232186589 40.69092954492386127, -73.979711884096929 40.6909290157446506, -73.97969470348570553 40.69081061990982562, -73.97893923520638282 40.69087290659831524),(-73.98041512302077649 40.69087817098922955, -73.98041297450320997 40.69086456332660617, -73.98034125375824033 40.69087153134806556, -73.98034296734195436 40.69088521321015861, -73.98008813191432864 40.69090990652193796, -73.98017046493990279 40.69143121845401367, -73.98035001690570311 40.69141206736919258, -73.98033979482477207 40.69134943613196498, -73.98056637467644236 40.69132525062082095, -73.98099182275821306 40.69091448237379183, -73.98107481215919279 40.69090646244679021, -73.98106255099855844 40.69083110744102783, -73.98102645907378871 40.69083462926276695, -73.98100279737587925 40.69065713765164105, -73.98064526649518768 40.6906917674269053, -73.98066570107700102 40.69085388714507445, -73.98041512302077649 40.69087817098922955)),((-73.97893923520638282 40.69087290659831524, -73.97906908769986956 40.69179203244080867, -73.97895999611766626 40.69102243152004661, -73.97893923520638282 40.69087290659831524)))', 4326)
        new_poly = poly.project(2263)
        self.assertIsInstance(new_poly, Polygon)
        self.assertEqual(new_poly.wkt, 'MULTIPOLYGON (((990090.545726848 190980.7714284807, 990105.7136862103 190836.86221491062, 990103.6530809792 190836.68320081008, 989934.1286188137 190830.76911647103, 989953.8170813756 190647.44587171113, 989904.8444907174 190649.39758559642, 989799.9058974272 190654.2729046806, 989650.6607404872 190661.27949507014, 989627.3614812416 190890.47132040688, 989625.91648505 190890.2637371388, 989427.1472064472 190867.69362075411, 989426.8675825992 190867.7805138414, 989376.2942155516 191333.25744911103, 989384.8055062235 191347.02467944685, 989730.9527776575 191330.48398858434, 989739.9915985699 191239.9968065761, 989779.0281106106 191173.6150190955, 989793.6432343778 191046.63678774683, 989812.353298121 191048.39895682113, 989815.473224598 191022.4863700508, 989875.3499796095 191029.03326215487, 989878.4508664699 191001.35636408877, 989876.2709437924 191001.163063597, 989881.0454447872 190958.02909506788, 990090.545726848 190980.7714284807), (989681.2538880042 190982.59444354082, 989681.8508207848 190977.6369064554, 989701.7397631672 190980.1800163933, 989701.2634356286 190985.16461310422, 989771.9320279008 190994.17707177554, 989749.056551624 191184.10111492194, 989699.2654013124 191177.11259232694, 989702.1052747524 191154.29483162425, 989639.2728302097 191145.46931935713, 989521.3213611478 190995.7885147993, 989498.307487147 190992.8616371843, 989501.713670799 190965.4083348984, 989511.7223677826 190966.69360365503, 989518.2982287761 190902.02963089035, 989617.4457903698 190914.66797771733, 989611.7658449265 190973.73169031116, 989681.2538880042 190982.59444354082)), ((990090.545726848 190980.7714284807, 990054.4551775004 191315.62729765527, 990084.7752515648 191035.24635651222, 990090.545726848 190980.7714284807)))')

        poly = Polygon('MultiPolygon (((-73.9536345214308426 40.75013046258509775, -73.9536620697627427 40.75005200369039216, -73.95385313811348738 40.74950781801577193, -73.95499775779462936 40.74974238781581448, -73.95487669032662836 40.74993136016745154, -73.95481710232581918 40.75002443935308349, -73.95472490203545135 40.7501721697492556, -73.95462295071591541 40.75033016116197615, -73.9536345214308426 40.75013046258509775)),((-73.95507561365576521 40.74962883431142302, -73.95507869449259886 40.7496243288538551, -73.95550306871396629 40.74971137514044983, -73.95545339922213657 40.74987587911346765, -73.95535428775281162 40.75000697890153845, -73.95522763673493216 40.7499882980820658, -73.95523721306511788 40.74994516747889151, -73.95516983358237439 40.7499314743074379, -73.95513782755703858 40.74992377426472956, -73.95518904407653338 40.74975723446802789, -73.9552154922069036 40.74967610083598402, -73.95520229419309999 40.74967609571840654, -73.95519134589386567 40.74967438319596624, -73.95518236148195967 40.7496718195979355, -73.95517337885627285 40.74966839780394423, -73.95515541343230836 40.74965984861553636, -73.95511275037507914 40.74963677003092499, -73.95510264459637995 40.74963249679476718, -73.95508804645299961 40.74962800655017503, -73.95507561365576521 40.74962883431142302)))', 4326)
        new_poly = poly.project(2263)
        self.assertIsInstance(new_poly, Polygon)
        self.assertEqual(new_poly.wkt, 'MULTIPOLYGON (((997096.5904499806 212572.81822543294, 997088.9726918113 212544.2290872872, 997036.1373313515 212345.93680227126, 996718.9480662923 212431.23311865123, 996752.457236849 212500.09907968715, 996768.9499782874 212534.019331315, 996794.4683458854 212587.8554575263, 996822.6863958932 212645.43142966126, 997096.5904499806 212572.81822543294)), ((996697.3974561213 212389.85085349856, 996696.5446769568 212388.20893270758, 996578.945336093 212419.86267965974, 996592.6769837695 212479.8037616105, 996620.1137867826 212527.58161172178, 996655.2088181967 212520.79349877685, 996652.5635066853 212505.0782767079, 996671.2350994422 212500.09896111523, 996680.1045454443 212497.29812795712, 996665.9448621449 212436.61506082854, 996658.6318894993 212407.05172242498, 996662.2887193152 212407.05172777764, 996665.3225295148 212406.42935233057, 996667.8123560136 212405.4966246486, 996670.3018477906 212404.2512285994, 996675.2811980577 212401.13903221564, 996687.1063411993 212392.73681635407, 996689.9071911714 212391.18137402725, 996693.9528011951 212389.54750702519, 996697.3974561213 212389.85085349856)))')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PolygonClassUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
