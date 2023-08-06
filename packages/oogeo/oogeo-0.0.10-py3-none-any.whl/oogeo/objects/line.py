# coding=utf-8
""" Contains objects related to lines.

"""
import itertools
# import logging
import math
import numpy as np

from itertools import islice
from more_itertools import pairwise
from osgeo.ogr import CreateGeometryFromWkt as wkt_to_ogr
from shapely.coords import CoordinateSequence
from shapely.ops import linemerge
from shapely.geometry import Point as ShapelyPoint, LineString, MultiLineString
from shapely.wkt import loads as wkt_to_geom
from src.oogeo.objects.multipointbase import MultipointBase
from src.oogeo.functions.conversions import upgrade_shapely_geometry
import src.oogeo.objects.point
import src.oogeo.objects.polygon


def correct_invalid_line(shapely_line, spatial_reference=2263):
    """

    :param shapely_polygon:
    :return:
    """

    # break the line down to edges
    duplicate_points = []
    lines = []
    for line in shapely_line.geoms:
        line_edges = []
        for point_1, point_2 in pairwise(list(line.coords)):
            point_1 = src.oogeo.objects.point.Point(point_1, spatial_reference)
            point_2 = src.oogeo.objects.point.Point(point_2, spatial_reference)
            if point_1.equals(point_2):
                duplicate_points.append(point_2)
                continue
            line_edges.append(src.oogeo.objects.line.Line([point_1, point_2], spatial_reference))
        lines.append(line_edges)

    # compare edges and find removal points
    removal_points = []
    for line_edges in lines:
        for edge_1, edge_2 in pairwise(line_edges):
            angle_1 = edge_1.endpoints_angle + 360 if edge_1.endpoints_angle < 0 else edge_1.endpoints_angle
            angle_2 = edge_2.endpoints_angle + 360 if edge_2.endpoints_angle < 0 else edge_2.endpoints_angle
            angle_diff = abs(angle_1 - angle_2) - 180
            if -1 < angle_diff < 1:
                removal_points.append(edge_2.first_point)

    # reconstruct line and remove offensive points
    new_lines = []
    for line in shapely_line.geoms:
        line_points = []
        for point in line.coords:
            point = src.oogeo.objects.point.Point(point, spatial_reference)
            remove = False
            for removal_point in removal_points:
                if point.equals(removal_point):
                    remove = True
                    break
            if not remove:
                for duplicate_point in duplicate_points:
                    if point.equals(duplicate_point):
                        duplicate_points.remove(duplicate_point)
                        remove = True
                        break
            if not remove:
                line_points.append(point.geometry)
        new_lines.append(LineString(line_points))

    if len(new_lines) == 0:
        return None
    return MultiLineString(new_lines)


def has_consecutive_near_points(test_line, other_line):
    """ Determines if two or more consecutive vertices of the test line are near the other line.
    This indicates that the two lines share a line segment.

    :param test_line: The line to be evaluated.
    :param other_line: The line for comparison.
    :return: True if two or more consecutive vertices of the test line are near the other line, otherwise False.
    """
    first_near_found = False
    for point in test_line.points:
        # get the distance from this vertex to the other edge -
        # if we're < 0.001 feet away, consider the vertex to be
        # on the edge
        test_distance = point.distance_to(other_line)
        if test_distance < 0.001:
            if not first_near_found:
                # flag that we found a the first near vertex
                first_near_found = True
            else:
                # if we're here it means we found two near vertices
                # in a row, so share a line segment with is true
                return True
        else:
            first_near_found = False
    return False


def unloop(linestring):
    """ Removes either starting or ending segment if the linestring is detected to be a loop.

    :param linestring: Shapely LineString object
    :return: Shapely LineString object
    """
    v = linestring.coords
    if v[0] != v[-1]:
        # Not a loop
        return linestring

    # logging.warning('Warning - loop line detected - correcting.')

    # find the longest line segment
    start_length = (v[1][0] - v[0][0]) ** 2 + (v[1][1] - v[0][1]) ** 2
    end_length = (v[-1][0] - v[-2][0]) ** 2 + (v[-1][1] - v[-2][1]) ** 2

    # remove a segment based on the lengths
    # logging.debug('start_length^2 = %s, end_length^2 = %s', start_length, end_length)
    if start_length > end_length:
        # logging.debug('Removing start segment')
        return LineString(v[1:])
    else:
        # logging.debug('Removing end segment')
        return LineString(v[:-1])


