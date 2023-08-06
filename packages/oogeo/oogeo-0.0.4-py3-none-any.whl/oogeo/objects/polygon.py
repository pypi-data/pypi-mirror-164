# coding=utf-8
""" Contains objects related to polygons.

"""

# import logging

from itertools import islice, combinations
from more_itertools import pairwise

from shapely import speedups
from shapely.coords import CoordinateSequence
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon, Point as ShapelyPoint, LineString, MultiLineString
from shapely.ops import linemerge, unary_union, polygonize
from shapely.wkt import loads as wkt_to_geom
from osgeo.ogr import CreateGeometryFromWkt as wkt_to_ogr

from src.oogeo.objects.multipointbase import MultipointBase
import src.oogeo.objects.line
import src.oogeo.objects.point

def parse_multipolygon(point_list):
    """

    """
    assert isinstance(point_list, list), 'Points must be a list'

    if not isinstance(point_list[0], list):
        return MultiPolygon([parse_polygon(point_list)])
    else:
        return MultiPolygon([parse_polygon(poly_points) for poly_points in point_list])

def parse_polygon(point_list):
    """

    """
    assert isinstance(point_list, list), 'Points must be a list'

    exterior = []
    rings = []
    for point in point_list:
        if isinstance(point, tuple):
            exterior.append((point[0], point[1]))
        elif isinstance(point, dict):
            exterior.append((point['x'], point['y']))
        elif isinstance(point, src.oogeo.objects.point.Point):
            exterior.append((point.x, point.y))
        elif isinstance(point, list):
            ring = []
            for ring_point in point:
                if isinstance(ring_point, tuple):
                    ring.append((ring_point[0], ring_point[1]))
                elif isinstance(ring_point, dict):
                    ring.append((ring_point['x'], ring_point['y']))
                elif isinstance(point, src.oogeo.objects.point.Point):
                    ring.append((ring_point.x, ring_point.y))
            rings.append(ring)

    return ShapelyPolygon(exterior, rings)


def remove_invalid_vertices(shapely_polygon, spatial_reference=2263):
    """

    :param shapely_polygon:
    :param spatial_reference:
    :return:
    """

    # remove duplicate vertices
    env_polygon = Polygon(shapely_polygon, spatial_reference, allow_invalid=True)
    clean_env_polygon = env_polygon.remove_duplicate_vertices(allow_invalid=True)
    shapely_polygon = clean_env_polygon.geometry

    # if shapely_polygon.is_valid:
    #     return shapely_polygon, False

    # break the polygon down to edges
    duplicate_points = []
    polygons = []

    for polygon_index, polygon in enumerate(shapely_polygon):
        polygon_edges = []
        for ring_index, ring in enumerate([polygon.exterior] + [interior for interior in polygon.interiors]):
            ring_edges = []
            for point_1, point_2 in pairwise(list(ring.coords)):
                point_1 = src.oogeo.objects.point.Point(point_1, spatial_reference)
                point_2 = src.oogeo.objects.point.Point(point_2, spatial_reference)
                if point_1.equals(point_2):
                    duplicate_points.append({'polygon_index': polygon_index, 'ring_index': ring_index, 'point': point_2})
                    continue
                ring_edges.append(src.oogeo.objects.line.Line([point_1, point_2], spatial_reference))
            if len(ring_edges) > 0:
                polygon_edges.append(ring_edges)
        if len(polygon_edges) > 0:
            polygons.append(polygon_edges)

    # if we didn't find any valid polygons in the multipolygon, return none
    if len(polygons) == 0:
        return None, False

    # compare edges and find removal points
    removal_points = []
    for polygon_index, polygon_edges in enumerate(polygons):
        for ring_index, ring_edges in enumerate(polygon_edges):
            for edge_1, edge_2 in pairwise(ring_edges):
                angle_1 = edge_1.endpoints_angle + 360 if edge_1.endpoints_angle < 0 else edge_1.endpoints_angle
                angle_2 = edge_2.endpoints_angle + 360 if edge_2.endpoints_angle < 0 else edge_2.endpoints_angle
                angle_diff = abs(angle_1 - angle_2) - 180
                if -0.5 < angle_diff < 0.5:
                    removal_points.append({'polygon_index': polygon_index, 'ring_index': ring_index, 'point': edge_2.first_point})
            # finally, check the last edge against the first edge
            edge_1 = ring_edges[-1]
            edge_2 = ring_edges[0]
            angle_1 = edge_1.endpoints_angle + 360 if edge_1.endpoints_angle < 0 else edge_1.endpoints_angle
            angle_2 = edge_2.endpoints_angle + 360 if edge_2.endpoints_angle < 0 else edge_2.endpoints_angle
            angle_diff = abs(angle_1 - angle_2) - 180
            if -0.1 < angle_diff < 0.1:
                removal_points.append({'polygon_index': polygon_index, 'ring_index': ring_index, 'point': edge_2.first_point})

    # look for panhandles
    for polygon_index, polygon_edges in enumerate(polygons):
        for ring_index, ring_edges in enumerate(polygon_edges):
            if len(ring_edges) <= 4:
                continue
            # grab the angle of the last edge for initial comparison
            first_angle = ring_edges[-1].endpoints_angle + 360 if ring_edges[-1].endpoints_angle < 0 else ring_edges[-1].endpoints_angle
            idx = 0
            for middle_edge, last_edge in pairwise(ring_edges):
                middle_angle = middle_edge.endpoints_angle + 360 if middle_edge.endpoints_angle < 0 else middle_edge.endpoints_angle
                last_angle = last_edge.endpoints_angle + 360 if last_edge.endpoints_angle < 0 else last_edge.endpoints_angle
                angle_diff = abs(first_angle - last_angle) - 180
                if -5 < angle_diff < 5 and middle_edge.length < 0.1:
                    removal_points.append({'polygon_index': polygon_index, 'ring_index': ring_index, 'point': middle_edge.first_point})
                    removal_points.append({'polygon_index': polygon_index, 'ring_index': ring_index, 'point': middle_edge.last_point})
                first_angle = middle_angle
                idx += 1

    # reconstruct polygon and remove offensive points
    new_polygons = []
    adjusted = False
    for polygon_index, polygon in enumerate(shapely_polygon):
        new_rings = []
        for ring_index, ring in enumerate([polygon.exterior] + [interior for interior in polygon.interiors]):
            ring_points = []
            for point in ring.coords:
                point = src.oogeo.objects.point.Point(point, spatial_reference)
                remove = False
                for removal_point in removal_points:
                    if polygon_index == removal_point['polygon_index'] and ring_index == removal_point['ring_index'] and point.equals(removal_point['point']):
                        remove = True
                        break
                if not remove:
                    for duplicate_point in duplicate_points:
                        if polygon_index == duplicate_point['polygon_index'] and ring_index == duplicate_point['ring_index'] and point.equals(duplicate_point['point']):
                            duplicate_points.remove(duplicate_point)
                            remove = True
                            break
                if not remove:
                    ring_points.append(point.geometry)
                else:
                    adjusted = True
            if len(ring_points) >= 3:
                new_rings.append(LineString(ring_points))
        if len(new_rings) == 0:
            continue
        exterior_ring = new_rings[0]
        interior_rings = new_rings[1:]

        new_polygons.append(ShapelyPolygon(exterior_ring, interior_rings))

    if len(new_polygons) == 0:
        return None, adjusted
    return MultiPolygon(new_polygons), adjusted


