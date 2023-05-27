# pylint: disable=too-many-instance-attributes
"""
A class inheriting from the Hotel class.
"""
from models.hotel import Hotel
class EcoHotel(Hotel):
    """
    A class inheriting from the Hotel class.
    """
    def __init__(self, name, total_rooms, available_rooms,# pylint: disable=too-many-arguments
                 rating, gym, garden):# pylint: disable=too-many-arguments
        """
        Initialize a ResortHotel object with the specified attributes.

        Args:
          name(str):The name of the hotel
          total_rooms(int):The number of the total rooms.
          available_rooms(int):The number of the available rooms.
          rating(int):This is a rating of hotels.
          gym(int):The number of gym in hotel.
          garden(bool):The availability of garden in hotel.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.gym = gym
        self.garden = garden

    def __str__(self):
        return f"""Name:{self.name}, Total Rooms: {self.total_rooms},
        Available Rooms: {self.available_rooms}, Rating: {self.rating},
        Gym: {self.gym}, Garden: {self.garden}"""

    def __repr__(self):
        return f"EcoHotel:'{self.name}', total_rooms={self.total_rooms},\
        available_rooms={self.available_rooms},rating={self.rating},\
        gym={self.gym}, garden={self.garden}"

    def get_location(self):
        """
        Abstract method to get location of hotel.
        This method should be implemented by the concrete hotel classes.
        """
        return None # pylint: disable=C0303   
