# coding=utf-8
""" Base class for all geometry objects. Contains properties and methods common to all geometry types.

"""

from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon, \
    Point as ShapelyPoint, LineString, MultiLineString, MultiPoint, GeometryCollection
from shapely.ops import nearest_points

from abc import ABC as abstract_base

import src.oogeo
from src.oogeo.objects.geometrybase import GeometryBase
from src.oogeo.functions.constants import BUFFER_END_STYLES, BUFFER_JOIN_STYLES
from src.oogeo.functions.conversions import string_to_units


def get_near_points(target_geometry, near_geometry, tolerance):
    """ Find the vertices in the target geometry that are close to the near geometry
    (within the specified tolerance).

    :param target_geometry: The geometry containing the vertices to be analyzed
    :param near_geometry: The geometry to measure to.
    :param tolerance: The maximum distance a point can be away from the near geometry
        and be considered a "near point"
    :return: A list of `Point()` objects representing the vertices of the target
        geometry that are near the near geometry.
    """

    # loop through the vertices of the target geometry and
    # find the points close to the near geometry
    return_list = []

    if isinstance(near_geometry.geometry, MultiPolygon):
        near_geometries = near_geometry.to_lines()
    elif isinstance(near_geometry.geometry, MultiLineString):
        near_geometries = near_geometry.split_line_at_vertices()
    else:
        near_geometries = [near_geometry]

    target_points = [target_geometry] if isinstance(target_geometry.geometry, ShapelyPoint) else target_geometry.points

    if isinstance(target_geometry.geometry, MultiPolygon):
        target_edges = target_geometry.to_lines()
    elif isinstance(target_geometry.geometry, MultiLineString):
        target_edges = target_geometry.split_line_at_vertices()
    else:
        target_edges = []

    for index, point in enumerate(target_points):
        distance = None
        edge = None
        for near_edge in near_geometries:
            test_distance = point.distance_to(near_edge)
            if test_distance > tolerance:
                continue
            if not distance or distance > test_distance:
                distance = test_distance
                edge = near_edge
        if not edge:
            continue

        # if we found a near edge do an out-front test
        nearest_point = edge.nearest_point(point) if isinstance(edge, src.oogeo.objects.line.Line) else edge
        if not nearest_point.equals(point):
            test_line = src.oogeo.objects.line.Line([point, nearest_point], point.spatial_reference)
            if not test_line.is_perpendicular(edge, tolerance=3):
                continue
            crosses_other_edge = False
            for target_edge in target_edges:
                if target_edge.first_point.equals(point) or target_edge.last_point.equals(point):
                    continue
                if test_line.crosses(target_edge):
                    crosses_other_edge = True
                    break
            if crosses_other_edge:
                continue

        # if we make it here the out-front test passed
        # now check for nearby vertices that are better candidates
        previous_point = target_points[index - 1] if index > 0 else None
        next_point = target_points[index + 1] if index + 1 < len(target_points) else None

        analyze = True
        for test_point in [previous_point, next_point]:
            if not test_point:
                continue

            # if the test point is further away from the edge than this point, don't consider it
            if test_point.distance_to(edge) > distance:
                continue

            # if the test point is closer to the edge than this point, do
            # and out-front test on the test point - if its not out front don't consider it
            test_nearest_point = edge.nearest_point(test_point)
            if not test_point.equals(test_nearest_point):
                test_line = src.oogeo.objects.line.Line([test_point, test_nearest_point], point.spatial_reference)
                if not test_line.is_perpendicular(edge, tolerance=3):
                    continue

            # if the test point is closer and out front, see if the line formed between the
            # two points are perpendicular to the edge - if so we want to ignore this
            # point for analysis
            test_line = src.oogeo.objects.line.Line([test_point, point], point.spatial_reference)
            if test_line.is_perpendicular(edge):
                analyze = False

        # if we decided not to analyze this point, continue
        if not analyze:
            continue

        # if we're here then this is a point we want to consider for transfer
        # so see if we need to snap it to a vertex or derive a point on the edge
        first_point_distance = point.distance_to(edge.first_point)
        last_point_distance = point.distance_to(edge.last_point)
        snap = first_point_distance <= tolerance or last_point_distance <= tolerance
        new_point = edge.first_point if first_point_distance <= tolerance and first_point_distance < last_point_distance else \
            edge.last_point if last_point_distance <= tolerance and last_point_distance < first_point_distance else \
            edge.nearest_point(point)

        if not point.equals(new_point):
            return_list.append({
                'point': point,
                'new_point': new_point,
                'snap': snap}
            )

    # find points in the near geometry that need to be added
    # to the target
    near_points = near_geometry.points if not isinstance(near_geometry.geometry, ShapelyPoint) else [near_geometry]
    target_boundary = target_geometry.boundary if isinstance(target_geometry.geometry, MultiPolygon) else target_geometry
    near_points = list(filter(lambda x: x.distance_to(target_boundary) <= tolerance, near_points))
    for near_point in near_points:
        found = False
        for return_object in return_list:
            if return_object['new_point'].equals(near_point):
                found = True
                break
        if not found:
            return_list.append({
                'point': None,
                'new_point': near_point,
                'snap': False}
            )

    return return_list