def correct_invalid_polygon(shapely_polygon, spatial_reference=2263):
    """

    :param shapely_polygon:
    :return:
    """

    env_polygon = Polygon(shapely_polygon, spatial_reference, allow_invalid=True)
    env_polygon = env_polygon.remove_shards(allow_invalid=True)
    return env_polygon.geometry

    # if shapely_polygon.is_valid:
    #     return shapely_polygon
    # if not shapely_polygon.is_valid:
    #     zero_buffer_polygon = shapely_polygon.buffer(0)
    #     if isinstance(zero_buffer_polygon, ShapelyPolygon):
    #         zero_buffer_polygon = MultiPolygon([zero_buffer_polygon])
    #     shapely_polygon = zero_buffer_polygon if zero_buffer_polygon.is_valid and not zero_buffer_polygon.is_empty and abs(shapely_polygon.area - zero_buffer_polygon.area) < 2 else shapely_polygon
    #
    # for i in range(1, 5):
    #     shapely_polygon, adjusted = remove_invalid_vertices(shapely_polygon, spatial_reference)
    #     if shapely_polygon is None or not adjusted:
    #         if shapely_polygon is None:
    #             logging.info('  Invalid polygon could not be corrected - returning null')
    #         elif shapely_polygon.is_valid and adjusted:
    #             logging.info('  Invalid polygon was corrected - returning corrected polygon')
    #         elif not shapely_polygon.is_valid and not adjusted:
    #             # logging.info('  Invalid polygon could not be adjusted - wkt: {}'.format(shapely_polygon.wkt))
    #             logging.info('  Invalid polygon could not be adjusted')
    #         return shapely_polygon
    #
    # # logging.info('  Invalid polygon could not be adjusted after max number of attempts - wkt: {}'.format(shapely_polygon.wkt))
    # logging.info(
    #     '  Invalid polygon could not be adjusted after max number of attempts')
    # return shapely_polygon


