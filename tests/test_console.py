#!/usr/bin/python3
"""The console unit test module."""

import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test for the HBNBCommand class."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test the 'help' command."""
        with patch('builtins.input', return_value="help"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("EOF  - Exit the program", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid(self, mock_stdout):
        """Test the 'create' command with a valid class."""
        with patch('builtins.input', return_value="create BaseModel"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("Generated ID:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test the 'create' command with an invalid class."""
        with patch('builtins.input', return_value="create InvalidClass"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test the 'create' command with a missing class."""
        with patch('builtins.input', return_value="create"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_valid(self, mock_stdout):
        """Test the 'show' command with a valid class and ID."""
        with patch('builtins.input', return_value="show BaseModel 123"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel with ID 123:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test the 'show' command with an invalid class."""
        with patch('builtins.input', return_value="show InvalidClass 123"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test the 'show' command with a missing class."""
        with patch('builtins.input', return_value="show"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_valid(self, mock_stdout):
        """Test the 'destroy' command with a valid class and ID."""
        with patch('builtins.input', return_value="destroy BaseModel 123"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("Instance deleted:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test the 'destroy' command with an invalid class."""
        with patch('builtins.input', return_value="destroy InvalidClass 123"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test the 'destroy' command with a missing class."""
        with patch('builtins.input', return_value="destroy"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test the 'destroy' command with a missing ID."""
        with patch('builtins.input', return_value="destroy BaseModel"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** instance id missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_valid(self, mock_stdout):
        """Test the 'all' command with a valid class."""
        with patch('builtins.input', return_value="all BaseModel"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("Displaying all 0 instances", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        """Test the 'all' command with an invalid class."""
        with patch('builtins.input', return_value="all InvalidClass"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_valid(self, mock_stdout):
        """Test the 'count' command with a valid class."""
        with patch('builtins.input', return_value="count BaseModel"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("Number of instances of BaseModel:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_invalid_class(self, mock_stdout):
        """Test the 'count' command with an invalid class."""
        with patch('builtins.input', return_value="count InvalidClass"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_valid(self, mock_stdout):
        """Test the updatecommand with a valid class, ID, attribute,value."""
        with patch('builtins.input',
                   return_value="update BaseModel 123 name John"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("Attribute updated:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test the 'update' command with an invalid class."""
        with patch('builtins.input',
                   return_value="update InvalidClass 123 name John"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test the 'update' command with a missing class."""
        with patch('builtins.input', return_value="update"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test the 'update' command with a missing ID."""
        with patch('builtins.input', return_value="update BaseModel"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** instance id missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attribute(self, mock_stdout):
        """Test the 'update' command with a missing attribute."""
        with patch('builtins.input', return_value="update BaseModel 123"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** attribute name missing **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        """Test the 'update' command with a missing value."""
        with patch('builtins.input', return_value="update BaseModel 123 name"):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn("** value missing **", output)


if __name__ == '__main__':
    unittest.main()
