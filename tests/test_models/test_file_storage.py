import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by creating a temporary file path and a new
        FileStorage instance.
        """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """
        Clean up the test environment by removing the temporary file if it
        exists.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """
        Test that the 'new' method adds a new object to the storage dictionary.
        """
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), all_objects)

    def test_save_and_reload(self):
        """
        Test saving and reloading objects from the storage.
        """
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), all_objects)
        reloaded_model = all_objects["BaseModel.{}".format(new_model.id)]
        self.assertEqual(new_model.to_dict(), reloaded_model.to_dict())

    def test_save_empty(self):
        """
        Test that saving when there are no objects doesn't create a file.
        """
        self.storage.save()
        self.assertFalse(os.path.exists(self.file_path))


if __name__ == "__main__":
    unittest.main()