class Line(MultipointBase):
    """ Provides support for analyzing polyline features in shapefiles.

    The Line class abstracts some of the logic in accessing attribute of polyline features from shapefiles,
    while providing support methods for common operations.
    """

    def __init__(self, geometry, spatial_reference, allow_invalid=False):
        """ Initializes the line object.

        :param geometry: The geometry object representing a polyline. May be a list of coordinates (as tuples
            or dicts), ogr LineString, or Shapely LineString.
        :param spatial_reference: The spatial reference of the line.
        :param allow_invalid: If true, errors for invalid geometries will be ignored. Set this
            flag to true when loading datasets where you expect to encounter invalid geometries.
        """

        if isinstance(geometry, str):
            geometry = wkt_to_geom(geometry)
        if isinstance(geometry, CoordinateSequence):
            geometry = LineString(geometry)
        if isinstance(geometry, list):
            if not isinstance(geometry[0], list):
                points = []
                for point in geometry:
                    if isinstance(point, tuple):
                        points.append((point[0], point[1]))
                    elif isinstance(point, dict):
                        points.append((point['x'], point['y']))
                    elif isinstance(point, src.oogeo.objects.point.Point):
                        points.append((point.x, point.y))
                geometry = LineString(points)
            else:
                parts = []
                for part in geometry:
                    points = []
                    for point in part:
                        if isinstance(point, tuple):
                            points.append((point[0], point[1]))
                        elif isinstance(point, dict):
                            points.append((point['x'], point['y']))
                        elif isinstance(point, src.oogeo.objects.point.Point):
                            points.append((point.x, point.y))
                    parts.append(LineString(points))
                geometry = MultiLineString(parts)

        assert isinstance(geometry, LineString) or isinstance(geometry, MultiLineString), 'A line could not be created.'

        # elevate the geometry to a multigeometry if necessary
        if isinstance(geometry, MultiLineString):
            geometry = linemerge(geometry)
        if isinstance(geometry, LineString):
            geometry = MultiLineString([geometry])

        super(Line, self).__init__(geometry, spatial_reference, allow_invalid)

        self._segments = None
        self._cached_chord = None
        self._cached_points = None

    @staticmethod
    def create_ray(start_point, angle, length):
        """ Creates a `Line()` object beginning at the specified point and extending at the specified angle for
        the specified length.

        Note: This formula was found on GitHub here: https://gist.github.com/karolba/71755c3ac66c58ee02c095bd70a82457
        **It does not support Geographic projections**

        :param start_point: The start point to begin the line.
        :param angle: The angle at which to draw the line.
        :param length: The length of the line.
        :return: A `Line()` object beginning at the specified point and extending at the specified angle for
        the specified length.
        """
        x = start_point.x + math.sin(math.radians(angle)) * length
        y = start_point.y + math.cos(math.radians(angle)) * length
        end_point = src.oogeo.objects.point.Point((x, y), start_point.spatial_reference)
        return Line([start_point, end_point], start_point.spatial_reference)

    @staticmethod
    def count_right_angles(lines, tolerance=5):
        """ Counts the number of right angles between the lines in the provided list.

        :param lines: List of `Line` objects to compare.
        :param tolerance: Number of degrees that a right angle can deviate from 90 or -90.
        :return: Number of right angles between the lines.
        """
        if len(lines) < 2:
            return 0

        # iterate through the lines and check the angles of the ones that touch
        angles = (a.angle_between(b)
            for a, b in itertools.combinations(lines, 2) if a.touches(b))

        return sum(abs(angle - 90) <= tolerance for angle in angles)

    @staticmethod
    def is_parallelogram(lines):
        """ Analyzes the provided list of lines and determines if they can form a parallelogram.

        :param lines: The list of `Line` objects to be evaluated.
        :return: True if the lines form a parallogram, otherwise False.
        """
        return len(lines) == 4 and Line.count_parallel_sets(lines) == 2

    @staticmethod
    def count_parallel_sets(lines):
        """ Counts the number of parallel, non-adjacent lines in a list of lines.

        :param lines: The list of `Line` objects to be evaluated.
        :return: The number of parallel lines found in the list of lines.
        """
        parallel_line_count = 0
        for line_1, line_2 in itertools.combinations(lines, 2):
            # if the lines touch do not compare them
            if line_1.touches(line_2):
                continue
            if line_1.is_parallel(line_2, tolerance=10):
                parallel_line_count += 1

        return parallel_line_count

    @staticmethod
    def angle(p1, p2):
        """ Returns the angle between two points. Assumes a planar measurement method.

        Based on previous conventions, this returns the angle of the vector formed from point one
        to point two, measured clockwise from the positive y-axis.

        :param p1: The first point, as a `Point()` object.
        :param p2: The second point, as a `Point()` object.
        :return: Number, ranging 0-360.
        """
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        if dx == 0 and dy == 0:
            # logging.warning('Points are coincident, returning zero for angle.')
            return 0
        angle = 90 - np.rad2deg(np.arctan2(dy, dx))
        return angle if angle >= 0 else 360 + angle

    @staticmethod
    def degrees_off_parallel(degrees):
        """ Returns absolute degrees removed from 0 or 180, whichever is closer.

        :param degrees: Number of degrees.
        :return: Number, ranging 0 to 90.
        """

        if np.isnan(degrees):
            # this happens when we get an invalid geometry.
            # log it and return zero for now (need to think
            # about a better way to handle it).
            # logging.warning('Invalid input - cannot determine degrees of parallel for NaN')
            return 0
        if 0 <= degrees <= 90:
            return degrees
        elif 90 < degrees <= 180:
            return 180 - degrees
        elif 180 < degrees <= 360:
            return Line.degrees_off_parallel(degrees - 180)
        elif degrees > 360:
            return Line.degrees_off_parallel(degrees % 360)
        else:
            return Line.degrees_off_parallel(-degrees)

    @property
    def chord(self):
        """

        :return:
        """
        if self._cached_chord is None:
            self._cached_chord = np.array((self.last_point.x, self.last_point.y)) - np.array(
                (self.first_point.x, self.first_point.y))
        return self._cached_chord

    @property
    def first_point(self):
        """ Returns coordinates for the first vertex of this Line.

        :return: A `Point()` object representing the first point in the line.
        """
        # get the first point from the first geometry
        return self.get_point(0)

    @property
    def last_point(self):
        """ Returns coordinates for the last vertex of this Line.

        :return: A `Point()` object representing the last point in the line.
        """
        return self.get_point(self.point_count - 1)

    @property
    def chord_length(self):
        """ The straight-distance length between first and last points of the Line.

        :return: Number.
        """
        return np.linalg.norm(self.chord)

    @property
    def first_segment(self):
        """ The first segment of a multi-segmented polyline (or the entire line if the line on
        has a single segment).

        :return: A `Line()` object representing the first segment of a multi-segment polyline.
        """
        # get the first segment from the first geometry
        first_point = self.get_point(0)
        second_point = self.get_point(1)
        return Line([first_point, second_point], self.spatial_reference)

    @property
    def last_segment(self):
        """ The last segment of a multi-segmented polyline (or the entire line if the line on
        has a single segment).

        :return: A `Line()` object representing the last segment of a multi-segment polyline.
        """
        # get the last segment from the last geometry
        first_point = self.get_point(self.point_count - 2)
        second_point = self.get_point(self.point_count - 1)
        return Line([first_point, second_point], self.spatial_reference)

    @property
    def length(self):
        """ Returns the length of this Line, i.e. the sum of all segment lengths.

        :return: Number.
        """
        total = 0
        for linestring in self.geometry.geoms:
            total += linestring.length
        return total

    @property
    def is_closed(self):
        """ Indicates if the line is closed (begins and ends at the same vertex).

        :return: True of the line is closed, otherwise False.
        """
        return True if self.first_point.equals(self.last_point) else False

    @property
    def endpoints_angle(self):
        """ Returns the angle in degrees from this line's first vertex to last vertex.

        :return: Number.
        """
        return Line.angle(self.first_point, self.last_point)

    @property
    def endpoints_theta(self):
        """ Returns the theta angle in degrees from this line's first vertex to last vertex.

        :return: Number.
        """
        delta_x = self.last_point.x - self.first_point.x
        delta_y = self.last_point.y - self.first_point.y
        theta_radians = math.atan2(delta_y, delta_x)
        return math.degrees(theta_radians)

    @property
    def first_angle(self):
        """ Returns the angle in degrees from this line's first vertex to second vertex.

        :return: Number.
        """
        return Line.angle(self.first_point, self.get_point(1))

    @property
    def last_angle(self):
        """ Returns the angle in degrees from this line's second-to-last vertex to last vertex.

        :return: Number.
        """
        return Line.angle(self.get_point(self.point_count - 2), self.last_point)

    @property
    def centroid(self):
        """ Returns coordinates for point representing the centroid of the line.

        :return: A `Point()` object representing the centroid of the geometry.
        """
        return src.oogeo.objects.point.Point(self.geometry.centroid, self.spatial_reference)

    @property
    def turn_count(self):
        """ Returns the number of line segments that turn the overall line substantially (>45 degrees).

        :return: Number of turns greater than 45 degrees in the line.
        """
        # get the line segments for the line
        angles = (a.angle_between(b)
            for a, b in self.get_line_segment_pairs())

        return sum(angle > 45 for angle in angles)

    def _get_cached_points(self):
        """ Caches the vertices of the geometry as points and insures that the points are only collected once.

        :return: A list of `Point()` objects representing the vertices of the geometry.
        """
        if self._cached_points is not None:
            return self._cached_points

        self._cached_points = []
        for linestring in self.geometry.geoms:
            for point in linestring.coords:
                self._cached_points.append(src.oogeo.objects.point.Point(point, self.spatial_reference))

        return self._cached_points

    def get_point(self, index):
        """ Returns coordinates for vertex at the provided index of this Line.

        :param index: The integer index of the desired vertex. Negative integers will count backward from the last
            vertex, with -1 returning the last point.
        :return: Tuple (length 2) with x-y coordinates.
        """
        return self.points[index]

    @property
    def point_count(self):
        """ Returns the number of points in the geometry.

        :return: The number of points in the geometry.
        """
        return len(self.points)

    @property
    def points(self):
        """ Returns a list of coordinates representing the vertices of the line.

        :return: A list of `Point()` objects representing the points in the line.
        """
        return self._get_cached_points()

    def split_line_at_turns(self, tolerance=45):
        """ Splits the line into line segments based on where the line turns.

        :param tolerance: The angle which defines a "turn" in degrees. The default is 45 degrees.
        :return: A list of `Line()` objects representing the segments of the split line.
        """

        # initialize the return array
        return_list = []

        # get the line segments for the line
        line_segments = self.split_line_at_vertices()

        if len(line_segments) == 1:
             return line_segments

        segment_a = line_segments.pop(0)
        for segment_b in line_segments:
            if not segment_a.touches(segment_b):
                return_list.append(segment_a)
                segment_a = segment_b
                continue
            turn_angle = segment_a.angle_between(segment_b)
            if tolerance <= turn_angle < (360 - tolerance):
                return_list.append(segment_a)
                segment_a = segment_b
                continue
            segment_a = segment_a.union(segment_b)
        return_list.append(segment_a)

        # at this point, segment a is now the last segment in the list -
        # compare it to the first to make sure we went all the way around the edges
        if len(return_list) > 2:
            first_segment = return_list[0]
            last_segment = return_list[-1]
            if first_segment.touches(last_segment):
                turn_angle = first_segment.angle_between(last_segment)
                if tolerance <= turn_angle < (360 - tolerance):
                    return_list[0] = first_segment.union(last_segment)
                    return_list = return_list[:-1]

        return return_list

    def turn_direction(self, next_line):
        """ Indicates if the "next" line turns to the left or right relative to the current line.

        :param next_line: The line to be compared to the current line.
        :return: -1 if the next line turns to the left relative to the current line or +1 if it turns to the right
            (or 0 if exactly straight, which is very rare).
        """
        # (turn flag is -1 if turning to the left, +1 if turning to the right)

        direction = -1 * np.cross(self.chord, next_line.chord)
        return 1 if direction > 0 else -1 if direction < 0 else 0

    @property
    def is_curve(self):
        """ Indicates if segments in the polyline represent a curve.

        :return: True if the segments in the polyline have a consistent curve, else False.
        """
        # constants that may need tweaking
        min_curve_count = 4
        max_length = 40

        # if there are less than 4 segments then the line cannot curve
        if self.point_count < min_curve_count + 1:
            return False

        # get the line segments for the line
        segment_pairs = self.get_line_segment_pairs()

        turns = ({
            'within_length': segment_a.length < max_length and segment_b.length < max_length,
            'direction': segment_a.turn_direction(segment_b),
            'angle': segment_a.angle_between(segment_b)
        } for segment_a, segment_b in segment_pairs)

        last_turn_direction = 0
        curve_count = 0
        for turn in turns:
            if (turn['within_length']
                and 0.8 <= turn['angle'] <= 10
                and turn['direction'] != 0
                and turn['direction'] + last_turn_direction != 0):
                curve_count += 1
                if curve_count >= min_curve_count:
                    return True
                last_turn_direction = turn['direction']
            else:
                curve_count = 0
                last_turn_direction = 0

        return False

    @property
    def midpoint(self):
        """ Returns the midpoint of the line.

        :return: The midpoint of the line.
        """
        return self.point_at_distance(0.5, True)

    def is_parallel(self, other_line, tolerance=45):
        """ Determine whether line is parallel with another line, within some angle tolerance.

        This method measures the angle between the line segments formed by the respective endpoints of this Line object
        and another provided Line. It then determines if the line segments are parallel within some tolerance, measured
        in degrees.

        :param other_line: A Line object to compare angles with.
        :param tolerance: The tolerance in degrees away from 0 or 180 degree angle formed by the line segments.
        :return: Boolean.
        """
        a = Line.degrees_off_parallel(self.angle_between(other_line))
        return a <= tolerance

    def is_perpendicular(self, other_line, tolerance=45):
        """ Determine whether line is parallel with another line, within some angle tolerance.

        This method measures the angle between the line segments formed by the respective endpoints of this Line object
        and another provided Line. It then determines if the line segments are parallel within some tolerance, measured
        in degrees.

        :param other_line: A Line object to compare angles with.
        :param tolerance: The tolerance in degrees away from 0 or 180 degree angle formed by the line segments.
        :return: Boolean.
        """
        tolerance = 90 - tolerance
        a = Line.degrees_off_parallel(self.angle_between(other_line))
        return a >= tolerance

    def generalize(self, max_offset=1):
        """ Reduces the number of vertices in the line.

        Generalizing a line alters its path and will cause it to deviate from the original line depending on
        how many vertices are removed. The `max_offset` parameter specifies a maximum distance (in map units)
        that the line will be permitted to deviate from the original path. As the `max_offset` value grows larger,
        there will be fewer vertices in the resulting line, and the resulting line will deviate more from the
        original. Under the hood, this uses Shapely's `simplify` method.

        :param max_offset: The maximum distance that the line will be permitted to deviate
            from the original path.
        :return: A `Line` object representing the simplified line.
        """
        self._segments = None
        return Line(self.geometry.simplify(max_offset), self.spatial_reference)

    def densify(self, distance):
        """ Add vertices to the line using the specified method.

        :param distance: The maximum distance between vertices. The actual distance between vertices will usually
            be less than the maximum distance as new vertices will be evenly distributed along the original segment.
            If using a type of DISTANCE or ANGLE, the distance is measured in the units of the geometry's spatial
            reference. If using a type of GEODESIC, the distance is measured in meters.
        :return: A new `Line` object representing the densified line.
        """
        ogr_geometry = wkt_to_ogr(self.wkt)
        ogr_geometry.Segmentize(distance)
        return Line(wkt_to_geom(ogr_geometry.ExportToWkt()), self.spatial_reference)

    def intersect(self, other, return_geometry_type, exact=False):
        """ Returns a geometry representing the intersection of this geometry and the provided geometry. The
        method will return the specified geometry type ('POINT', 'POLYLINE', or 'POLYGON')

        :param other: The geometry to be compared to this geometry.
        :param return_geometry_type: The type of geometry to be returned. Valid values are:
            * 'POINT': A point representing the intersection point of the two geometries will be returned.
            * 'POLYLINE': A polyline will be returned, representing the edges where the two geometries intersect.
            * 'POLYGON': A polygon will be returned, representing the area where the two geometries intersect.
        :param exact: If True, the geometries will be compared exactly as they are. If False, the vertices
            of the geometries will be merged prior to comparison to mitigate for tiny gaps and overlaps.
        :return: A geometry object of the specified type representing the intersection of the two geometries.
        """

        if not exact:
            merged_self, merged_other = MultipointBase.merge_vertices(self, other)
        else:
            merged_self = self
            merged_other = other

        # return None if the geometries do not intersect at all
        if merged_self.disjoint(merged_other):
            return None

        intersection_geometries = merged_self.geometry.intersection(merged_other.geometry)
        return_geometries = []
        if not isinstance(intersection_geometries, list):
            intersection_geometries = [intersection_geometries]
        for geometry in intersection_geometries:
            if isinstance(geometry, ShapelyPoint):
                if not return_geometry_type == 'POINT':
                    continue
                return_geometries.append(src.oogeo.objects.point.Point(geometry, self.spatial_reference))
            elif isinstance(geometry, LineString) or isinstance(geometry, MultiLineString):
                line = Line(geometry, self.spatial_reference)
                if return_geometry_type == 'POLYLINE':
                    return_geometries.append(line)
                else:
                    return_geometries.append(line.first_point)

        if len(return_geometries) == 0:
            return None
        if len(return_geometries) == 1:
            return return_geometries[0]
        return return_geometries

    def snap_point(self, point):
        """ Returns the point along the line that is nearest to the indicated point.

        :param point: The point to be snapped.
        :return: `Point()` object representing a point along the line that is nearest to the specified point.
        """
        distance_along_line = self.geometry.project(point.geometry)
        return self.point_at_distance(distance_along_line)

    def point_at_distance(self, distance, use_percentage=False):
        """ Returns a PointGeometry object representing the point along the line that is the specified distance
        from the beginning of the line. The distance can be expressed in both map units and as a percentage of
        the length of the line if the `use_percentage` flag is set.

        If the `distance` value is less than zero the start point of the line will be returned. If the `distance`
        value is greater than the length of the line the end point of the line will be returned.

        :param distance: The distance to measure from the beginning of the line. The distance can be expressed in
        both map units and as a percentage of the length of the line if the `use_percentage` flag is set. The
        percentage should be expressed as a decimal value ranging from 0 to 1.
        :param use_percentage: If `True` the `distance` parameter will be interpreted as a percentage along the
        line. The percentage should be expressed as a decimal value ranging from 0 to 1.
        :return: A `Point()` object representing the point at the specified distance along the line.
        """
        return src.oogeo.objects.point.Point(self.geometry.interpolate(distance, use_percentage), self.spatial_reference)

    def add_point(self, point, allow_invalid=False):
        """ Adds the specified point to the geometry.

        :param point: The point to be added.
        :return: A new geometry object with the new point inserted into the points list.
        """

        # look through the line to see if we already have this point

        # find the nearest points to the specified point
        nearest_index = None
        for edge_index, edge in enumerate(self.geometry.geoms):
            for point_index in range(len(edge.coords)):
                # if this is the last vertex, associate it with the first one to make an edge
                if point_index == len(edge.coords) - 1:
                    vertex_pair = [src.oogeo.objects.point.Point(edge.coords[point_index], self.spatial_reference),
                                   src.oogeo.objects.point.Point(edge.coords[0], self.spatial_reference)]
                else:
                    vertex_pair = [src.oogeo.objects.point.Point(coords, self.spatial_reference) for coords in
                                   islice(edge.coords, point_index, point_index + 2)]

                # if this point equals the test point, do not add the point
                # simply return a copy of the main geometry
                if vertex_pair[0].equals(point) or vertex_pair[0].distance_to(point) < 0.000001:
                    return Line(MultiLineString(self.geometry), self.spatial_reference)

                if vertex_pair[0].equals(vertex_pair[1]):
                    continue
                test_line = Line(vertex_pair, self.spatial_reference)

                test_index = {
                    'edge_index': edge_index,
                    'point_index': point_index,
                    'distance': point.distance_to(test_line)
                }
                if not nearest_index or test_index['distance'] < nearest_index['distance']:
                    nearest_index = test_index

        # create the new geometry
        shapely_lines = []
        for edge_index, edge in enumerate(self.geometry.geoms):
            new_edge_points = []
            for point_index, test_point in enumerate(edge.coords):
                new_edge_points.append(ShapelyPoint(test_point))
                if nearest_index['edge_index'] == edge_index \
                    and nearest_index['point_index'] == point_index:
                    new_edge_points.append(ShapelyPoint(point.x, point.y))
            shapely_lines.append(LineString(new_edge_points))
        for test_line in shapely_lines:
            if not test_line.is_valid:
                return self.clone()
        return Line(MultiLineString(shapely_lines), self.spatial_reference, allow_invalid=allow_invalid)

    @property
    def normalized_chord(self):
        """ Returns a numpy.array object representing the 2d normalized vector of the line's endpoints.

        :return: numpy.array of numbers.
        """
        if np.count_nonzero(self.chord) == 0:
            return self.chord
        norm = np.linalg.norm(self.chord)
        return np.true_divide(self.chord, norm)

    def angle_between(self, other_line):
        """ Returns angle in degrees formed between two lines.

        This method measures the angle formed by the vectors formed by the respective endpoints of this Line object and
        another provided Line. This angle is measured from between the two vectors when starting from the same point.

        :param other_line: A Line object to compare angles with.
        :return: Number ranging from 0 to 180.
        """
        dot = np.dot(self.normalized_chord, other_line.normalized_chord)

        # check for -1 (to within 7 decimals) to prevent NaN error
        normalized_dot = round(np.float64(dot).item(), 7)
        return 180 if normalized_dot == float(-1.0) else 0 if normalized_dot == float(1.0) else np.degrees(
            np.arccos(dot))

    def get_line_segment_pairs(self):
        """ Returns every pair of touching line segments in the LineString.

        :return: List of 2-item tuples, each a pair of Line objects.
        """
        if self.point_count < 3:
            return []

        segments = self.split_line_at_vertices()

        # If there are two segments, just return them as the only pair.
        # This avoids the edge case where the second segment is just the first segment in reverse,
        # which will trigger the latter algorithm to return the same pair twice.
        if len(segments) == 2:
            return [segments]

        # All consecutive segments are touching, since they always share a vertex. But we also check
        # on the last segment and first segment, since this may be a loop.
        pairs = list(zip(segments[:-1], segments[1:]))
        if segments[-1].touches(segments[0]):
            pairs.append((segments[-1], segments[0]))
        return pairs

    def split_line_at_vertices(self):
        """ Returns a list of `Line()` objects based on the vertices of the current line.

        :return: A list of `Line()` objects.
        """
        if self._segments:
            return self._segments

        self._segments = []
        points = self.points
        for point_1, point_2 in pairwise(points):
            if point_1.equals(point_2):
                continue
            self._segments.append(Line([point_1, point_2], self.spatial_reference))

        return self._segments

    def union(self, other_line):
        """ Joins this line to the other line.

        :param other_line: The other line object to be joined.
        :return: A new Line object representing the unified line.
        """
        # assert not self.disjoint(other_line)
        union = self.geometry.union(other_line.geometry)
        if isinstance(union, LineString):
            return Line(union, self.spatial_reference)
        if isinstance(union, MultiLineString):
            union = linemerge(union)
            return Line(union, self.spatial_reference)
        return src.oogeo.objects.polygon.Polygon(union, self.spatial_reference)

    def split(self, point):
        """ Splits the line at the indicated point.

        :param point: A `Point()` object representing the split location.
        :return: A tuple containing two `Line()` objects representing the split lines.
        """

        # find the nearest points to the specified point
        nearest_index = None
        for edge_index, edge in enumerate(self.geometry.geoms):
            for point_index in range(len(edge.coords)):
                # if this is the last vertex, associate it with the first one to make an edge
                if point_index == len(edge.coords) - 1:
                    vertex_pair = [src.oogeo.objects.point.Point(edge.coords[point_index], self.spatial_reference),
                                   src.oogeo.objects.point.Point(edge.coords[0], self.spatial_reference)]
                else:
                    vertex_pair = [src.oogeo.objects.point.Point(coords, self.spatial_reference) for coords in
                                   islice(edge.coords, point_index, point_index + 2)]
                if vertex_pair[0].equals(vertex_pair[1]):
                    continue
                test_line = Line(vertex_pair, self.spatial_reference)
                test_index = {
                    'edge_index': edge_index,
                    'point_index': point_index,
                    'distance': point.distance_to(test_line)
                }
                if not nearest_index or test_index['distance'] < nearest_index['distance']:
                    nearest_index = test_index

        # create the new geometries
        shapely_lines = []
        return_line_1 = None
        return_line_2 = None
        for edge_index, edge in enumerate(self.geometry.geoms):
            new_edge_points = []
            for point_index, test_point in enumerate(edge.coords):
                if len(new_edge_points) == 0:
                    new_edge_points.append(ShapelyPoint(test_point))
                else:
                    shapely_test_point = ShapelyPoint(test_point)
                    if not new_edge_points[-1].equals(shapely_test_point):
                        new_edge_points.append(shapely_test_point)
                if nearest_index['edge_index'] == edge_index \
                    and nearest_index['point_index'] == point_index:
                    # split the line here
                    if not new_edge_points[-1].equals(point.geometry):
                        new_edge_points.append(point.geometry)
                    if len(new_edge_points) > 1:
                        shapely_lines.append(LineString(new_edge_points))
                        return_line_1 = Line(MultiLineString(shapely_lines), self.spatial_reference)
                        shapely_lines = []
                        new_edge_points = [point.geometry]
            if len(new_edge_points) > 1:
                shapely_lines.append(LineString(new_edge_points))
        if len(shapely_lines) > 0:
            return_line_2 = Line(MultiLineString(shapely_lines), self.spatial_reference)
        if not return_line_1:
            return return_line_2, None
        return return_line_1, return_line_2

    def shares_a_segment(self, other_line):
        """ Determines if two line objects share a line segment.

        :param other_line: The other line object to be analyzed.
        :return: True of the two edges have a line segment in common, otherwise False.
        """

        # test each vertex to see if two consecutive vertices in the source line are
        # very close to the other line - this would indicate a shared edge
        if has_consecutive_near_points(self, other_line) or has_consecutive_near_points(other_line, self):
            return True

        # if the two lines to not touch at all, return False
        if self.disjoint(other_line):
            return False

        # simplest case - lines share a segment if the lines overlap,
        # if one line either contains or is within the other line, or
        # if the lines are equal
        if self.contains(other_line) or self.overlaps(other_line) or self.within(other_line) or self.equals(other_line):
            return True

        # merge the vertices of the lines together and re-attempt. This uses
        # the "weld point" technique that has been fairly successful correcting
        # polygon cuts.
        merged_self, merged_other = MultipointBase.merge_vertices(self, other_line)
        if merged_self.contains(other_line) or merged_self.overlaps(other_line) or \
                merged_self.within(other_line) or merged_self.equals(other_line):
            return True

        # create small buffers around the edges in order to give them a little
        # thickness, and test with those. This technique has been successful
        # when performing similar queries using spatial SQL (see the
        # `Layer.select_layer_by_location()` method to see the related spatial query)
        buffered_self = self.buffer(0.001, end_style='SQUARE', join_style='MITRE')
        buffered_other = other_line.buffer(0.001, end_style='SQUARE', join_style='MITRE')
        if other_line.overlaps(buffered_self) or other_line.within(buffered_self, exact=True) or \
                self.overlaps(buffered_other) or self.within(buffered_other, exact=True):
            return True

        # test using the intersection of the two lines. This is a different
        # approach for determining if lines share a segment. In this case
        # we expect the intersection of lines that share a segment to
        # be a line object, whereas other relationships (crosses, touches, etc.)
        # will return point objects.
        intersection = self.intersection(other_line)
        if isinstance(intersection, Line):
            return True

        return False

    def is_concave(self, tolerance=135):
        """ Determines if the line is concave within a certain tolerance.

        Concavity in this case is defined as the angle between the first vertex and the last vertex
        exceeds the angle formed by the first and second vertices by more than the specified tolerance.

        :return: `True` if the line is concave within the specified tolerance, otherwise `False`.
        """
        concavity = abs(self.first_angle - self.endpoints_angle)
        return tolerance < concavity < 360 - tolerance

    def snap_to_vertex(self, other_geometry, tolerance, allow_invalid=False):
        """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
        that fall within the specified tolerance will be snapped.

        :param other_geometry: The geometry to use as a snapping target.
        :param tolerance: The tolerance to use for snapping.
        :return: A copy of the original geometry with snapped vertices.
        """
        return_geometry = self._snap_(other_geometry, tolerance)
        return_line = Line(return_geometry, self.spatial_reference, allow_invalid=allow_invalid)
        if return_line.is_valid or allow_invalid:
            return return_line
        return self.clone()

    # def snap_to_edge(self, other_geometry, tolerance):
    #     """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
    #     that fall within the specified tolerance will be snapped.
    #
    #     :param other_geometry: The geometry to use as a snapping target.
    #     :param tolerance: The tolerance to use for snapping.
    #     :return: A copy of the original geometry with snapped vertices.
    #     """
    #     return_geometry = self.clone()
    #     for point in self.points:
    #         snap_point = other_geometry.snap_point(point)
    #         return_geometry = return_geometry.snap_to_vertex(snap_point, tolerance=tolerance)
    #
    #     return return_geometry

    def snap_to_edge(self, other_geometry, tolerance, allow_invalid=False, densify=False):
        """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
        that fall within the specified tolerance will be snapped.

        :param other_geometry: The geometry to use as a snapping target.
        :param tolerance: The tolerance to use for snapping.
        :return: A copy of the original geometry with snapped vertices.
        """
        return_geometry = self.clone()
        other_edge = other_geometry.boundary if isinstance(other_geometry, src.oogeo.objects.polygon.Polygon) else other_geometry
        for point in self.points:
            if other_edge.distance_to(point) > tolerance:
                continue
            snap_point = other_geometry.snap_point(point)
            return_geometry = return_geometry.replace_point(point, snap_point, allow_invalid=allow_invalid)

        if densify:
            for other_point in other_edge:
                if other_point.distance_to(return_geometry) > tolerance or return_geometry.contains_point(other_point):
                    continue
                return_geometry = return_geometry.add_point(other_point)

        return return_geometry

    def to_singlepart(self):
        """ Separates multi-part geometries into single parts.

        :return: A list of geometries representing the parts of the multi-part geometry.
        """

        if not self.is_multipart:
            return [self]
        parts = [part for part in self.geometry.geoms]
        merged_parts = linemerge(parts)
        if isinstance(merged_parts, LineString):
            return [Line(merged_parts, self.spatial_reference)]
        return [Line(part, self.spatial_reference) for part in merged_parts.geoms]

    @staticmethod
    def is_panhandle(first_line, middle_line, last_line, max_panhandle_width=15):
        """ Compares 3 lines together to see if they form a panhandle shape.

        :param first_line: The first line to be compared.
        :param middle_line: The second line to be compared.
        :param last_line: The third line to be compared.
        :return: True if the lines form the shape of a panhandle, otherwise False.
        """
        distance_1 = first_line.midpoint.distance_to(last_line)
        distance_2 = last_line.midpoint.distance_to(first_line)
        panhandle_width = distance_1 if distance_1 < distance_2 else distance_2
        return (panhandle_width <= max_panhandle_width
                and first_line.length > 10 and last_line.length > 10
                and 170 <= (first_line.angle_between(middle_line) + middle_line.angle_between(last_line)) <= 190
                and first_line.turn_direction(middle_line) == middle_line.turn_direction(last_line))

    @staticmethod
    def unify_lines(lines):
        """ Loops through a collection of Line objects and unions them if they touch.

        :param lines: A list of lines to be unified.
        :return: A list of unified lines.
        """

        # if only one line is provided just return the input lines
        if len(lines) == 1:
            return lines

        try:
            unmerged_lines = []
            for multiline in lines:
                for line in multiline.geometry.geoms:
                    unmerged_lines.append(line)
            merged_lines = linemerge(unmerged_lines)

            merged_lines = upgrade_shapely_geometry(merged_lines)
            if not merged_lines:
                # logging.warning(' Cannot unify line geometries. merged_lines is None.')
                return None
            # remove zero-length lines and repair remaining ones
            return [Line(linegeom, lines[0].spatial_reference) for linegeom in merged_lines.geoms if linegeom.length > 0]

        except Exception as e:
            # logging.warning('  Cannot unify invalid line geometries. Exception: %s', e)
            return None

    def clone(self):
        """ Creates a copy of the geometry.

        :return: A copy of the geometry.
        """
        return Line(MultiLineString(self.geometry), self.spatial_reference, allow_invalid=self.allow_invalid)

    def replace_point(self, original_point, new_point, allow_invalid=False):
        """ Will replace the specified vertex with the new vertex. If the new vertex already exists in the
        geometry, the original vertex will be removed and no new vertex will be added.

        :param original_point: The original vertex to be replaced.
        :param new_point: The new vertex.
        :return: A geometry object with updated vertices.
        """

        # loop through the geometry's points and add replace the point
        new_vertices = []
        for point in self.points:
            if point.equals(original_point):
                new_vertices.append(new_point)
            else:
                new_vertices.append(point.clone())

        test_line = Line(new_vertices, self.spatial_reference, allow_invalid=True)
        if test_line.is_valid or allow_invalid:
            return test_line
        return self.clone()
