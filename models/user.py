#!/usr/bin/python3
"""The user module contains the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """The user class inherits from the BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
