# coding=utf-8
""" Base class for all geometry objects. Contains properties and methods common to all geometry types.

"""
import matplotlib.pyplot as plt
from abc import ABC as abstract_base
from geoalchemy2.shape import from_shape, WKBElement
from shapely.geometry import Point as ShapelyPoint, MultiLineString
from shapely.ops import snap
from shapely.validation import explain_validity
from pyproj import CRS, Transformer

import oogeo
from src.oogeo.functions.conversions import string_to_units


class GeometryBase(abstract_base):
    """ Common base class for all geometry objects

    """

    def __init__(self, geometry, spatial_reference=None, allow_invalid=False):
        """ Initializes the geometry object.

        :param geometry: The geometry object representing the underlying geometry.
        :param spatial_reference: The spatial reference for the geometry.
        :param allow_invalid: If true, errors for invalid geometries will be ignored. Set this
            flag to true when loading datasets where you expect to encounter invalid geometries.
        """
        # set the base geometry object
        self.geometry = geometry
        self._spatial_reference = spatial_reference
        self.allow_invalid = allow_invalid
        self.ax = None
        if not allow_invalid and not self.is_valid:
            msg = 'Invalid geometry detected: {}\n\n{}\n'.format(
                explain_validity(self.geometry), self.ewkt)
            raise ValueError(msg)

    @property
    def wkt(self):
        """ The well-known text string for the geometry.

        :return: A string representing the well-known text for the geometry.
        """
        return self.geometry.wkt

    @property
    def ewkt(self):
        """ The well-known text string for the geometry.

        :return: A string representing the well-known text for the geometry.
        """
        return 'SRID={};{}'.format(self.spatial_reference, self.wkt)

    @property
    def wkb(self):
        """ The well-known binary for the geometry.

        :return: Binary data representing the geometry.
        """
        return self.geometry.wkb

    @property
    def spatial_reference(self):
        """ The spatial reference for the geometry.

        :return: The spatial reference for the geometry.
        """
        return self._spatial_reference

    @property
    def is_empty(self):
        """ Indicates if the geometry is empty (i.e. 'MULTIPOLYGON EMPTY').

        :return: True if the geometry is empty, otherwise False.
        """
        return self.geometry.is_empty

    @property
    def is_multipart(self):
        """ Indicates if a geometry is multi-part. For our purposes, shapes that
        are of a multi-geometry object type but only contain a single geometry will be considered
        single-part geometries.

        :return: True if the geometry is multi-part, otherwise False.
        """

        if len(self.geometry.geoms) > 1:
            return True
        return False

    def distance_to(self, other):
        """ Retrieves the straight-line distance between this geometry and the provided geometry.

        :param other: The other geometry to be measured to.
        :return: A float value representing the distance between the two geometries.
        """
        return self.geometry.distance(other.geometry)

    def equals(self, other, decimals=None):
        """ Returns True if the other geometry equals this geometry, otherwise False.

        :param other: The geometry object to be compared to this object.
        :param decimals: If provided, geometries will be considered equal if their vertices are equal when
            rounded to the number of decimal places provided.
        :return: True if the other geometry equals this geometry, otherwise False.
        """
        if decimals:
            return self.geometry.almost_equals(other.geometry, decimals)
        return self.geometry.wkt == other.geometry.wkt

    def disjoint(self, other):
        """ Returns True if this geometry does not touch or intersect the provided geometry in any way, otherwise False.

        :param other: The geometry to be compared to this geometry.
        :return: True if this geometry does not touch or intersect the provided geometry in any way, otherwise False.
        """
        return self.geometry.disjoint(other.geometry)

    def touches(self, other):
        """ Determines if this line object touches the other geometry object.

        :param other: The other geometry object to be evaluated.
        :return: True if the geometries touch, otherwise False.
        """
        return self.geometry.touches(other.geometry)

    def intersects(self, other):
        """ Determines if this object intersects the other geometry in any way.

        :param other: The other geometry object to be evaluated
        :return: True if the geometries intersect, otherwise False.
        """
        if self.geometry.intersects(other.geometry):
            return True
        if not hasattr(self, 'merge_vertices'):
            return False
        merged_self, merged_other = self.merge_vertices(self, other)
        return merged_self.geometry.intersects(merged_other.geometry)

    def within(self, other, exact=False):
        """ Determines if this geometry is within the provided geometry.

        :param other: The other geometry object to be evaluated.
        :return: True if this geometry is within the other geometry, otherwise False.
        """
        if isinstance(self.geometry, ShapelyPoint):
            return self.geometry.within(other.geometry)
        if self.geometry.within(other.geometry):
            return True
        if not exact:
            merged_self, merged_other = self.merge_vertices(self, other)
        else:
            merged_self = self.clone()
            merged_other = other.clone()
        return merged_self.geometry.within(merged_other.geometry)

    def _snap_(self, target_geometry, tolerance):
        """ Snaps the vertices in this geometry to the vertices in the other geometry.

        :param target_geometry: The geometry to use as a snap target.
        :return: A Shapely geometry object. The subclasses that call this
            method are responsible for wrapping the Shapely object in the
            appropriate Envelope geometry object.
        """
        # parse tolerance if necessary
        if isinstance(tolerance, str):
            tolerance = string_to_units(tolerance, 'FEET')

        # perform the snap using shapely and return the raw geometry object
        # (this will be reprocessed into the proper output type by overriding callers)
        return snap(self.geometry, target_geometry.geometry, tolerance)

    def to_geoalchemy(self):
        """ Returns a GeoAlchemy geometry object that can be stored in a PostGIS geodatabase.

        :return: A GeoAlchemy object that can be stored in the geodatabase.
        """

        return from_shape(self.geometry, srid=self.spatial_reference)

    def to_postgis(self):
        """ Converts the well-known binary representation of the geometry into a binary format that
        can be consumed by PostGIS.

        :return: The well-known binary representation of the geometry into a binary format that
        can be consumed by PostGIS.
        """
        return WKBElement(self.wkb, self.spatial_reference)

    def plot(self, ax=None, xlim=None, ylim=None, **kwargs):
        """ Plots the geometry to a `matplotlib` figure for display within Jupyter Notebooks.

        :param ax: An existing axes object to draw the geometry into. If no axes is provided
            the geometry will be rendered into a new axes.
        :param kwargs: Arguments to be passed to the `matplotlib` renderer to specify rendering styles.
        """
        # set up the plot
        if not ax:
            fig, ax = plt.subplots()

        if isinstance(self.geometry, ShapelyPoint):
            x, y = self.x, self.y
            ax.scatter([x], [y], **kwargs)
        elif isinstance(self.geometry, MultiLineString):
            for geom in self.geometry.geoms:
                xs, ys = geom.xy
                ax.plot(xs, ys, **kwargs)
        else:
            for geom in self.geometry.geoms:
                xs, ys = geom.exterior.xy
                ax.fill(xs, ys, **kwargs)
                ring_kwargs = kwargs.copy()
                ring_kwargs['color'] = 'white'
                if ring_kwargs.get('zorder'):
                    ring_kwargs['zorder'] += 1
                else:
                    ring_kwargs['zorder'] = 1
                for interior in geom.interiors:
                    xs, ys = interior.xy
                    ax.fill(xs, ys, **ring_kwargs)
        self.ax = ax

        if xlim:
            plt.xlim(xlim)
        if ylim:
            plt.ylim(ylim)
        return ax

    def label(self, label_text, **kwargs):
        """ Labels geometry drawn in a `matplotlib` drawing with the provided text. If the geometry
        has not been plotted yet an error will be raised.

        :param label_text: The text to label the geometry with.
        :param kwargs: Arguments to be passed to `matplotlib` to format the drawing, such as color, etc.
        :return: None.
        """
        assert self.ax, 'Geometry must be plotted before it can be labeled'
        assert label_text, 'Label text is required'

        kw_keys = kwargs.keys()
        set_alignment = 'ha' not in kw_keys and 'horizontalalignment' not in kw_keys \
                    and 'va' not in kw_keys and 'verticalalignment' not in kw_keys
        set_xy = 'xy' not in kw_keys

        if set_xy:
            if isinstance(self.geometry, ShapelyPoint):
                label_point = self
                if set_alignment:
                    kwargs['ha'] = 'left'
                    kwargs['va'] = 'bottom'
            elif isinstance(self.geometry, MultiLineString):
                label_point = self.midpoint
                if set_alignment:
                    kwargs['ha'] = 'center'
                    kwargs['va'] = 'center'
            else:
                label_point = self.representative_point
                if set_alignment:
                    kwargs['ha'] = 'center'
            kwargs['xy'] = (label_point.x, label_point.y)
        elif isinstance(kwargs['xy'], GeometryBase):
            label_point = kwargs['xy']
            kwargs['xy'] = (label_point.x, label_point.y)
        self.ax.annotate(text=label_text, **kwargs)

    @property
    def is_valid(self):
        """ Returns True if the geometry is valid, otherwise False.

        :return: True if the geometry is valid, otherwise False.
        """
        return self.geometry.is_valid

    @property
    def geometry_type(self):
        """ Returns the type of geometry as a string.

        :return: 'Point', 'Polyline', or 'Polygon' based on the type of geometry.
        """

        if isinstance(self.geometry, ShapelyPoint):
            return 'Point'
        if isinstance(self.geometry, MultiLineString):
            return 'Polyline'
        return 'Polygon'

    def project(self, spatial_reference):
        """

        """

        input_crs = CRS.from_epsg(self.spatial_reference)
        output_crs = CRS.from_epsg(spatial_reference)
        projector = Transformer.from_crs(input_crs, output_crs, always_xy=True)

        if isinstance(self.geometry, ShapelyPoint):
            new_x, new_y = projector.transform(self.x, self.y)
            return oogeo.objects.point.Point({'x': new_x, 'y': new_y}, spatial_reference)
        elif isinstance(self.geometry, MultiLineString):
            parts = []
            for part in self.geometry.geoms:
                points = []
                for point in part.coords:
                    new_x, new_y = projector.transform(point[0], point[1])
                    points.append({'x': new_x, 'y': new_y})
                parts.append(points)
            return oogeo.objects.line.Line(parts, spatial_reference=spatial_reference)
        else:
            parts = []
            for part in self.geometry.geoms:
                exterior_points = []
                for point in part.exterior.coords:
                    new_x, new_y = projector.transform(point[0], point[1])
                    exterior_points.append({'x': new_x, 'y': new_y})

                for interior in part.interiors:
                    interior_points = []
                    for point in interior.coords:
                        new_x, new_y = projector.transform(point[0], point[1])
                        interior_points.append({'x': new_x, 'y': new_y})
                    if len(interior_points) > 0:
                        exterior_points.append(interior_points)
                parts.append(exterior_points)
            return oogeo.objects.polygon.Polygon(parts, spatial_reference)
