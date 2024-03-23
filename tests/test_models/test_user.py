#!/usr/bin/python3
"""Unit tests for User class"""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up a User instance before each test.
        """
        self.user = User()

    def test_attributes(self):
        """
        Test the existence of attributes.
        """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attribute_defaults(self):
        """
        Test default attribute values.
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.
        """
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test the type of the 'updated_at' attribute.
        """
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the User instance.
        """
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the User class.
        """
        obj_dict = self.user.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict["__class__"], "User")
        self.assertTrue("id" in obj_dict)
        self.assertTrue("created_at" in obj_dict)
        self.assertTrue("updated_at" in obj_dict)
        self.assertTrue("email" in obj_dict)
        self.assertTrue("password" in obj_dict)
        self.assertTrue("first_name" in obj_dict)
        self.assertTrue("last_name" in obj_dict)


if __name__ == "__main__":
    unittest.main()
