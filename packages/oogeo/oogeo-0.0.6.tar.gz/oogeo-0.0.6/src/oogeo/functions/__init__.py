"""
Contains functions common to all tools.
"""

import logging


def configure_logger(
    log_level='INFO',
    log_file=None,
    log_name='main'):
    """
    Configures the logger based on inputs from the user at the command line.

    :param log_level: The log level to be used by the application. The default value is logging.INFO
    :param log_file: The fully qualified path to a logging file where the logging output will be written.
    """

    # logging format constants
    log_format = '%(asctime)s %(message)s'
    date_format = '%m/%d/%Y %I:%M:%S %p'

    level = getattr(logging, log_level.upper()) if isinstance(log_level, str) else log_level
    # configure logging
    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
    if log_file:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger

def determine_oid_range(arguments):
    """

    """
    return '{0}-{0}'.format(arguments.oid) if arguments.oid else arguments.oid_range

def parse_args_and_configure_logger(argument_parser):
    """

    """
    arguments = argument_parser.parse_args()

    # configure logging
    logger = configure_logger(
        log_level=arguments.log_level.upper(),
        log_file=arguments.log_file)
    return arguments, logger

def add_input_and_output_parameters(argument_parser):
    """ Adds standard input and output arguments to the argument parser.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('-in', '--inputs',
        metavar='Inputs connection',
        dest='inputs_connection',
        default='Inputs',
        help='The connection name from the connections.ini file for the inputs geodatabase.')
    argument_parser.add_argument('-out', '--outputs',
        metavar='Outputs connection',
        dest='outputs_connection',
        default='Processing',
        help='The connection name from the connections.ini file for the outputs geodatabase.')


def add_oid_parameters(argument_parser):
    """ Adds parameters for collecting object ids to process.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('-oids', '--oid_range',
        metavar='Physical Block Object Ids',
        dest='oid_range',
        help='A range of physical block object ids to process. The format is a string with a dash separating the lower '
            'and upper boundaries of the range (ex: "100-200"). The range is inclusive and will include the lower '
            'and upper boundary values in the search.')
    argument_parser.add_argument('-oid', '--oid',
        metavar='Physical Block Object Id',
        dest='oid',
        type=int,
        default=None,
        help='A single physical block object id to process.')

def add_multiprocessing_parameters(argument_parser):
    """ Adds parameters for collecting multiprocessing settings.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('-p', '--processes',
        metavar='Processes',
        dest='processes',
        type=int,
        default=1,
        help='The number of processes to use when running the tool. If not specified one process will be used.')
    argument_parser.add_argument('-d', '--database',
        metavar='Database',
        dest='database',
        help='The preconfigured database to use for processing (should only be used internally when multiprocessing).')
    argument_parser.add_argument('-eo', '--errors_only',
        dest='errors_only',
        action='store_true',
        help='Only creates block outputs for blocks that appear to be missing or corrupt. This option can be used to '
             'restart failed processes when necessary.')


def add_change_input_parameters(argument_parser):
    """ Adds parameters for connecting to and using the changes geodatabase for changes-only processing.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('-cin', '--change_inputs',
        metavar='Change inputs connection',
        dest='change_connection',
        default='Differences',
        help='The connection name from the connections.ini file for the pluto differences geodatabase.')
    argument_parser.add_argument('-co', '--changes_only',
        dest='changes_only',
        action='store_true',
        help='Only processes blocks found in the changed blocks table.')


def add_database_name_parameters(argument_parser):
    """ Adds -id (input database) and -od (output database) to the provided argument parser.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('-id', '--input_database',
        metavar='Input database name',
        dest='input_database',
        default=None,
        help='If specified, the provided database name will override the database name derived from the connections.ini file for the inputs connection (useful for transferring working data).')
    argument_parser.add_argument('-od', '--output_database',
        metavar='Output database name',
        dest='output_database',
        default=None,
        help='If specified, the provided database name will override the database name derived from the connections.ini file for the outputs connection (useful for transferring working data).')


def add_locale_parameters(argument_parser):
    """ Adds -id (input database) and -od (output database) to the provided argument parser.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('locale',
        help='The region to process. Valid values are "NYC", "MIA", or "DC"',
        choices=['NYC', 'MIA', 'DC'])

def add_username_password_parameters(argument_parser):
    """ Adds username and password parameters to the provided argument parser.

    :param argument_parser: The argument parser object to be modified.
    :return: None
    """
    argument_parser.add_argument('-iun', '--input_user_name',
        metavar='Input user name',
        dest='input_user',
        default=None,
        help='If specified, the provided user name will override the user name derived from the connections.ini file for the inputs connection.')
    argument_parser.add_argument('-ipw', '--input_password',
        metavar='Input password',
        dest='input_password',
        default=None,
        help='If specified, the provided password will override the password derived from the connections.ini file for the inputs connection.')
    argument_parser.add_argument('-oun', '--output_user_name',
        metavar='Output user name',
        dest='output_user',
        default=None,
        help='If specified, the provided user name will override the user name derived from the connections.ini file for the outputs connection.')
    argument_parser.add_argument('-opw', '--output_password',
        metavar='Output password',
        dest='output_password',
        default=None,
        help='If specified, the provided password will override the password derived from the connections.ini file for the outputs connection.')



def add_logging_parameters(argument_parser, log_level='INFO'):
    """ Adds log level and log file inputs to the supplied argument parser.

    :param argument_parser: The argument_parser object to add arguments to.
    :param log_level: Configures the default log level for the tool. The default is 'INFO'.
    """
    argument_parser.add_argument('-ll', '--log_level',
        dest='log_level',
        help='Sets the logging level for the application.',
        default=log_level,
        metavar='Log Level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    argument_parser.add_argument('-lf', '--log_file',
        metavar='Log File',
        dest='log_file',
        help='Sets the path to the log file.')
