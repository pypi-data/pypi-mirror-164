"""
This module contains generic functions that support unit testing.
"""
import configparser

from os import path

temp_tables = [
    'create_point_test',
    'create_line_test',
    'create_polygon_test',
    'create_table_test',
    'duplicated_table_test',
    'copy_table_test',
    'layer_calc_field_test',
    'layer_calc_field_test_2',
    'single_shape_test',
    'lines_selection_test_1',
    'lines_selection_test_2',
    'add_column_test',
    'duplicated_layer_test',
    'test_copy',
    'identity_test',
    'intersect_test',
    'intersect_point_test',
    'intersect_line_test',
    'intersect_point_test_2',
    'clipped_layer_test',
    'vertices_to_points_test',
    'unique_shapes_test',
    'feature_to_points_test',
    'feature_to_points_inside_test',
    'copy_layer_test',
    'converted_table_test',
    'mbr_layer_test',
    'mbr_layer_2_test',
    'buffer_layer_test',
    'dissolve_layer_test',
    'dissolve_layer_2_test',
    'dissolve_layer_3_test',
    'dissolve_layer_4_test',
    'dissolve_layer_5_test',
    'dissolve_layer_6_test',
    'temp_lines_test',
    'temp_lines_dissolved_test',
    'split_lines_test',
    'unsplit_lines_test',
    'dissolve_lines_test',
    'near_layer_test',
    'snap_targets_test',
    'snap_lines_test',
    'lines_to_split_test',
    'split_points_test',
    'dissolve_lines_test',
    'lines_split_at_points_test',
    'merged_layer_test',
    'merge_copy_layer_test',
    'merged_layers_to_layer_test',
    'single_part_layer_test',
    'multi_part_layer_test',
    'lines_layer_test',
    'label_centroids_test',
    'remade_polygon_layer_test',
    'adjacency_table_test',
]


def get_ini_file():
    """
    Retrieves the path to the `unittest.ini` file.
    :return: The correct path to the `unittest.ini` file.
    """
    return path.join(path.dirname(path.realpath(__file__)), 'unittest.ini')


def get_configurations():
    """
    Retrieves the configuration settings from the `unittest.ini` file.
    :return: A `ConfigParser` object with the configuration from the `unittest.ini` file.
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(get_ini_file())
    return config_parser


def get_packages_directory():
    # find the packages directory
    unittest_root = path.abspath(path.dirname(__file__))
    code_root = path.dirname(unittest_root)
    return path.dirname(code_root)


def verify_edges(test_lines, target_points):
    """ Counts the number of lines that begin and end at the provided set of test points and returns it to the caller.
    This can be used to verify that an expected set of edges are within a collection of lines.

    :param test_lines: The set of `Line()` objects to evaluate.
    :param target_points: The set of points where lines are expected to begin and end.
    :return: The number of test lines that begin and end at the specified target points.
    """
    correct_edges = []
    for line in test_lines:
        start_point = {'x': line.first_point.x, 'y': line.first_point.y}
        end_point = {'x': line.last_point.x, 'y': line.last_point.y}
        if start_point in target_points and end_point in target_points:
            correct_edges.append(line)
    return len(correct_edges)
