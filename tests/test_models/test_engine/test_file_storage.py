#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save_and_reload(self):
        """Test saving and reloading objects using FileStorage."""
        model1 = BaseModel()
        model2 = BaseModel()
        user1 = User()
        user2 = User()
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()

        self.assertIn("BaseModel." + model1.id, self.storage.all())
        self.assertIn("BaseModel." + model2.id, self.storage.all())
        self.assertIn("User." + user1.id, self.storage.all())
        self.assertIn("User." + user2.id, self.storage.all())


if __name__ == "__main__":
    unittest.main()
