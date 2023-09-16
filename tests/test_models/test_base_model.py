import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        Set up a new BaseModel instance before each test.
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        Clean up after each test by deleting the BaseModel instance.
        """
        del self.model

    def test_instance_attributes(self):
        """
        Test if the BaseModel instance has the required attributes.
        """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        """
        Test if the 'id' attribute is generated as a string.
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        """
        Test if the 'created_at' attribute is of type datetime.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test if the 'updated_at' attribute is of type datetime.
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """
        Test the __str__ method to check if it returns the expected string.
        """
        expected_str = "[BaseModel] ({}) {}".format(
                self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """
        Test if the 'save' method updates the 'updated_at' attribute.
        """
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test if the 'to_dict' method returns a dictionary
        with the expected keys.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_to_dict_datetime_format(self):
        """
        Test if the 'to_dict' method returns datetime
        attributes in string format.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_datetime_isoformat(self):
        """
        Test if the 'to_dict' method returns datetime attributes in ISO format.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat()
        )

    def test_to_dict_attributes(self):
        """
        Test if the 'to_dict' method includes additional attributes
        in the dictionary.
        """
        self.model.name = "Test Model"
        self.model.number = 42
        model_dict = self.model.to_dict()
        self.assertIn('name', model_dict)
        self.assertIn('number', model_dict)
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['number'], 42)

    def test_create_instance_from_dict(self):
        """
        Test if a new BaseModel instance can be created from a dictionary
        representation.
        """
        orig_model = self.model
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(orig_model.id, new_model.id)
        self.assertEqual(orig_model.created_at, new_model.created_at)
        self.assertEqual(orig_model.updated_at, new_model.updated_at)
        self.assertEqual(
                orig_model.__class__.__name__, new_model.__class__.__name__)

    def test_invalid_attribute_type(self):
        """
        Test adding an attribute with an invalid type (should fail).
        """
        self.model.invalid_attr = [1, 2, 3]
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.invalid_attr, new_model.invalid_attr)

    def test_missing_required_attribute(self):
        """
        Test removing a required attribute (should fail).
        """
        model_dict = self.model.to_dict()
        del model_dict['__class__']
        new_model = BaseModel(**model_dict)
        self.assertEqual(
                self.model.__class__.__name__, new_model.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
