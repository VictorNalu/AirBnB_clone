import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up a Place instance before each test.
        """
        self.place = Place()

    def test_attributes(self):
        """
        Test the existence of attributes.
        """
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_attribute_defaults(self):
        """
        Test default attribute values.
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.
        """
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test the type of the 'updated_at' attribute.
        """
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the Place instance.
        """
        expected_str = "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__
        )
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the Place class.
        """
        obj_dict = Place()
        self.assertTrue("id" in obj_dict.__dir__())
        self.assertTrue("created_at" in obj_dict.__dir__())
        self.assertTrue("updated_at" in obj_dict.__dir__())
        self.assertTrue("city_id" in obj_dict.__dir__())
        self.assertTrue("user_id" in obj_dict.__dir__())
        self.assertTrue("name" in obj_dict.__dir__())
        self.assertTrue("description" in obj_dict.__dir__())
        self.assertTrue("number_rooms" in obj_dict.__dir__())
        self.assertTrue("number_bathrooms" in obj_dict.__dir__())
        self.assertTrue("max_guest" in obj_dict.__dir__())
        self.assertTrue("price_by_night" in obj_dict.__dir__())
        self.assertTrue("latitude" in obj_dict.__dir__())
        self.assertTrue("longitude" in obj_dict.__dir__())
        self.assertTrue("amenity_ids" in obj_dict.__dir__())


if __name__ == "__main__":
    unittest.main()
