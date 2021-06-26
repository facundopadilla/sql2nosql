from unittest import TestCase
from sql2nosql import Migrator
from sql2nosql.errors import NoDBClients
from .utils import powerset_dict

from copy import deepcopy
from typing import List, Dict, Any

"""
These tests are "designed" to work without real connection tests (therefore, there are no success cases).
If you want to run the tests to verify, you will need to install the dependencies it uses:

pip install mysql-connector-python pymysql pymongo

"""


class TestSQL2NoSQL(TestCase):
    def test_migrator(self):
        # region -- Erroneous arguments --

        # Empty arguments
        try:
            Migrator()
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # Bad arguments
        try:
            Migrator(None, None, None, None)
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # Arguments that pass but are wrong anyway.
        try:
            Migrator({}, "", {}, "")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        try:
            Migrator([], "", [], "")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # The string arguments doesn't implementeds
        try:
            Migrator({}, "example", {}, "example")
        except Exception as e:
            self.assertIsInstance(e, NotImplementedError)

        # Bad connection
        fake_connection = {
            "host": "FakeHost",
            "port": 1234,
            "username": "FakeUsername",
            "password": "FakePassword",
            "database": "FakeDatabase",
        }
        list_powerdict: List[Dict[str, Any]] = powerset_dict(fake_connection)

        # Trying with mysql.connector
        from mysql.connector.errors import DatabaseError

        for _dict in list_powerdict:
            try:
                Migrator(_dict, "mysql.connector", {}, "example")
            except Exception as e:
                self.assertIsInstance(e, DatabaseError)

        # Trying with pymysql
        from pymysql.err import OperationalError

        for _dict in deepcopy(list_powerdict):
            try:
                Migrator(_dict, "pymysql", {}, "example")
            except Exception as e:
                self.assertIsInstance(e, OperationalError)

        # Trying with PyMongo
        from pymongo.errors import ConfigurationError

        for _dict in list_powerdict:
            try:
                Migrator({}, "example", _dict, "pymongo")
            except Exception as e:
                self.assertIsInstance(e, ConfigurationError)

    def test_migrate_data(self):

        # region -- Migration denied --

        # Empty tables
        try:
            Migrator({}, "mysql.connector", {}, "pymongo").migrate_data()
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # Wrong data type for argument 'tables'
        try:
            Migrator({}, "mysql.connector", {}, "pymongo").migrate_data(tables=())
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # An empty list
        try:
            Migrator({}, "mysql.connector", {}, "pymongo").migrate_data(tables=[])
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # The clients are not connected to a database
        try:
            Migrator({}, "mysql.connector", {}, "pymongo").migrate_data(
                tables=["example"]
            )
        except Exception as e:
            self.assertIsInstance(e, NoDBClients)
        # endregion
