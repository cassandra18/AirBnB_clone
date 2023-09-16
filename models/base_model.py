#!/usr/bin/python3
"""The BaseModel class module"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel class

    Public instance attributes:

    id: string:
        assign with an uuid when an instance is created:
    created_at: datetime
        current datetime when instance is created
    updated_at: datetime
        current datetime when instance is created and
        will be updated on every object change
    __str__:
        should print:[<class name>] (<self.id>) <self.__dict__>

    Public instance methods:

    save(self):
        updates the updated_at with the current datetime
    to_dict(self):
        returns dictionary containing all keys/values of
         __dict__ of the instance:
        by using self.__dict__, only instance attributes set will be returned.
        a key __class__ must be added to this dictionary with the class name
        of the object.
        created_at and updated_at must be converted to string object in ISO
        format:
            format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            you can use isoformat() of datetime object
        This method will be the first piece of the serialization/
        deserialization process: create a dictionary representation with
        "simple object type" of our BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel

        If kwargs is not empty, set instance attributes based on its
            key-value pairs.
        If kwargs is empty, create a new instance with a unique ID and current
            datetime.

        Args:
            *args: Not used.
            **kwargs: Key-value pairs for initializing instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at with the current datetime
        The method should be called whenever the object is modified
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance for serialization.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict

    def __str__(self):
        """
        Return a human-readable string representation of the instance.

        Returns:
            str: A string containing class name, ID, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(
             self.__class__.__name__, self.id, self.__dict__)
