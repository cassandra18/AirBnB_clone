#!/usr/bin/python3


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class representing a place.

    Public class attributes:
    - city_id (str): The ID of the city where the place is located.
    - user_id (str): The ID of the user who owns the place.
    - name (str): The name of the place.
    - description (str): A description of the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number of bathrooms in the place.
    - max_guest (int): The maximum number of guests the place can accommodate.
    - price_by_night (int): The price per night for the place.
    - latitude (float): The latitude coordinates of the place.
    - longitude (float): The longitude coordinates of the place.
    - amenity_ids (list of str): A list of Amenity IDs associated with the
    place.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of Place.

        Args:
            *args: Not used.
            **kwargs: Key-value pairs for initializing instance attributes.
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        """
        Return a human-readable string representation of the Place instance.

        Returns:
            str: A string containing the class name, ID, and attribute
            dictionary.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