class Polygon(MultipointBase):
    """ Provides support for analyzing polygons features in GIS layers.

    """

    def __init__(self, geometry, spatial_reference, allow_invalid=False):
        """ Initializes the polygon object.

        :param geometry: Geometry object representing a polygon. May be a list of coordinates (as tuples
            or dicts), ogr Polygon or MultiPolygon, well-known text representation, or Shapely Polygon
            or MultiPolygon.
        :param spatial_reference: The spatial reference for the geometry
        """

        if isinstance(geometry, str):
            geometry = wkt_to_geom(geometry)
        elif isinstance(geometry, CoordinateSequence):
            geometry = ShapelyPolygon(geometry)
        elif isinstance(geometry, list):
            geometry = parse_multipolygon(geometry)
        elif isinstance(geometry, ShapelyPolygon) or isinstance(geometry, MultiPolygon):
            geometry = wkt_to_geom(geometry.wkt)

        assert isinstance(geometry, ShapelyPolygon) or isinstance(geometry, MultiPolygon), 'Geometry must be a polygon'

        # elevate the geometry to a multigeometry if necessary
        if isinstance(geometry, ShapelyPolygon):
            geometry = MultiPolygon([geometry])

        super(Polygon, self).__init__(geometry, spatial_reference, allow_invalid)
        self._cached_points = None
        self.speedups_disabled = False

    @property
    def boundary(self):
        """ Returns the boundary of the polygon as a `Line()` object. If the polygon has an interior ring,
        it will be removed and only the exterior edge of the polygon will be returned.

        :return: A `Line()` object representing the boundary of the polygon.
        """
        return src.oogeo.objects.line.Line(self.geometry.boundary, self.spatial_reference, allow_invalid=self.allow_invalid)

    @property
    def area(self):
        """ Returns the area of the polygon.

        :return: A float value indicating the area of the polygon.
        """
        return self.geometry.area

    @property
    def mbr(self):
        """ Returns a `Polygon()` object representing the minimum bounding rectangle surrounding the polygon.
        The mbr rectangle is not oriented to the spatial axis and does not represent the *extent* of the geometry
        in XY coordinates.

        :return: A `Polygon()` object representing the minimum bounding rectangle surrounding the polygon.
        """
        mbr = wkt_to_geom(self.geometry.minimum_rotated_rectangle.wkt)
        if isinstance(mbr, ShapelyPolygon) or isinstance(mbr, MultiPolygon):
            if not mbr.is_valid:
                return None
            return Polygon(mbr, self.spatial_reference)
        if isinstance(mbr, LineString) or isinstance(mbr, MultiLineString):
            return src.oogeo.objects.line.Line(mbr, self.spatial_reference)
        if isinstance(mbr, ShapelyPoint):
            return src.oogeo.objects.point.Point(mbr, self.spatial_reference)

    @property
    def mbr_short_edges(self):
        """ Returns a `Line()` object representing the shortest edge of the minimum bounding rectangle surrounding
        the polygon. The mbr rectangle is not oriented to the spatial axis and does not represent the *extent* of
        the geometry in XY coordinates.

        :return: A `Line()` object representing the shortest edge of the minimum bounding rectangle
            surrounding the polygon.
        """
        mbr = self.mbr
        if not mbr or not isinstance(mbr, Polygon):
            return None
        edges = mbr.to_lines()
        short_edge = None
        for edge in edges:
            short_edge = edge if not short_edge or edge.length < short_edge.length else short_edge
        short_edges = []
        for edge in edges:
            if abs(short_edge.length - edge.length) < 0.1:
                short_edges.append(edge)

        return short_edges

    @property
    def mbr_long_edges(self):
        """ Returns a `Line()` object representing the longest edge of the minimum bounding rectangle surrounding
        the polygon. The mbr rectangle is not oriented to the spatial axis and does not represent the *extent* of
        the geometry in XY coordinates.

        :return: A `Line()` object representing the longest edge of the minimum bounding rectangle
            surrounding the polygon.
        """
        mbr = self.mbr
        if not mbr or not isinstance(mbr, Polygon):
            return None
        edges = mbr.to_lines()
        long_edge = None
        for edge in edges:
            long_edge = edge if not long_edge or edge.length > long_edge.length else long_edge

        long_edges = []
        for edge in edges:
            if abs(long_edge.length - edge.length) < 0.1:
                long_edges.append(edge)
        return long_edges

    def is_sliver(self, threshold):
        """ Indicates if the polygons is a sliver that is narrower than the provided threshold.

        :param threshold: The width below which a polygon is considered to be a sliver.
        :return: True if the width of the polygon is less than the threshold, otherwise False.
        """
        mbr_short_edges = self.mbr_short_edges
        if mbr_short_edges:
            return mbr_short_edges[0].length <= threshold
        # if no short edges come back this is a tiny tiny polygon, so it's a sliver by definition
        return False

    def is_panhandle(self, threshold):
        """ Indicates if the polygon has a panhandle that is narrower than the specified threshold.

        :param threshold: The width below which an area of the polygon is considered to be a panhandle.
        :return: True of the polygon contains a sliver, otherwise False.
        """
        lines = self.to_lines()
        lines.append(lines[0])
        lines.append(lines[1])
        first_line = lines[-2]
        middle_line = lines[-1]
        for last_line in lines:
            if src.oogeo.objects.line.Line.is_panhandle(first_line, middle_line, last_line, max_panhandle_width=threshold):
                return True
            first_line = middle_line
            middle_line = last_line
        return False

    def panhandle_width(self, threshold):
        """ The width of the panhandle if the polygon has a panhandle, or -1 if it does not.

        :param threshold: The width below which an area of the polygon is considered to be a panhandle.
        :return: The width of the panhandle, or -1 if the polygon does not have a panhandle.
        """
        lines = self.to_lines()
        lines.append(lines[0])
        lines.append(lines[1])
        first_line = lines[-2]
        middle_line = lines[-1]
        for last_line in lines:
            if src.oogeo.objects.line.Line.is_panhandle(first_line, middle_line, last_line, max_panhandle_width=threshold):
                distance_1 = first_line.midpoint.distance_to(last_line)
                distance_2 = last_line.midpoint.distance_to(first_line)
                return distance_1 if distance_1 < distance_2 else distance_2
            first_line = middle_line
            middle_line = last_line
        return -1

    def rings_as_polygons(self):
        """ Returns the interior rings of the polygon as polygons.

        :return: A list of `Polygon()` objects representing the interior rings of the polygon.
        """
        ring_polygons = []
        for polygon in self.geometry.geoms:
            for ring in polygon.interiors:
                ring_points = []
                for point in ring.coords:
                    ring_points.append(src.oogeo.objects.point.Point(point, self.spatial_reference))
                ring_polygons.append(Polygon(ring_points, self.spatial_reference))
        return ring_polygons

    @property
    def convex_hull(self):
        """ Returns a `Polygon()` object representing the convex hull surrounding the polygon.

        :return: A `Polygon()` object representing the convex hull surrounding the polygon.
        """
        return Polygon(self.geometry.convex_hull, self.spatial_reference)

    @property
    def centroid(self):
        """ Returns the centroid of the polygon as a `Point()` object for use in locating distances.

        :return: A `Point()` object representing the centroid of the polygon.
        """

        return src.oogeo.objects.point.Point(self.geometry.centroid, self.spatial_reference)

    @property
    def representative_point(self):
        """ Returns a point that is guaranteed to be within the boundaries of the polygon. This is
        usually the centroid of the geometry except in cases where the centroid falls outside of
        the bounds of the polygon, such as "L" and "C"-shaped polygons.

        :return: A `Point()` object representing the point within the polygon.
        """
        if self.contains(self.centroid, exact=True):
            return self.centroid
        return src.oogeo.objects.point.Point(self.geometry.representative_point(), self.spatial_reference)

    def _get_cached_points(self):
        """ Caches the vertices of the geometry as points and insures that the points are only collected once.

        :return: A list of `Point()` objects representing the vertices of the geometry.
        """
        if self._cached_points is not None:
            return self._cached_points

        self._cached_points = []
        for polygon in self.geometry.geoms:
            for ring in [polygon.exterior] + [interior for interior in polygon.interiors]:
                for point in ring.coords:
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
    def length(self):
        """ Returns the length of the boundary of the polygon.

        """
        return self.boundary.length

    @property
    def points(self):
        """ Returns a list of coordinates representing the vertices of the line.

        :return: A list of `Point()` objects representing the points in the line.
        """
        return self._get_cached_points()

    def has_duplicate_vertices(self, decimals=None, tolerance=None):
        """ Indicates if the polygon has duplicate vertices.

        :return: True if the polygon has duplicate vertices, otherwise False.
        """
        for polygon in self.geometry.geoms:
            for ring in [polygon.exterior] + [interior for interior in polygon.interiors]:
                previous_point = None
                for test_point in ring.coords:
                    shapely_point = ShapelyPoint(test_point)
                    if previous_point:
                        if decimals:
                            if previous_point.almost_equals(shapely_point, decimals):
                                return True
                        elif tolerance:
                            if previous_point.distance(shapely_point) < tolerance:
                                return True
                        elif previous_point.wkt == shapely_point.wkt:
                            return True
                    previous_point = shapely_point
        return False

    def remove_duplicate_vertices(self, decimals=None, allow_invalid=False, tolerance=None):
        """ Creates a polygon based on the current polygon but with duplicate vertices removed.

        :return: A `Polygon()` object representing the current polygon with duplicate vertices removed.
        """

        # create the new geometry
        shapely_polygons = []
        for polygon_index, polygon in enumerate(self.geometry.geoms):
            shapely_lines = []
            for ring_index, ring in enumerate([polygon.exterior] + [interior for interior in polygon.interiors]):
                ring_points = []
                previous_point = None
                for point_index, test_point in enumerate(ring.coords):
                    shapely_point = ShapelyPoint(test_point)
                    if not previous_point:
                        ring_points.append(shapely_point)
                        previous_point = shapely_point
                        continue
                    if decimals:
                        if not previous_point.almost_equals(shapely_point, decimals):
                            ring_points.append(shapely_point)
                            previous_point = shapely_point
                    elif tolerance:
                        if not previous_point.distance(shapely_point) < tolerance:
                            ring_points.append(shapely_point)
                            previous_point = shapely_point
                    elif previous_point.wkt != shapely_point.wkt:
                        ring_points.append(shapely_point)
                        previous_point = shapely_point
                # if the first and last vertex do not match, that means the first index needs to go
                if ring_points[0].wkt != ring_points[-1].wkt:
                    ring_points[-1] = ring_points[0]
                if len(ring_points) > 2:
                    shapely_lines.append(LineString(ring_points))
            shapely_polygons.append(ShapelyPolygon(shapely_lines[0], shapely_lines[1:]))
        return Polygon(MultiPolygon(shapely_polygons), self.spatial_reference, allow_invalid=allow_invalid)

    def remove_shards(self, allow_invalid=False):
        """ Creates a polygon based on the current polygon but with duplicate vertices removed.

        :return: A `Polygon()` object representing the current polygon with duplicate vertices removed.
        """

        # first remove dupes
        working_geometry = self.remove_duplicate_vertices(allow_invalid=allow_invalid)

        # now find edges
        working_edges = working_geometry.to_lines()
        working_edges.append(working_edges[0])

        # if there are not enough edges, do not attempt
        if len(working_edges) < 4:
            return self.clone()

        # loop through the lines pairwise and find panhandles
        remove_points = []
        for edge_1, edge_2 in pairwise(working_edges):
            edge_angle_1 = edge_1.endpoints_angle + 360 if edge_1.endpoints_angle < 0 else edge_1.endpoints_angle
            edge_angle_2 = edge_2.endpoints_angle + 360 if edge_2.endpoints_angle < 0 else edge_2.endpoints_angle
            angle_diff = abs(edge_angle_1 - edge_angle_2) - 180
            if -0.5 < angle_diff < 0.5:
                remove_points.append(edge_1.last_point)

        for remove_point in remove_points:
            # logging.info('    Shard polygon found: %s', working_geometry.wkt)
            # logging.info('    Removing shard point: %s', remove_point.wkt)
            working_geometry = working_geometry.remove_point(remove_point)
            # logging.info('    Corrected polygon found: %s', working_geometry.wkt)
        return working_geometry

    def get_exterior_polygon(self):
        """ Returns the exterior (outer ring) of the polygon.

        :return: A `Polygon()` object representing the outer ring of the polygon.
        """
        return Polygon(self.geometry.exterior, self.spatial_reference)

    def to_lines(self):
        """ Converts the polygon to a set of `Line()` objects based on the polygon's vertices.

        :return: A list of `Line()` objects representing the edges of the polygon as lines.
        """
        lines = []
        for polygon in self.geometry.geoms:
            vertices = polygon.exterior.coords
            for v_a, v_b in zip(vertices[:-1], vertices[1:]):
                if not v_a == v_b:
                    lines.append(src.oogeo.objects.line.Line([v_a, v_b], self.spatial_reference))
            for interior in polygon.interiors:
                vertices = interior.coords
                for v_a, v_b in zip(vertices[:-1], vertices[1:]):
                    if not v_a == v_b:
                        lines.append(src.oogeo.objects.line.Line([v_a, v_b], self.spatial_reference))

        return lines

    def generalize(self, max_offset=1):
        """ Reduces the number of vertices in the polygon.

        Generalizing a line alters its path and will cause it to deviate from the original line depending on
        how many vertices are removed. The `max_offset` parameter specifies a maximum distance (in map units)
        that the line will be permitted to deviate from the original path. As the `max_offset` value grows larger,
        there will be fewer vertices in the resulting line, and the resulting line will deviate more from the
        original. Under the hood, this uses Shapely's `simplify` method.

        :param max_offset: The maximum distance that the line will be permitted to deviate
            from the original path.
        :return: A `Polygon` object representing the simplified polygon.
        """
        return Polygon(self.geometry.simplify(max_offset), self.spatial_reference)

    def union(self, other_polygon, allow_invalid=False):
        """ Merges two polygon objects together to form a single polygon.

        :param other_polygon: The other polygon object to be merged into this one.
        :return: A Polygon object representing the union of the two polygons.
        """
        return Polygon(unary_union([self.geometry, other_polygon.geometry]), self.spatial_reference, allow_invalid=allow_invalid)

    def cut(self, cutting_line):
        """ Cuts the polygon into two polygons along the provided cutting line.

        :param cutting_line: A `Line()` object representing the cutting edge.
        :return: A list with two `Polygon()` objects representing the two sides of the cut polygon.
        """
        cloned_geometry = self.clone()
        for cut_point in cutting_line.points:
            found_vertex = False
            for vertex in cloned_geometry.points:
                if cut_point.distance_to(vertex) <= 0.000001:
                    found_vertex = True
                    break
            if not found_vertex:
                cloned_geometry = cloned_geometry.add_point(cut_point)

        shapely_multi_geometry = cloned_geometry.geometry
        cut_geometry = cutting_line.geometry

        merged_edges = linemerge([shapely_multi_geometry.geoms[0].boundary, cut_geometry.geoms[0]])
        polygon_borders = unary_union(merged_edges)
        polygons = polygonize(polygon_borders)
        return_polygons = [Polygon(polygon, self.spatial_reference) for polygon in polygons]

        return return_polygons

    def remove_point(self, point, allow_invalid=False):
        """ Removes the specified vertex from the polygon.

        :param point: A `Point()` object representing the vertex to be removed.
        :return: A copy of this geometry without the specified vertex.
        """
        if not self.speedups_disabled:
            speedups.disable()
            self.speedups_disabled = True

        # create the new geometry
        shapely_polygons = []
        for polygon_index, polygon in enumerate(self.geometry.geoms):
            shapely_lines = []
            for ring_index, ring in enumerate([polygon.exterior] + [interior for interior in polygon.interiors]):
                ring_points = []
                first_point_removed = False
                last_point_removed = False
                for point_index, test_point in enumerate(ring.coords):
                    shapely_point = ShapelyPoint(test_point)
                    if shapely_point.wkt == point.geometry.wkt:
                        if point_index == 0:
                            first_point_removed = True
                        elif point_index == len(ring.coords) - 1:
                            last_point_removed = True
                        continue
                    ring_points.append(shapely_point)
                if first_point_removed and last_point_removed:
                    ring_points.append(ShapelyPoint(ring_points[0]))
                shapely_lines.append(LineString(ring_points))
            shapely_polygons.append(ShapelyPolygon(shapely_lines[0], shapely_lines[1:]))
        if not allow_invalid:
            for test_polygon in shapely_polygons:
                if not test_polygon.is_valid:
                    return self.clone()
        return Polygon(MultiPolygon(shapely_polygons), self.spatial_reference, allow_invalid=allow_invalid)

    def add_point(self, point, allow_invalid=False):
        """ Adds the specified point to the geometry.

        :param point: The point to be added.
        :return: A new geometry object with the new point inserted into the points list.
        """
        # if we already contain this point, return a clone of this geometry
        if self.contains_point(point):
            return self.clone()

        # find the nearest points to the specified point
        nearest_index = None
        for polygon_index, polygon in enumerate(self.geometry.geoms):
            for ring_index, ring in enumerate([polygon.exterior] + [interior for interior in polygon.interiors]):
                for point_index in range(len(ring.coords)):
                    # if this is the last vertex, associate it with the first one to make an edge
                    if point_index == len(ring.coords) - 1:
                        vertex_pair = [src.oogeo.objects.point.Point(ring.coords[point_index], self.spatial_reference),
                                       src.oogeo.objects.point.Point(ring.coords[0], self.spatial_reference)]
                    else:
                        vertex_pair = [src.oogeo.objects.point.Point(coords, self.spatial_reference) for coords in
                                       islice(ring.coords, point_index, point_index + 2)]
                    if vertex_pair[0].equals(vertex_pair[1]):
                        continue

                    # if this point equals the test point, do not add the point
                    # simply return a copy of the main geometry
                    if vertex_pair[0].equals(point):
                        return self.clone()
                    # if vertex_pair[0].distance_to(point) < 0.000001:
                    #     return Polygon(MultiPolygon(self.geometry), self.spatial_reference)

                    test_line = src.oogeo.objects.line.Line(vertex_pair, self.spatial_reference)
                    test_index = {
                        'polygon_index': polygon_index,
                        'ring_index': ring_index,
                        'point_index': point_index,
                        'distance': point.distance_to(test_line)
                    }
                    if not nearest_index or test_index['distance'] < nearest_index['distance']:
                        nearest_index = test_index

        # create the new geometry
        shapely_polygons = []
        for polygon_index, polygon in enumerate(self.geometry.geoms):
            shapely_lines = []
            for ring_index, ring in enumerate([polygon.exterior] + [interior for interior in polygon.interiors]):
                new_ring_points = []
                for point_index, test_point in enumerate(ring.coords):
                    new_ring_points.append(ShapelyPoint(test_point))
                    if nearest_index['polygon_index'] == polygon_index \
                        and nearest_index['ring_index'] == ring_index \
                        and nearest_index['point_index'] == point_index:
                        new_ring_points.append(ShapelyPoint(point.x, point.y))
                shapely_lines.append(LineString(new_ring_points))
            shapely_polygons.append(ShapelyPolygon(shapely_lines[0], shapely_lines[1:]))
        if not allow_invalid:
            for test_polygon in shapely_polygons:
                if not test_polygon.is_valid:
                    return self.clone()
        return Polygon(MultiPolygon(shapely_polygons), self.spatial_reference, allow_invalid=allow_invalid)

    def densify(self, distance):
        """ Add vertices to the polygon using the specified method.

        :param distance: The maximum distance between vertices. The actual distance between vertices will usually
            be less than the maximum distance as new vertices will be evenly distributed along the original segment.
        :return: A new `Polygon` object representing the densified polygon.
        """
        ogr_geometry = wkt_to_ogr(self.wkt)
        ogr_geometry.Segmentize(distance)
        return Polygon(wkt_to_geom(ogr_geometry.ExportToWkt()), self.spatial_reference)

    def snap_point(self, point):
        """ Returns the point along the edge of the polygon that is nearest to the indicated point.

        :param point: The point to be snapped.
        :return: `Point()` object representing a point along the line that is nearest to the specified point.
        """
        exterior_line = src.oogeo.objects.line.Line(self.geometry.geoms[0].exterior.coords, self.spatial_reference)
        distance_along_line = exterior_line.geometry.project(point.geometry)
        return exterior_line.point_at_distance(distance_along_line)

    def snap_to_vertex(self, other_geometry, tolerance, allow_invalid=False):
        """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
        that fall within the specified tolerance will be snapped.

        :param other_geometry: The geometry to use as a snapping target.
        :param tolerance: The tolerance to use for snapping.
        :return: A copy of the original geometry with snapped vertices.
        """
        snap_points = other_geometry.points if isinstance(other_geometry, Polygon) or \
                      isinstance(other_geometry, src.oogeo.objects.line.Line) else [other_geometry]

        return_geometry = self.clone()

        for snap_point in snap_points:
            nearest_point = None
            distance = None
            for point in return_geometry.points:
                if not nearest_point:
                    nearest_point = point
                    distance = snap_point.distance_to(point)
                    continue
                test_distance = snap_point.distance_to(point)
                if test_distance < distance:
                    nearest_point = point
                    distance = test_distance

            if nearest_point and distance <= tolerance:
                return_geometry = return_geometry.replace_point(nearest_point, snap_point, allow_invalid=allow_invalid)
        return return_geometry

    def to_singlepart(self):
        """ Separates multi-part geometries into single parts.

        :return: A list of geometries representing the parts of the multi-part geometry.
        """

        if not self.is_multipart:
            return [self]

        return [Polygon(part, self.spatial_reference) for part in self.geometry.geoms]

    def symmetric_difference(self, other):
        """

        :return:
        """

        merged_self, merged_other = MultipointBase.merge_vertices(self, other)
        difference = merged_self.geometry.symmetric_difference(merged_other.geometry)
        if isinstance(difference, ShapelyPolygon) or isinstance(difference, MultiPolygon):
            if not difference.is_valid:
                difference = difference.buffer(0)
            return Polygon(difference, self.spatial_reference)
        return None

    def difference(self, other, exact=False, allow_invalid=False):
        """ Returns a `Polygon` object representing the difference between this polygon and the provided polygon.

        :param other: The other geometry to be compared.
        :param exact: If True, the geometries will be compared exactly as they are. If False, the vertices
            of the geometries will be merged prior to comparison to mitigate for tiny gaps and overlaps.
        :return: A `Polygon` object representing the difference between this polygon and the provided polygon.
        """
        if not exact:
            merged_self, merged_other = MultipointBase.merge_vertices(self, other)
        else:
            merged_self = self.clone()
            merged_other = other.clone()
        try:
            difference = merged_self.geometry.difference(merged_other.geometry)
            if isinstance(difference, ShapelyPolygon) or isinstance(difference, MultiPolygon):
                return Polygon(difference, self.spatial_reference, allow_invalid=allow_invalid) if difference is not None else None
            return None
        except:
            return None

    def clone(self):
        """ Creates a copy of the geometry.

        :return: A copy of the geometry.
        """
        return Polygon(MultiPolygon(self.geometry), self.spatial_reference, allow_invalid=self.allow_invalid)

    def snap_to_edge(self, other_geometry, tolerance, allow_invalid=False, densify=False):
        """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
        that fall within the specified tolerance will be snapped.

        :param other_geometry: The geometry to use as a snapping target.
        :param tolerance: The tolerance to use for snapping.
        :return: A copy of the original geometry with snapped vertices.
        """
        other_edge = other_geometry.boundary if isinstance(other_geometry, Polygon) else other_geometry
        boundary = self.boundary

        # get the points in this geom that are close enough to the
        # target geom to be snapped
        local_points = list(filter(lambda x: other_edge.distance_to(x) <= tolerance, self.points))

        # also get the points in the target geom that are within range of this geom
        target_points = list(filter(lambda x: boundary.distance_to(x) <= tolerance, other_edge.points))

        # finally, get the edge segments that are near the area
        local_edges = list(filter(lambda x: other_edge.distance_to(x) <= tolerance, self.to_lines()))

        # find points to snap
        snap_points = []
        for local_point in local_points:
            # check local point to see if it is part of a perpendicular edge - if so don't snap it
            intersecting_edges = list(filter(lambda x: local_point.intersects(x), local_edges))
            parallel_edge_found = False
            for intersecting_edge in intersecting_edges:
                if intersecting_edge.is_parallel(other_edge):
                    parallel_edge_found = True
                    break

            snap_point = other_edge.snap_point(local_point)
            if len(target_points) > 0:
                nearest_target_point = list(sorted(target_points, key=lambda x: x.distance_to(local_point)))[0]
                # if the nearest target is close to the snap point, snap these points
                snap_diff = abs(local_point.distance_to(nearest_target_point) - local_point.distance_to(snap_point))
                if snap_diff < 1:
                    point_map = {'original_point': local_point.clone(), 'new_point': nearest_target_point,
                                 'snap_type': 'VERTEX_TO_VERTEX'}
                    snap_points.append(point_map)
                    continue

            # if we didn't find a parallel edge, move to the next point
            if not parallel_edge_found:
                continue

            # if there was not a vertex in the target that was close enough, find the nearest point on the edge
            point_map = {'original_point': local_point.clone(), 'new_point': snap_point,
                         'snap_type': 'VERTEX_TO_EDGE'}
            snap_points.append(point_map)

        # filter duplicate targets
        new_snap_points = []
        delete_points = []
        for snap_point in snap_points:
            found = False
            remove = False
            for new_snap_point in new_snap_points:
                if new_snap_point['new_point'].equals(snap_point['new_point']):
                    found = True
                    if not new_snap_point['original_point'].equals(snap_point['original_point']):
                        remove = True
                    break
            if not found:
                new_snap_points.append(snap_point)
            elif remove:
                delete_points.append(snap_point)

        # loop through and snap points
        snapped_geometry = self.clone()
        for snap_point in new_snap_points:
            snapped_geometry = snapped_geometry.replace_point(snap_point['original_point'], snap_point['new_point'], allow_invalid=allow_invalid)

        # remove unnecessary vertices
        for snap_point in delete_points:
            snapped_geometry = snapped_geometry.remove_point(snap_point['original_point'], allow_invalid=allow_invalid)

        # return here if we do not need to densify the edge
        if not densify:
            return snapped_geometry

        # find target points that need to be transferred
        missing_points = []
        for target_point in target_points:
            found = False
            for new_snap_point in new_snap_points:
                if new_snap_point['new_point'].equals(target_point):
                    found = True
                    break
            if not found:
                missing_points.append(target_point)

        for missing_point in missing_points:
            if snapped_geometry.boundary.distance_to(missing_point) < 0.1:
                snapped_geometry = snapped_geometry.add_point(missing_point, allow_invalid=allow_invalid)

        return snapped_geometry

    def replace_point(self, original_point, new_point, allow_invalid=False):
        """ Will replace the specified vertex with the new vertex. If the new vertex already exists in the
        geometry, the original vertex will be removed and no new vertex will be added.

        :param original_point: The original vertex to be replaced.
        :param new_point: The new vertex.
        :return: A geometry object with updated vertices.
        """

        # create the new geometry
        shapely_polygons = []
        replaced_point = False
        for polygon in self.geometry.geoms:
            shapely_lines = []
            for ring in [polygon.exterior] + [interior for interior in polygon.interiors]:
                new_ring_points = []
                for point in ring.coords:
                    shapely_point = ShapelyPoint(point)
                    if original_point.geometry.wkt == shapely_point.wkt:
                        new_ring_points.append(new_point.geometry)
                        replaced_point = True
                    else:
                        new_ring_points.append(shapely_point)
                shapely_lines.append(LineString(new_ring_points))
            shapely_polygons.append(ShapelyPolygon(shapely_lines[0], shapely_lines[1:]))
        if not replaced_point:
            # logging.warning('Could not replace point.')
            # logging.warning('  Original point wkt: %s', original_point.wkt)
            # logging.warning('  New point wkt: %s', new_point.wkt)
            return self.clone()
        return Polygon(MultiPolygon(shapely_polygons), self.spatial_reference, allow_invalid=allow_invalid)

    def replace_points(self, point_map):
        """ Will replace the specified vertex with the new vertex. If the new vertex already exists in the
        geometry, the original vertex will be removed and no new vertex will be added.

        :param original_point: The original vertex to be replaced.
        :param new_point: The new vertex.
        :return: A geometry object with updated vertices.
        """

        # remove any duplicate new points
        for map_1, map_2 in combinations(point_map, 2):
            if not map_1['new_point'] or not map_2['new_point']:
                continue
            if map_1['new_point'].distance_to(map_2['new_point']) < 0.5:
                if map_2['separation'] >= map_1['separation']:
                    map_2['new_point'] = None
                else:
                    map_1['new_point'] = None

        # check to see if we need to add the new point as a vertex
        for map in point_map:
            if not map['new_point']:
                continue
            for point in self.points:
                if point.equals(map['original_point']):
                    continue
                if not point.distance_to(map['new_point']) < 0.000001:
                    continue
                map['new_point'] = None
                break

        # loop through the geometry's points and add replace the point
        new_vertices = []

        for ring in [self.geometry.geoms[0].exterior] + [interior for interior in self.geometry.geoms[0].interiors]:
            new_ring = []
            for point in ring.coords:
                ring_point = src.oogeo.objects.point.Point(point, self.spatial_reference)
                for map in point_map:
                    if not ring_point.equals(map['original_point']):
                        continue
                    # if we reach here we have a vertex that needs to be replaced
                    ring_point = map['new_point']
                    break
                if ring_point:
                    new_ring.append(ring_point.clone())
            new_vertices.append(new_ring)

        if len(new_vertices[0]) < 3:
            # logging.info('  Could not replace point due to too few vertices. len(new_vertices[0]) = {}'.format(len(new_vertices[0])))
            return self.clone()
        test_polygon = Polygon(new_vertices, self.spatial_reference, allow_invalid=True)
        if test_polygon.is_valid:
            return test_polygon
        return self.clone()
