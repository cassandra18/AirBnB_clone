#!/usr/bin/python3
"""The file_storage module."""

import json
from os.path import exists


class FileStorage:
	"""Serialize instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects if the file exists.
        If the file doesn't exist, no exception should be raised.
        """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj_class = eval(class_name)
                        obj = obj_class(**value)
                        FileStorage.__objects[key] = obj
                except Exception as e:
                    pass  
