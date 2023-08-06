"""
Base class for all test fixtures that require a file geodatabase for testing. The base class will establish
file geodatabases in a working directory based on the configurations found in the
[`unittest.ini`](https://github.com/envelopecity/GIS/blob/dev/envelopegis/unittest/unittest.ini) file, and will
provide links to these databases to its inheritors.

"""

import json
import unittest

from src.oogeo.objects.workspace import Workspace
from src.oogeo.unittests.utilities import get_configurations, temp_tables


def clean_database(database_config):
    Workspace.drop_geodatabase(database_config, 'test_geodatabase')
    workspace = Workspace(database_config)
    feature_classes = workspace.list_feature_classes()
    tables = workspace.list_tables()
    for table in temp_tables:
        if table in feature_classes or table in tables:
            workspace.delete_feature_classes(table)


class DatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # get the configurations
        cls._configurations = get_configurations()

        # grab the databases provide links that can be used by the test fixtures
        cls._databases = {}
        database_configs = cls._configurations.options('Databases')
        for database in database_configs:
            cls._databases[database] = json.loads(cls._configurations.get('Databases', database))
            clean_database(cls._databases[database])
