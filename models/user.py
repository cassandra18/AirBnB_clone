#!/usr/bin/python3
"""The user module contains the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """The user class inherits from the BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize the User class."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """The __str__ method formats the ouput string."""
        user_dict = self.to_dict()
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(
                class_name,
                user_dict['id'],
                user_dict
                )
