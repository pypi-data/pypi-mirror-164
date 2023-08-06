# coding=utf-8
""" Contains objects related to layers.

Classes in the layer file help manage the layers
that are used by the application.
They also help abstract the gis processing library
(arcpy) from the application processing logic.
"""

import copy
import uuid

from itertools import combinations
import matplotlib.pyplot as plt
from pyproj import CRS
import numpy as np

from shapely.geometry import Polygon as ShapelyPolygon, LineString as ShapelyLineString, \
    MultiPolygon as ShapelyMultiPolygon, MultiLineString as ShapelyMultiLineString
from shapely.ops import linemerge, unary_union, polygonize
from shapely.wkb import loads as wkb_to_geom

from src.oogeo.objects.line import Line
from src.oogeo.objects.point import Point
from src.oogeo.objects.polygon import Polygon
from src.oogeo.objects.table import Table
from src.oogeo.objects.table import TableBase
from src.oogeo.objects.selectionset import SelectionSet
from src.oogeo.functions.conversions import string_to_units
from src.oogeo.functions.database import format_query_string, prepare_query

from geoalchemy2 import Geometry, WKBElement
from sqlalchemy import Table as AlchemyTable, Column, MetaData, Integer


def get_uuid():
    """ Creates a uuid for use in naming temporary tables to help avoid table name collisions.

    """
    new_uuid = str(uuid.uuid4())
    return new_uuid.replace('-', '_')


def merge_geodataframes(base_gdf, overlay_gdf, spatial_reference):
    """ Aligns an overlay geodataframe to a base geodataframe and vice versa.

    :param base_gdf: The base geodataframe to be aligned.
    :param overlay_gdf: The overlay geodataframe to be aligned.
    :param spatial_reference: The spatial reference to use.
    :return: A tuple containing the aligned base and overlay geodataframes respectively.
    """

    # get the base geometries in a list, and align the overlay geometries to the base geometries
    # (do this first, because we prefer the vertices in the base geometry over the overlay geometries)
    base_geometries = base_gdf.geometry.tolist()
    overlay_gdf.geometry = overlay_gdf.geometry.apply(align_vertices, merge_geometries=base_geometries, spatial_reference=spatial_reference)

    # now align the base geometries to the overlay geometries
    overlay_geometries = overlay_gdf.geometry.tolist()
    base_gdf.geometry = base_gdf.geometry.apply(align_vertices, merge_geometries=overlay_geometries, spatial_reference=spatial_reference)
    return base_gdf, overlay_gdf


def align_geodataframe(geodataframe, spatial_reference):
    """ Aligns the geometries in a geodataframe to themselves.

    :param geodataframe: The geodataframe to be aligned.
    :param spatial_reference: The spatial reference to use.
    :return: A geodataframe with aligned geometries.
    """

    # get the geometries in the dataframe as a list
    geometries = geodataframe.geometry.tolist()

    # align the vertices of the geometries in the dataframe to themselves
    geodataframe.geometry = geodataframe.geometry.apply(align_vertices, merge_geometries=geometries, spatial_reference=spatial_reference)
    return geodataframe


def align_vertices(geometry, merge_geometries, spatial_reference, tolerance=0.0000001):
    """ Takes the provided shapely geometry object and aligns it to the geometries provided in the
    merge geometries list. Designed to be used with the geopandas `apply()` method.

    :param geometry: The shapely geometry to be aligned.
    :param merge_geometries: A list of shapely geometries used to align the main geometry.
    :param spatial_reference: The spatial reference to use.
    :param tolerance: The maximum distance that a vertex will be moved (in map units).
    :return: A shapely geometry that has been aligned to the provided merge geometries.
    """

    # filter this geometry out of the merge geometries if necessary
    # (this allows us to align a layer to itself).
    merge_geometries = list(filter(lambda x: not x.wkt == geometry.wkt, merge_geometries))

    # get the boundary of the polygon
    geometry = Polygon(geometry, spatial_reference)
    boundary = geometry.boundary

    # loop through the merge geometries and align the main geometry
    for merge_geometry in merge_geometries:
        # get the boundary of the merge geometry
        merge_geometry = Polygon(merge_geometry, spatial_reference)
        merge_boundary = merge_geometry.boundary

        # if the boundary is not near the current geometry, do not align
        if not (boundary.intersects(merge_boundary) or boundary.distance_to(merge_boundary) <= tolerance):
            continue

        # build a list of points in the current geometry to be replaced.
        replace_points = []

        # look for vertices in the main geometry that are near the merge geometry and adjust them
        for point in boundary.points:
            # if this vertex is too far away to adjust, skip it
            if point.distance_to(merge_boundary) > tolerance:
                continue

            # check to see if there are vertices in the merge geometry that are near the current vertex
            # if so, move the current vertex to the merge vertex
            found_merge_point = False
            for merge_point in merge_boundary.points:
                if merge_point.wkt == point.wkt:
                    found_merge_point = True
                    break
                if merge_point.distance_to(point) <= tolerance:
                    replace_points.append({'old_point': point, 'new_point': merge_point})
                    found_merge_point = True
                    break

            # if a nearby vertex was not found in the merge geometry, derive a point along
            # the edge of merge boundary and adjust the current vertex to that point
            if not found_merge_point:
                snap_point = merge_boundary.snap_point(point)
                if point.distance_to(snap_point) <= tolerance:
                    replace_points.append({'old_point': point, 'new_point': snap_point})

        # replace the points in the current geometry with adjusted points
        for replace_point in replace_points:
            geometry = geometry.replace_point(replace_point['old_point'], replace_point['new_point'])

        # re-establish the geometry boundary with freshly adjusted points
        boundary = geometry.boundary

        # create a list of points from the merge geometry to be added to the current geometry
        add_points = []
        for merge_point in merge_boundary.points:
            # if the point in the merge geometry is not near the current geometry, skip it
            if merge_point.distance_to(boundary) > tolerance:
                continue

            # look to see if this point already exists in the current geometry's boundary
            # if not, add it
            found_point = False
            for point in boundary.points:
                if merge_point.wkt == point.wkt:
                    found_point = True
                    break
            # this point does not exists in the current geometry, so add it to our list
            if not found_point:
                add_points.append(merge_point)

        # loop through list of points to add and add them
        for point in add_points:
            geometry = geometry.add_point(point)

    # return shapely geometry
    return geometry.geometry


def get_dissolve_records(source_layer, output_layer, dissolve_fields):
    """ Retrieves a list of the currently selected records in the source layer and prepares them for use
    by the dissolve function.

    :param source_layer: The layer containing the records to dissolve.
    :param output_layer: The output layer where the results will be contained.
    :param dissolve_fields: The fields to dissolve on.
    :return: A list of row objects that can be analysed and inserted into the output layer.
    """
    # logging.debug('Getting dissolve records')

    dissolve_records = []
    dissolve_fields = [] if dissolve_fields is None else dissolve_fields
    search_fields = [source_layer.shape] + dissolve_fields
    with source_layer.get_search_cursor(search_fields) as cursor:
        for index, row in enumerate(cursor, start=1):
            # logging.debug('  Processing record {} of {}'.format(index, len(cursor)))
            record = {}
            for field in search_fields:
                if field == source_layer.shape:
                    record[output_layer.shape] = row[field]
                else:
                    record[field] = row[field]
            dissolve_records.append(record)
    return dissolve_records


def dissolve_records_match(record_1, record_2):
    """ Returns True if the attributes for the two records passed in match, otherwise False.

    :param record_1: The first record to compare.
    :param record_2: The second record to compare.
    :return: True if the attributes for the two records passed in match, otherwise False.
    """
    # get a list of fields to loop through
    fields = list(record_1.keys())

    # loop through the fields and compare attributes
    for field in fields:
        # skip geometry fields
        if isinstance(record_1[field], Line) or isinstance(record_1[field], Polygon) or isinstance(record_1[field],
            Point):
            continue
        # if the attribute fields don't match, return false
        if record_1[field] != record_2[field]:
            return False
    # if we make it through the loop then the records match - return true
    return True


