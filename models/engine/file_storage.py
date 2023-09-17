#!/usr/bin/python3
"""The FileStorage module serializes instances to JSON file.
It deserializes JSON file to instances."""

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serialize instance to JAson File.
    Deserialize JSON file to instance."""
    __file_path = "file.json"
    __objects = {
            'BaseModel': {},
            'User': {},
            'Place': {},
            'State': {},
            'City': {},
            'Amenity': {},
            'Review': {}
            }

    def all(self, cls=None):
        """Return the dictionary representation of __objects."""
        if cls is not None:
            return self.__objects.get(cls.__name__, {})
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, BaseModel):
                serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as fl:
            json.dump(serialized_objects, fl)

    def reload(self):
        """
        Deserialize the JSON file to __objects if __file_path exista.
        If the file doesn't exist, no exceptio should be raised."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as fl:
                try:
                    data = json.load(fl)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        valid_classes = {
                            'BaseModel': BaseModel,
                            'User': User,
                            'Place': Place,
                            'State': State,
                            'City': City,
                            'Amenity': Amenity,
                            'Review': Review
                        } 
                        if class_name in valid_classes:
                            obj_class = valid_classes[class_name]
                            obj = obj_class(**value)
                            self.__objects[key] = obj
                except FileNotFoundError:
                    pass
