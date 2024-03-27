#!/usr/bin/python3
"""FileStorage module"""
import unittest
import os
import json
from models.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up method to reset FileStorage class attributes."""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down method to remove created files after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method."""
        obj = BaseModel()
        fs = FileStorage()
        fs.new(obj)
        self.assertEqual(
            fs.all(),
            {"BaseModel.{}".format(obj.id): obj}
        )

    def test_new(self):
        """Test new method."""
        obj = BaseModel()
        fs = FileStorage()
        fs.new(obj)
        self.assertEqual(
            fs.all(),
            {"BaseModel.{}".format(obj.id): obj}
        )

    def test_save_reload(self):
        """Test save and reload methods."""
        obj = BaseModel()
        fs = FileStorage()
        fs.new(obj)
        fs.save()
        fs2 = FileStorage()
        fs2.reload()
        self.assertEqual(
            fs2.all(),
            fs.all()
        )

    def test_reload_no_file(self):
        """Test reload method when file doesn't exist."""
        fs = FileStorage()
        fs.reload()
        self.assertEqual(
            fs.all(),
            {}
        )


if __name__ == '__main__':
    unittest.main()
