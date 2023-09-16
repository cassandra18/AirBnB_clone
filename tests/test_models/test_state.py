import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def test_instance_attributes(self):
        """Test that instance attributes are correctly initialized."""
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
        self.assertEqual(state.name, "")

    def test_set_attributes(self):
        """Test setting attributes of the State instance."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """Test the to_dict() method of the State instance."""
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'New York')
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('id' in state_dict)

    def test_str_representation(self):
        """Test the string representation of the State instance."""
        state = State()
        state.name = "Texas"
        state_str = str(state)
        self.assertTrue(isinstance(state_str, str))
        self.assertIn("[State]", state_str)
        self.assertIn(str(state.id), state_str)
        self.assertIn("'name': 'Texas'", state_str)

    def test_save(self):
        """Test saving the State instance and updating the 'updated_at'
        attribute."""
        state = State()
        state.name = "Florida"
        state.save()
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_to_dict_with_attributes(self):
        """Test to_dict() method when attributes are set."""
        state = State()
        state.name = "Nevada"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], 'Nevada')

    def test_to_dict_with_updated_at(self):
        """Test to_dict() method with updated_at attribute."""
        state = State()
        state.name = "Arizona"
        state.save()
        state_dict = state.to_dict()
        self.assertTrue('updated_at' in state_dict)

    def test_empty_name(self):
        """Test an empty name attribute."""
        state = State()
        state.name = ""
        self.assertEqual(state.name, "")

    def test_non_string_name(self):
        """Test setting non-string values in the name attribute."""
        state = State()
        state.name = "12345"
        self.assertEqual(state.name, "12345")

    def test_negative_name(self):
        """Test setting negative name values."""
        state = State()
        state.name = -1
        self.assertEqual(state.name, -1)

    def test_float_name(self):
        """Test setting float values in the name attribute."""
        state = State()
        state.name = 1.5
        self.assertEqual(state.name, 1.5)


if __name__ == '__main__':
    unittest.main()
