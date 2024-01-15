#!/usr/bin/python3
"""Test module for the State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """Test class for State"""

    def setUp(self):
        """Set up for test"""
        super().setUp()
        self.name = "State"
        self.value = State

    def test_state_name(self):
        """Test the name attribute of State"""
        new = self.value(name='name')
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
