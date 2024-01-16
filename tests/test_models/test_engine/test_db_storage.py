#!/usr/bin/python3
"""Test module for db storage"""

import unittest
from models import storage
from os import getenv
import MySQLdb
from models.user import User
from models.place import Place


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'reason')
class TestDBStorage(unittest.TestCase):
    """Test DB storage"""

    @classmethod
    def setUpClass(cls):
        """Set up the class for testing
        runs one time at the beginning of the testing"""
        cls.engine = MySQLdb.connect(
                host=getenv('HBNB_MYSQL_HOST'),
                user=getenv('HBNB_MYSQL_USER'),
                passwd=getenv('HBNB_MYSQL_PWD'),
                db=getenv('HBNB_MYSQL_DB'))
        cls.cursor = cls.engine.cursor()
        cls.cursor.execute("SHOW TABLES")
        tables = cls.cursor.fetchall()
        cls.tables_before = set(table[0] for table in tables)

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after testing
        runs one time when all tests finish to clean up any changes
        made in DB by the tests after they have been executed"""
        cls.cursor.execute("SHOW TABLES")
        tables = cls.cursor.fetchall()
        tables_after = set(table[0] for table in tables)
        for table in tables_after - cls.tables_before:
            cls.cursor.execute(f"DROP TABLE {table}")
        cls.cursor.close()
        cls.engine.close()

    def setUp(self):
        """Set up for each test"""
        self.storage = storage

    def tearDown(self):
        """Tear down for each test"""
        pass

    def test_all(self):
        """Test the all method"""
        pass

    def test_new(self):
        """Test the new method"""
        user = User(first_name="Sherif",
                    last_name="Hamdy",
                    email="s.h@mail.com",
                    password="secured_pass")

        self.storage.new(user)
        self.storage.save()
        res = self.storage.all(User)
        print(res)
        self.assertIn("User.{}".format(user.id), res)

    def test_save(self):
        """Test the save method"""
        pass

    def test_delete(self):
        """Test the delete method"""
        pass

    def test_reload(self):
        """Test the reload method"""
        pass


if __name__ == '__main__':
    unittest.main()
