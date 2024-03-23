#!/usr/bin/python3
"""Unittest for AmenityClass"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up an Amenity instance before each test.
        """
        self.amenity = Amenity()

    def test_attributes(self):
        """
        Test the existence of attributes.
        """
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attribute_defaults(self):
        """
        Test default attribute values.
        """
        self.assertEqual(self.amenity.name, "")

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.
        """
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test the type of the 'updated_at' attribute.
        """
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the Amenity instance.
        """
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__
        )
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the Amenity class.
        """
        obj_dict = Amenity()
        self.assertTrue("id" in obj_dict.__dir__())
        self.assertTrue("created_at" in obj_dict.__dir__())
        self.assertTrue("updated_at" in obj_dict.__dir__())
        self.assertTrue("name" in obj_dict.__dir__())


if __name__ == "__main__":
    unittest.main()
