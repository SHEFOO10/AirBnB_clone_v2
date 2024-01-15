#!/usr/bin/python3
""""""

import unittest
from models import storage
from os import getenv


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'reason')
class TestDBStorage(unittest.TestCase):
    def test_skip(self):
        print("not skipped then Iam a database")


if __name__ == '__name__':
    unittest.main()
