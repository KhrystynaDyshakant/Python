# pylint: disable=too-many-instance-attributes
"""
A class inheriting from the Hotel class
"""
from models.hotel import Hotel
class Motel(Hotel):
    """
    A class inheriting from the Hotel class.
    """

    def __init__(self, name, total_rooms, available_rooms, rating,# pylint: disable=too-many-arguments
                 number_of_track, kilometer_of_track, start_city,# pylint: disable=too-many-arguments
                 end_city, name_of_track):# pylint: disable=too-many-arguments
        """
        Initialize a Motel object with the specified attributes.

        Args:
          name(str):The name of the hotel
          total_rooms(int):The number of the total rooms.
          available_rooms(int):The number of the available rooms.
          rating(int):This is a rating of hotels.
          number_of_track(int):The number of track.
          kilometer_of_track(int):The kilometer of track.
          start_city(str):The name of start city.
          end_city(str):The name of end city.
          name_of_track(str):The name of track.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.number_of_track = number_of_track
        self.kilometer_of_track = kilometer_of_track
        self.start_city = start_city
        self.end_city = end_city
        self.name_of_track = name_of_track

    def __str__(self):
        return f"""Name:{self.name}, Total Rooms: {self.total_rooms},
        Available Rooms: {self.available_rooms}, Rating: {self.rating},
        Number Of Track: {self.number_of_track},
        Kilometer Of Track: {self.kilometer_of_track},
        Start City: {self.start_city}, End City: {self.end_city},
        Name Of Track: {self.name_of_track}"""
    def __repr__(self):
        return f"Motel='{self.name}', total_rooms={self.total_rooms},\
        available_rooms={self.available_rooms}, rating={self.rating},\
        number_of_track={self.number_of_track},\
        kilometer_of_track={self.kilometer_of_track},\
        start_city='{self.start_city}', end_city='{self.end_city}',\
        name_of_track='{self.name_of_track}'"
    def get_location(self):
        """
        Return the name of track and kilometer of track.

        Return:
         str:The remaining name of track.
         int:The remaining kilometer of track.
        """
        return self.name_of_track() + self.kilometer_of_track()
