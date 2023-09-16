import unittest
import json
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def test_instance_attributes(self):
        """Test that instance attributes are correctly initialized."""
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_set_attributes(self):
        """Test setting attributes of the City instance."""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_to_dict(self):
        """Test the to_dict() method of the City instance."""
        city = City()
        city.state_id = "NY"
        city.name = "New York City"
        city_dict = city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], 'NY')
        self.assertEqual(city_dict['name'], 'New York City')
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)
        self.assertTrue('id' in city_dict)

    def test_str_representation(self):
        """Test the string representation of the City instance."""
        city = City()
        city.state_id = "IL"
        city.name = "Chicago"
        city_str = str(city)
        self.assertTrue(isinstance(city_str, str))
        self.assertIn("[City]", city_str)
        self.assertIn(str(city.id), city_str)
        self.assertIn("'state_id': 'IL'", city_str)
        self.assertIn("'name': 'Chicago'", city_str)

    def test_save(self):
        """Test saving the City instance and updating the 'updated_at'
        attribute."""
        city = City()
        city.state_id = "WA"
        city.name = "Seattle"
        city.save()
        self.assertTrue(hasattr(city, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
