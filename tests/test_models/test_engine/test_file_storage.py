#!/usr/bin/python3
"""Testing the file_storage module"""

import unittest
import os
import time
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        # Create a FileStorage instance for each test
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up the test environment."""
        # Remove the file created during the tests, if it exists
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save_and_reload(self):
        """Test saving and reloading objects using FileStorage."""
        # Create two BaseModel instances
        model1 = BaseModel()
        model2 = BaseModel()

        # Add the BaseModel instances to the FileStorage and save
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.save()

        # Clear the FileStorage and reload from the file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        # Verify that the objects were reloaded correctly
        self.assertEqual(len(self.storage.all()), 2)
        self.assertIn("BaseModel." + model1.id, self.storage.all())
        self.assertIn("BaseModel." + model2.id, self.storage.all())


if __name__ == "__main__":
    unittest.main()
