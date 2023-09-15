#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class representing a city.

    Public class attributes:
    - state_id (str): The ID of the state to which the city belongs.
    - name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of City.

        Args:
            *args: Not used.
            **kwargs: Key-value pairs for initializing instance attributes.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """
        Return a human-readable string representation of the City instance.

        Returns:
            str: A string containing the class name, ID, and attribute
            dictionary.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
