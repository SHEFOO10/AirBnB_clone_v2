#!/usr/bin/python3
"""Test module for the Place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test class for Place"""

    def setUp(self):
        """Set up for test"""
        super().setUp()
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test the city_id attribute of Place"""
        new = self.value(city_id="some_city_id")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test the user_id attribute of Place"""
        new = self.value(user_id="some_user_id")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test the name attribute of Place"""
        new = self.value(name="some_name")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test the description attribute of Place"""
        new = self.value(description="some_description")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test the number_rooms attribute of Place"""
        new = self.value(number_rooms=5)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test the number_bathrooms attribute of Place"""
        new = self.value(number_bathrooms=3)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test the max_guest attribute of Place"""
        new = self.value(max_guest=8)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test the price_by_night attribute of Place"""
        new = self.value(price_by_night=100)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test the latitude attribute of Place"""
        new = self.value(latitude=40.7128)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test the longitude attribute of Place"""
        new = self.value(longitude=-74.0060)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test the amenity_ids attribute of Place"""
        new = self.value(amenity_ids=["amenity1", "amenity2"])
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
