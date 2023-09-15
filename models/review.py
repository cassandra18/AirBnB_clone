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

    place_id = ""
    user_id = ""
    text = ""
