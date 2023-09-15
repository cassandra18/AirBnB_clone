#!/usr/bin/python3
"""State class model that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class representing a state.

    Public class attributes:
    - name (str): The name of the state.
    """
    name = ""
