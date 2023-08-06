# coding=utf-8
"""
Runs the unit tests in this directory.
"""

import argparse
import sys
import unittest
from src.oogeo.unittests.layertest import LayerClassUnitTests
from src.oogeo.unittests.linetest import LineClassUnitTests
from src.oogeo.unittests.pointtest import PointClassUnitTests
from src.oogeo.unittests.polygontest import PolygonClassUnitTests
from src.oogeo.unittests.tabletest import TableClassUnitTests
from src.oogeo.unittests.utilstest import UtilsUnitTests
from src.oogeo.unittests.workspacetest import WorkspaceClassUnitTests

from src.oogeo.functions import add_logging_parameters, parse_args_and_configure_logger

def run_tests(test_suite, test_case=None):
    """ Runs the unit tests specified in the tool parameters, or all tests if no options are provided.

    :param test_suite: The name of the test suite to execute, or None to execute all test suites.
    :param test_case: The name of the test case within the test suite to execute. If not provided,
        all tests in the test suite will be executed.
    """

    run_suites = []
    if test_suite is not None:
        if test_suite == 'LayerClass':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(LayerClassUnitTests))
            else:
                run_suites.append(LayerClassUnitTests(test_case))
        elif test_suite == 'PointClass':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(PointClassUnitTests))
            else:
                run_suites.append(PointClassUnitTests(test_case))
        elif test_suite == 'LineClass':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(LineClassUnitTests))
            else:
                run_suites.append(LineClassUnitTests(test_case))
        elif test_suite == 'WorkspaceClass':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(WorkspaceClassUnitTests))
            else:
                run_suites.append(WorkspaceClassUnitTests(test_case))
        elif test_suite == 'TableClass':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(TableClassUnitTests))
            else:
                run_suites.append(TableClassUnitTests(test_case))
        elif test_suite == 'PolygonClass':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(PolygonClassUnitTests))
            else:
                run_suites.append(PolygonClassUnitTests(test_case))
        elif test_suite == 'Utilities':
            if not test_case:
                run_suites.append(unittest.TestLoader().loadTestsFromTestCase(UtilsUnitTests))
            else:
                run_suites.append(UtilsUnitTests(test_case))
        elif test_suite == 'API':
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(UtilsUnitTests))
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(PointClassUnitTests))
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(LineClassUnitTests))
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(PolygonClassUnitTests))
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(WorkspaceClassUnitTests))
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(TableClassUnitTests))
            run_suites.append(unittest.TestLoader().loadTestsFromTestCase(LayerClassUnitTests))

    else:
        # run all suites
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(UtilsUnitTests))
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(PointClassUnitTests))
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(LineClassUnitTests))
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(PolygonClassUnitTests))
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(WorkspaceClassUnitTests))
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(TableClassUnitTests))
        run_suites.append(unittest.TestLoader().loadTestsFromTestCase(LayerClassUnitTests))

    suite = unittest.TestSuite(run_suites)
    results = unittest.TextTestRunner(verbosity=2).run(suite)
    if not results.wasSuccessful():
        sys.exit(1)

# if running from a command line, gather command line args and call run_tests
if __name__ == '__main__':

    # get incoming script arguments
    argument_parser = argparse.ArgumentParser(
        description='Runs the unit tests for the GIS processing application.'
    )
    # add test suite argument
    argument_parser.add_argument('-ts', '--test_suite',
        dest='test_suite',
        help='The name of test suite to execute. If no test suite is provided, all tests will be executed. Valid '
             'values are: "API", "LayerClass", "TableClass", "WorkspaceClass", "PolygonClass", "LineClass", "PointClass", "Utilities"',
        default=None,
        metavar='Test Suites',
        choices=['API', 'LayerClass', 'TableClass', 'WorkspaceClass', 'PolygonClass', 'LineClass', 'Utilities', 'PointClass'])
    argument_parser.add_argument('-tc', '--test_case',
        dest='test_case',
        help='If specified, runs a specific test case within a test suite. The text must match the name of the test '
             'function exactly (i.e. "test_block_MN_362"). Ignored when multiple suites are run simultaneously',
        default=None,
        metavar='Test Case')

    add_logging_parameters(argument_parser, log_level='ERROR')

    arguments, logger = parse_args_and_configure_logger(argument_parser)

    # run the test
    run_tests(arguments.test_suite, arguments.test_case)
