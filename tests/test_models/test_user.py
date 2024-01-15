#!/usr/bin/python3
"""Test module for the User class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_User(test_basemodel):
    """Test class for User"""

    def setUp(self):
        """Set up for test"""
        super().setUp()
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test the first_name attribute of User"""
        new = self.value(first_name="John")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test the last_name attribute of User"""
        new = self.value(last_name="Doe")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test the email attribute of User"""
        new = self.value(email="sherif.h@example.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test the password attribute of User"""
        new = self.value(password="I_am_a_secure_password")
        self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()
