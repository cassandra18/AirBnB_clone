import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class."""

    def test_instance_attributes(self):
        """Test that instance attributes are correctly initialized."""
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_attributes(self):
        """Test setting attributes of the Place instance."""
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Cozy Cabin"
        place.description = "A lovely cabin in the woods"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["1", "2", "3"]

        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.description, "A lovely cabin in the woods")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_to_dict(self):
        """Test the to_dict() method of the Place instance."""
        place = Place()
        place.name = "Cottage"
        place_dict = place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], 'Cottage')
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)
        self.assertTrue('id' in place_dict)

    def test_str_representation(self):
        """Test the string representation of the Place instance."""
        place = Place()
        place.name = "Mountain Chalet"
        place_str = str(place)
        self.assertTrue(isinstance(place_str, str))
        self.assertIn("[Place]", place_str)
        self.assertIn(str(place.id), place_str)
        self.assertIn("'name': 'Mountain Chalet'", place_str)

    def test_save(self):
        """Test saving the Place instance and updating the 'updated_at'
        attribute."""
        place = Place()
        place.name = "Beach House"
        place.save()
        self.assertTrue(hasattr(place, 'updated_at'))

    def test_to_dict_with_attributes(self):
        """Test to_dict() method when attributes are set."""
        place = Place()
        place.name = "Luxury Villa"
        place.number_rooms = 5
        place_dict = place.to_dict()
        self.assertEqual(place_dict['name'], 'Luxury Villa')
        self.assertEqual(place_dict['number_rooms'], 5)

    def test_to_dict_with_updated_at(self):
        """Test to_dict() method with updated_at attribute."""
        place = Place()
        place.name = "Mountain Cabin"
        place.save()
        place_dict = place.to_dict()
        self.assertTrue('updated_at' in place_dict)

    def test_empty_description(self):
        """Test an empty description attribute."""
        place = Place()
        place.description = ""
        self.assertEqual(place.description, "")

    def test_negative_values(self):
        """Test setting negative values for numeric attributes."""
        place = Place()
        place.number_rooms = -2
        place.number_bathrooms = -1
        place.max_guest = -4
        place.price_by_night = -100
        self.assertEqual(place.number_rooms, -2)
        self.assertEqual(place.number_bathrooms, -1)
        self.assertEqual(place.max_guest, -4)
        self.assertEqual(place.price_by_night, -100)

    def test_float_values(self):
        """Test setting float values for numeric attributes."""
        place = Place()
        place.latitude = 40.7128
        place.longitude = -74.0060
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)

    def test_empty_amenity_ids(self):
        """Test an empty amenity_ids attribute."""
        place = Place()
        place.amenity_ids = []
        self.assertEqual(place.amenity_ids, [])

    def test_set_amenity_ids(self):
        """Test setting amenity_ids with a list of IDs."""
        place = Place()
        place.amenity_ids = ["1", "2", "3"]
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_non_string_amenity_ids(self):
        """Test setting non-string values in amenity_ids."""
        place = Place()
        place.amenity_ids = [1, 2, 3]
        self.assertEqual(place.amenity_ids, [1, 2, 3])

    def test_negative_float_amenity_ids(self):
        """Test setting negative float values in amenity_ids."""
        place = Place()
        place.amenity_ids = [-1.5, 2.5, -3.5]
        self.assertEqual(place.amenity_ids, [-1.5, 2.5, -3.5])

    def test_non_empty_description(self):
        """Test a non-empty description attribute."""
        place = Place()
        place.description = "A cozy cottage in the woods"
        self.assertEqual(place.description, "A cozy cottage in the woods")


if __name__ == '__main__':
    unittest.main()
