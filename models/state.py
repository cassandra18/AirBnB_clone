#!/usr/bin/python3
"""State class model that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class representing a state.

    Public class attributes:
    - name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of State.

        Args:
            *args: Not used.
            **kwargs: Key-value pairs for initializing instance attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """
        Return a human-readable string representation of the State instance.

        Returns:
            str: A string containing the class name, ID, and attribute
            dictionary.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
