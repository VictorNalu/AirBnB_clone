#!/usr/bin/python3
"""Test for Review Class"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up a Review instance before each test.
        """
        self.review = Review()

    def test_attributes(self):
        """
        Test the existence of attributes.
        """
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attribute_defaults(self):
        """
        Test default attribute values.
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.
        """
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test the type of the 'updated_at' attribute.
        """
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the Review instance.
        """
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__
        )
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the Review class.
        """
        obj_dict = Review()
        self.assertTrue("id" in obj_dict.__dir__())
        self.assertTrue("created_at" in obj_dict.__dir__())
        self.assertTrue("updated_at" in obj_dict.__dir__())
        self.assertTrue("place_id" in obj_dict.__dir__())
        self.assertTrue("user_id" in obj_dict.__dir__())
        self.assertTrue("text" in obj_dict.__dir__())


if __name__ == "__main__":
    unittest.main()
