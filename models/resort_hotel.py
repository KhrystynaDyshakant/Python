# pylint: disable=too-many-instance-attributes
"""
A class inheriting from the Hotel class.
"""
from models.hotel import Hotel
class ResortHotel(Hotel):
    """
    A class inheriting from the Hotel class.
    """
    def __init__(self, name, total_rooms, available_rooms, rating,# pylint: disable=too-many-arguments
                 number_of_restaurants, number_pools_for_children,# pylint: disable=too-many-arguments
                 number_pools_for_adults):# pylint: disable=too-many-arguments
        """
        Initialize a ResortHotel object with the specified attributes.

        Args:
        name(str):The name of the hotel
        total_rooms(int):The number of the total rooms.
        available_rooms(int):The number of the available rooms.
        rating(int):This is a rating of hotels.
        number_of_restaurants(int):The number of restaurants.
        number_pools_for_children(int):The number of pools for children.
        number_pools_for_adults(int):The number of pools for adults
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.number_of_restaurants = number_of_restaurants
        self.number_pools_for_children = number_pools_for_children
        self.number_pools_for_adults = number_pools_for_adults

    def __str__(self):
        return f"""Name:{self.name}, Total Rooms: {self.total_rooms},
        Available Rooms: {self.available_rooms}, Rating: {self.rating},
        Number Of Restaurant: {self.number_of_restaurants},
        Number Pools For Children: {self.number_pools_for_children},
        Number Pools For Adults: {self.number_pools_for_adults}"""

    def __repr__(self):
        return f"ResortHotel='{self.name}', total_rooms={self.total_rooms},\
    available_rooms={self.available_rooms}, rating={self.rating},\
    number_of_restaurants={self.number_of_restaurants},\
    number_pools_for_children={self.number_pools_for_children},\
    number_pools_for_adults={self.number_pools_for_adults}"
    def get_location(self):
        """
        Return the name of the hotel.
        Return:
              str:The remaining name of the hotel.
        """
        return self.name
