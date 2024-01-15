#!/usr/bin/python3
"""Testing city class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(test_basemodel):
    """Test class for City"""

    def setUp(self):
        """Set up for test"""
        super().setUp()
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the state_id attribute of City"""
        new = self.value(state_id="some_state_id")
        self.assertIsNotNone(new.state_id)
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the name attribute of City"""
        new = self.value(name="some_name")
        self.assertIsNotNone(new.name)
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
