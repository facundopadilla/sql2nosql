from unittest import TestCase
from sql2nosql import Migrator
from sql2nosql.errors import NoDBClients

"""These tests run on the basis of the docker-compose"""

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
        
        # endregion

    def test_migrate_data(self):
        
        # region -- Migration denied --

        # Empty tables
        try:
            Migrator({}, "mysql.connector", {}, "pymongo").migrate_data()
        except Exception as e:
            self.assertIsInstance(e, TypeError)
        
        # Wrong data type for argument 'tables'
        try:
            Migrator({}, "mysql.connector", {}, 'pymongo').migrate_data(tables=())
        except Exception as e:
            self.assertIsInstance(e, TypeError)
        
        # An empty list
        try:
            Migrator({}, "mysql.connector", {}, 'pymongo').migrate_data(tables=[])
        except Exception as e:
            self.assertIsInstance(e, TypeError)

        # The clients are not connected to a database
        try:
            Migrator({}, "mysql.connector", {}, "pymongo").migrate_data(tables=["example"])
        except Exception as e:
            self.assertIsInstance(e, NoDBClients)
        # endregion

