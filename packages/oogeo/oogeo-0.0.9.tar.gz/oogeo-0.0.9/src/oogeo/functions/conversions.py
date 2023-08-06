"""
Common functions for parsing well-known string formats.
"""

import re

from pint import UnitRegistry
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon as ShapelyMultiPolygon, \
    LineString as ShapelyLineString, MultiLineString as ShapelyMultiLineString
from shapely.wkt import loads as wkt_to_geom

CONVERSION_UNITS = [
    'MILLIMETERS',
    'CENTIMETERS',
    'METERS',
    'KILOMETERS',
    'INCHES',
    'FEET',
    'MILES',
]


def string_to_units(measurement_string, default_units):
    """ Parses a measurement string and converts it to map units. Currently only supports feet and meters,
    but could be expanded in the future.

    :param measurement_string: The measurement string (i.e. '100 FEET')
    :param default_units: The units of the base map (i.e. 'FEET')
    :return: A decimal representing the parsed measurement in map units.
    """
    measurements = measurement_string.split(' ')
    value = float(measurements[0])
    measure_units = measurements[1].upper()

    if 'FOOT' in measure_units or 'FEET' in measure_units:
        measure_units = 'FEET'
    elif 'METER' in measure_units:
        measure_units = 'METERS'

    # if the measure and map units match, return the unadjusted value
    if measure_units == default_units:
        return value

    # handle feet to meters
    if measure_units == 'FEET':
        return value * 0.3048

    # handle meters to feet
    return value * 3.28084

    # TODO: convert to use measurements library (code below)
    # # handle meters to feet
    # if measure_units == 'FEET':
    #     distance = Distance(ft=value)
    #     return distance.m
    #
    # # handle meters to feet
    # distance = Distance(m=value)
    # return distance.ft


def parse_expression(table, field, expression):
    """ Parses esri-style query strings and returns a string that can be injected into SQL.

    :param table: The `Table()` object being updated.
    :param field: The field in the specified table to be updated.
    :param expression: The expression to be evaluated.
    :return: A string that can replace the expression in an SQL statement.
    """

    # return NULL if expression is None
    if expression is None or (isinstance(expression, str) and expression.upper() == 'NULL'):
        return 'NULL'

    # if the expression is not a string, simply return the value
    if not isinstance(expression, str):
        return expression

    # replace field names (bounded by exclamation marks) with SQL-formatted field names
    if expression.count('!') > 0:
        # check for not operator
        if not (expression.count('!=') == 1 and expression.count('!') == 1):
            # check for special case expressions involving shape or oid
            if '!shape.area@squarefeet!' in expression.lower():
                return 'ST_Area("{}")'.format(table.shape)

            # parse out the field name and replace it
            regex_return = re.search('!(.+?)!', expression)
            if regex_return:
                field_name = regex_return.group(1)
                expression = expression.replace('!{}!'.format(field_name), '"{}"'.format(field_name))
    elif 'VARCHAR' in table.get_field_type(field) \
            and not expression.upper().startswith('CASE WHEN') \
            and not expression.upper().startswith('CONCAT') \
            and not expression.upper().startswith('TRIM'):
        # first strip off any surrounding single quotes
        expression = expression.strip()
        expression = expression.strip("'")

        # now escape any unescaped quotes in the string
        if expression.count("'") > 0 and expression.count("''") == 0:
            expression = expression.replace("'", "''")

        # now replace the leading and trailing quotes
        expression = "'{}'".format(expression)

    return expression


