#!/usr/bin/python3
"""Test for BaseModelClass"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_attributes(self):
        """Test the existence of attributes."""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_attribute_defaults(self):
        """Test default attribute values."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of the BaseModel instance."""
        obj = BaseModel()
        class_name = obj.__class__.__name__
        expected_str = "[{}] ({}) {}".format(class_name, obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Test the save method."""
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn("__class__", obj_dict)
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

    def test_to_dict_created_at_format(self):
        """Test the format of created_at in the to_dict method."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        created_at = obj_dict["created_at"]
        self.assertEqual(datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f"),
                         obj.created_at)

    def test_to_dict_updated_at_format(self):
        """Test the format of updated_at in the to_dict method."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        updated_at = obj_dict["updated_at"]
        self.assertEqual(datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f"),
                         obj.updated_at)


if __name__ == "__main__":
    unittest.main()
