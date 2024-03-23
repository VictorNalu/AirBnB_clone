#!/usr/bin/python3
"""Unit tests for User class"""

import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test suite for User class."""

    def test_user_creation(self):
        """Test User object creation."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_to_dict(self):
        """Test User object to_dict method."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
