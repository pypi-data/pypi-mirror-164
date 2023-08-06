"""
Unit tests for the Line class. For more information see the
[API Tests](https://github.com/envelopecity/GIS/tree/dev#api-tests) section of the GIS repository.
"""

import unittest

from shapely.geometry import MultiLineString

from src.oogeo.objects.line import Line
from src.oogeo.objects.point import Point
from src.oogeo.objects.polygon import Polygon
from src.oogeo.unittests.utilities import verify_edges


class LineClassUnitTests(unittest.TestCase):

    def test_initialize_single_point(self):
        # try to create a line with a single point - this should error
        self.assertRaises(AssertionError, Line, {'x': 0, 'y': 0}, 2263)

    def test_initialize_tuple(self):
        # initialize the line using a list of arcpy points
        point_array = [(0, 0), (1, 1)]
        Line(point_array, 2263)

    def test_initialize_dict(self):
        # initialize the line using a list of arcpy points
        point_array = [{'x': 0, 'y': 0}, {'x': 1, 'y': 1}]
        Line(point_array, 2263)

    def test_is_curve(self):
        # create a new line w/ 5 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        self.assertFalse(test_line.is_curve)

        # create a new line w/ 15 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4},
            {'x': 5, 'y': 5},
            {'x': 6, 'y': 6},
            {'x': 7, 'y': 7},
            {'x': 8, 'y': 8},
            {'x': 9, 'y': 9},
            {'x': 10, 'y': 10},
            {'x': 11, 'y': 11},
            {'x': 12, 'y': 12},
            {'x': 13, 'y': 13},
            {'x': 14, 'y': 14},
        ], 2263)
        self.assertFalse(test_line.is_curve)

        # create a new line w/ 15 points and a sharp turn to the right
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4},
            {'x': 5, 'y': 5},
            {'x': 6, 'y': 6},
            {'x': 7, 'y': 7},
            {'x': 8, 'y': 8},
            {'x': 9, 'y': 9},
            {'x': 10, 'y': 10},
            {'x': 11, 'y': 10},
            {'x': 12, 'y': 10},
            {'x': 13, 'y': 10},
            {'x': 14, 'y': 10},
        ], 2263)
        self.assertFalse(test_line.is_curve)

        # create a new line w/ 15 points and a sharp turn to the left that is not a curve
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4},
            {'x': 5, 'y': 5},
            {'x': 6, 'y': 6},
            {'x': 7, 'y': 7},
            {'x': 8, 'y': 8},
            {'x': 9, 'y': 9},
            {'x': 10, 'y': 10},
            {'x': 10, 'y': 11},
            {'x': 10, 'y': 12},
            {'x': 10, 'y': 13},
            {'x': 10, 'y': 14},
        ], 2263)
        self.assertFalse(test_line.is_curve)

        # create a new line w/ 15 points and a sharp turn to the left that is not a curve
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4},
            {'x': 0, 'y': 5},
            {'x': 0, 'y': 6},
            {'x': 0, 'y': 7},
            {'x': 0, 'y': 8},
            {'x': 0, 'y': 9},
            {'x': -1, 'y': 10},
            {'x': -2, 'y': 11},
            {'x': -3, 'y': 12},
            {'x': -4, 'y': 13},
            {'x': -5, 'y': 14},
        ], 2263)
        self.assertFalse(test_line.is_curve)

        # create a new line with a curve (these coordinate came from a real curve in Pluto)
        test_line = Line([
            {'x': 984574.921, 'y': 212397.725},
            {'x': 984585.576, 'y': 212392.202},
            {'x': 984594.656, 'y': 212387.916},
            {'x': 984603.887, 'y': 212383.925},
            {'x': 984613.249, 'y': 212380.235},
            {'x': 984622.718, 'y': 212376.852},
            {'x': 984630.347, 'y': 212374.412},
            {'x': 984638.048, 'y': 212372.237},
            {'x': 984645.819, 'y': 212370.335},
            {'x': 984653.653, 'y': 212368.702},
            {'x': 984661.537, 'y': 212367.345},
            {'x': 984669.461, 'y': 212366.264},
            {'x': 984677.422, 'y': 212365.462},
            {'x': 984685.406, 'y': 212364.936},
            {'x': 984693.404, 'y': 212364.689},
            {'x': 984701.403, 'y': 212364.720},
            {'x': 984709.398, 'y': 212365.031},
            {'x': 984717.308, 'y': 212365.615},
            {'x': 984733.448, 'y': 212367.660},
            {'x': 984744.696, 'y': 212369.305},
        ], 2263)
        self.assertTrue(test_line.is_curve)

        # these coordinates represent a curve to the left
        test_line = Line([
            {'x': 984898.649, 'y': 212353.496},
            {'x': 984888.475, 'y': 212356.921},
            {'x': 984878.192, 'y': 212360.006},
            {'x': 984867.811, 'y': 212362.742},
            {'x': 984857.348, 'y': 212365.130},
            {'x': 984846.806, 'y': 212367.170},
            {'x': 984836.202, 'y': 212368.852},
            {'x': 984825.548, 'y': 212370.178},
            {'x': 984814.017, 'y': 212371.220},
            {'x': 984802.458, 'y': 212371.875},
            {'x': 984790.883, 'y': 212372.137},
            {'x': 984779.309, 'y': 212372.012},
            {'x': 984767.741, 'y': 212371.498},
            {'x': 984756.200, 'y': 212370.595},
            {'x': 984744.696, 'y': 212369.305},
        ], 2263)
        self.assertTrue(test_line.is_curve)

        # these coordinates represent a line that is slightly "S" shaped, but not curved
        # enough to be flagged as a curve
        test_line = Line([
            {'x': 984701.403, 'y': 212364.720},
            {'x': 984709.398, 'y': 212365.031},
            {'x': 984717.308, 'y': 212365.615},
            {'x': 984733.448, 'y': 212367.660},
            {'x': 984744.696, 'y': 212369.305},
            {'x': 984756.200, 'y': 212370.595},
            {'x': 984767.741, 'y': 212371.498},
            {'x': 984779.309, 'y': 212372.012},
        ], 2263)
        self.assertFalse(test_line.is_curve)

    def test_snap_point(self):
        # create a line and a point, and snap the point to the line
        vertical_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        snap_point = Point(
            {'x': 1, 'y': 1}, 2263
        )

        snapped_point = vertical_line.snap_point(snap_point)

        self.assertEqual(snapped_point.x, 0)
        self.assertEqual(snapped_point.y, 1)

    def test_snap_to_vertex(self):
        # create a line and set of snap targets to snap the line to
        line = Line([
            {'x': 3, 'y': 0},
            {'x': 6, 'y': 0}
        ], 2263)

        snap_square = Polygon([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 0},
        ], 2263)
        snap_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0}
        ], 2263)
        snap_point = Point(
            {'x': 2, 'y': 0}, 2263
        )

        result = line.snap_to_vertex(snap_point, 2)
        self.assertIsInstance(result, Line)
        self.assertEqual(result.point_count, 2)
        self.assertEqual(result.first_point.x, 2)
        self.assertEqual(result.first_point.y, 0)

        result = line.snap_to_vertex(snap_line, 2)
        self.assertIsInstance(result, Line)
        self.assertEqual(result.point_count, 2)
        self.assertEqual(result.first_point.x, 2)
        self.assertEqual(result.first_point.y, 0)

        result = line.snap_to_vertex(snap_square, 2)
        self.assertIsInstance(result, Line)
        self.assertEqual(result.point_count, 2)
        self.assertEqual(result.first_point.x, 2)
        self.assertEqual(result.first_point.y, 0)

    def test_turn_direction(self):
        # create a simple turn to the right
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1}
        ], 2263)
        test_line_2 = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), 1)

        # create a simple turn to the left
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1}
        ], 2263)
        test_line_2 = Line([
            {'x': 0, 'y': 1},
            {'x': -1, 'y': 1}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), -1)

        # create an inverted turn to the right
        test_line_1 = Line([
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 0}
        ], 2263)
        test_line_2 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': 0}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), 1)

        # create an inverted turn to the left
        test_line_1 = Line([
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 0}
        ], 2263)
        test_line_2 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 0}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), -1)

        # create a left turn in the first quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)
        test_line_2 = Line([
            {'x': 1, 'y': 1},
            {'x': 0, 'y': 2}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), -1)

        # create a right turn in the first quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)
        test_line_2 = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 0}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), 1)

        # create a left turn in the fourth quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': 1}
        ], 2263)
        test_line_2 = Line([
            {'x': -1, 'y': 1},
            {'x': -2, 'y': 0}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), -1)

        # create a right turn in the fourth quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': 1}
        ], 2263)
        test_line_2 = Line([
            {'x': -1, 'y': 1},
            {'x': 0, 'y': 2}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), 1)

        # create a left turn in the third quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': -1}
        ], 2263)
        test_line_2 = Line([
            {'x': -1, 'y': -1},
            {'x': 0, 'y': -2}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), -1)

        # create a right turn in the third quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': -1}
        ], 2263)
        test_line_2 = Line([
            {'x': -1, 'y': -1},
            {'x': -2, 'y': 0}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), 1)

        # create a right turn in the second quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': -1}
        ], 2263)
        test_line_2 = Line([
            {'x': 1, 'y': -1},
            {'x': 0, 'y': -2}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), 1)

        # create a left turn in the second quadrant
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': -1}
        ], 2263)
        test_line_2 = Line([
            {'x': 1, 'y': -1},
            {'x': 2, 'y': 0}
        ], 2263)
        self.assertEqual(test_line_1.turn_direction(test_line_2), -1)

    def test_split_at_turns(self):
        # create a new line w/ 2 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)

        split_lines = test_line.split_line_at_turns()
        self.assertEqual(len(split_lines), 1)

        # create a new line w/ 5 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)

        split_lines = test_line.split_line_at_turns()
        self.assertEqual(len(split_lines), 1)

        # create a new line w/ 3 points and 1 turn
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1}
        ], 2263)

        split_lines = test_line.split_line_at_turns()
        self.assertEqual(len(split_lines), 2)

        # create a new line w/ 4 points and 2 turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2}
        ], 2263)
        split_lines = test_line.split_line_at_turns()
        self.assertEqual(len(split_lines), 3)

        # create a new line w/ 5 points and 3 turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
        ], 2263)
        split_lines = test_line.split_line_at_turns()
        self.assertEqual(len(split_lines), 4)

        # create a new line w/ 8 points, 3 turns, and 2 long straight edges (basically almost a rectangle)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 1},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 1},
            {'x': 4, 'y': 0},
            {'x': 3, 'y': 0},
            {'x': 2, 'y': 0}
        ], 2263)
        split_lines = test_line.split_line_at_turns()
        self.assertEqual(len(split_lines), 4)

    def test_turn_count_simple_line(self):
        # create a new line w/ 2 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)
        self.assertEqual(test_line.turn_count, 0)

    def test_turn_count_straight_line(self):
        # create a new line w/ 5 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        self.assertEqual(test_line.turn_count, 0)

    def test_turn_count_simple_turn(self):
        # create a new line w/ 3 points and 1 turn
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1}
        ], 2263)
        self.assertEqual(test_line.turn_count, 1)

    def test_turn_count_two_turn(self):
        # create a new line w/ 4 points and 2 turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2}
        ], 2263)
        self.assertEqual(test_line.turn_count, 2)

    def test_turn_count_three_turn(self):
        # create a new line w/ 5 points and 3 turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
        ], 2263)
        self.assertEqual(test_line.turn_count, 3)

    def test_turn_count_complex_edge(self):
        # create a new line w/ 8 points, 3 turns, and 2 long straight edges (basically almost a rectangle)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 1},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 1},
            {'x': 4, 'y': 0},
            {'x': 3, 'y': 0},
            {'x': 2, 'y': 0}
        ], 2263)
        self.assertEqual(test_line.turn_count, 3)

    def test_right_angles_straight_line(self):
        # create edges in a line with no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_right_angles(test_lines), 0)

    def test_right_angles_simple_turn(self):
        # create a new line w/ 3 points and 1 turn
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1}
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_right_angles(test_lines), 1)

    def test_right_angles_two_turn(self):
        # create a new line w/ 4 points and 2 turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2}
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_right_angles(test_lines), 2)

    def test_right_angle_three_turn(self):
        # create a new line w/ 5 points and 3 turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 2},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_right_angles(test_lines), 3)

    def test_is_parallelogram(self):
        # create a new line in the shape of a parallelogram
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 2},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertTrue(Line.is_parallelogram(test_lines))

    def test_parallel_sets(self):
        # create an irregular quadrilateral with 1 set of parallel edges
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 3, 'y': 2},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_parallel_sets(test_lines), 1)

        # create a new line in the shape of a rectangle (should have 2 parallel sets)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_parallel_sets(test_lines), 2)

        # create a new line in the shape of a parallelogram (should have 2 parallel sets)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 2},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_parallel_sets(test_lines), 2)

        # create a new line in the shape of a "hockey stick" (should have 3 parallel sets)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 4},
            {'x': 3, 'y': 4},
            {'x': 1, 'y': 2},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_parallel_sets(test_lines), 3)

        # create an irregular quadrilateral with no parallel edges (a "kite" shape)
        test_line = Line([
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 1, 'y': 5},
            {'x': 2, 'y': 4},
            {'x': 1, 'y': 0},
        ], 2263)
        test_lines = test_line.split_line_at_vertices()
        self.assertEqual(Line.count_parallel_sets(test_lines), 0)

    def test_generalize(self):
        # create a line with many points and then generalize it.
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4},
            {'x': 0, 'y': 5},
            {'x': 0, 'y': 6},
            {'x': 0, 'y': 7},
            {'x': 0, 'y': 8},
            {'x': 0, 'y': 9},
            {'x': 0, 'y': 10},
        ], 2263)

        generalized_line = test_line.generalize()
        self.assertEqual(generalized_line.point_count, 2)

        # create a turning line that cannot be generalized
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 10},
            {'x': 10, 'y': 10},
            {'x': 10, 'y': 0},
        ], 2263)
        generalized_line = test_line.generalize()
        self.assertEqual(generalized_line.point_count, 4)

    def test_first_point(self):
        # create a new line w/ 2 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)
        self.assertEqual(test_line.first_point.x, 0)
        self.assertEqual(test_line.first_point.y, 0)

    def test_last_point(self):
        # create a new line w/ 2 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)
        self.assertEqual(test_line.last_point.x, 1)
        self.assertEqual(test_line.last_point.y, 1)

    def test_points(self):
        # create a new line w/ 5 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        self.assertEqual(test_line.point_count, 5)
        self.assertEqual(len(test_line.points), 5)

        test_line_2 = Line([
            {'x': 6, 'y': 6},
            {'x': 7, 'y': 7},
            {'x': 8, 'y': 8},
            {'x': 9, 'y': 9},
            {'x': 10, 'y': 10}
        ], 2263)

        # test multiline geometry
        multiline_geometry = MultiLineString([test_line.geometry.geoms[0], test_line_2.geometry.geoms[0]])
        test_line_3 = Line(multiline_geometry, 2263)

        test_point = test_line_3.get_point(0)
        self.assertEqual(test_point.x, 0)
        self.assertEqual(test_point.y, 0)
        test_point = test_line_3.get_point(4)
        self.assertEqual(test_point.x, 4)
        self.assertEqual(test_point.y, 4)
        test_point = test_line_3.get_point(5)
        self.assertEqual(test_point.x, 6)
        self.assertEqual(test_point.y, 6)
        test_point = test_line_3.get_point(9)
        self.assertEqual(test_point.x, 10)
        self.assertEqual(test_point.y, 10)

    def test_centroid(self):
        # create a new line w/ 2 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        self.assertEqual(test_line.centroid.x, 1)
        self.assertEqual(test_line.centroid.y, 1)

    def test_midpoint(self):
        # create a new line w/ 2 points and no turns
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        self.assertEqual(test_line.midpoint.x, 1)
        self.assertEqual(test_line.midpoint.y, 1)

        # test a line with a turn
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 2},
            {'x': 2, 'y': 2}
        ], 2263)
        self.assertEqual(test_line.midpoint.x, 0)
        self.assertEqual(test_line.midpoint.y, 2)

    def test_nearest_point(self):
        # create two lines and find the nearest points between them
        test_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0}
        ], 2263)
        test_line_2 = Line([
            {'x': 0, 'y': 1},
            {'x': 2, 'y': 1}
        ], 2263)
        nearest_point = test_line_1.nearest_point(test_line_2.first_point)
        self.assertEqual(nearest_point.x, 0)
        self.assertEqual(nearest_point.y, 0)

        nearest_point = test_line_1.nearest_point(test_line_2.centroid)
        self.assertEqual(nearest_point.x, 1)
        self.assertEqual(nearest_point.y, 0)

        nearest_point = test_line_1.nearest_point(test_line_2.last_point)
        self.assertEqual(nearest_point.x, 2)
        self.assertEqual(nearest_point.y, 0)

        nearest_point = test_line_2.nearest_point(test_line_1.first_point)
        self.assertEqual(nearest_point.x, 0)
        self.assertEqual(nearest_point.y, 1)

        nearest_point = test_line_2.nearest_point(test_line_1.centroid)
        self.assertEqual(nearest_point.x, 1)
        self.assertEqual(nearest_point.y, 1)

        nearest_point = test_line_2.nearest_point(test_line_1.last_point)
        self.assertEqual(nearest_point.x, 2)
        self.assertEqual(nearest_point.y, 1)

    def test_length(self):
        # create a line along the axis
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4}
        ], 2263)
        self.assertEqual(test_line.length, 4)

    def test_is_parallel(self):
        # create two lines that are parallel and one that is perpendicular
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        parallel_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 3},
            {'x': 3, 'y': 4},
            {'x': 4, 'y': 5}
        ], 2263)
        perpendicular_line = Line([
            {'x': 0, 'y': 4},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 0}
        ], 2263)
        self.assertTrue(test_line.is_parallel(parallel_line))
        self.assertFalse(test_line.is_parallel(perpendicular_line))

    def test_is_perpendicular(self):
        # create two lines that are parallel and one that is perpendicular
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        parallel_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 3},
            {'x': 3, 'y': 4},
            {'x': 4, 'y': 5}
        ], 2263)
        perpendicular_line = Line([
            {'x': 0, 'y': 4},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 0}
        ], 2263)
        self.assertFalse(test_line.is_perpendicular(parallel_line, 1))
        self.assertTrue(test_line.is_perpendicular(perpendicular_line, 1))

    def test_distance_to(self):
        # create two lines that are parallel along an axis
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4}
        ], 2263)
        parallel_line = Line([
            {'x': 1, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 1, 'y': 3},
            {'x': 1, 'y': 4}
        ], 2263)

        self.assertEqual(test_line.distance_to(parallel_line), 1)

    def test_is_concave(self):
        # create a straight line, and contoured line that is not concave, and a line that is concave
        straight_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        right_angle_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1}
        ], 2263)
        concave_line = Line([
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 2, 'y': 1},
            {'x': 2, 'y': 0},
            {'x': 1, 'y': 0}
        ], 2263)
        self.assertFalse(straight_line.is_concave())
        self.assertFalse(right_angle_line.is_concave())
        self.assertTrue(concave_line.is_concave())

    def test_endpoints_theta(self):

        line_0 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 0},
        ], 2263)

        line_45 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
        ], 2263)

        line_90 = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
        ], 2263)

        line_135 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': 1},
        ], 2263)

        line_n45 = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': -1},
        ], 2263)

        line_n90 = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': -1},
        ], 2263)

        line_n135 = Line([
            {'x': 0, 'y': 0},
            {'x': -1, 'y': -1},
        ], 2263)

        self.assertEqual(line_0.endpoints_theta, 0)
        self.assertEqual(line_45.endpoints_theta, 45)
        self.assertEqual(line_90.endpoints_theta, 90)
        self.assertEqual(line_135.endpoints_theta, 135)
        self.assertEqual(line_n45.endpoints_theta, -45)
        self.assertEqual(line_n90.endpoints_theta, -90)
        self.assertEqual(line_n135.endpoints_theta, -135)

    def test_endpoints_angle(self):
        # The NY State Plane coordinate system seems to be oriented off-north by -2.3020971383770115 degrees,
        # so a straight line drawn at an angle along it's axis will have a bearing of roughly -2.3 degrees off of
        # what you'd expect.

        # create a new line w/ 5 points running at along the y-axis
        # bearing is -2.3 degrees (0 degrees - 2.3)
        # bearing_off_north = -2.3
        bearing_off_north = 0

        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 0, 'y': 2},
            {'x': 0, 'y': 3},
            {'x': 0, 'y': 4}
        ], 2263)
        self.assertAlmostEqual(test_line.endpoints_angle, 0 + bearing_off_north, 1)

        # create a new line w/ 5 points running at 45 degrees
        # bearing is 42.7 degrees (45 degrees - 2.3)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        self.assertAlmostEqual(test_line.endpoints_angle, 45 + bearing_off_north, 1)

        # create a new line w/ 5 points running at 90 degrees
        # bearing is 87.7 degrees (90 degrees - 2.3)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 3, 'y': 0},
            {'x': 4, 'y': 0}
        ], 2263)
        self.assertAlmostEqual(test_line.endpoints_angle, 90 + bearing_off_north, 1)

    def test_union(self):
        # create two lines to union together
        first_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1}
        ], 2263)
        second_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        union_line = first_line.union(second_line)
        self.assertEqual(round(union_line.first_point.x), 0)
        self.assertEqual(round(union_line.first_point.y), 0)
        self.assertEqual(round(union_line.last_point.x), 2)
        self.assertEqual(round(union_line.last_point.y), 2)

    def test_touches(self):
        # create four lines, one that touches, one that crosses, and one that does not touch the test line
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        touching_line = Line([
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3}
        ], 2263)
        crossing_line = Line([
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        non_touching_line = Line([
            {'x': 1, 'y': 0},
            {'x': 3, 'y': 2}
        ], 2263)
        overlapping_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 3}
        ], 2263)
        zig_zag_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0.5}
        ], 2263)
        contained_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        within_line = Line([
            {'x': -1, 'y': -1},
            {'x': 4, 'y': 4}
        ], 2263)

        self.assertTrue(test_line.touches(touching_line))
        self.assertFalse(test_line.touches(crossing_line))
        self.assertFalse(test_line.touches(non_touching_line))
        self.assertFalse(test_line.touches(overlapping_line))
        self.assertFalse(test_line.touches(zig_zag_line))
        self.assertFalse(test_line.touches(contained_line))
        self.assertFalse(test_line.touches(within_line))

    def test_crosses(self):
        # create four lines, one that touches, one that crosses, and one that does not cross the test line
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        touching_line = Line([
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3}
        ], 2263)
        crossing_line = Line([
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        non_touching_line = Line([
            {'x': 1, 'y': 0},
            {'x': 3, 'y': 2}
        ], 2263)
        overlapping_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 3}
        ], 2263)
        zig_zag_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0.5}
        ], 2263)
        contained_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        within_line = Line([
            {'x': -1, 'y': -1},
            {'x': 4, 'y': 4}
        ], 2263)

        self.assertFalse(test_line.crosses(touching_line))
        self.assertTrue(test_line.crosses(crossing_line))
        self.assertFalse(test_line.crosses(non_touching_line))
        self.assertFalse(test_line.crosses(overlapping_line))
        self.assertTrue(test_line.crosses(zig_zag_line))
        self.assertFalse(test_line.crosses(contained_line))
        self.assertFalse(test_line.crosses(within_line))

    def test_overlaps(self):
        # create four lines, one that touches, one that crosses, and one that does not cross the test line
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        touching_line = Line([
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3}
        ], 2263)
        crossing_line = Line([
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        non_touching_line = Line([
            {'x': 1, 'y': 0},
            {'x': 3, 'y': 2}
        ], 2263)
        overlapping_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 3}
        ], 2263)
        zig_zag_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0.5}
        ], 2263)
        contained_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        within_line = Line([
            {'x': -1, 'y': -1},
            {'x': 4, 'y': 4}
        ], 2263)

        self.assertFalse(test_line.overlaps(touching_line))
        self.assertFalse(test_line.overlaps(crossing_line))
        self.assertFalse(test_line.overlaps(non_touching_line))
        self.assertTrue(test_line.overlaps(overlapping_line))
        self.assertFalse(test_line.overlaps(zig_zag_line))
        self.assertFalse(test_line.overlaps(contained_line))
        self.assertFalse(test_line.overlaps(within_line))

    def test_within(self):
        # create four lines, one that touches, one that crosses, and one that does not cross the test line
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        touching_line = Line([
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3}
        ], 2263)
        crossing_line = Line([
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        non_touching_line = Line([
            {'x': 1, 'y': 0},
            {'x': 3, 'y': 2}
        ], 2263)
        overlapping_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 3}
        ], 2263)
        zig_zag_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0.5}
        ], 2263)
        contained_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        within_line = Line([
            {'x': -1, 'y': -1},
            {'x': 4, 'y': 4}
        ], 2263)

        self.assertFalse(test_line.within(touching_line))
        self.assertFalse(test_line.within(crossing_line))
        self.assertFalse(test_line.within(non_touching_line))
        self.assertFalse(test_line.within(overlapping_line))
        self.assertFalse(test_line.within(zig_zag_line))
        self.assertFalse(test_line.within(contained_line))
        self.assertTrue(test_line.within(within_line))

    def test_contains(self):
        # create four lines, one that touches, one that crosses, and one that does not cross the test line
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        touching_line = Line([
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3}
        ], 2263)
        crossing_line = Line([
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        non_touching_line = Line([
            {'x': 1, 'y': 0},
            {'x': 3, 'y': 2}
        ], 2263)
        overlapping_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 3}
        ], 2263)
        zig_zag_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0.5}
        ], 2263)
        contained_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        within_line = Line([
            {'x': -1, 'y': -1},
            {'x': 4, 'y': 4}
        ], 2263)

        self.assertFalse(test_line.contains(touching_line))
        self.assertFalse(test_line.contains(crossing_line))
        self.assertFalse(test_line.contains(non_touching_line))
        self.assertFalse(test_line.contains(overlapping_line))
        self.assertFalse(test_line.contains(zig_zag_line))
        self.assertTrue(test_line.contains(contained_line))
        self.assertFalse(test_line.contains(within_line))

    def test_share_a_segment(self):
        # create four lines, one that touches, one that crosses, and one that does not cross the test line
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2}
        ], 2263)
        touching_line = Line([
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3}
        ], 2263)
        crossing_line = Line([
            {'x': 2, 'y': 0},
            {'x': 0, 'y': 2}
        ], 2263)
        non_touching_line = Line([
            {'x': 1, 'y': 0},
            {'x': 3, 'y': 2}
        ], 2263)
        overlapping_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 3}
        ], 2263)
        zig_zag_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0},
            {'x': 0, 'y': 0.5}
        ], 2263)
        contained_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)
        within_line = Line([
            {'x': -1, 'y': -1},
            {'x': 4, 'y': 4}
        ], 2263)

        self.assertFalse(test_line.shares_a_segment(touching_line))
        self.assertFalse(test_line.shares_a_segment(crossing_line))
        self.assertFalse(test_line.shares_a_segment(non_touching_line))
        self.assertTrue(test_line.shares_a_segment(overlapping_line))
        self.assertFalse(test_line.shares_a_segment(zig_zag_line))
        self.assertTrue(test_line.shares_a_segment(contained_line))
        self.assertTrue(test_line.shares_a_segment(within_line))

    def test_split_line_at_vertices(self):
        # create a straight line with three vertices
        straight_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2}
        ], 2263)

        line_segments = straight_line.split_line_at_vertices()
        self.assertEqual(len(line_segments), 2)

    def test_angle_between(self):
        # create two lines that are parallel, one that is perpendicular and one that is reversed
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 3},
            {'x': 4, 'y': 4}
        ], 2263)
        parallel_line = Line([
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 3},
            {'x': 3, 'y': 4},
            {'x': 4, 'y': 5}
        ], 2263)
        perpendicular_line = Line([
            {'x': 0, 'y': 4},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 3, 'y': 1},
            {'x': 4, 'y': 0}
        ], 2263)
        reversed_line = Line([
            {'x': 4, 'y': 5},
            {'x': 3, 'y': 4},
            {'x': 2, 'y': 3},
            {'x': 1, 'y': 2},
            {'x': 0, 'y': 1}
        ], 2263)

        self.assertEqual(test_line.angle_between(parallel_line), 0)
        self.assertEqual(test_line.angle_between(perpendicular_line), 90)
        self.assertEqual(test_line.angle_between(reversed_line), 180)

    def test_is_multipart(self):
        # create a single-part polygon and a multi-part and verify their properties
        single_part_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
        ], 2263)

        multi_part_points = [
            [
                {'x': 0, 'y': 0},
                {'x': 0, 'y': 4},
                {'x': 4, 'y': 4},
            ],
            [
                {'x': 5, 'y': 5},
                {'x': 5, 'y': 8},
                {'x': 8, 'y': 8},
            ],
        ]
        multi_part_line = Line(multi_part_points, 2263)
        self.assertTrue(multi_part_line.is_multipart)
        self.assertFalse(single_part_line.is_multipart)

    def test_split_at_point(self):
        # create a straight line and split it in the middle
        point_0 = Point({'x': 0, 'y': 0}, 2263)
        point_15 = Point({'x': 1.5, 'y': 1.5}, 2263)
        point_2 = Point({'x': 2, 'y': 2}, 2263)
        point_4 = Point({'x': 4, 'y': 4}, 2263)

        split_line = Line([point_0, point_4], 2263)
        line_1, line_2 = split_line.split(point_2)
        self.assertIsInstance(line_1, Line)
        self.assertIsInstance(line_2, Line)
        self.assertTrue(line_1.first_point.equals(point_0))
        self.assertTrue(line_1.last_point.equals(point_2))
        self.assertTrue(line_2.first_point.equals(point_2))
        self.assertTrue(line_2.last_point.equals(point_4))

        split_line = Line([point_0, point_2, point_4], 2263)
        line_1, line_2 = split_line.split(point_2)
        self.assertIsInstance(line_1, Line)
        self.assertIsInstance(line_2, Line)
        self.assertTrue(line_1.first_point.equals(point_0))
        self.assertTrue(line_1.last_point.equals(point_2))
        self.assertTrue(line_2.first_point.equals(point_2))
        self.assertTrue(line_2.last_point.equals(point_4))

        split_line = Line([point_0, point_2, point_4], 2263)
        line_1, line_2 = split_line.split(point_15)
        self.assertIsInstance(line_1, Line)
        self.assertIsInstance(line_2, Line)
        self.assertTrue(line_1.first_point.equals(point_0))
        self.assertTrue(line_1.last_point.equals(point_15))
        self.assertTrue(line_2.first_point.equals(point_15))
        self.assertTrue(line_2.points[1].equals(point_2))
        self.assertTrue(line_2.last_point.equals(point_4))

        split_line = Line([point_0, point_2, point_4], 2263)
        line_1, line_2 = split_line.split(point_0)
        self.assertIsInstance(line_1, Line)
        self.assertIsNone(line_2)
        self.assertTrue(line_1.first_point.equals(point_0))
        self.assertTrue(line_1.last_point.equals(point_4))

        split_line = Line([point_0, point_2, point_4], 2263)
        line_1, line_2 = split_line.split(point_4)
        self.assertIsInstance(line_1, Line)
        self.assertIsNone(line_2)
        self.assertTrue(line_1.first_point.equals(point_0))
        self.assertTrue(line_1.last_point.equals(point_4))

    def test_buffer(self):
        # create a small polygon and buffer around it
        test_line = Line([
            {'x': 1, 'y': 1},
            {'x': 2, 'y': 1},
        ], 2263)
        buffer_polygon = test_line.buffer(1)
        self.assertIsInstance(buffer_polygon, Polygon)

    def test_unify_lines(self):
        test_lines = [
            Line([
                {'x': 0, 'y': 0},
                {'x': 1, 'y': 1},
            ], 2263),
            Line([
                {'x': 1, 'y': 1},
                {'x': 2, 'y': 2},
            ], 2263),
            Line([
                {'x': 2, 'y': 2},
                {'x': 3, 'y': 3},
            ], 2263),
        ]

        unified_lines = Line.unify_lines(test_lines)
        self.assertEqual(len(unified_lines), 1)
        unified_line = unified_lines[0]
        self.assertEqual(unified_line.first_point.x, 0)
        self.assertEqual(unified_line.first_point.y, 0)
        self.assertEqual(unified_line.last_point.x, 3)
        self.assertEqual(unified_line.last_point.y, 3)

        test_lines = [
            Line([
                {'x': 0, 'y': 0},
                {'x': 1, 'y': 1},
            ], 2263),
            Line([
                {'x': 1, 'y': 1},
                {'x': 2, 'y': 2},
            ], 2263),
            Line([
                {'x': 2, 'y': 2},
                {'x': 3, 'y': 3},
            ], 2263),
            Line([
                {'x': 4, 'y': 4},
                {'x': 5, 'y': 5},
            ], 2263),
            Line([
                {'x': 5, 'y': 5},
                {'x': 6, 'y': 6},
            ], 2263),
            Line([
                {'x': 6, 'y': 6},
                {'x': 7, 'y': 7},
            ], 2263),

        ]
        unified_lines = Line.unify_lines(test_lines)
        self.assertEqual(len(unified_lines), 2)
        unified_line = unified_lines[0]
        self.assertEqual(unified_line.first_point.x, 0)
        self.assertEqual(unified_line.first_point.y, 0)
        self.assertEqual(unified_line.last_point.x, 3)
        self.assertEqual(unified_line.last_point.y, 3)
        unified_line = unified_lines[1]
        self.assertEqual(unified_line.first_point.x, 4)
        self.assertEqual(unified_line.first_point.y, 4)
        self.assertEqual(unified_line.last_point.x, 7)
        self.assertEqual(unified_line.last_point.y, 7)

        test_lines = [
            Line([
                {'x': 0, 'y': 0},
                {'x': 0, 'y': 1},
            ], 2263),
            Line([
                {'x': 0, 'y': 1},
                {'x': 1, 'y': 1},
            ], 2263),
            Line([
                {'x': 1, 'y': 1},
                {'x': 1, 'y': 0},
            ], 2263),
            Line([
                {'x': 1, 'y': 0},
                {'x': 0, 'y': 0},
            ], 2263),
        ]

        unified_lines = Line.unify_lines(test_lines)
        self.assertEqual(len(unified_lines), 1)
        unified_line = unified_lines[0]
        self.assertEqual(unified_line.first_point.x, 0)
        self.assertEqual(unified_line.first_point.y, 0)
        self.assertEqual(unified_line.last_point.x, 0)
        self.assertEqual(unified_line.last_point.y, 0)

    def test_is_closed(self):
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
            {'x': 0, 'y': 0},
        ], 2263)
        self.assertTrue(test_line.is_closed)
        test_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 1},
        ], 2263)
        self.assertFalse(test_line.is_closed)


    def test_intersection(self):
        # create a test line
        test_line = Line([
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 1},
        ], 2263)

        # create a line that touches at a vertex
        vertex_touch_line = Line([
            {'x': 3, 'y': 1},
            {'x': 5, 'y': 1},
        ], 2263)

        # create a line that crosses the test line
        cross_line = Line([
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
        ], 2263)

        # create a line that shares a line segment with the test lilne
        shares_segment_line = Line([
            {'x': 2, 'y': 1},
            {'x': 4, 'y': 1},
        ], 2263)

        vertex_intersection = test_line.intersection(vertex_touch_line)
        self.assertIsInstance(vertex_intersection, Point)
        self.assertEqual(vertex_intersection.x, 3)
        self.assertEqual(vertex_intersection.y, 1)

        cross_intersection = test_line.intersection(cross_line)
        self.assertIsInstance(cross_intersection, Point)
        self.assertEqual(cross_intersection.x, 2)
        self.assertEqual(cross_intersection.y, 1)

        segment_intersection = test_line.intersection(shares_segment_line)
        self.assertIsInstance(segment_intersection, Line)
        self.assertEqual(segment_intersection.first_point.x, 2)
        self.assertEqual(segment_intersection.first_point.y, 1)
        self.assertEqual(segment_intersection.last_point.x, 3)
        self.assertEqual(segment_intersection.last_point.y, 1)

    def test_add_point(self):
        line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ], 2263)

        new_line = line.add_point(Point({'x': 1, 'y': 3}, 2263))

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]
        self.assertEqual(verify_edges(new_line.split_line_at_vertices(), target_points), 4)

    def test_to_singlepart(self):
        # create a single-part polygon and a multi-part and verify their properties
        single_part_line = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
        ], 2263)

        sub_line_1 = Line([
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 4},
            {'x': 4, 'y': 4},
        ], 2263)

        sub_line_2 = Line([
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 8},
            {'x': 8, 'y': 8},
        ], 2263)

        multi_part_points = [
            [
                {'x': 0, 'y': 0},
                {'x': 0, 'y': 4},
                {'x': 4, 'y': 4},
            ],
            [
                {'x': 5, 'y': 5},
                {'x': 5, 'y': 8},
                {'x': 8, 'y': 8},
            ],
        ]
        multi_part_line = Line(multi_part_points, 2263)

        # test single part polygon
        single_parts = single_part_line.to_singlepart()
        self.assertEqual(len(single_parts), 1)
        self.assertTrue(single_parts[0].equals(single_part_line))

        # test multi part polygon
        single_parts = multi_part_line.to_singlepart()
        self.assertEqual(len(single_parts), 2)
        self.assertTrue(single_parts[0].equals(sub_line_1))
        self.assertTrue(single_parts[1].equals(sub_line_2))

    def test_polgon_contains_line(self):
        test_polygon = Polygon('MULTIPOLYGON (((987667.5584415999 214777.6128173, 987619.8912140999 214691.1297226, 987641.7596087001 214679.0142612, 987594.0910689 214592.5305103, 987462.8761082001 214665.2134358, 987510.5446481 214751.6968586, 987556.3572205 214726.3179724, 987576.1472070999 214715.3570363, 987598.0185545 214703.2425592, 987645.6867662 214789.7259821, 987667.5584415999 214777.6128173)))', 2263)
        test_line = Line('MULTILINESTRING ((987528.48358855 214628.87197305, 987554.2807953705 214727.468253956))', 2263)
        self.assertTrue(test_polygon.contains(test_line))

        test_polygon = Polygon('MULTIPOLYGON (((988558.3854001 204391.4869361, 988576.5500620001 204381.3927961, 988575.1852353 204378.8829587, 988608.0007865001 204360.6707247, 988554.6534522 204264.4816126, 988473.7211994 204309.4175464, 988528.4185965999 204408.1102624, 988558.3854001 204391.4869361)))', 2263)
        test_line = Line('MULTILINESTRING ((988514.1873258001 204286.9495795, 988591.5930109001 204369.7768417))', 2263)
        self.assertTrue(test_polygon.contains(test_line))

        test_polygon = Polygon('MULTIPOLYGON (((987604.0247760999 214812.8000829, 987556.3572205 214726.3179724, 987510.5446481 214751.6968586, 987462.8761082001 214665.2134358, 987441.0024643 214677.3210231, 987536.3392159001 214850.2868846, 987604.0247760999 214812.8000829)))', 2263)
        test_line = Line('MULTILINESTRING ((987570.181996 214831.54348375, 987533.4509343 214739.0074155))', 2263)
        self.assertTrue(test_polygon.contains(test_line))

    def test_create_ray(self):
        start_point = Point({'x': 0, 'y': 0}, 2263)
        test_ray = Line.create_ray(start_point, 90, 2)
        self.assertEqual(test_ray.length, 2)
        self.assertEqual(test_ray.endpoints_angle, 90)

        test_ray = Line.create_ray(start_point, 180, 2)
        self.assertEqual(test_ray.length, 2)
        self.assertEqual(test_ray.endpoints_angle, 180)

        test_ray = Line.create_ray(start_point, 270, 2)
        self.assertEqual(test_ray.length, 2)
        self.assertEqual(test_ray.endpoints_angle, 270)

    def test_replace_point(self):
        line = Line([
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ], 2263)

        new_line = line.replace_point(Point({'x': 2, 'y': 0}, 2263), Point({'x': 3, 'y': 0}, 2263))

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 3, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]
        self.assertTrue(new_line.is_valid)
        self.assertEqual(verify_edges(new_line.split_line_at_vertices(), target_points), 3)

        new_line = line.replace_point(Point({'x': 2, 'y': 0}, 2263), Point({'x': 2, 'y': 2}, 2263))

        # verify each edge is correct
        target_points = [
            {'x': 0, 'y': 0},
            {'x': 2, 'y': 2},
            {'x': 0, 'y': 2}
        ]
        self.assertTrue(new_line.is_valid)
        self.assertEqual(verify_edges(new_line.split_line_at_vertices(), target_points), 2)

    def test_project(self):
        line = Line('MultiLineString ((-73.95464287601815556 40.74966966239151134, -73.95455218961726018 40.74981121223466829), (-73.95479703870847743 40.75005658688614574, -73.95373675256685431 40.74983929945528871))', 4326)
        new_line = line.project(2263)
        self.assertIsInstance(new_line, Line)
        self.assertTrue(new_line.is_multipart)
        self.assertEqual(new_line.wkt, 'MULTILINESTRING ((996774.5030155828 212545.73457977013, 997068.3210598892 212466.72315637575), (996817.2902652338 212404.78762293016, 996842.3903712946 212456.37180539063))')

        line = Line('MultiLineString ((-73.95479703870847743 40.75005658688614574, -73.95373675256685431 40.74983929945528871))', 4326)
        new_line = line.project(2263)
        self.assertIsInstance(new_line, Line)
        self.assertFalse(new_line.is_multipart)
        self.assertEqual(new_line.wkt, 'MULTILINESTRING ((996774.5030155828 212545.73457977013, 997068.3210598892 212466.72315637575))')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LineClassUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
