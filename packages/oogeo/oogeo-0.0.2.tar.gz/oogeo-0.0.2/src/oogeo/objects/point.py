# coding=utf-8
""" Contains objects related to points.

"""

from shapely.geometry import Point as ShapelyPoint
from shapely.wkt import loads as wkt_to_geom
from src.oogeo.objects.geometrybase import GeometryBase
import src.oogeo.objects.polygon


class Point(GeometryBase):
    """ Provides support for analyzing point features in GIS layers.

    """

    def __init__(self, geometry, spatial_reference, allow_invalid=False):
        """ Initializes the point object.

        :param geometry: The geometry object representing a point.
        """
        # use shapely to construct a wkt string for creating new ogr geometry objects
        # (required to work around a bug in ogr)
        if isinstance(geometry, str):
            geometry = wkt_to_geom(geometry)
        elif isinstance(geometry, tuple):
            geometry = ShapelyPoint(geometry[:2])
        elif isinstance(geometry, dict):
            geometry = ShapelyPoint((geometry['x'], geometry['y']))

        assert isinstance(geometry, ShapelyPoint), 'A point must be provided'

        super(Point, self).__init__(geometry, spatial_reference, allow_invalid)

    @property
    def x(self):
        """ The 'x' coordinate for the point.

        :return: A float value representing the 'x' portion of the coordinates.
        """
        return self.geometry.x

    @property
    def y(self):
        """ The 'y' coordinate for the point.

        :return: A float value representing the 'y' portion of the coordinates.
        """
        return self.geometry.y

    def buffer(self, distance):
        """ Creates a circular buffer around the point at the specified distance.

        :param distance: The buffer distance.
        :return: A `Polygon()` object representing the buffer around the point
        """
        return src.oogeo.objects.polygon.Polygon(self.geometry.buffer(distance), self.spatial_reference)

    def snap_to_vertex(self, other_geometry, tolerance, allow_invalid=False):
        """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
        that fall within the specified tolerance will be snapped.

        :param other_geometry: The geometry to use as a snapping target.
        :param tolerance: The tolerance to use for snapping.
        :return: A copy of the original geometry with snapped vertices.
        """
        return Point(self._snap_(other_geometry, tolerance), self.spatial_reference, allow_invalid=allow_invalid)

    def snap_to_edge(self, other_geometry, tolerance, allow_invalid=False, densify=False):
        """ Snaps the vertices of this geometry to the vertices of the provided geometry. Only points
        that fall within the specified tolerance will be snapped.

        :param other_geometry: The geometry to use as a snapping target.
        :param tolerance: The tolerance to use for snapping.
        :return: A copy of the original geometry with snapped vertices.
        """

        snap_point = other_geometry.snap_point(self) if not isinstance(other_geometry, Point) else other_geometry
        return_geometry = self.snap_to_vertex(snap_point, tolerance=tolerance, allow_invalid=allow_invalid)

        return return_geometry

    def clone(self):
        """ Creates a copy of the geometry.

        :return: A copy of the geometry.
        """
        return Point(ShapelyPoint(self.geometry), self.spatial_reference, allow_invalid=self.allow_invalid)

    def scale(self, scale_factor):
        """ Scales the shape by multiplying each of it's vertices by the provided scale factor.

        :param scale_factor: The factor to multiple each x/y value by for each vertex in the shape.
        :return: A new geometry object with the x/y values scaled by the provided scale factor.
        """
        return Point({'x': self.x * scale_factor, 'y': self.y * scale_factor}, self.spatial_reference)

    def transform(self, delta_x, delta_y):
        """ Moves the geometry by the specified delta values by adding the delta values to the x/y
        values of each vertex in the geometry. Providing positive delta values will generally move
        the geometry to the north and east, whereas negative values will generally move the geometry
        to the south and west.

        :param delta_x: The value to add to the x coordinate of each vertex in the geometry.
        :param delta_y: The value to add to the y coordinate of each vertex in the geometry.
        :return: A new geometry that has been transformed based on the provided inputs.
        """
        return Point({'x': self.x + delta_x, 'y': self.y + delta_y}, self.spatial_reference)
