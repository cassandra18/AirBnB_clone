#!/usr/bin/python3
"""Review Class Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class representing a review.

    Public class attributes:
    - place_id (str): The ID of the place associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of Review.

        Args:
            *args: Not used.
            **kwargs: Key-value pairs for initializing instance attributes.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        """
        Return a human-readable string representation of the Review instance.

        Returns:
            str: A string containing the class name, ID, and attribute
            dictionary.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