def upgrade_shapely_geometry(geometry):
    """

    :param geometry:
    :return:
    """

    rounded_geometry = wkt_to_geom(geometry.wkt)

    return None if not rounded_geometry or rounded_geometry.is_empty \
        else ShapelyMultiPolygon([rounded_geometry]) if isinstance(rounded_geometry, ShapelyPolygon) \
        else ShapelyMultiLineString([rounded_geometry]) if isinstance(rounded_geometry, ShapelyLineString) else rounded_geometry

    ## NOTE: Code below contains an early attempt to clean geometries coming out of Geopandas
    # # if the geometry is multi-part, loop through it's parts and filter out invalid pieces
    # # due to issue w/ geopandas. See https://github.com/geopandas/geopandas/issues/756 for more info.
    # if isinstance(geometry, ShapelyMultiPolygon):
    #     test_polygon = wkt_to_geom(geometry.wkt)
    #     if not test_polygon.is_valid:
    #         clean_polygons = list(filter(lambda x: x.is_valid, test_polygon.geoms))
    #         geometry = ShapelyMultiPolygon(clean_polygons)
    # if isinstance(geometry, ShapelyMultiLineString):
    #     test_line = wkt_to_geom(geometry.wkt)
    #     if not test_line.is_valid:
    #         clean_lines = list(filter(lambda x: x.is_valid, test_line.geoms))
    #         geometry = ShapelyMultiLineString(clean_lines)
    #
    # return ShapelyMultiPolygon([geometry]) if isinstance(geometry, ShapelyPolygon) \
    #     else ShapelyMultiLineString([geometry]) if isinstance(geometry, ShapelyLineString) else geometry


def get_conversion_factor(from_units, to_units):
    """ Returns the conversion factor for converting numbers from one unit to another.

    :param from_units: A string representing the units to be converted from. Valid values are
        "INCHES", "FEET", "MILES", "MILLIMETERS", "CENTIMETERS", "METERS", "KILOMETERS".
    :param to_units: A string representing the units to be converted to. Valid values are
        "INCHES", "FEET", "MILES", "MILLIMETERS", "CENTIMETERS", "METERS", "KILOMETERS".
    :return: A number representing the conversion factor between the from and to units. This
        number can be used as a multiplier to convert any value between the specified units.
    """
    # insure that the units are upper-case
    from_units = from_units.upper()
    to_units = to_units.upper()

    # establish a unit registry in the "from" units
    ureg = UnitRegistry()
    from_reg = None
    if from_units in ['IN', 'INCH', 'INCHES']:
        from_reg = 1 * ureg.inch
    elif from_units in ['FT', 'FOOT', 'FEET']:
        from_reg = 1 * ureg.foot
    elif from_units in ['MI', 'MILE', 'MILES']:
        from_reg = 1 * ureg.mile
    elif from_units in ['MM', 'MILLIMETER', 'MILLIMETERS']:
        from_reg = 1 * ureg.millimeter
    elif from_units in ['CM', 'CENTIMETER', 'CENTIMETERS']:
        from_reg = 1 * ureg.centimeter
    elif from_units in ['M', 'METER', 'METERS']:
        from_reg = 1 * ureg.meter
    elif from_units in ['KM', 'KILOMETER', 'KILOMETERS']:
        from_reg = 1 * ureg.kilometer

    assert from_reg, 'From unit {} not found'.format(from_units)

    # return the conversion units or raise an error
    # if the to units are not specified correctly
    if to_units in ['IN', 'INCH', 'INCHES']:
        return from_reg.to(ureg.inch).magnitude
    elif to_units in ['FT', 'FOOT', 'FEET']:
        return from_reg.to(ureg.foot).magnitude
    elif to_units in ['MI', 'MILE', 'MILES']:
        return from_reg.to(ureg.mile).magnitude
    elif to_units in ['MM', 'MILLIMETER', 'MILLIMETERS']:
        return from_reg.to(ureg.millimeter).magnitude
    elif to_units in ['CM', 'CENTIMETER', 'CENTIMETERS']:
        return from_reg.to(ureg.centimeter).magnitude
    elif to_units in ['M', 'METER', 'METERS']:
        return from_reg.to(ureg.meter).magnitude
    elif to_units in ['KM', 'KILOMETER', 'KILOMETERS']:
        return from_reg.to(ureg.kilometer).magnitude
    raise ValueError('To unit {} not found'.format(to_units))