class Layer(TableBase):
    """ Provides support for manipulating layers.

    The layer class manages layer names and the association
    with its underlying shapefile. It also provides access
    to most geoprocessing tools that take layers as inputs.
    """

    def __init__(self, layer, workspace, schema=None):
        """ Initializes the layer object.

        :param layer: The name of the layer in the geodatabase.
        :param workspace: The workspace where the layer is located.
        """

        super(Layer, self).__init__(layer, workspace, schema=schema)

        self.sliver_cbbls = set()
        self.error_cbbls = set()
        self._cached_shape_field = None
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None
        self._cached_geometry_type = None
        self.search_index = 0
        self.ax = None

    @property
    def spatial_reference(self):
        """ The well-known id for the spatial reference of the geometry.

        :return: The well-know id for the geometry.
        """
        # if we've already determined the shape field name, just return it
        if self._cached_shape_field is not None:
            return self._cached_shape_field['srid']

        geometry_columns = self.get_geometry_columns()
        if len(geometry_columns) > 1:
            geometry_columns = list(filter(lambda x: x['name'].upper() in ['GEOM', 'SHAPE'], geometry_columns))

        self._cached_shape_field = geometry_columns.pop()
        return self._cached_shape_field['srid']

    def get_next_search_index(self):
        """ Returns the next search index to be used for querying geometries. This index insures that all spatial
        queries are unique.

        :return: The next index to be used for querying geometries.
        """
        self.search_index += 1
        return self.search_index

    # SELECTION METHODS
    def select_layer_by_location(self, overlap_type, search_object,
        search_distance=0,
        selection_type='NEW_SELECTION',
        invert_spatial_relationship='NOT_INVERT',
        attribute_query=None):
        """ Creates a selection set in the layer based on its spatial relationship with the provided search layer.

        This method selects records based on the spatial relationships between the geometries in the layer and the
        geometries in the provided search layer. Several input options are available to control the search.

        :param overlap_type: The spatial relationship to be evaluated. Options are:
            INTERSECT - Selects features that intersect with the selecting feature. Corresponds with the
                "intersect" predicate in DE-9IM.
            WITHIN_A_DISTANCE - Draws a buffer around the selecting feature, and selects features that
                intersect with that buffer. Specify a distance in the search_distance parameter.
            CONTAINS - Selects features that cover the selecting feature. Despite the name, this corresponds
                with the "covers" predicate in DE-9IM, and is computationally faster than DE-9IM's "contains".
            WITHIN - Selects features that are covered by the selecting feature. Despite the name, this
                corresponds with the "covered by" predicate in DE-9IM, and is computationally faster than
                DE-9IM's "within".
            BOUNDARY_TOUCHES - Selects features if they have a boundary that touches, but doesn't cross, the
                selecting feature.
            SHARE_A_LINE_SEGMENT_WITH - Selects features if they share a line segment with a selecting feature.
                The input and selecting features must be line or polygon (considers its boundary).
            CROSSED_BY_THE_OUTLINE_OF - Selects features if they are crossed by the outline of a selecting
                feature. The input and selecting features must be lines or polygons (considers its boundary).
                Lines that cross at a point will be selected, not lines that share a line segment.
            HAVE_THEIR_CENTER_IN - Selects features if their center falls within a selecting feature. "Center"
                is defined as centroid for polygons and multipoints, and midpoint for lines.
        :param search_object: The geometry object or a layer object representing the selecting features.
        :param search_distance: This parameter is only valid if the overlap_type parameter is set to one of the
            following: WITHIN_A_DISTANCE_GEODESIC, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_3D, INTERSECT, INTERSECT_3D,
            HAVE_THEIR_CENTER_IN, CONTAINS, or WITHIN. If the WITHIN_A_DISTANCE_GEODESIC option is used, a linear unit
            such as Kilometers or Miles should be used.
        :param selection_type: Determines how the selection will be applied to the input and how to combine with an
            existing selection. Options are:
                NEW_SELECTION - The resulting selection replaces any existing selection. This is the default.
                ADD_TO_SELECTION - The resulting selection is added to an existing selection, if one exists. If no
                    selection exists, this is the same as the NEW_SELECTION option.
                REMOVE_FROM_SELECTION - The resulting selection is removed from an existing selection. If no
                    selection exists, the operation will have no effect.
                SUBSET_SELECTION - The resulting selection is combined with the existing selection. Only records that
                    are common to both remain selected.
        :param invert_spatial_relationship: After the spatial relationship is evaluated, this option determines if
            the result should be used as is, or inverted. For example, this option can be used to quickly get a list
            of features that do not intersect or are not within a distance of features in another layer.
        """

        # convert the search distance to a number if it is a string
        if isinstance(search_distance, str):
            search_distance = string_to_units(search_distance, 'FEET')

        # bust the currently cached query string
        self._cached_query_string = None
        self._cached_update_clause = None

        # clear the existing selection if necessary
        if selection_type == 'NEW_SELECTION':
            self.clear_selection()

        # force to 'NEW_SELECTION' if there are currently no other selections on the layer
        if len(self._selections) == 0:
            selection_type = 'NEW_SELECTION'

        search_index = self.get_next_search_index()
        search_edge_buffer_field = 'EDGE_BUFFERS_{}'.format(search_index)
        update_buffer_clause = None
        use_edge_buffers = True if overlap_type == 'SHARE_A_LINE_SEGMENT_WITH' or \
                                   (overlap_type == 'INTERSECT' and isinstance(search_object, Layer) and self.geometry_type == 'Polyline') \
            else False

        if use_edge_buffers and not self.has_search_column:
            self.add_search_column()

        if isinstance(search_object, Layer):
            use_search_edge_buffers = True if overlap_type == 'SHARE_A_LINE_SEGMENT_WITH' or \
                                       (overlap_type == 'INTERSECT' and search_object.geometry_type == 'Polyline') \
                else False

            if use_search_edge_buffers and not search_object.has_search_column:
                search_object.add_search_column()

            search_table_name = "{}_geom_{}".format(search_object.table_name, search_index)
            search_shape_field = '{}_{}'.format(search_object.shape, search_index)

            if use_search_edge_buffers:
                # find edge buffer field name
                edge_buffer_col = list(filter(lambda x: x['name'].lower() == 'edge_buffers',
                                              search_object.get_geometry_columns(include_hidden=True))).pop()
                edge_buffer_field = edge_buffer_col['name']

                search_table_clause = '(SELECT "{}" AS "{}", "{}" AS "{}" FROM "{}"."{}" {}) {}'.format(
                    search_object.shape, search_shape_field, edge_buffer_field, search_edge_buffer_field,
                    search_object.schema, search_object.table_name, search_object.where_clause, search_table_name)
            else:
                search_table_clause = '(SELECT "{}" AS "{}" FROM "{}"."{}" {}) {}'.format(
                    search_object.shape, search_shape_field, search_object.schema, search_object.table_name, search_object.where_clause, search_table_name)

            search_objects = []
            merge_objects = []
            merge_buffers = []
            if not search_object.geometry_type == 'Point':
                with search_object.get_search_cursor([search_object.shape], allow_invalid=True) as cursor:
                    for row in cursor:
                        search_objects.append(row[search_object.shape])
                        merge_objects.append(row[search_object.shape].geometry)
                merged_geometry = unary_union(merge_objects)
                update_clause = "(SELECT ST_GeomFromWKB(DECODE('{}', 'hex'),{}))".format(
                    WKBElement(merged_geometry.wkb, search_object.spatial_reference), search_object.spatial_reference)
                if use_search_edge_buffers:
                    # find edge buffer field name
                    edge_buffer_col = list(filter(lambda x: x['name'].lower() == 'edge_buffers',
                                                    search_object.get_geometry_columns(include_hidden=True))).pop()
                    edge_buffer_field = edge_buffer_col['name']

                    with search_object.get_search_cursor([edge_buffer_field]) as cursor:
                        for row in cursor:
                            merge_buffers.append(row[edge_buffer_field].geometry)
                    merged_buffers = unary_union(merge_buffers)
                    update_buffer_clause = "(SELECT ST_GeomFromWKB(DECODE('{}', 'hex'),{}))".format(
                        WKBElement(merged_buffers.wkb, search_object.spatial_reference), search_object.spatial_reference)
            else:
                with search_object.get_search_cursor([search_object.shape], allow_invalid=True) as cursor:
                    for row in cursor:
                        search_objects.append(row[search_object.shape])
                        merge_objects.append(row[search_object.shape].geometry)
                merged_geometry = unary_union(merge_objects)
                update_clause = "(SELECT ST_GeomFromWKB(DECODE('{}', 'hex'),{}))".format(
                    WKBElement(merged_geometry.wkb, search_object.spatial_reference), search_object.spatial_reference)

        elif isinstance(search_object, Line) or isinstance(search_object, Polygon) or isinstance(search_object, Point):
            if isinstance(search_object, Point) and overlap_type == 'INTERSECT':
                search_object = search_object.buffer(0.000001)
            search_table_name = "manual_geom_{}".format(search_index)
            search_shape_field = 'custom_shape_{}'.format(search_index)
            search_table_clause = "(SELECT ST_GeomFromWKB(DECODE('{}', 'hex'),{}) as \"{}\") as {}".format(
                search_object.to_postgis(), search_object.spatial_reference, search_shape_field, search_table_name)
            update_clause = "(SELECT ST_GeomFromWKB(DECODE('{}', 'hex'),{}))".format(
                search_object.to_postgis(), search_object.spatial_reference)
            search_objects = [search_object]
        else:
            raise ValueError('search_object must be Layer, Line, Polygon, or Point')

        # create a query string that will query the geometries nearest to the geometry of interest
        # (the results will be further filtered in a subsequent step)
        query_string = None
        if overlap_type == 'INTERSECT':
            # handle separately if this is a layer search using line data
            if isinstance(search_object, Layer) and (use_edge_buffers or use_search_edge_buffers):
                # find edge buffer field name
                edge_buffer_col = list(filter(lambda x: x['name'].lower() == 'edge_buffers',
                                              search_object.get_geometry_columns(include_hidden=True))).pop()
                edge_buffer_field = edge_buffer_col['name']

                if self.geometry_type == 'Polyline' and search_object.geometry_type == 'Polyline':
                    query_string = 'ST_Intersects("{}"."{}"."{}", {}."{}")'.format(
                        self.schema, self.table_name, edge_buffer_field, search_table_name, search_edge_buffer_field)
                    update_clause = 'ST_Intersects("{}"."{}"."{}", {})'.format(
                        self.schema, self.table_name, self.shape, update_clause)
                elif self.geometry_type == 'Polyline':
                    query_string = 'ST_Intersects("{}"."{}"."{}", {}."{}")'.format(
                        self.schema, self.table_name, edge_buffer_field, search_table_name, search_shape_field)
                    update_clause = 'ST_Intersects("{}"."{}"."{}", {})'.format(
                        self.schema, self.table_name, self.shape, update_clause)
                elif search_object.geometry_type == 'Polyline':
                    query_string = 'ST_Intersects("{}"."{}"."{}", {}."{}")'.format(
                        self.schema, self.table_name, self.shape, search_table_name, search_edge_buffer_field)
                    update_clause = 'ST_Intersects("{}"."{}"."{}", {})'.format(
                        self.schema, self.table_name, self.shape, update_clause)
            else:
                query_string = 'ST_Intersects("{}"."{}"."{}", {}."{}")'.format(
                    self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
                update_clause = 'ST_Intersects("{}"."{}"."{}", {})'.format(
                    self.schema, self.table_name, self.shape, update_clause)
        elif overlap_type == 'CONTAINS':
            query_string = 'ST_Contains("{}"."{}"."{}", {}."{}")'.format(
                self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
            update_clause = 'ST_Contains("{}"."{}"."{}", {})'.format(
                self.schema, self.table_name, self.shape, update_clause)
        elif overlap_type == 'WITHIN':
            query_string = 'ST_Within("{}"."{}"."{}", {}."{}")'.format(
                self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
            update_clause = 'ST_Within("{}"."{}"."{}", {})'.format(
                self.schema, self.table_name, self.shape, update_clause)
        elif overlap_type == 'DISJOINT':
            query_string = 'ST_Disjoint("{}"."{}"."{}", {}."{}")'.format(
                self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
            update_clause = 'ST_Disjoint("{}"."{}"."{}", {})'.format(
                self.schema, self.table_name, self.shape, update_clause)
        elif overlap_type == 'HAVE_THEIR_CENTER_IN':
            if not self.has_centroid_column:
                query_string = 'ST_Within(ST_Centroid("{}"."{}"."{}"), {}."{}")'.format(
                    self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
                update_clause = 'ST_Within(ST_Centroid("{}"."{}"."{}"), {})'.format(
                    self.schema, self.table_name, self.shape, update_clause)
            else:
                query_string = 'ST_Within("{}"."{}"."centroid", {}."{}")'.format(
                    self.schema, self.table_name, search_table_name, search_shape_field)
                update_clause = 'ST_Within("{}"."{}"."centroid", {})'.format(
                    self.schema, self.table_name, update_clause)
        elif overlap_type == 'HAVE_SURFACE_POINT_IN':
            if search_distance == 0:
                query_string = 'ST_Within(ST_PointOnSurface("{}"."{}"."{}"), {}."{}")'.format(
                    self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
                update_clause = 'ST_Within(ST_PointOnSurface("{}"."{}"."{}"), {})'.format(
                    self.schema, self.table_name, self.shape, update_clause)
            else:
                query_string = 'ST_DWithin(ST_PointOnSurface("{}"."{}"."{}"), {}."{}", {})'.format(
                    self.schema, self.table_name, self.shape, search_table_name, search_shape_field, search_distance)
                update_clause = 'ST_DWithin(ST_PointOnSurface("{}"."{}"."{}"), {}, {})'.format(
                    self.schema, self.table_name, self.shape, update_clause, search_distance)

        elif overlap_type == 'WITHIN_A_DISTANCE':
            query_string = 'ST_DWithin("{}"."{}"."{}", {}."{}", {})'.format(
                self.schema, self.table_name, self.shape, search_table_name, search_shape_field, search_distance)
            update_clause = 'ST_DWithin("{}"."{}"."{}", {}, {})'.format(
                self.schema, self.table_name, self.shape, update_clause, search_distance)
        elif overlap_type == 'OVERLAPS':
            query_string = 'ST_Overlaps("{}"."{}"."{}", {}."{}")'.format(
                self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
            update_clause = 'ST_Overlaps("{}"."{}"."{}", {})'.format(
                self.schema, self.table_name, self.shape, update_clause)
        elif overlap_type == 'SHARE_A_LINE_SEGMENT_WITH':
            # handle separately if this is a layer search
            if isinstance(search_object, Layer):
                # REQUIRE EDGE BUFFERS
                # change overlap type to avoid filtering the results
                overlap_type = 'SHARE_A_LINE_SEGMENT_WITH_LAYER'

                # use shares a segment database function
                query_string = 'shares_a_segment("{}"."{}"."{}", {}."{}")'.format(
                    self.schema, self.table_name, self.shape, search_table_name, search_edge_buffer_field)
                update_clause = 'shares_a_segment("{}"."{}"."{}", {})'.format(
                    self.schema, self.table_name, self.shape, update_buffer_clause)
            else:
                # handle geometry searches manually
                query_string = 'ST_Intersects(ST_Envelope("{}"."{}"."{}"), ST_Envelope({}."{}"))'.format(
                    self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
                update_clause = ''
        elif overlap_type == 'MIDPOINT_NEAR':
            if not self.has_midpoint_column:
                self.add_midpoint_column()
            query_string = 'ST_DWithin("{}"."{}"."midpoint", {}."{}", 0.00001)'.format(
                self.schema, self.table_name, search_table_name, search_shape_field)
            update_clause = 'ST_DWithin("{}"."{}"."midpoint", {}, 0.00001)'.format(
                self.schema, self.table_name, update_clause)

        else:
            # manual searches - CROSSED_BY_THE_OUTLINE_OF, and BOUNDARY_TOUCHES
            query_string = 'ST_Intersects(ST_Envelope("{}"."{}"."{}"), ST_Envelope({}."{}"))'.format(
                self.schema, self.table_name, self.shape, search_table_name, search_shape_field)
            update_clause = ''

        # append attribute query to end of query strings
        if attribute_query:
            attribute_query = format_query_string(self, attribute_query)
            query_string = '({}) AND ({})'.format(query_string, attribute_query)
            update_clause = '({}) AND ({})'.format(update_clause,
                attribute_query) if not update_clause == '' else attribute_query

        # add selection to list
        self._selections.append({
            'selection_type': selection_type,
            'query': query_string,
            'update_clause': update_clause,
            'overlap_type': overlap_type,
            'from_tables': [f'"{self.schema}"."{self.table_name}"', search_table_clause],
            'search_objects': search_objects,
            'search_distance': search_distance,
        })

        # if we are inverting the relationsship, add a SWITCH_SELECTION to the selection list
        if invert_spatial_relationship == 'INVERT':
            self._selections.append({
                'selection_type': 'SWITCH_SELECTION',
                'query': '',
                'update_clause': update_clause,
                'overlap_type': 'ATTRIBUTE',
                'from_tables': [f'"{self.schema}"."{self.table_name}"'],
                'search_objects': []
            })

    def get_selection_set(self, field_names=None):
        """ Gets the selected features in the table in a SelectionSet object.

        :return: A `SelectionSet()` object containing the selected objects in the table.
        """
        field_names = self.field_names + [self.shape] if field_names is None else field_names
        return SelectionSet(self, field_names, self.query_string())

    # SCHEMA MANAGEMENT METHODS
    def duplicate_layer(self, output_layer_name,
        output_workspace=None,
        output_schema=None,
        new_geom_type=None,
        new_spatial_reference=None):
        """
        Duplicates the layer's schema as a new empty shapefile. The data in the source shapefile is *not*
        copied to the new shapefile. Use the `copy_to_new_table` method if you wish to copy the source
        data into a new layer.

        :param output_layer_name: The name of the new layer.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: The new empty layer
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace
        output_workspace.create_schema(output_schema)

        # set the spatial reference if necessary
        spatial_reference = new_spatial_reference if new_spatial_reference else self.spatial_reference

        field_defs = []
        for field in self.fields:
            if field.name == self.oid:
                field_def = Column(field.name, Integer, primary_key=True, autoincrement=True)
            elif field.name.lower() in [field_name.lower() for field_name in self.get_geometry_field_names()]:
                new_geom_type = new_geom_type.upper() if new_geom_type is not None else self.geometry_type.upper()
                if new_geom_type == 'POLYGON':
                    new_geom_type = 'MULTIPOLYGON'
                elif new_geom_type == 'POLYLINE':
                    new_geom_type = 'MULTILINESTRING'
                field_def = Column(field.name, Geometry(new_geom_type, srid=spatial_reference))
            else:
                field_def = Column(field.name, field.type)
            field_defs.append(field_def)

        alchemy_table = AlchemyTable(output_layer_name, MetaData(), schema=output_schema, *field_defs)
        alchemy_table.create(output_workspace.alchemy_engine)

        return Layer(output_layer_name, output_workspace, schema=output_schema)

    def delete_other_fields(self, preserve_fields):
        """
        Deletes all of the fields in the table except those specified in the `preserve_fields` set. Fields
        required by all shapefiles (FID, Shape, etc.) will be preserved automatically.

        :param preserve_fields: A set of fields not to be deleted.
        :return: None
        """
        # insure that the preserve fields are a list
        if preserve_fields is None:
            preserve_fields = []
        if isinstance(preserve_fields, str):
            preserve_fields = [preserve_fields]

        #  add shape as a required field
        preserve_fields = preserve_fields + [self.shape, 'edge_buffers', 'centroid', 'midpoint', 'EDGE_BUFFERS', 'CENTROID', 'MIDPOINT'] if self.shape not in preserve_fields \
            else preserve_fields + ['edge_buffers', 'centroid', 'midpoint', 'EDGE_BUFFERS', 'CENTROID', 'MIDPOINT']

        # call the base class method to do the work
        return super(Layer, self).delete_other_fields(preserve_fields)

    def get_shape_field(self):
        """ Gets the name of the shape field for this layer.

        The "Shape" field is the field that contains the geometry in an Esri feature class. Typically,
        the name of the shape field is "Shape" but not always, so this method should be used to insure
        that the correct name is always used.

        :return: A string with the name of the Shape field for this layer.
        """

        # if we've already determined the shape field name, just return it
        if self._cached_shape_field is not None:
            return self._cached_shape_field['name']

        geometry_columns = self.get_geometry_columns()
        if len(geometry_columns) > 1:
            geometry_columns = list(filter(lambda x: x['name'].upper() == 'GEOM', geometry_columns))

        self._cached_shape_field = geometry_columns.pop()
        return self._cached_shape_field['name']

    def get_geometry_columns(self, include_hidden=False):
        """ Gets a list of geometry columns for the layer.

        :param include_hidden: If true, columns that are otherwise hidden such as edge_buffers, midpoint, and centroid
            will be included in the results.
        :return: A list of geometry column names for the layer.
        """

        if not include_hidden:
            if self._cached_geometry_columns_reduced:
                return self._cached_geometry_columns_reduced
            self._cached_geometry_columns_reduced = self.workspace.get_geometry_columns(self.table_name, include_hidden, schema=self.schema)
            return self._cached_geometry_columns_reduced
        if self._cached_geometry_columns:
            return self._cached_geometry_columns
        self._cached_geometry_columns = self.workspace.get_geometry_columns(self.table_name, include_hidden, schema=self.schema)
        return self._cached_geometry_columns

    def get_geometry_field_names(self, include_hidden=False):
        """ Gets a list of geometry columns for the layer.

        :param include_hidden: If true, columns that are otherwise hidden such as edge_buffers, midpoint, and centroid
            will be included in the results.
        :return: A list of geometry column names for the layer.
        """

        geometry_columns = self.get_geometry_columns(include_hidden)
        if geometry_columns:
            return [column['name'] for column in geometry_columns]
        return None

    def nearest_item(self, geometry):
        """ Finds the item in the layer that is nearest to the provided geometry.

        :param geometry: The geometry to be used.
        :return: A tuple containing the objectId and geometry of the item nearest to the provided geometry.
        """

        # backup the current selection on the layer so we can restore it later
        current_selections = self.clone_selections()

        selection_type = 'SUBSET_SELECTION' if len(current_selections) > 0 else 'NEW_SELECTION'

        # first see if any features intersect - if not, search using
        # an exponentially increasing distance search until some feature
        # are found to evaluate
        radius = 100
        self.select_layer_by_location('WITHIN_A_DISTANCE', geometry, selection_type=selection_type,
            search_distance=radius)
        while self.count == 0 and radius < 10000:
            radius *= 10
            self.apply_selections(current_selections)
            self.select_layer_by_location('WITHIN_A_DISTANCE', geometry,
                selection_type=selection_type, search_distance=radius)

        # loop through the found shapes and record the oid and distance
        # of the shape that is nearest to the target shape
        with self.get_search_cursor([self.oid, self.shape],
            sql_clause=(None,
            'ORDER BY ST_Distance("{schema_name}"."{table_name}"."{shape_field}", ST_GeomFromWKB(DECODE(\'{wkb}\', \'hex\'), {srid})), "{schema_name}"."{table_name}"."{oid_field}" ASC LIMIT 1'.format(
                schema_name=self.schema, table_name=self.table_name, shape_field=self.shape, wkb=geometry.to_postgis(),
                srid=geometry.spatial_reference, oid_field=self.oid))) as near_cursor:
            if len(near_cursor) > 0:
                near_row = next(near_cursor)
                return_data = (near_row[self.oid], near_row[self.shape])
            else:
                return_data = (-1, None)

        # reapply original selections to near layer before exiting
        self.apply_selections(current_selections)
        return return_data

    def near(self, near_layer):
        """ Adds proximity attribute fields to the layer.

        Calculates distance and additional proximity information between the layer and the closest feature in another
        layer, and adds these as attribute fields to the layer. If the attributes already exist, it will update their
        values.

        :param near_layer: The layer containing the near feature candidates. Features can be point, polyline, polygon,
            or multipoint.
        """

        # backup the current selection on the layer so we can restore it later
        current_selections = self.clone_selections()

        # clear selections and add\clear fields
        self.clear_selection()

        # establish output columns
        if 'near_fid' not in self.field_names:
            self.add_field('near_fid', 'LONG', -1, add_index=True)
        else:
            self.calculate_field('near_fid', -1)

        if 'near_dist' not in self.field_names:
            self.add_field('near_dist', 'FLOAT', -1)
        else:
            self.calculate_field('near_dist', -1)

        # reapply the selection to the current layer
        self.apply_selections(current_selections)

        # loop through and select near features
        with self.get_update_cursor([self.shape, 'near_fid', 'near_dist']) as cursor:
            for row in cursor:
                near_oid, near_geometry = near_layer.nearest_item(row[self.shape])
                distance = row[self.shape].distance_to(near_geometry) if near_geometry else -1
                row['near_dist'] = distance
                row['near_fid'] = near_oid

                # update the results in the row
                cursor.update_row(row)

    # DATA MANIPULATION METHODS

    def get_geometries(self):
        """
        Gets a list of geometry objects for the selected features in the layer (or all features if no features
        are selected)

        :return: A list of geometry objects
        """
        with self.get_search_cursor([self.shape]) as cursor:
            geometries = [row[self.shape] for row in cursor]
        return geometries

    def get_lines(self):
        """
        Gets a list of line objects for the selected features in the layer (or all features if no features
        are selected). Only valid if the layer is a line or polygon layer

        :return: A list of line objects
        """
        # if this is a point layer throw an error
        if self.geometry_type == 'Polyline':
            line_geometries = self.get_geometries()
        elif self.geometry_type == 'Polygon':
            with self.split_lines_to_layer('get_lines_temp_layer') as line_temp_layer:
                line_geometries = line_temp_layer.get_geometries()
        else:
            raise ValueError('Lines can only be obtained from line or polygon layers.')

        # loop through geometries and create a collection of line objects to return
        return line_geometries

    def get_unique_shapes(self, query_string=None):
        """ Gets a set of unique shapes found in the selected features.

        :param query_string: An SQL expression used to select a subset of records.
        :return: A list of unique shapes.
        """
        with self.get_search_cursor(self.shape, query_string) as cursor:
            shapes = [row[self.shape] for row in cursor]
        unique_shapes = [shapes.pop()]
        for shape in shapes:
            duplicate = False
            for unique_shape in unique_shapes:
                duplicate = True if shape.equals(unique_shape) else False
                # bail out of our loop if we find a dupe
                if duplicate:
                    break
            # if we went through all of the unique shapes and did not find the target shape,
            # add the target shape to the list of unique shapes
            if not duplicate:
                unique_shapes.append(shape)
        return unique_shapes

    def generalize_to_layer(self, output_layer_name, max_offset=1, output_workspace=None, output_schema=None):
        """ Creates a new layer with generalized versions of the geometries in the current layer.

        :param output_layer_name: The name of the output layer in the geodatabase.
        :param max_offset: The maximum deviation allow when removing vertices as part of the generalization process.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A layer object representing the newly created layer.
        """

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # copy the current layer to a new layer
        return_layer = self.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)

        # loop through records and generalize geometries
        with return_layer.get_update_cursor([return_layer.shape]) as cursor:
            for row in cursor:
                row[return_layer.shape] = row[return_layer.shape].generalize(max_offset)
                cursor.update_row(row)

        return return_layer

    def copy_to_new_table(self, output_layer_name,
        output_workspace=None, output_schema=None):
        """ Copies the contents of the layer to a new layer.

        This function copies the contents of the layer to a new
        layer. If the current layer contains a selection set,
        only the selected features will be copied.

        :param output_layer_name: The name of the layer that the
            features will be copied to. If a path to a shapefile is
            specified, the shapefile will be created in the specified
            location and the layer will have the same name as the shapefile
            without the .shp extension. If only a name is specified, the
            layer will be exported to a shapefile in the same directory
            as the source layer's shapefile.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A layer object representing the newly created layer.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        db_transfer = not (self.workspace.connection_info['host'] == output_workspace.connection_info['host'] and
                      self.workspace.connection_info['port'] == output_workspace.connection_info['port'] and
                      self.workspace.connection_info['database'] == output_workspace.connection_info['database'])

        copy_layer = self.duplicate_layer(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)

        # go ahead and retrieve the where clause (this forces
        # the execution of any spatial queries and insures
        # that our from clause is correct
        where_clause = self.where_clause

        if not db_transfer:
            query_string = 'INSERT INTO "{output_schema}"."{output_layer_name}" ({output_field_names}) \
                SELECT DISTINCT {field_names}  FROM {from_clause} {where_clause}' \
                .format(
                output_schema=output_schema,
                output_layer_name=output_layer_name,
                output_field_names=','.join(
                    ['"{}"'.format(field_name) for field_name in copy_layer.get_geometry_field_names() + self.field_names]),
                field_names=','.join(['"{}"'.format(field_name) for field_name in self.get_geometry_field_names() + self.field_names]),
                from_clause=self.from_clause,
                where_clause=where_clause)
        else:
            where_clause = where_clause.replace("'", "''") if where_clause else where_clause
            query_string = "INSERT INTO {output_layer_name} ({output_field_names}) \
                SELECT {field_names} FROM dblink('host={host} port={port} dbname={database} \
                user={user} password={password} options=-csearch_path=', 'select distinct {field_names} from {from_clause} {where_clause}') \
                as link_table({field_definitions})" \
                .format(
                output_layer_name='"{}"."{}"'.format(output_schema, output_layer_name),
                output_field_names=','.join(
                    ['"{}"'.format(field_name) for field_name in copy_layer.get_geometry_field_names() + self.field_names]),
                field_names=','.join(['"{}"'.format(field_name) for field_name in self.get_geometry_field_names() + self.field_names]),
                from_clause=self.from_clause,
                where_clause=where_clause,
                host=self.workspace.connection_info['host'],
                database=self.workspace.connection_info['database'],
                port=self.workspace.connection_info['port'],
                user=self.workspace.connection_info['user'],
                password=self.workspace.connection_info['password'],
                field_definitions=','.join(
                    ['"{}" {}'.format(field_name, self.get_field_type(field_name)) for field_name in
                        copy_layer.get_geometry_field_names() + self.field_names]))

        output_workspace.execute_simple_sql(query_string)

        return copy_layer

    def select_to_layer(self, output_layer_name, query_string,
        output_workspace=None, output_schema=None):
        """ Copies features of the layer to a new layer, selected using SQL query.

        This function copies features of the layer to a new layer, selected using SQL query. This is equivalent
        to calling select_layer_by_attribute and copy_to_new_table in sequence.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param query_string: An SQL expression used to select a subset of features.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A layer object representing the newly created layer.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # if the query string is an integer, use it to query the oid field

        query_string = '' if query_string is None else '"{}" = {}'.format(self.oid, query_string) \
            if isinstance(query_string, int) else format_query_string(self, query_string)
        where_clause = ' WHERE {}'.format(query_string) if not query_string == '' else ''
        copy_layer = self.duplicate_layer(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
        query_string = "INSERT INTO {output_layer_name} ({output_field_names}) \
            SELECT {field_names} FROM {from_clause} {where_clause}" \
            .format(
            output_layer_name=f'"{output_schema}"."{output_layer_name}"',
            output_field_names=','.join(
                ['"{}"'.format(field_name) for field_name in self.field_names + [copy_layer.shape]]),
            field_names=','.join(['"{}"'.format(field_name) for field_name in self.field_names + [self.shape]]),
            from_clause=f'"{self.schema}"."{self.table_name}"',
            where_clause=where_clause)

        output_workspace.execute_simple_sql(query_string)

        return copy_layer

    def append(self, add_layers, schema_type='TEST'):
        """ Appends features from one or more layers to this layer. This mutates the layer.

        :param add_layers: A list of layers with features to append to this layer.
        :param schema_type: A string specifying if the schema of the layers should match. Valid options are:
            TEST - Schema must match, otherwise throw error.
            NO_TEST - Schema do not have to match.
        """
        if not isinstance(add_layers, list):
            add_layers = [add_layers]

        for index, layer in enumerate(add_layers):
            assert isinstance(layer, Layer)

            # check schema match option here
            if schema_type == 'TEST':
                self._assert_matching_fields(layer)

            # copy the data
            fields = self.field_names + [layer.shape]
            add_rows = []
            with layer.get_search_cursor(fields) as cursor:
                for row in cursor:
                    new_row = {}
                    for field in fields:
                        if field == layer.shape:
                            new_row[self.shape] = row[layer.shape]
                        else:
                            new_row[field] = row[field]

                    add_rows.append(new_row)

                    # flush the rows every 1000 or so to save memory
                    if len(add_rows) >= 1000:
                        self.add_rows(add_rows)
                        add_rows = []

            # flush the final rows
            if len(add_rows) > 0:
                self.add_rows(add_rows)

    def convert_to_table(self, output_table_name,
        output_workspace=None, output_schema=None,
        query_string=None):
        """ Converts the layer to a standard table by dropping its spatial attributes

        :param output_table_name: The name of the newly created output table.
        :param output_workspace: The workspace where the output table will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :param query_string: An SQL query that can be used to reduce the data that is exported to the table.
        :return: A Table object representing the new table.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # copy the layer to the new table name
        if query_string:
            self.select_layer_by_attribute(query_string)
        copy_layer = self.copy_to_new_table(output_table_name, output_workspace, output_schema=output_schema)

        # drop the geometry column
        copy_layer.delete_field(copy_layer.shape)
        if copy_layer.has_search_column:
            copy_layer.drop_search_column()
        if copy_layer.has_centroid_column:
            copy_layer.drop_centroid_column()
        if copy_layer.has_midpoint_column:
            copy_layer.drop_midpoint_column()
        # sql_command = "SELECT DiscardGeometryColumn('{}', '{}')".format(copy_layer.table_name, copy_layer.shape)
        # output_workspace.execute_simple_sql(sql_command)
        return Table(output_table_name, output_workspace, schema=output_schema)

    # GEOPROCESSING FUNCTIONS

    def minimum_bounding_geometry_to_layer(self, output_layer_name,
        geometry_type='RECTANGLE_BY_AREA',
        omit_field_options='NO_MBG_FIELDS',
        output_workspace=None, output_schema=None):
        """ Creates a layer containing the minimum bounding geometries surrounding the specified features in the layer.

        Creates a layer containing polygons which represent a specified minimum bounding geometry enclosing each
        input feature or each group of input features.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param geometry_type: Specifies what type of minimum bounding geometry the output polygons will represent.
        Valid values are:
            RECTANGLE_BY_AREA - The rectangle of the smallest area enclosing an input feature. This is the default.
            CONVEX_HULL - The smallest convex polygon enclosing an input feature.
        :param omit_field_options: Specifies whether to add the geometric attributes in the output feature class or
            omit them in the output feature class. Valid values are:
                NO_MBG_FIELDS - Omits any input attributes in the output feature class. This is the default.
                MBG_FIELDS - Adds the geometric attributes in the output feature class.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # only valid for polygon layers
        assert self.geometry_type == 'Polygon', 'MBRs can only be generated for polygon layers.'

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # duplicate the layer and add "orig_fid" field
        output_layer = self.duplicate_layer(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
        output_layer.add_field('orig_fid', 'LONG')

        # add mbg fields if necessary
        if omit_field_options == 'MBG_FIELDS':
            output_layer.add_field('mbg_width', 'FLOAT')
            output_layer.add_field('mbg_length', 'FLOAT')

        # copy rows into the new layer
        new_rows = []
        field_names = self.field_names + [self.oid, self.shape]
        with self.get_search_cursor(field_names) as cursor:
            for row in cursor:
                new_row = {}
                for field in field_names:
                    if field == self.oid:
                        new_row['orig_fid'] = row[self.oid]
                    elif field == self.shape:
                        geometry = row[self.shape]
                        new_row[output_layer.shape] = geometry.convex_hull \
                            if geometry_type == 'CONVEX_HULL' else geometry.mbr
                        if omit_field_options == 'MBG_FIELDS':
                            # get mbr edges and measure them
                            short_length = -1
                            long_length = -1
                            edges = geometry.mbr.to_lines()
                            for edge in edges:
                                short_length = edge.length \
                                    if short_length == -1 or edge.length < short_length else short_length
                                long_length = edge.length if edge.length > long_length else long_length

                            new_row['mbg_width'] = short_length
                            new_row['mbg_length'] = long_length
                    else:
                        new_row[field] = row[field]

                # add new row to list
                new_rows.append(new_row)

                # commit rows every 1000 or so to conserve memory
                if len(new_rows) >= 1000:
                    output_layer.add_rows(new_rows)
                    new_rows = []

        # insert any final rows before exiting
        if len(new_rows) > 0:
            output_layer.add_rows(new_rows)

        return output_layer

    def buffer_to_layer(self, output_layer_name, buffer_distance,
        line_side='MITRE',
        line_end_type='ROUND',
        dissolve_option='NONE',
        dissolve_field=None,
        output_workspace=None,
        output_schema=None):
        """ Creates a buffer around the layers selected features.

        This method will create a buffer layer containing polygons that are based on a buffered distance around the
        features in the current layer.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param buffer_distance: The distance around the input features that will be buffered. Distances can be provided
            as either a value representing a linear distance or as a field from the input features that contains the
            distance to buffer each feature. If linear units are not specified or are entered as Unknown, the linear
            unit of the input features' spatial reference is used.
        :param line_side: The sides of the input features that will be buffered. Valid values are:
            FULL - For line input features, buffers will be generated on both sides of the line. For polygon input
                features, buffers will be generated around the polygon and will contain and overlap the area of the
                input features. For point input features, buffers will be generated around the point. This is the
                default. Valid values are:
            LEFT - For line input features, buffers will be generated on the topological left of the line. This
                option is not valid for polygon input features.
            RIGHT - For line input features, buffers will be generated on the topological right of the line. This
                option is not valid for polygon input features.
            OUTSIDE_ONLY - For polygon input features, buffers will be generated only outside the input polygon
                (the area inside the input polygon will be erased from the output buffer). This option is not
                valid for line input features.
        :param line_end_type: The shape of the buffer at the end of line input features. This parameter is not valid
            for polygon input features. Valid values are:
            ROUND - The ends of the buffer will be round, in the shape of a half circle. This is the default.
            FLAT - The ends of the buffer will be flat, or squared, and will end at the endpoint of the input line
                feature.
        :param dissolve_option: Specifies the dissolve to be performed to remove buffer overlap. Valid values are:
            NONE - An individual buffer for each feature is maintained, regardless of overlap. This is the default.
            ALL - All buffers are dissolved together into a single feature, removing any overlap.
            LIST - Any buffers sharing attribute values in the listed fields (carried over from the input features)
                are dissolved.
        :param dissolve_field: The list of fields from the input features on which to dissolve the output buffers.
            Any buffers sharing attribute values in the listed fields (carried over from the input features) are
            dissolved.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        with self.duplicate_layer('wb_{}'.format(get_uuid()), self.workspace, new_geom_type='Polygon', output_schema=output_schema) as ind_buffer_layer, \
            self.get_search_cursor([self.shape] + self.field_names) as source_cursor:

            with ind_buffer_layer.get_insert_cursor([ind_buffer_layer.shape] + self.field_names) as write_cursor:
                for row in source_cursor:
                    row[self.shape] = row[self.shape].buffer(buffer_distance, join_style=line_side, end_style=line_end_type)
                    write_cursor.insert_row(row)

            if dissolve_option == 'NONE':
                return_layer = ind_buffer_layer.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)
            else:
                return_layer = ind_buffer_layer.dissolve_to_layer(output_layer_name, dissolve_field,
                    output_workspace=output_workspace, output_schema=output_schema)

        return return_layer

    def union_geometries(self):
        """ Unions all of the selected geometries in the table together as a single geometry.

        :return: A geometry representing the union of all selected geometries in the table.
        """
        sql = 'SELECT ST_AsEWKB(ST_Union(ARRAY(SELECT "{}" FROM "{}"."{}" {}))) AS "{}";'.format(self.shape, self.schema, self.table_name, self.where_clause, self.shape)
        results = self.workspace.execute_simple_sql(sql)
        feature = next(results)
        if not feature[self.shape]:
            return None
        shapely_geometry = wkb_to_geom(feature[self.shape].tobytes())
        if isinstance(shapely_geometry, ShapelyMultiPolygon) or isinstance(shapely_geometry, ShapelyPolygon):
            return Polygon(shapely_geometry, self.spatial_reference)
        elif isinstance(shapely_geometry, ShapelyMultiLineString) or isinstance(shapely_geometry, ShapelyLineString):
            return Line(shapely_geometry, self.spatial_reference)
        raise ValueError('Unsupported geometry type')

    def dissolve_to_layer(self, output_layer_name,
        dissolve_fields=None,
        multi_part=True,
        output_workspace=None,
        output_schema=None):
        """ Aggregates features based on specified attributes.

        This method will consolidate features based on the attributes specified.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param dissolve_fields: The field or fields on which to aggregate features.
        :param multi_part: Specifies whether multipart features are allowed in the output layer. Valid values are:
            MULTI_PART  - Specifies multipart features are allowed. This is the default.
            SINGLE_PART  - Specifies multipart features are not allowed. Instead of creating multipart features,
                individual features will be created for each part.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # logging.debug('Dissolving table {} to {}'.format(self.table_name, output_layer_name))

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # copy the table to the output workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        with self.copy_to_new_table('wd_{}'.format(get_uuid()), output_workspace) as temp_layer:

            # duplicate the current layer
            if not multi_part:
                output_layer = temp_layer.copy_to_new_table('wd_2_{}'.format(get_uuid()), output_workspace, output_schema=output_schema)
            else:
                output_layer = temp_layer.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)

            # delete all rows in the copied table
            output_layer.truncate()

            # delete all fields but the dissolve fields
            dissolve_fields = [] if not dissolve_fields else [dissolve_fields] if isinstance(dissolve_fields, str) else dissolve_fields
            output_layer.delete_other_fields(dissolve_fields)

            if self.geometry_type == 'Point':
                spatial_sql = '(ST_Dump(ST_Union("{}"))).geom'.format(self.shape)
            else:
                spatial_sql = 'ST_Multi(ST_Union("{}"))'.format(self.shape)

            if len(dissolve_fields) == 0:
                sql = 'INSERT INTO "{output_schema}"."{output_table}" ("{output_shape}") ' \
                      '(SELECT {spatial_sql} FROM "{input_schema}"."{input_table}");'.format(
                    output_schema=output_schema,
                    output_table=output_layer.table_name,
                    output_shape=output_layer.shape,
                    spatial_sql=spatial_sql,
                    input_schema=temp_layer.schema,
                    input_table=temp_layer.table_name
                )
            else:
                key_attributes = ','.join(['"{}"'.format(field) for field in dissolve_fields])
                sql = 'INSERT INTO "{output_schema}"."{output_table}" ({key_attributes}, "{output_shape}") ' \
                      'SELECT {key_attributes}, {spatial_sql} FROM "{input_schema}"."{input_table}" ' \
                      'GROUP BY {key_attributes};'.format(
                    output_schema=output_schema,
                    output_table=output_layer.table_name,
                    output_shape=output_layer.shape,
                    key_attributes=key_attributes,
                    spatial_sql=spatial_sql,
                    input_schema=temp_layer.schema,
                    input_table=temp_layer.table_name
                )

            temp_layer.workspace.execute_simple_sql(sql)

            # if this is a line layer, merge the multilinestrings together using linemerge
            if self.geometry_type == 'Polyline':
                sql = 'UPDATE "{output_schema}"."{output_table}" SET "{output_shape}" = ST_Multi(ST_LineMerge("{output_shape}"))'.format(
                    output_schema=output_layer.schema,
                    output_table=output_layer.table_name,
                    output_shape=output_layer.shape
                )
                temp_layer.workspace.execute_simple_sql(sql)

            if not multi_part:
                single_part_layer = output_layer.to_single_part_layer(output_layer_name, output_workspace, output_schema=output_schema)
                output_layer.delete()
                return single_part_layer
            return output_layer

    def reproject_to_layer(self, output_layer_name, spatial_reference, output_schema=None):
        """ Reprojects the layer to the specified spatial reference.

        :param output_layer_name: The name of the output layer in the geodatabase.
        :param spatial_reference: The new spatial reference for the geometry.
        """
        # set the output schema if necessary
        output_schema = self.schema if not output_schema else output_schema

        # create the output layer
        output_layer = self.duplicate_layer(output_layer_name, output_schema=output_schema, new_spatial_reference=spatial_reference)

        new_rows = []
        with self.get_search_cursor(self.field_names + [self.shape]) as cursor:
            for row in cursor:
                new_row = copy.deepcopy(row)
                new_row[self.shape] = new_row[self.shape].project(spatial_reference)
                new_rows.append(new_row)
        output_layer.add_rows(new_rows)
        return output_layer

    def intersection_points_to_layer(self, intersects_layer, output_layer_name, output_workspace=None, output_schema=None):
        """

        """

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # create points layer to hold outputs
        output_layer = output_workspace.create_feature_class(output_layer_name, 'POINT', schema=output_schema)

        # loop through records in this feature class and find the features they intersect with
        with self.get_search_cursor([self.shape]) as cursor:
            edges = [row[self.shape] if isinstance(row[self.shape], Line) else row[self.shape].boundary for row in cursor]

        original_selection = intersects_layer.clone_selections()
        for edge in edges:
            intersects_layer.select_layer_by_location('INTERSECT', edge, selection_type='SUBSET_SELECTION')
            with intersects_layer.get_search_cursor([self.shape]) as cursor:
                intersection_edges = [row[self.shape] if isinstance(row[self.shape], Line) else row[self.shape].boundary for row in cursor]
            for intersection_edge in intersection_edges:
                if intersection_edge.disjoint(edge):
                    continue
                intersection_results = intersection_edge.intersection(edge, exact=True)
                if not isinstance(intersection_results, list):
                    intersection_results = [intersection_results]
                intersections = []
                for result in intersection_results:
                    if isinstance(result, Point):
                        intersections.append(result)
                    elif isinstance(result, Line):
                        intersections = intersections + result.points
                for intersection_point in intersections:
                    output_layer.add_rows([{output_layer.shape: intersection_point}])
            # reset the selection on the intersection layer for the next loop
            intersects_layer.apply_selections(original_selection)

        # reapply original selections before returning
        intersects_layer.apply_selections(original_selection)
        return output_layer

    def intersect_to_layer(self, intersects_layer, output_layer_name,
        join_attributes='ALL',
        output_type='INPUT',
        output_workspace=None,
        output_schema=None):
        """ Creates a layer containing the intersecting geometries between the current layer and the intersects layer.

        This method will create a layer based on the intersections with the geometries in the current layer compared
        to the geometries in the intersects layer.

        :param intersects_layer: The layer object containing the features to intersect.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param join_attributes: Determines which attributes from the current layer will be transferred to the output
            layer. Valid values are:
                ALL - All the attributes from the Input Features will be transferred to the Output Feature Class.
                    This is the default.
                NO_FID - All the attributes except the FID from the current layer will be transferred to the
                    output layer.
                ONLY_FID - Only the FID field from the current layer will be transferred to the output layer.
        :param output_type: Choose what type of intersection you want to find. Valid values are:
            INPUT - The intersections returned will be the same geometry type as the layer with the lowest dimension
            geometry. If all inputs are polygons, the output feature class will contain polygons. If one of the inputs
            are lines and none of the inputs are points, the output will be line. If one or more of the inputs are
            points, the output feature class will contain points. This is the default.
            POLYLINE - Line intersections will be returned. This is only valid if none of the inputs are points.
            POINT - Point intersections will be returned.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # query the selected features for the identity table (honor the join_attributes flag here).
        if join_attributes in intersects_layer.field_names:
            identity_fields = [intersects_layer.shape, join_attributes]
        else:
            identity_fields = [intersects_layer.shape, intersects_layer.oid] if join_attributes == 'ONLY_FID' else [intersects_layer.shape] + intersects_layer.field_names

        # check the output type flag here
        if output_type == 'INPUT':
            if self.geometry_type == 'Polygon' or intersects_layer.geometry_type == 'Polygon':
                output_type = 'POLYGON'
            elif self.geometry_type == 'Polyline' or intersects_layer.geometry_type == 'Polyline':
                output_type = 'POLYLINE'
            else:
                output_type = 'POINT'



        # copy this layer to the output layer
        #output_layer = self.duplicate_layer(output_layer_name, output_workspace, output_schema=output_schema, new_geom_type=output_type)
        output_layer = self.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)
        output_field_names = self.field_names + [self.shape]

        # pull the shapely geometries for the output layer into a list
        with self.get_search_cursor([self.shape]) as cursor:
            output_geometries = [row[self.shape].geometry for row in cursor]

        # copy the currently selected features in the intersect table to a working table
        # (that way we don't have to worry about preserving the selection set in the identity table)
        with intersects_layer.copy_to_new_table('wi_{}'.format(get_uuid()), output_workspace, output_schema=output_schema) as working_intersect_layer:
            # first, align the intersect geometries with the output geometries
            update_counter = 0
            with working_intersect_layer.get_update_cursor([working_intersect_layer.shape]) as cursor:
                for row in cursor:
                    row[working_intersect_layer.shape].geometry = align_vertices(row[working_intersect_layer.shape].geometry, output_geometries, row[working_intersect_layer.shape].spatial_reference)
                    cursor.update_row(row)
                    update_counter += 1
                    if update_counter >= 1000:
                        working_intersect_layer.vacuum()
                        update_counter = 0
            working_intersect_layer.vacuum()

            # pull the intersect geometries into a list
            with working_intersect_layer.get_search_cursor([working_intersect_layer.shape]) as cursor:
                intersect_geometries = [row[working_intersect_layer.shape].geometry for row in cursor]

            # next, align the output geometries with the identity geometries
            update_counter = 0
            with output_layer.get_update_cursor([output_layer.shape]) as cursor:
                for row in cursor:
                    row[output_layer.shape].geometry = align_vertices(row[output_layer.shape].geometry, intersect_geometries, row[output_layer.shape].spatial_reference)
                    cursor.update_row(row)
                    update_counter += 1
                    if update_counter >= 1000:
                        output_layer.vacuum()
                        update_counter = 0
            output_layer.vacuum()

            # re-pull the intersect geometries as Envelope shapes into a list
            with working_intersect_layer.get_search_cursor([working_intersect_layer.shape]) as cursor:
                intersect_geometries = [row[working_intersect_layer.shape] for row in cursor]

            # cut the geometries in the output layer along the edges of the identity layer
            update_counter = 0
            for identity_geometry in intersect_geometries:
                new_rows = []
                output_layer.select_layer_by_location('INTERSECT', identity_geometry.boundary)
                with output_layer.get_search_cursor(output_field_names) as cursor:
                    for row in cursor:
                        new_row_template = {}
                        original_shape = None
                        for field_name in output_field_names:
                            # if this is a regular field, just copy it
                            if not field_name == output_layer.shape:
                                new_row_template[field_name] = row[field_name]
                            else:
                                # grab the original shape
                                original_shape = row[field_name]
                        # now cut the original geometry with the identity geometry and create new rows
                        # based on the polygons
                        intersection_geometries = original_shape.intersection(identity_geometry)
                        intersection_geometries = [intersection_geometries] if not isinstance(intersection_geometries, list) else intersection_geometries

                        new_polygons = list(filter(lambda x: isinstance(x, Polygon) and not x.is_empty, intersection_geometries))

                        for new_polygon in new_polygons:
                            new_row = copy.deepcopy(new_row_template)
                            new_row[output_layer.shape] = new_polygon
                            new_rows.append(new_row)
                # now that we've split these rows, delete the old rows and add the new rows
                output_layer.delete_selected_rows()
                output_layer.add_rows(new_rows)
                update_counter += 1
                if update_counter >= 1000:
                    output_layer.vacuum()
                    update_counter = 0
            output_layer.clear_selection()

            # now add identity fields to output layer
            for identity_field in identity_fields:
                if identity_field == working_intersect_layer.shape:
                    continue
                field_type = working_intersect_layer.get_field_type(identity_field)

                if 'VARCHAR' in field_type:
                    field_length = working_intersect_layer.get_field_length(identity_field)
                    output_layer.add_field(identity_field, 'TEXT', field_length=field_length)
                else:
                    output_layer.add_field(identity_field, field_type)

            # loop through geometries in the identity layer and update the output layer
            # logging.debug('Requested identity fields:')
            with working_intersect_layer.get_search_cursor(identity_fields) as identity_cursor:
                for identity_row in identity_cursor:
                    identity_geometry = identity_row[working_intersect_layer.shape]
                    output_layer.select_layer_by_location('INTERSECT', identity_geometry)
                    with output_layer.get_update_cursor(identity_fields) as update_cursor:
                        for output_row in update_cursor:
                            if not identity_geometry.contains(output_row[working_intersect_layer.shape].representative_point):
                                continue

                            for identity_field in identity_fields:
                                if identity_field == working_intersect_layer.shape:
                                    continue
                                use_quotes = True if 'VARCHAR' in working_intersect_layer.get_field_type(identity_field) else False
                                value = "{}".format(identity_row[identity_field].replace("'", "''")) if identity_row[identity_field] and use_quotes else identity_row[identity_field]
                                output_row[identity_field] = value
                            update_cursor.update_row(output_row)

        output_layer.clear_selection()
        return output_layer

    def feature_vertices_to_points_layer(self, output_layer_name,
        output_workspace=None,
        output_schema=None):
        """ Exports the vertices of the geometries in the layer as a points layer.

        This method will extract the vertices from line and polygon layers and export them into a points layer.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # if this is a point layer just return a copy
        if self.geometry_type == 'Point':
            return self.copy_to_new_table(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)

        # query the selected features for the main table
        return_layer = self.duplicate_layer(output_layer_name, output_workspace,
            new_geom_type='Point', output_schema=output_schema)
        rows = []
        with self.get_search_cursor([self.shape] + self.field_names) as cursor:
            for row in cursor:
                for point in row[self.shape].points:
                    row_template = {return_layer.shape: point}
                    for field in self.field_names:
                        row_template[field] = row[field]
                    rows.append(row_template)
        return_layer.add_rows(rows)
        return return_layer

    def split_lines_to_layer(self, output_layer_name,
        output_workspace=None,
        output_schema=None):
        """ Splits the polylines or polygons in the layer into individual lines.

        This method will parse line and polygon layers into a new layer that contains individual line segments.
        For polygon layers, each edge will become a line in the resulting line layer. For line layers, complex lines
        with many vertices will be split into simpler lines with only start and end points.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        split_layer = self.duplicate_layer(output_layer_name, output_workspace,
            new_geom_type='Polyline', output_schema=output_schema)

        new_rows = []
        with self.get_search_cursor([self.shape] + self.field_names) as source_cursor:
            for row in source_cursor:
                if self.geometry_type == 'Polygon':
                    geom = row[self.shape]
                    lines = geom.to_lines()
                elif self.geometry_type == 'Polyline':
                    geom = row[self.shape]
                    lines = geom.split_line_at_vertices()
                else:
                    raise ValueError

                for line in lines:
                    if line.length == 0:
                        continue
                    new_row = row.copy()
                    new_row[self.shape] = line
                    new_rows.append(new_row)
        split_layer.add_rows(new_rows)
        return split_layer

    def split_lines_at_points_to_layer(self, point_layer, output_layer_name, search_radius=0, output_workspace=None, output_schema=None):
        """ Splits line features based on intersection or proximity to point features.

        :param point_layer: The input point features whose locations will be used to split the input lines.
        :param output_layer_name: The new layer that will be created containing the split lines.
        :param search_radius: Used to split lines by their proximity to point features. Points within the
            search distance to an input line will be used to split those lines at the nearest location to
            the point along the line segment. If this parameter is unspecified, the single nearest point
            will be used to split the line feature. If a radius is specified, all points within the radius
            will be used to split the line.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # verify the proper geometry types
        assert self.geometry_type == 'Polyline'
        assert point_layer.geometry_type == 'Point'

        # parse the search radius
        if isinstance(search_radius, str):
            search_radius = string_to_units(search_radius, 'FEET')
        overlap_type = 'WITHIN_A_DISTANCE' if search_radius > 0 else 'INTERSECT'

        # copy the current layer to the output layer
        output_layer = self.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)

        # loop through the point layer and select lines near each point
        # and cut them
        with point_layer.get_search_cursor([point_layer.shape]) as point_cursor:
            for point_row in point_cursor:
                # select the lines in the output layer that are within the search radius
                output_layer.select_layer_by_location(overlap_type, point_row[point_layer.shape], search_radius)
                search_fields = [output_layer.shape] + output_layer.field_names
                new_rows = []
                with output_layer.get_update_cursor(search_fields) as cursor:
                    for row in cursor:
                        line = row[output_layer.shape]
                        if not line or line.is_empty:
                            # logging.warning('  Warning: Empty line detected')
                            continue

                        nearest_point = line.nearest_point(point_row[point_layer.shape]) if line.disjoint(point_row[point_layer.shape]) else point_row[point_layer.shape]
                        split_line_1, split_line_2 = line.split(nearest_point)

                        # if the split only returned one line, continue
                        if not split_line_1 or not split_line_2 or split_line_1.is_empty or split_line_2.is_empty or split_line_1.length == 0 or split_line_2 == 0:
                            continue

                        # update the geometry on one row and add a new row
                        # with the other geometry
                        row[output_layer.shape] = split_line_1
                        cursor.update_row(row)
                        new_row = {}
                        for field in search_fields:
                            if field == output_layer.shape:
                                new_row[output_layer.shape] = split_line_2
                            else:
                                new_row[field] = row[field]
                        new_rows.append(new_row)
                if len(new_rows) > 0:
                    output_layer.add_rows(new_rows)
        # delete zero-length lines
        output_layer.clear_selection()
        output_layer.delete_zero_length_lines()
        return output_layer

    def delete_zero_length_lines(self):
        """ Deletes rows in the table with zero-length line geometries. Only applies to line layers.

        :return: None
        """

        assert self.geometry_type == 'Polyline', 'Only line layers can be processed with this method'

        sql = 'DELETE FROM "{schema_name}"."{table_name}" WHERE ST_Length("{shape}") = 0'.format(schema_name=self.schema, table_name=self.table_name, shape=self.shape)
        self.workspace.execute_simple_sql(sql)

    def correct_topology(self, output_layer_name, tolerance=0.0000001, output_workspace=None, output_schema=None):
        """
        """
        assert self.geometry_type == 'Polygon'

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        output_workspace = self.workspace if not output_workspace else output_workspace

        output_layer = self.copy_to_new_table(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
        with output_layer.get_search_cursor([output_layer.oid, output_layer.shape]) as cursor:
            geometries = [{'oid': row[output_layer.oid], 'shape': row[output_layer.shape]} for row in cursor]

        for analysis_geometry in geometries:
            for analysis_point in analysis_geometry['shape'].points:
                for index, other_geometry in enumerate(geometries):
                    if other_geometry['oid'] == analysis_geometry['oid']:
                        continue
                    if analysis_point.distance_to(other_geometry['shape'].boundary) > tolerance:
                        continue
                    found_point = False
                    for other_point in other_geometry['shape'].points:
                        if other_point.equals(analysis_point):
                            found_point = True
                            break
                    if found_point:
                        continue

                    other_geometry['shape'] = other_geometry['shape'].add_point(analysis_point).remove_duplicate_vertices()
                    geometries[index] = other_geometry

        for geometry in geometries:
            output_layer.select_layer_by_attribute(geometry['oid'])
            with output_layer.get_update_cursor([output_layer.shape]) as cursor:
                for row in cursor:
                    row[output_layer.shape] = geometry['shape']
                    cursor.update_row(row)
        output_layer.clear_selection()
        return output_layer


    def unsplit_lines_to_layer(self, output_layer_name,
                               dissolve_fields=None,
                               output_workspace=None,
                               output_schema=None):
        """ Merges lines that have coincident endpoints and, optionally, common attribute values.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param dissolve_fields: The field or fields on which to aggregate features.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # verify this is a polyline layer
        assert self.geometry_type == 'Polyline'

        # validate dissolve fields
        dissolve_fields = [] if dissolve_fields is None else [dissolve_fields] if isinstance(dissolve_fields,
            str) else dissolve_fields

        # duplicate the current layer
        output_layer = self.duplicate_layer(output_layer_name, output_workspace, output_schema=output_schema)

        # delete all fields but the dissolve fields
        output_layer.delete_other_fields(dissolve_fields)

        # load the required geometries and fields into a list
        dissolve_records = get_dissolve_records(self, output_layer, dissolve_fields)

        # back-up current selection set to replace later
        current_selections = self.clone_selections()

        # loop through the records and merge them
        for record_1, record_2 in combinations(dissolve_records, 2):
            # if either record's geometry has been set to None, skip comparison
            if record_1[output_layer.shape] is None or record_2[output_layer.shape] is None:
                continue

            # pull out geometries for convenience
            first_line = record_1[output_layer.shape]
            second_line = record_2[output_layer.shape]

            if len(dissolve_fields) > 0:
                # if the attributes in the records match, merge the geometry into one record
                # and set the other record's geometry to None (this will flag it for deletion later)
                if dissolve_records_match(record_1, record_2) and first_line.touches(second_line) \
                    and (first_line.first_point.intersects(second_line.last_point)
                         or first_line.last_point.intersects(second_line.first_point)):
                    record_2[output_layer.shape] = first_line.union(second_line)
                    record_1[output_layer.shape] = None
            else:
                # if no dissolve fields are provided join edges where they have a single intersection
                if not first_line.touches(second_line):
                    continue
                intersect_point = first_line.first_point if first_line.first_point.intersects(second_line.first_point) \
                                                            or first_line.first_point.intersects(
                    second_line.last_point) else first_line.last_point \
                    if first_line.last_point.intersects(second_line.first_point) \
                       or first_line.last_point.intersects(second_line.last_point) else None
                if intersect_point is None:
                    continue

                # query the table for the intersection point to see how many edges touch the point.
                # (if more than 2 edges touch do not merge the lines)
                self.select_layer_by_location('INTERSECT', intersect_point)
                if self.count != 2:
                    continue

                record_2[output_layer.shape] = first_line.union(second_line)
                record_1[output_layer.shape] = None

        # filter out records that have null shape fields
        # (this means they were dissolved into another shape)
        dissolve_records = list(filter(lambda x: x[output_layer.shape] is not None, dissolve_records))

        # insert the dissolve records into the output table
        output_layer.add_rows(dissolve_records)

        # replace selection set on current layer
        self.apply_selections(current_selections)

        # delete the working layer and return the final layer
        return output_layer

    @staticmethod
    def merge_layers_to_layer(layers, output_layer_name, output_workspace, output_schema=None, remove_duplicates=False):
        """ Merges the specified layers into a new layer.

        :param layers: The layer objects to be merged.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be located.
        :return: A new layer object that represents the layer containing the results of the process.
        """

        layers = layers.copy()
        template_layer = layers.pop(0)
        assert isinstance(template_layer, Layer)

        # set the schema if necessary
        output_schema = output_workspace.schema if not output_schema else output_schema
        output_workspace.create_schema(output_schema)

        all_option = 'ALL' if not remove_duplicates else ''
        field_names = ','.join(['"{}"'.format(field_name) for field_name in template_layer.field_names] + ['"{}"'.format(template_layer.oid), '"{}"'.format(template_layer.shape)])
        sql = 'CREATE TABLE "{}"."{}" AS SELECT {} FROM "{}"."{}"'.format(output_schema, output_layer_name, field_names, template_layer.schema, template_layer.table_name)
        # logging.debug('Merge layers to layer: Creating table: %s', sql)
        restart = False
        for count, layer in enumerate(layers, start=1):
            if restart:
                sql = 'INSERT INTO "{}"."{}" SELECT {} FROM "{}"."{}"'.format(output_schema, output_layer_name, field_names, layer.schema, layer.table_name)
                restart = False
            else:
                sql = '{} UNION {} SELECT {} FROM "{}"."{}"'.format(sql, all_option, field_names, layer.schema, layer.table_name)
            # process query every 50 layers
            if count % 50 == 0:
                # logging.debug('Merge layers to layer: Executing sql: %s', sql)
                output_workspace.execute_simple_sql(sql)
                restart = True
        if not restart:
            output_workspace.execute_simple_sql(sql)
        output_workspace.execute_simple_sql(
            'ALTER TABLE "{}"."{}" DROP COLUMN "{}"'.format(output_schema, output_layer_name, template_layer.oid))
        output_workspace.execute_simple_sql(
            'ALTER TABLE "{}"."{}" ADD COLUMN "{}" bigserial'.format(output_schema, output_layer_name, template_layer.oid))
        output_workspace.execute_simple_sql(
            'ALTER TABLE "{}"."{}" ADD PRIMARY KEY ("{}")'.format(output_schema, output_layer_name, template_layer.oid))

        output_workspace.create_sequence(output_layer_name, template_layer.oid, schema=output_schema)

        return Layer(output_layer_name, output_workspace, schema=output_schema)

    def merge_to_layer(self, other_layers, output_layer_name, output_workspace=None, output_schema=None):
        """ Merges the specified layers and the current layer into a new layer.

        This method will merge the current layer with the other layers that are provided (similar to a union operation
        in SQL).

        :param other_layers: The other layer objects to be merged with this one.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :param output_workspace: The workspace where the output layer will be located.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # convert other_layers to a list if a Layer object is provided
        if isinstance(other_layers, Layer):
            other_layers = [other_layers]
        merge_layer = [self] + other_layers
        return Layer.merge_layers_to_layer(merge_layer, output_layer_name, output_workspace, output_schema=output_schema)

    def get_geodataframe(self, fields=None):
        """ Converts the data in this layer to a geopandas geodataframe.

        :param fields: A list of fields from the layer to be included in the geodataframe.
        :return: A geopandas geodataframe containing the data from this layer.
        """
        try:
            import geopandas
        except Exception as e:
            raise ValueError('Geopandas is not installed')

        if fields is None:
            fields = self.field_names
        if isinstance(fields, str):
            fields = [fields]
        if self.oid not in fields:
            fields.append(self.oid)
        if self.shape not in fields:
            fields.append(self.shape)

        # get a query to feed to geopandas
        query = prepare_query(self, fields, self.query_string(), None, use_raw_fields=True)
        self.workspace.open_pandas_connection()
        geodataframe = geopandas.GeoDataFrame.from_postgis(query, self.workspace.pandas_connection, geom_col=self.shape)
        self.workspace.close_pandas_connection()
        geodataframe.set_index(self.oid, inplace=True)
        return geodataframe

    @property
    def extent(self):
        """
        Returns the extent of the selected features in the layer as a `Polygon` object.
        """
        sql = f'SELECT ST_AsText(ST_SetSRID(ST_Extent("{self.shape}"), {self.spatial_reference})) AS the_geom FROM "{self.schema}"."{self.table_name}" {self.where_clause}'
        results = self.workspace.execute_simple_sql(sql)
        wkt = next(results)['the_geom']
        return Polygon(wkt, self.spatial_reference)

    def plot(self, ax=None, boundary=False, **kwargs):
        """ Draws the layer in a `matplotlib` axes.

        :param ax: A `matplotlib.axes` object to draw the layer into. If no axes is provided the layer will be drawn
            in a new axes.
        :param kwargs: Arguments to be passed to `matplotlib` to format the drawing, such as color, etc.
        :return: The `matplotlib.axes` object that the layer is rendered in. This can be used to add
            renderings to the same plot.
        """

        if not ax:
            fig, ax = plt.subplots()
            crs = CRS.from_epsg(self.spatial_reference)
            if crs and crs.is_geographic:
                min_y = None
                max_y = None
                for point in self.extent.points:
                    min_y = point.y if not min_y or point.y < min_y else min_y
                    max_y = point.y if not max_y or point.y > max_y else max_y

                y_coord = np.mean([min_y, max_y])
                ax.set_aspect(1 / np.cos(y_coord * np.pi / 180))
            else:
                ax.set_aspect("equal")

        local_kwargs = kwargs.copy()
        edge_kwargs = local_kwargs.copy()
        edge_kwargs['color'] = 'white'
        edge_kwargs['linewidth'] = 0.25
        if edge_kwargs.get('zorder'):
            edge_kwargs['zorder'] += 1
        else:
            edge_kwargs['zorder'] = 1

        if not local_kwargs.get('color'):
            local_kwargs['color'] = '#7092BE'
        with self.get_search_cursor(self.shape) as cursor:
            for row in cursor:
                if boundary and self.geometry_type == 'Polygon':
                    row[self.shape].boundary.plot(ax=ax, **local_kwargs)
                else:
                    row[self.shape].plot(ax=ax, **local_kwargs)
                    if self.geometry_type == 'Polygon':
                        row[self.shape].boundary.plot(ax=ax, **edge_kwargs)

        self.ax = ax
        return self.ax

    def label(self, label_field, ha='center', **kwargs):
        """ Labels features in a `matplotlib` drawing based on the provided label field. If the layer
        has not been plotted yet an error will be raised.

        :param label_field: The name of the attribute field to label features with.
        :param kwargs: Arguments to be passed to `matplotlib` to format the drawing, such as color, etc.
        :return: None.
        """
        assert self.ax, 'Layer must be plotted before it can be labeled'
        assert label_field in self.field_names, 'Specified field not found'

        with self.get_search_cursor([label_field, self.shape]) as cursor:
            for row in cursor:
                if isinstance(row[self.shape], Point):
                    label_point = row[self.shape]
                elif isinstance(row[self.shape], Line):
                    label_point = row[self.shape].midpoint
                else:
                    label_point = row[self.shape].representative_point
                self.ax.annotate(text=row[label_field], xy=(label_point.x, label_point.y), ha=ha, **kwargs)


    def identity_to_layer(self, identity_layer, output_layer_name, join_attributes='ALL', output_workspace=None, output_schema=None,
                          eliminate_slivers=False, min_area=None, min_width=None):
        """ Combines the attributes of the current layer with those of the identity layer.

        Computes a geometric intersection of the input features and identity features. The input features or
        portions thereof that overlap identity features will get the attributes of those identity features.

        :param identity_layer: The layer object with the geometries that will be used to identity features.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param join_attributes: Determines what attributes will be transferred to the output layer. Valid values are:
            ALL - All the attributes (including FIDs) from the input features, as well as the identity features,
                will be transferred to the output features. If no intersection is found the identity feature values will
                not be transferred to the output (their values will be set to empty strings or 0) and the identity
                feature FID will be -1. This is the default.
            NO_FID - All the attributes except the FID from the input features and identity features will be
                transferred to the output features. If no intersection is found the identity feature values will
                not be transferred to the output (their values will be set to empty strings or 0).
            ONLY_FID - All the attributes from the input features but only the FID from the identity features will
                be transferred to the output features. The identity features FID attribute value in the output
                will be -1 if no intersection is found.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # query the selected features for the identity table (honor the join_attributes flag here).
        if join_attributes in identity_layer.field_names:
            identity_fields = [identity_layer.shape, join_attributes]
        else:
            identity_fields = [identity_layer.shape, identity_layer.oid] if join_attributes == 'ONLY_FID' else [identity_layer.shape] + identity_layer.field_names

        # copy this layer to the output layer
        output_layer = self.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)
        output_field_names = output_layer.field_names + [output_layer.shape]

        # pull the shapely geometries for the output layer into a list
        with output_layer.get_search_cursor([output_layer.shape]) as cursor:
            output_geometries = [row[output_layer.shape].geometry for row in cursor]

        # copy the currently selected features in the identity table to a working table
        # (that way we don't have to worry about preserving the selection set in the identity table)
        with identity_layer.copy_to_new_table('wi_{}'.format(get_uuid()), output_workspace, output_schema=output_schema) as working_identity_layer:
            # first, align the identity geometries with the output geometries
            update_counter = 0
            with working_identity_layer.get_update_cursor([output_layer.shape]) as cursor:
                for row in cursor:
                    row[output_layer.shape].geometry = align_vertices(row[output_layer.shape].geometry, output_geometries, row[output_layer.shape].spatial_reference)
                    cursor.update_row(row)
                    update_counter += 1
                    if update_counter >= 1000:
                        working_identity_layer.vacuum()
                        update_counter = 0
            working_identity_layer.vacuum()

            # pull the identity geometries into a list
            with working_identity_layer.get_search_cursor([working_identity_layer.shape]) as cursor:
                identity_geometries = [row[working_identity_layer.shape].geometry for row in cursor]

            # next, align the output geometries with the identity geometries
            update_counter = 0
            with output_layer.get_update_cursor([output_layer.shape]) as cursor:
                for row in cursor:
                    row[output_layer.shape].geometry = align_vertices(row[output_layer.shape].geometry, identity_geometries, row[output_layer.shape].spatial_reference)
                    cursor.update_row(row)
                    update_counter += 1
                    if update_counter >= 1000:
                        output_layer.vacuum()
                        update_counter = 0
            output_layer.vacuum()

            # re-pull the identity geometries as Envelope shapes into a list
            with working_identity_layer.get_search_cursor([working_identity_layer.shape]) as cursor:
                identity_geometries = [row[working_identity_layer.shape] for row in cursor]

            # cut the geometries in the output layer along the edges of the identity layer
            update_counter = 0
            for identity_geometry in identity_geometries:
                new_rows = []
                output_layer.select_layer_by_location('INTERSECT', identity_geometry.boundary)
                with output_layer.get_search_cursor(output_field_names) as cursor:
                    for row in cursor:
                        new_row_template = {}
                        original_shape = None
                        for field_name in output_field_names:
                            # if this is a regular field, just copy it
                            if not field_name == output_layer.shape:
                                new_row_template[field_name] = row[field_name]
                            else:
                                # grab the original shape
                                original_shape = row[field_name]
                        # now cut the original geometry with the identity geometry and create new rows
                        # based on the polygons
                        intersection_geometries = original_shape.intersection(identity_geometry)
                        intersection_geometries = [intersection_geometries] if not isinstance(intersection_geometries, list) else intersection_geometries
                        difference_geometry = original_shape.difference(identity_geometry)
                        difference_parts = difference_geometry.to_singlepart() if difference_geometry and isinstance(difference_geometry, Polygon) else []
                        new_polygons = intersection_geometries + difference_parts

                        new_polygons = list(filter(lambda x: isinstance(x, Polygon) and not x.is_empty, new_polygons))

                        # check new polygons for slivers if necessary
                        if eliminate_slivers:
                            slivers = []
                            non_slivers = []
                            for new_polygon in new_polygons:
                                if new_polygon.area < min_area or new_polygon.is_sliver(min_width):
                                    slivers.append(new_polygon)
                                else:
                                    non_slivers.append(new_polygon)

                            # replace new polygons w/ the original polygon if a sliver was created
                            if len(slivers) > 0 and len(non_slivers) == 0:
                                new_polygons = [original_shape]
                            elif len(slivers) == 1 and len(non_slivers) == 1:
                                # check to see if we want to remerge these now or later
                                non_sliver = non_slivers[0]
                                sliver = slivers[0]
                                # find all the points in the sliver that touch the main poly
                                touch_points = []
                                for point in sliver.points:
                                    if point.intersects(non_sliver):
                                        touch_points.append(point)
                                if len(touch_points) > 1:
                                    touch_line = Line(touch_points, self.spatial_reference)
                                    if touch_line.length >= sliver.length * 0.4:
                                        new_polygons = [original_shape]

                        for new_polygon in new_polygons:
                            new_row = copy.deepcopy(new_row_template)
                            new_row[output_layer.shape] = new_polygon
                            new_rows.append(new_row)
                # now that we've split these rows, delete the old rows and add the new rows
                output_layer.delete_selected_rows()
                output_layer.add_rows(new_rows)
                update_counter += 1
                if update_counter >= 1000:
                    output_layer.vacuum()
                    update_counter = 0
            output_layer.clear_selection()

            # now add identity fields to output layer
            for identity_field in identity_fields:
                if identity_field == working_identity_layer.shape:
                    continue
                field_type = working_identity_layer.get_field_type(identity_field)
                # logging.debug('Adding field to output layer {}: {}, type: {}'.format(output_layer.table_name, identity_field, field_type))
                if 'VARCHAR' in field_type:
                    field_length = working_identity_layer.get_field_length(identity_field)
                    output_layer.add_field(identity_field, 'TEXT', field_length=field_length)
                else:
                    output_layer.add_field(identity_field, field_type)

            # loop through geometries in the identity layer and update the output layer
            # logging.debug('Requested identity fields:')
            with working_identity_layer.get_search_cursor(identity_fields) as identity_cursor:
                for identity_row in identity_cursor:
                    identity_geometry = identity_row[working_identity_layer.shape]
                    output_layer.select_layer_by_location('INTERSECT', identity_geometry)
                    with output_layer.get_update_cursor(identity_fields) as update_cursor:
                        for output_row in update_cursor:
                            if not identity_geometry.contains(output_row[working_identity_layer.shape].representative_point):
                                continue

                            for identity_field in identity_fields:
                                if identity_field == working_identity_layer.shape:
                                    continue
                                use_quotes = True if 'VARCHAR' in working_identity_layer.get_field_type(identity_field) else False
                                value = "{}".format(identity_row[identity_field].replace("'", "''")) if identity_row[identity_field] and use_quotes else identity_row[identity_field]
                                output_row[identity_field] = value
                            update_cursor.update_row(output_row)

        output_layer.clear_selection()
        return output_layer

    def to_single_part_layer(self, output_layer_name, output_workspace=None, output_schema=None):
        """ Creates a layer containing single-part features generated by separating multipart input features.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # logging.debug('Splitting layer {} to single parts. Output layer: {}'.format(self.table_name, output_layer_name))

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # if this is a point layer, simply copy it
        if self.geometry_type == 'Point':
            return self.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)

        # duplicate the layer
        output_layer = self.duplicate_layer(output_layer_name, output_workspace, output_schema=output_schema)
        field_names = ",".join('"{}"'.format(field_name) for field_name in self.field_names)
        field_names = ',{}'.format(field_names) if field_names else ''
        sql = 'INSERT INTO "{output_schema}"."{output_layer_name}" ("{output_shape_field}" {field_names}) ' \
              'SELECT ST_Multi((ST_Dump("{input_shape_field}")).geom) AS "{output_shape_field}" {field_names} FROM "{input_schema}"."{input_table_name}" {where_clause}'.format(
            output_layer_name=output_layer.table_name,
            output_schema=output_schema,
            field_names=field_names,
            output_shape_field=output_layer.shape,
            input_shape_field=self.shape,
            input_schema=self.schema,
            input_table_name=self.table_name,
            where_clause=self.where_clause
        )
        self.workspace.execute_simple_sql(sql)
        return output_layer

    def to_multi_part_layer(self, output_layer_name, key_attribute, output_workspace=None, output_schema=None):
        """ Creates a layer containing single-part features generated by separating multipart input features.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # get field def for key attribute
        key_field = self.get_field(key_attribute)

        output_layer = output_workspace.create_feature_class(output_layer_name, self.geometry_type, self.spatial_reference, schema=output_schema)
        output_layer.add_field(key_field.name, key_field.type)

        sql = 'INSERT INTO "{output_schema}"."{output_table}" ("{key_attribute}", "{output_shape}") ' \
              'SELECT "{key_attribute}", ST_Multi(ST_Union("{input_shape}")) FROM "{input_schema}"."{input_table}" ' \
              'GROUP BY "{key_attribute}";'.format(
            output_table=output_layer.table_name,
            output_schema=output_schema,
            output_shape=output_layer.shape,
            key_attribute=key_attribute,
            input_shape=self.shape,
            input_schema=self.schema,
            input_table=self.table_name
        )
        output_workspace.execute_simple_sql(sql)
        return output_layer

    def feature_to_point_layer(self, output_layer_name,
                               point_location='CENTROID',
                               output_workspace=None,
                               output_schema=None):
        """
        Creates a layer containing points generated from the representative locations of input features.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param point_location: Specifies whether to use representative centers of input features or locations
        contained by input features as the output point locations.
            CENTROID - Uses the representative center of an input feature as its output point location.
            This is the default. This point location may not always be contained by the input feature.
            INSIDE - Uses a location contained by an input feature as its output point location.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # if this is a point layer just return a copy
        if self.geometry_type == 'Point':
            return self.copy_to_new_table(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)

        return_layer = self.copy_to_new_table(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
        if point_location == 'CENTROID':
            return_layer.add_centroid_column()
        else:
            return_layer.add_centroid_column(inside=True)

        return_layer.delete_field(return_layer.shape)
        return_layer.add_field('geom', 'GEOMETRY', geometry_type='Point', spatial_reference=self.spatial_reference)
        return_layer.copy_field_values('centroid', 'geom')
        return_layer.drop_centroid_column()
        return return_layer


    def boundaries_to_layer(self, output_layer_name, output_workspace=None, output_schema=None):
        """ Exports the boundaries from a polygon layer into a line layer. Boundary lines are polylines that represent
        a single line for each polygon, and are different from the results of the  `split_lines_to_layer` method,
        which splits polygons into lines based on vertices.

        """
        # this function only works on polygon layers
        assert self.geometry_type == 'Polygon'

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # create an output layer
        output_layer = output_workspace.create_feature_class(output_layer_name, 'POLYLINE', schema=output_schema)

        with self.get_search_cursor([self.shape]) as cursor:
            new_rows = [{output_layer.shape: row[self.shape].boundary} for row in cursor]

        output_layer.add_rows(new_rows)
        return output_layer

    def add_vertices_from_points_layer(self, points_layer, output_layer_name, cluster_tolerance=0.000001, output_workspace=None, output_schema=None):
        """ Uses the points in the provided points layer to add vertices to the geometries in the current layer.

        :param points_layer: The points layer containing points to be used as vertices.
        :param output_layer_name: The name of the new layer containing the geometries with added vertices.
        :param cluster_tolerance: The allowable distance that a point can be from an edge and still be added
            as a vertex for the edge. If this number is large is can significantly alter the target geometry.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new `Layer()` object representing the output layer in the geodatabase.
        """

        # this function only works on line and polygon layers
        assert self.geometry_type == 'Polyline' or self.geometry_type == 'Polygon'

        # input layer must be points
        assert points_layer.geometry_type == 'Point'

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # copy the current layer to the output table
        output_layer = self.copy_to_new_table(output_layer_name, output_workspace, output_schema=output_schema)

        # grab the original selection on the point layer so it can be replaced layer
        original_point_selections = points_layer.clone_selections()

        # loop through the geometries in the points layer
        with output_layer.get_update_cursor([output_layer.shape]) as cursor:
            for row in cursor:
                shape = row[output_layer.shape]
                if isinstance(shape, Polygon):
                    lines = shape.to_lines()
                    edges = Line.unify_lines(lines)
                else:
                    edges = [shape]

                for edge in edges:
                    points_layer.select_layer_by_location('WITHIN_A_DISTANCE', edge, search_distance=cluster_tolerance, selection_type='SUBSET_SELECTION')
                    with points_layer.get_search_cursor([points_layer.shape]) as point_cursor:
                        for point_row in point_cursor:
                            shape = shape.add_point(point_row[points_layer.shape])
                    points_layer.apply_selections(original_point_selections)
                row[points_layer.shape] = shape
                cursor.update_row(row)

        # reapply the original selections to the points layer before returning
        points_layer.apply_selections(original_point_selections)

        return output_layer

    def feature_to_polygon_layer(self, output_layer_name,
                                 cluster_tolerance='',
                                 attributes_layer=None,
                                 output_workspace=None,
                                 output_schema=None):
        """ Creates a layer containing polygons generated from areas enclosed by input line or polygon features.

        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param cluster_tolerance: The minimum distance separating all feature coordinates, and the distance a
            coordinate can move in X, Y, or both during spatial computation. The default XY tolerance is set to
            0.001 meter or its equivalent in feature units.
        :param attributes_layer: A point layer containing attributes to be transferred to the new polygons.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """

        # this function only works on line layers
        assert self.geometry_type == 'Polyline'

        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # create a list of shapely geometries
        with self.get_search_cursor([self.shape]) as cursor:
            shapely_lines = [row[self.shape].geometry.geoms[0] for row in cursor]

        # create polygons from edges
        merged_edges = linemerge(shapely_lines)
        polygon_borders = unary_union(merged_edges)
        polygons = polygonize(polygon_borders)

        # create output layer
        output_layer = output_workspace.create_feature_class(output_layer_name, 'Polygon', self.spatial_reference, schema=output_schema)

        # if an attribute layer is provided, add attributes and backup selection
        attributes_selection = attributes_layer.clone_selections() if attributes_layer else None
        if attributes_layer:
            for field in attributes_layer.fields:
                if field.name not in [attributes_layer.oid, attributes_layer.shape]:
                    output_layer.add_field(field.name, field.type)

        # loop through and add polygons and new attributes to layer
        new_rows = []
        for polygon in polygons:
            polygon = Polygon(polygon, self.spatial_reference)
            new_row = {
                output_layer.shape: polygon
            }
            if attributes_layer:
                attributes_layer.select_layer_by_location('WITHIN', polygon)
                with attributes_layer.get_search_cursor(attributes_layer.field_names) as cursor:
                    if len(cursor) > 0:
                        attribute_row = next(cursor)
                        for field in attributes_layer.field_names:
                            new_row[field] = attribute_row[field]
                    else:
                        for field in attributes_layer.field_names:
                            new_row[field] = None
            new_rows.append(new_row)

            # commit to the table every 1000 rows
            if len(new_rows) >= 1000:
                output_layer.add_rows(new_rows)
                new_rows = []

        # commit to the final rows
        if len(new_rows) > 0:
            output_layer.add_rows(new_rows)

        # reapply selection to attribute layer
        if attributes_layer:
            attributes_layer.apply_selections(attributes_selection)

        return output_layer

    def snap(self, snap_environments):
        """ Snaps vertices from layer features to vertices, edges, or end points of other features.

        :param snap_environments: A list of 'snap environments'. Each snap environment is also a list containing three
            parameters: a Layer with the features to snap to, a string representing type of features to snap to
            (END | VERTEX | EDGE), and a string representing distance within which vertices can be snapped.
        """

        # back-up the current selection set in the layer
        current_selections = self.clone_selections()
        selection_type = 'NEW_SELECTION' if len(current_selections) == 0 else 'SUBSET_SELECTION'

        # loop through snap environments and perform snap operations
        for environment in snap_environments:
            # parse out environment properties
            target_layer = environment[0]
            snap_option = environment[1]
            tolerance = string_to_units(environment[2], 'FEET')

            current_target_selections = target_layer.clone_selections()
            target_selection_type = 'NEW_SELECTION' if len(current_target_selections) == 0 else 'SUBSET_SELECTION'

            # find the geometries that are within the tolerance distance of the target geometries and snap them
            self.select_layer_by_location('WITHIN_A_DISTANCE', target_layer, search_distance=tolerance,
                selection_type=selection_type)
            with self.get_update_cursor([self.shape], allow_invalid=True) as update_cursor:
                for row in update_cursor:
                    # find the target that is nearest to the current geometry
                    search_geometry = row[self.shape].boundary if isinstance(row[self.shape], Polygon) else row[self.shape]
                    target_layer.select_layer_by_location('WITHIN_A_DISTANCE', search_geometry, search_distance=tolerance,
                        selection_type=target_selection_type)
                    with target_layer.get_search_cursor([target_layer.shape]) as target_cursor:
                        target_geometries = [target_row[target_layer.shape] for target_row in target_cursor]

                    for target_geometry in target_geometries:
                        if snap_option == 'VERTEX':
                            row[self.shape] = row[self.shape].snap_to_vertex(target_geometry, tolerance, allow_invalid=True)
                        elif snap_option == 'EDGE':
                            row[self.shape] = row[self.shape].snap_to_edge(target_geometry, tolerance, allow_invalid=True, densify=True)
                        else:
                            if not isinstance(target_geometry, Point):
                                first_point_result = row[self.shape].snap_to_vertex(target_geometry.first_point, tolerance, allow_invalid=True)
                                row[self.shape] = first_point_result.snap_to_vertex(target_geometry.last_point, tolerance, allow_invalid=True)
                            else:
                                row[self.shape] = row[self.shape].snap_to_vertex(target_geometry, tolerance, allow_invalid=True)

                    update_cursor.update_row(row)

                    # reapply original selection set to the target layer before exiting loop
                    target_layer.apply_selections(current_target_selections)

        # reapply original selections before exiting
        self.apply_selections(current_selections)

    @property
    def geometry_type(self):
        """
        Returns the type of geometry stored in the layer. Valid values are: 'Polygon', 'Polyline', 'Point',
        'MultiPoint', and 'MultiPatch'.

        :return: A string indicating the type of geometry stored in the layer.
        """
        # if we've already determined the shape field name, just return it
        if self._cached_geometry_type is not None:
            return self._cached_geometry_type
        if self._cached_shape_field is None:
            geometry_columns = self.get_geometry_columns()
            if len(geometry_columns) > 1:
                geometry_columns = list(filter(lambda x: x['name'].upper() == 'GEOM', geometry_columns))
            self._cached_shape_field = geometry_columns.pop()
        if self._cached_shape_field['type'] == 'MULTIPOLYGON' or self._cached_shape_field['type'] == 'POLYGON':
            self._cached_geometry_type = 'Polygon'
        elif self._cached_shape_field['type'] == 'MULTILINESTRING' or self._cached_shape_field['type'] == 'LINESTRING':
            self._cached_geometry_type = 'Polyline'
        else:
            self._cached_geometry_type = 'Point'
        return self._cached_geometry_type

    def clip_to_layer(self, clip_boundary_layer, output_layer_name,
        output_workspace=None, output_schema=None):
        """ Extracts features that overlay the clip features.

        This method creates a new layer containing features clipped from this layer using other features as boundaries.

        :param clip_boundary_layer: The layer containing features used to clip.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        output_workspace = self.workspace if output_workspace is None else output_workspace

        # dissolve the clip boundary layer to remove internal edges
        dissolved_boundary_layer = clip_boundary_layer.dissolve_to_layer('{}_dissolve_temp'.format(output_layer_name),
            output_workspace=output_workspace, output_schema=output_schema)
        return_layer = self.intersect_to_layer(dissolved_boundary_layer, output_layer_name, join_attributes=self.shape, output_schema=output_schema)
        dissolved_boundary_layer.delete()
        return return_layer

    def identity_and_eliminate_to_layer(self, identity_layer, output_layer_name,
        min_area, min_width,
        copy_fields=None,
        flag_fields=None,
        eliminate_slivers=True, output_workspace=None, output_schema=None):
        """ Performs both identity and, if needed, eliminate operations.

        :param identity_layer: The layer object with the geometries that will be used to identity features.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param min_area: The minimum area required to be considered a sliver.
        :param min_width: The minimum width required to be considered a sliver.
        :param primary_lot_lines: The lines layer provided to the Eliminate operation to prevent it from
            eliminating primary lot lines.
        :param copy_fields: The list of tuples matching field names with their new names.
        :param eliminate_slivers: If True, sliver elimination processing will occur.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set up output workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        if copy_fields is None:
            copy_fields = []
        if flag_fields is None:
            flag_fields = []
        identity_layer.select_layer_by_location('INTERSECT', self)
        if identity_layer.get_selection_count() > 0:
            with identity_layer.copy_to_new_table('wic_{0}'.format(get_uuid()), output_workspace=output_workspace, output_schema=output_schema) as identity_copy_layer:
                for field_pair in copy_fields:
                    identity_copy_layer.add_field(field_pair[1], 'TEXT')
                    identity_copy_layer.copy_field_values(field_pair[0], field_pair[1])

                with self.identity_to_layer(
                    identity_layer=identity_copy_layer,
                    join_attributes='NO_FID',
                    output_layer_name='working_post_identity_{0}'.format(self.table_name),
                    min_area=min_area, min_width=min_width, eliminate_slivers=False,
                    output_workspace=output_workspace, output_schema=output_schema) as post_identity_layer:


                    for field_name in flag_fields:
                        if field_name not in post_identity_layer.field_names:
                            post_identity_layer.add_field(field_name, 'SHORT',
                                default_value=0)

                    with identity_copy_layer.get_search_cursor(identity_copy_layer.shape) as id_cursor:
                        for id_row in id_cursor:
                            id_shape = id_row[identity_copy_layer.shape]
                            for field_name in flag_fields:
                                post_identity_layer.select_layer_by_location('INTERSECT', id_shape)
                                with post_identity_layer.get_update_cursor([field_name, post_identity_layer.shape]) as pi_cursor:
                                    for output_row in pi_cursor:
                                        if id_shape.contains(output_row[post_identity_layer.shape].representative_point):
                                            output_row[field_name] = 1
                                            pi_cursor.update_row(output_row)

                    # set any missed flag fields to 0
                    for field_name in flag_fields:
                        post_identity_layer.select_layer_by_attribute('{} IS NULL'.format(field_name))
                        post_identity_layer.calculate_field(field_name, 0)

                    post_identity_layer.clear_selection()
                    topo_corrected_layer = post_identity_layer.correct_topology(
                        output_layer_name='working_ptc_{0}'.format(self.table_name), output_workspace=output_workspace, output_schema=output_schema)

                    if eliminate_slivers and topo_corrected_layer.get_selection_count() > self.get_selection_count():
                        output_layer = topo_corrected_layer.eliminate_slivers_to_layer(
                            output_layer_name=output_layer_name,
                            min_area=min_area,
                            min_width=min_width, output_workspace=output_workspace, output_schema=output_schema)
                    else:
                        output_layer = topo_corrected_layer.copy_to_new_table(
                            output_layer_name=output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
                    topo_corrected_layer.delete()
        else:
            # logging.info('  No identity overlay was performed because no overlay geometries were in the areas.')
            output_layer = self.copy_to_new_table(
                output_layer_name=output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
            for field_pair in copy_fields:
                output_layer.add_field(field_pair[1], 'TEXT')
            for field_name in flag_fields:
                output_layer.add_field(field_name, 'SHORT', default_value=0)

        # clear selection on identity layer
        identity_layer.clear_selection()
        return output_layer

    def drop_search_column(self):
        """ Drops the `edge_buffers` column on the layer if it exists. This can increase performance for operations
        that do not require edge related searches.

        :return: None
        """
        self.workspace.drop_geometry_search_column(self.table_name, schema=self.schema)
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None

    def add_search_column(self):
        """ Add an `edge_buffers` column to the layer. This column assists in performing edge related searches
        such as  `SHARES_A_LINE_SEGMENT_WITH`.

        :return: None
        """
        if 'EDGE_BUFFERS' in self.get_geometry_field_names(include_hidden=True):
            self.drop_search_column()

        if 'edge_buffers' in self.get_geometry_field_names(include_hidden=True):
            spatial_sql = 'ST_Boundary("edge_buffers")' if self.geometry_type == 'Polygon' else '"edge_buffers"'
            spatial_sql = 'ST_Multi(ST_Buffer({}, 0.001, \'endcap=square join=mitre\'))'.format(spatial_sql)
            self.workspace.execute_simple_sql('UPDATE "{0}"."{1}" SET "edge_buffers" = {2}'.format(self.schema, self.table_name, spatial_sql))
            self.vacuum()
        else:
            self.workspace.create_geometry_search_column(self.table_name, self.geometry_type, self.shape, self.spatial_reference, schema=self.schema)
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None

    @property
    def has_search_column(self):
        """ Indicates if the layer has an `edge_buffers` search column.

        :return: True if the layer has a search column, otherwise False.
        """
        return self.workspace.has_geometry_search_column(self.table_name, schema=self.schema)

    def add_centroid_column(self, inside=False):
        """ Adds a `centroid` column to the layer. This column can increase performance for `HAVE_THEIR_CENTER_IN`
        searches.

        :return: None
        """
        if self.has_centroid_column:
            self.drop_centroid_column()

        self.workspace.create_centroid_columm(self.table_name, self.shape, self.spatial_reference, inside, schema=self.schema)
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None


    def drop_centroid_column(self):
        """ Drops the `centroid` column from the layer. This can increase performance for operations that do not
        require `HAVE_THEIR_CENTER_IN` searches.

        :return: None
        """
        self.workspace.drop_centroid_column(self.table_name, schema=self.schema)
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None

    @property
    def has_centroid_column(self):
        """ Indicates if the layer has a `centroid` column.

        :return: True if the layer has a `centroid` column, otherwise False.
        """
        return self.workspace.has_centroid_column(self.table_name, schema=self.schema)

    def add_midpoint_column(self):
        """ Adds a `midpoint` column to the layer.
        searches.

        :return: None
        """
        assert self.geometry_type == 'Polyline', 'Midpoint columns can only be created on line layer.'
        if self.has_midpoint_column:
            self.drop_midpoint_column()

        self.workspace.create_midpoint_columm(self.table_name, self.shape, self.spatial_reference, schema=self.schema)
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None

    def drop_midpoint_column(self):
        """ Drops the `midpoint` column from the layer. This can increase performance for operations that do not
        require `MIDPOINT_NEAR` searches.

        :return: None
        """
        self.workspace.drop_midpoint_column(self.table_name, schema=self.schema)
        self._cached_geometry_columns = None
        self._cached_geometry_columns_reduced = None

    @property
    def has_midpoint_column(self):
        """ Indicates if the layer has a `midpoint` column.

        :return: True if the layer has a `midpoint` column, otherwise False.
        """
        return self.workspace.has_midpoint_column(self.table_name, schema=self.schema)

    def generate_adjacency_table(self, output_table_name, id_field='CBBL',
                                 min_edge_length=0,
                                 output_workspace=None,
                                 output_schema=None):
        """
        Creates a cross-reference table of polygons that are adjacent to other polygons. If an `id_field` value
        is provided, polygons having the same id will be treated as a single polygon in the adjacency analysis.

        Only polygons that have an adjacent edge greater than or equal to the `min_edge_length` value will be
        considered to be adjacent.

        The output table will contain 4 fields:

            * src_id_field (i.e. "cbbl"): The id of the source polygon.
            * nbr_id_field (i.e. "nbr_cbbl"): The id of the neighbor polygon.
            * length: The length of the common edge between the two polygons.
            * node_count: The number of nodes that the two edges have in common.

        :param output_table_name: The name of the output table to be generated.
        :param id_field: The field to use to identify unique polygons in the layer. The default value is `cbbl`.
        :param min_edge_length: The minimum length of the common edge between two polygons for them to be considered
            adjacent. The default value is 0 feet.
        :param output_workspace: The workspace where the output layer will be created.
            If not provided, the layer will be created in the same workspace as the existing layer.
        :return: A `Table` object representing the new table with adjacency data.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        # validate that this is a polygon layer (other layer types are invalid for this operation)
        assert self.geometry_type == 'Polygon', 'Adjacency data can only be generated for polygon layers.'

        # clear selection in the layer
        self.clear_selection()

        # create the output table
        output_table = output_workspace.create_table(output_table_name, schema=output_schema)
        neighbor_id_field = 'nbr_{}'.format(id_field)
        output_table.add_field(id_field, 'TEXT')
        output_table.add_field(neighbor_id_field, 'TEXT')
        output_table.add_field('length', 'DOUBLE')
        output_table.add_field('node_count', 'SHORT')

        # query the ids and geometries from the table
        new_rows = []
        with self.get_search_cursor([id_field, self.shape]) as cursor:
            for search_row in cursor:
                self.clear_selection()

                query_string = "\"{}\" != '{}' AND ST_Intersects(ST_Envelope(\"{}\"), ST_Envelope(ST_GeomFromWKB(DECODE('{}', 'hex'), {})))".format(
                    id_field, search_row[id_field],
                    self.shape, search_row[self.shape].to_postgis(), search_row[self.shape].spatial_reference)

                with self.get_search_cursor([id_field, self.shape], query_string) as neighbor_cursor:
                    for neighbor_row in neighbor_cursor:
                        # if the geometries do not touch skip them
                        if neighbor_row[self.shape].disjoint(search_row[self.shape]):
                            continue

                        # establish a row dictionary
                        new_row = {id_field: search_row[id_field], neighbor_id_field: neighbor_row[id_field]}
                        # get the intersection geometry
                        intersection = neighbor_row[self.shape].intersection(search_row[self.shape])

                        # if the intersection is a point, record a node row
                        if isinstance(intersection, Point):
                            new_row['length'] = 0
                            new_row['node_count'] = 1

                        # if the intersection is a list of points, record a node row
                        if isinstance(intersection, list):
                            new_row['length'] = 0
                            new_row['node_count'] = len(intersection)

                        # if the intersection is a Line, record it's length
                        if isinstance(intersection, Line):
                            new_row['length'] = intersection.length
                            new_row['node_count'] = 0

                        # if the intersection is a polygon, record the length of it's boundary
                        if isinstance(intersection, Polygon):
                            new_row['length'] = intersection.boundary.length
                            new_row['node_count'] = 0

                        # enforce min edge length
                        if min_edge_length > 0 and new_row['length'] < min_edge_length:
                            continue

                        # add the new row, and send the rows to the table every 1000
                        new_rows.append(new_row)
                        if len(new_rows) >= 1000:
                            output_table.add_rows(new_rows)
                            new_rows = []

        # insert any remaining rows
        if len(new_rows) > 0:
            output_table.add_rows(new_rows)

        # return the new table
        return output_table


    def eliminate_slivers_to_layer(self, output_layer_name, min_area, min_width,
                                   output_workspace=None,
                                   output_schema=None):
        """ Eliminates slivers detected based on the minimum area and width inputs.
        :param output_layer_name: The name of the output layer that will contain the processed data.
        :param min_area: The minimum area required to be considered a sliver.
        :param min_width: The minimum width required to be considered a sliver.
        :return: A new layer object that represents the layer containing the results of the process.
        """
        # set the schema if necessary
        output_schema = output_workspace.schema if output_workspace and not output_schema \
            else self.schema if not output_schema else output_schema

        # set the workspace if necessary
        output_workspace = self.workspace if output_workspace is None else output_workspace

        try:
            single_part_layer = self.to_single_part_layer(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
        except:
            # if we can't split the layer into single parts, copy the layer to the output layer and bail out
            # logging.warning('WARNING - could not split %s to a single-part layer. Skipping sliver elimination.',self.table_name)
            return_layer = self.copy_to_new_table(output_layer_name, output_workspace=output_workspace, output_schema=output_schema)
            return_layer.sliver_cbbls = set([])
            return return_layer

        # logging.debug('%s base features.', single_part_layer.count)
        single_part_layer.eliminate_slivers('CBBL', min_area, min_width)
        return single_part_layer


    def eliminate_slivers(self, dissolve_field, area_tolerance, width_tolerance):
        """ Merges sliver polygons into it's neighbors. Neighbors will be grouped by the dissolve field specified
        (usually CBBL).

        :param dissolve_field: The field to use to group records (usually CBBL).
        :param area_tolerance: The threshold for what is considered a sliver based on area.
        :param width_tolerance: The threshold for what is considered a sliver based on width.
        :return: None
        """

        # get a list of cbbls in the layer
        cbbls = [value['CBBL'] for value in self.get_distinct_field_values(dissolve_field)]

        # loop through each lot and eliminate slivers
        for cbbl in cbbls:
            # logging.debug('  Eliminating slivers for lot %s', cbbl)
            # grab the geometries for the lot
            self.select_layer_by_attribute("{} = '{}'".format(dissolve_field, cbbl))
            with self.get_search_cursor([self.oid, self.shape]) as cursor:
                lot_shapes = [{'oid': row[self.oid], 'shape': row[self.shape], 'area': row[self.shape].area, 'is_sliver': row[self.shape].is_sliver(width_tolerance)} for row in cursor]

            # if the lot only has one shape, it cannot be considered for sliver elimination
            # logging.debug('    Total lot shapes: %s', len(lot_shapes))
            if len(lot_shapes) <= 1:
                continue

            # count slivers in the lot and handle special case where all polygons in the lot are slivers
            sliver_shapes = list(filter(lambda x: x['area'] < area_tolerance or x['is_sliver'], lot_shapes))
            # logging.debug('    Total sliver shapes: %s', len(sliver_shapes))
            if len(sliver_shapes) == len(lot_shapes):
                # logging.debug('    Sliver-on-sliver merge detected.')
                # pull out the largest sliver shape and treat it as not-a-sliver
                largest_sliver = None
                for sliver_shape in sliver_shapes:
                    if not largest_sliver or largest_sliver['area'] < sliver_shape['area']:
                        largest_sliver = sliver_shape
                # logging.debug('    Removing largest sliver - area: %s', largest_sliver['area'])
                sliver_shapes.remove(largest_sliver)
                # logging.debug('    New total sliver shapes: %s', len(sliver_shapes))

            # merge slivers
            sliver_oids = [sliver_shape['oid'] for sliver_shape in sliver_shapes]
            for sliver_shape in sliver_shapes:
                # select the portions of the lot that intersect the sliver
                # logging.debug('  Sliver detected: oid %s, area %s, is_sliver %s', sliver_shape['oid'], sliver_shape['area'], sliver_shape['is_sliver'])
                self.select_layer_by_location('INTERSECT', sliver_shape['shape'])
                with self.get_search_cursor([self.oid, self.shape, dissolve_field]) as cursor:
                    adjacent_shapes = [{'oid': row[self.oid], 'shape': row[self.shape], 'dissolve_value': row[dissolve_field]} for row in cursor]
                    adjacent_shapes = list(filter(lambda x: x['oid'] not in sliver_oids and x['dissolve_value'] == cbbl, adjacent_shapes))
                    # logging.debug('      Adjacent shapes detected: %s', len(adjacent_shapes))
                # find the shape to merge the sliver into
                merge_shape = None
                merge_intersections = None
                for adjacent_shape in adjacent_shapes:
                    if merge_shape is None:
                        merge_shape = adjacent_shape
                        merge_intersections = adjacent_shape['shape'].intersection(sliver_shape['shape'])
                    else:
                        adjacent_intersections = adjacent_shape['shape'].intersection(sliver_shape['shape'])

                        # if merge intersections is a line and adjacent intersections is not, keep
                        # the current merge shape
                        if isinstance(merge_intersections, Line) and not isinstance(adjacent_intersections, Line):
                            continue

                        # if the adjacent intersections is a line and the merge intersections are not,
                        # make the merge shape the adjacent shape
                        if isinstance(adjacent_intersections, Line) and not isinstance(merge_intersections, Line):
                            merge_shape = adjacent_shape
                            merge_intersections = adjacent_intersections
                            continue

                        # if we make it here both shape are lines, so take the one with the longest
                        # shared segment with the sliver geometry
                        if isinstance(adjacent_intersections, Line) and isinstance(merge_intersections, Line):
                            if adjacent_intersections.length > merge_intersections.length:
                                merge_shape = adjacent_shape
                                merge_intersections = adjacent_intersections
                                continue

                # if we make it here we should have a merge shape, so do the merge
                if not merge_shape:
                    # logging.warning('WARNING - no merge shape created in sliver elimination for lot %s', cbbl)
                    continue
                # logging.debug('  Selected merge shape: oid %s', merge_shape['oid'])

                # update the geometry we're merging into
                new_shape = merge_shape['shape'].union(sliver_shape['shape'])


                # logging.debug('    Sliver geom: %s', sliver_shape['shape'].wkt)
                # logging.debug('    Merge geom: %s', merge_shape['shape'].wkt)
                # logging.debug('    New geom: %s', new_shape.wkt)
                self.select_layer_by_attribute(merge_shape['oid'])
                with self.get_update_cursor(self.shape) as cursor:
                    for row in cursor:
                        row[self.shape] = new_shape
                        cursor.update_row(row)

                # # update the merged-into geometry in our current loop list
                # for lot_shape in sliver_shapes:
                #     if not lot_shape['oid'] == merge_shape['oid']:
                #         continue
                #     lot_shape['shape'] = new_shape
                #     lot_shape['area'] = new_shape.area
                #     lot_shape['is_sliver'] = new_shape.is_sliver(width_tolerance)
                #     break

                # delete the sliver geometry
                self.select_layer_by_attribute(sliver_shape['oid'])
                self.delete_selected_rows()
                self.clear_selection()
        self.clear_selection()

    # shape field property
    shape = property(fget=get_shape_field)