def insert_weld_points(geometry, weld_points):
    if isinstance(geometry.geometry, ShapelyPoint):
        return geometry
    for point in weld_points:
        if point['point']:
            geometry = geometry.replace_point(point['point'], point['new_point'])
        else:
            geometry = geometry.add_point(point['new_point'])
    return geometry


class MultipointBase(GeometryBase, abstract_base):
    """ Common base class for all geometry objects

    """

    def __init__(self, geometry, spatial_reference=None, allow_invalid=False):
        """ Initializes the geometry object.

        :param geometry: The geometry object representing the underlying geometry.
        :param spatial_reference: The spatial reference of the geometry.
        :param allow_invalid: If true, errors for invalid geometries will be ignored. Set this
            flag to true when loading datasets where you expect to encounter invalid geometries.
        """
        super(MultipointBase, self).__init__(geometry, spatial_reference, allow_invalid)

    @staticmethod
    def remove_sliver_polygons(multipolygon):
        """

        :param multipolygon:
        :return:
        """
        if not isinstance(multipolygon, MultiPolygon):
            return multipolygon
        valid_polygons = list(filter(lambda x: x.is_valid and x.area > 25, multipolygon.geoms))
        return MultiPolygon(valid_polygons) if len(valid_polygons) > 0 else None

    def intersection(self, other, exact=False, allow_invalid=False):
        """ Determines the intersecting area between this geometry and the other geometry. The method will return
        a `Polygon()` object if the geometries overlap, a `Line()` object if they only share an edge, or a `Point()`
        object if they intersect at a single point.

        :param other: The other geometry object to be evaluated.
        :param exact: If True, the geometries will be compared exactly as they are. If False, the vertices
            of the geometries will be merged prior to comparison to mitigate for tiny gaps and overlaps.
        :return: A `Polygon()` object if the geometries overlap, a `Line()` object if they only share an edge,
            or a `Point()` object if they intersect at a single point.
        """

        if exact:
            merged_self = self
            merged_other = other
        else:
            merged_geometries = MultipointBase.merge_vertices(self, other)
            merged_self = merged_geometries[0]
            merged_other = merged_geometries[1]
        # merged_self, merged_other =  if not exact else self, other
        intersection_geometries = merged_self.geometry.intersection(merged_other.geometry)

        return_geometries = []
        intersection_geometries = [geom for geom in intersection_geometries.geoms] if isinstance(intersection_geometries, GeometryCollection) \
            else [intersection_geometries] if not isinstance(intersection_geometries, list) \
            else intersection_geometries
        for geometry in intersection_geometries:
            if isinstance(geometry, ShapelyPoint):
                return_geometries.append(src.oogeo.objects.point.Point(geometry, self.spatial_reference, allow_invalid=allow_invalid))
            elif (isinstance(geometry, LineString) or isinstance(geometry, MultiLineString)) and not geometry.is_empty:
                return_geometries.append(src.oogeo.objects.line.Line(geometry, self.spatial_reference, allow_invalid=allow_invalid))
            elif isinstance(geometry, ShapelyPolygon) or isinstance(geometry, MultiPolygon):
                if geometry:
                    return_geometries.append(src.oogeo.objects.polygon.Polygon(geometry, self.spatial_reference, allow_invalid=allow_invalid))
            elif isinstance(geometry, MultiPoint):
                for point in geometry.geoms:
                    return_geometries.append(src.oogeo.objects.point.Point(point, self.spatial_reference, allow_invalid=allow_invalid))

        if len(return_geometries) == 0:
            return None
        if len(return_geometries) == 1:
            return return_geometries[0]
        return return_geometries

    def buffer(self, distance, end_style='FLAT', join_style='BEVEL', allow_invalid=False):
        """ Returns a `Polygon()` object representing the specified buffer around the geometry.

        :param distance: The distance that the buffer should expand around the geometry.
        :param end_style: The end style to apply to the buffer. Valid values are:
            'ROUND': Creates rounded ends that extend beyond the endpoints of the geometry at the specified distance.
            'FLAT': Does not extend any buffer beyond the endpoints of the geometry.
            'SQUARE': Creates square ends that extend beyond the endpoints of the geometry at the specified distance.
        :param join_style: The joint style to apply to the buffer. Valid values are:
            'ROUND': Creates rounded intersections along the edge of the buffer.
            'MITRE': Creates mitred intersections along the edge of the buffer.
            'BEVEL': Creates beveled intersections along the edge of the buffer.
        :return: A `Polygon()` object representing the specified buffer around the geometry.
        """
        if isinstance(distance, str):
            distance = string_to_units(distance, 'FEET')

        if distance == 0:
            return src.oogeo.objects.polygon.Polygon(self.geometry.buffer(distance), self.spatial_reference, allow_invalid=allow_invalid)

        buffer_polygon = src.oogeo.objects.polygon.Polygon(
            self.geometry.buffer(distance,
                resolution=100,
                cap_style=BUFFER_END_STYLES[end_style],
                join_style=BUFFER_JOIN_STYLES[join_style]),
            self.spatial_reference, allow_invalid=allow_invalid)

        if distance > 0:
            return buffer_polygon

        # for negative buffers, clip the original geometry with the
        # buffer polygon to get the real
        if buffer_polygon.is_empty:
            return self.clone()
        return self.difference(buffer_polygon, allow_invalid=allow_invalid)

    def crosses(self, other_geometry):
        """ Determines if this line object crosses the other line object.

        :param other_geometry: The other line object to be evaluated.
        :return: True if the lines cross, otherwise False.
        """
        return self.geometry.crosses(other_geometry.geometry)

    def overlaps(self, other_line):
        """ Returns True if this line overlaps the provided line, otherwise False.

        :param other_line: The line to be compared to this line.
        :return: True if this line overlaps the provided line, otherwise False.
        """
        return self.geometry.overlaps(other_line.geometry)

    def nearest_point(self, point):
        """ Returns the point along the polygon edge that is nearest to the specified point.

        :param point: The point to analyze.
        :return: `Point()` object representing a point along the edge of the polygon
            that is nearest to the specified point.
        """
        nearest_point = nearest_points(self.geometry, point.geometry)[0]
        return src.oogeo.objects.point.Point(nearest_point, self.spatial_reference)

    def nearest_vertex(self, point):
        """ Returns the vertex nearest to the specified point.

        :param point: A `Point()` object representing the point to be analyzed.
        :return: A `Point()` object representing the vertex in the line or polygon nearest to the specified point.
        """
        return_point = None
        distance = -1
        for edge_point in self.points:
            test_distance = edge_point.distance_to(point)
            if not return_point or test_distance < distance:
                return_point = edge_point
                distance = test_distance
        return return_point

    def contains(self, other_geometry, exact=False):
        """ Returns True if the polygon contains the other geometry, otherwise False.

        :param other_geometry: The geometry to be tested.
        :return: True if the polygon contains the other geometry, otherwise False.
        """
        if exact or isinstance(other_geometry, src.oogeo.objects.point.Point):
           return self.geometry.contains(other_geometry.geometry)

        if self.geometry.contains(other_geometry.geometry):
            return True

        merged_self, merged_other = self.merge_vertices(self, other_geometry)
        return merged_self.geometry.contains(merged_other.geometry)

    def contains_point(self, point, tolerance=None):
        """ Returns True if the specified point exists along the edge of the line or polygon, otherwise False.

        :param point: A `Point()` object representing the point to be examined.
        :param tolerance: A distance representing how near points can be to be considered the same point.
            If not provided, points must be exactly the same for `True` to be returned.
        :return: True if the line or polygon contains the specified point, otherwise false.
        """

        for test_point in self.points:
            if not tolerance and test_point.equals(point):
                return True
            if tolerance and test_point.distance_to(point) <= tolerance:
                return True
        return False

    @staticmethod
    def merge_vertices(first_geometry, second_geometry, tolerance=0.0000001):

        # clone the geometries so that they are not mutated
        geometry_1 = first_geometry.clone()
        geometry_2 = second_geometry.clone()
        geometry_1 = geometry_1.remove_duplicate_vertices() if isinstance(geometry_1.geometry,
                                                                          MultiPolygon) else geometry_1
        geometry_2 = geometry_2.remove_duplicate_vertices() if isinstance(geometry_2.geometry,
                                                                          MultiPolygon) else geometry_2
        # get list of vertices to evaluate for each geometry
        weld_points_1 = get_near_points(geometry_1, geometry_2, tolerance)
        weld_points_1 = list(filter(lambda x: not x['snap'], weld_points_1))
        geometry_1 = insert_weld_points(geometry_1, weld_points_1)
        weld_points_2 = get_near_points(geometry_2, geometry_1, tolerance)
        geometry_2 = insert_weld_points(geometry_2, weld_points_2)

        return geometry_1, geometry_2

    def scale(self, scale_factor):
        """ Scales the shape by multiplying each of it's vertices by the provided scale factor.

        :param scale_factor: The factor to multiple each x/y value by for each vertex in the shape.
        :return: A new geometry object with the x/y values scaled by the provided scale factor.
        """
        new_geometry = self.clone()
        for point in self.points:
            new_geometry = new_geometry.replace_point(point, src.oogeo.objects.point.Point({'x': point.x * scale_factor, 'y': point.y * scale_factor}, self.spatial_reference), self.allow_invalid)
        return new_geometry

    def transform(self, delta_x, delta_y):
        """ Moves the geometry by the specified delta values by adding the delta values to the x/y
        values of each vertex in the geometry. Providing positive delta values will generally move
        the geometry to the north and east, whereas negative values will generally move the geometry
        to the south and west.

        :param delta_x: The value to add to the x coordinate of each vertex in the geometry.
        :param delta_y: The value to add to the y coordinate of each vertex in the geometry.
        :return: A new geometry that has been transformed based on the provided inputs.
        """
        new_geometry = self.clone()
        for point in self.points:
            new_geometry = new_geometry.replace_point(point, src.oogeo.objects.point.Point({'x': point.x + delta_x, 'y': point.y + delta_y}, self.spatial_reference), allow_invalid=True)
        if self.allow_invalid or new_geometry.is_valid:
            return new_geometry
        raise ValueError('Invalid geometry detected: {}'.format(new_geometry.ewkt))
