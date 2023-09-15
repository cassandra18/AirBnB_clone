#!/usr/bin/python3
"""The FileStorage module serializes instances to JSON file.
It deserializes JSON file to instances."""

import json
from os.path import exists


class FileStorage:
    """Serialize instance to JAson File.
    Deserialize JSON file to instance."""
    __file_path = "storage_file"
    __objects = {}

    def all(self):
        """Return the dictionary representation of __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        serialized_objets = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects if __file_path exista.
        If the file doesn't exist, no exceptio should be raised."""
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
