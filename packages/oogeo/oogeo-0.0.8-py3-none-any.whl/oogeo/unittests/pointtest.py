"""
Unit tests for the Point class. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""

from shapely.wkt import loads as wkt_to_geom

import unittest

from src.oogeo.objects.point import Point
import src.oogeo.objects.line
import src.oogeo.objects.polygon


class PointClassUnitTests(unittest.TestCase):

    def test_initialize_tuple(self):
        # initialize the point using a tuple
        point = (1, 1)
        point = Point(point, 2263)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 1)

    def test_initialize_dict(self):
        # initialize the point using a dictionary
        point = {'x': 1, 'y': 1}
        point = Point(point, 2263)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 1)

    def test_initialize_wkt(self):
        # initialize the point with well-known text
        wkt = "POINT (1 1)"
        point = Point(wkt, 2263)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 1)
        self.assertEqual(point.wkt, wkt)

    def test_initialize_spatial_reference(self):
        # initialize the point with well-known text and a spatial reference
        wkt = "POINT (1 1)"
        test_point = Point(wkt, 2263)
        self.assertEqual(test_point.spatial_reference, 2263)

    def test_initialize_geometry(self):
        # initialize the point using a shapely geometry
        wkt = "POINT (1 1)"
        point = wkt_to_geom(wkt)
        point = Point(point, 2263)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 1)

    def test_wkt(self):
        # initialize the point using a well-known text
        wkt = "POINT (1 1)"
        test_point = Point(wkt, 2263)
        self.assertEqual(test_point.wkt, wkt)

    def test_xy_properties(self):
        # verify that the x and y properties return appropriate values
        point = {'x': 1, 'y': 2}
        test_point = Point(point, 2263)
        self.assertEqual(test_point.x, 1)
        self.assertEqual(test_point.y, 2)

    def test_distance_to(self):
        # create two point that are one unit apart
        first_point = Point({'x': 1, 'y': 1}, 2263)
        second_point = Point({'x': 1, 'y': 2}, 2263)
        self.assertEqual(first_point.distance_to(second_point), 1)

    def test_buffer(self):
        # create a buffer around a point
        buffer_point = Point({'x': 1, 'y': 1}, 2263)
        buffer = buffer_point.buffer(1)
        self.assertIsInstance(buffer, src.oogeo.objects.polygon.Polygon)
        self.assertAlmostEqual(buffer.area, 3.14, 2)

    def test_snap_to_vertex(self):
        # create a line and set of snap targets to snap the line to
        point = Point(
            {'x': 3, 'y': 0}, 2263
        )

        snap_square = src.oogeo.objects.polygon.Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        snap_line = src.oogeo.objects.line.Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0}
        ], 2263)
        snap_point = Point(
            {'x': 2, 'y': 0}, 2263
        )

        result = point.snap_to_vertex(snap_point, 2)
        self.assertIsInstance(result, Point)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 0)

        result = point.snap_to_vertex(snap_line, 2)
        self.assertIsInstance(result, Point)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 0)

        result = point.snap_to_vertex(snap_square, 2)
        self.assertIsInstance(result, Point)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 0)

    def test_project(self):
        point = Point(
            {'x': -80, 'y': 50}, 4326
        )
        new_point = point.project(26917)
        self.assertAlmostEqual(new_point.x, 571666.4475041276, 6)
        self.assertAlmostEqual(new_point.y, 5539109.815175673, 6)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PointClassUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
