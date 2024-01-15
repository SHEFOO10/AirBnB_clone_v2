#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """testing basemodel"""

    def tearDown(self):
        """Remove the 'file.json' if it exists"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test creating an instance of BaseModel with default values"""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Test creating an instance of BaseModel with kwargs"""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test creating an instance of BaseModel with kwargs
        containing an int"""
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        i = BaseModel()
        self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(i.id,
                         i.__dict__))

    def test_todict(self):
        """Test the to_dict method of BaseModel"""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test creating an instance of BaseModel with kwargs=None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """Test creating an instance of BaseModel with one key in kwargs"""
        n = {'Name': 'test'}
        new = BaseModel(**n)
        self.assertTrue(hasattr(new, 'Name'))
        self.assertEqual(new.Name, 'test')

    def test_id(self):
        """Test the id attribute of BaseModel"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the created_at attribute of BaseModel"""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test the updated_at attribute of BaseModel"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == '__main__':
    unittest.main()
