#!/usr/bin/python3
"""Test for City class"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a City instance before each test.
        """
        self.city = City()

    def test_attributes(self):
        """
        Test the existence of attributes.
        """
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attribute_defaults(self):
        """
        Test default attribute values.
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.
        """
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test the type of the 'updated_at' attribute.
        """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the City instance.
        """
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__
        )
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the City class.
        """
        obj_dict = City()
        self.assertTrue("id" in obj_dict.__dir__())
        self.assertTrue("created_at" in obj_dict.__dir__())
        self.assertTrue("updated_at" in obj_dict.__dir__())
        self.assertTrue("state_id" in obj_dict.__dir__())
        self.assertTrue("name" in obj_dict.__dir__())


if __name__ == "__main__":
    unittest.main()
