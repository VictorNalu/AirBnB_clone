import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up a State instance before each test.
        """
        self.state = State()

    def test_attributes(self):
        """
        Test the existence of attributes.
        """
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))

    def test_attribute_defaults(self):
        """
        Test default attribute values.
        """
        self.assertEqual(self.state.name, "")

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.
        """
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test the type of the 'updated_at' attribute.
        """
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the State instance.
        """
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__
        )
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the State class.
        """
        obj_dict = State()
        self.assertTrue("id" in obj_dict.__dir__())
        self.assertTrue("created_at" in obj_dict.__dir__())
        self.assertTrue("updated_at" in obj_dict.__dir__())
        self.assertTrue("name" in obj_dict.__dir__())


if __name__ == "__main__":
    unittest.main()
