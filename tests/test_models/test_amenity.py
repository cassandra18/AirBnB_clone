import unittest
from datetime import datetime
import json
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def test_instance_attributes(self):
        """Test that instance attributes are correctly initialized."""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_set_attributes(self):
        """Test setting attributes of the Amenity instance."""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict(self):
        """Test the to_dict() method of the Amenity instance."""
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Gym')
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)
        self.assertTrue('id' in amenity_dict)

    def test_from_dict(self):
        """Test creating an Amenity instance from a dictionary."""
        amenity_data = {
            '__class__': 'Amenity',
            'name': 'Spa',
            'id': '12345',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        amenity = Amenity(**amenity_data)
        self.assertTrue(isinstance(amenity, Amenity))
        self.assertEqual(amenity.name, 'Spa')
        self.assertEqual(amenity.id, '12345')
        self.assertTrue(isinstance(amenity.created_at, datetime))
        self.assertTrue(isinstance(amenity.updated_at, datetime))

    def test_str_representation(self):
        """Test the string representation of the Amenity instance."""
        amenity = Amenity()
        amenity.name = "Sauna"
        amenity_str = str(amenity)
        self.assertTrue(isinstance(amenity_str, str))
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(str(amenity.id), amenity_str)
        self.assertIn("'name': 'Sauna'", amenity_str)

    def test_save(self):
        """Test saving the Amenity instance and updating the '
        updated_at' attribute."""
        amenity = Amenity()
        amenity.name = "Restaurant"
        amenity.save()
        self.assertTrue(hasattr(amenity, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
