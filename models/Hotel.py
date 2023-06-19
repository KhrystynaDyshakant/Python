"""
Abstract class
"""
from abc import ABC, abstractmethod

class Hotel(ABC):
    """
    Absract base class represetning a hotel
    """
    def __init__(self, name="Zirka", total_rooms=10, available_rooms=5, rating=3):
        """
        Initialize a Hotel object.

        Args:
            name(str):The name of the hotel
            total_rooms(int):The number of the total rooms.
            available_rooms(int):The number of the available rooms.
            rating(int):This is a rating of hotels.
        """
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.rating = rating

    def __str__(self):
        return f"""Name:{self.name}, Total Rooms: {self.total_rooms},
        Available Rooms: {self.available_rooms}, Rating: {self.rating}"""

    def __repr__(self):
        return f"Hotel='{self.name}', total_rooms={self.total_rooms},\
        available_rooms={self.available_rooms}, rating={self.rating}"

    def book_room(self):
        """
        Reduces the number of available rooms by 1.

        Args:
            available_rooms(int): The current count of available rooms.
        """
        if self.available_rooms:
            self.available_rooms -= 1

    def release_room(self):
        """
        Increases the count of available rooms by 1 when releasing a room.

        Args:
            available_rooms (int): The current count of available rooms.
        """
        self.available_rooms += 1

    def get_booked_rooms_count(self):
        """
        Booked a room from the number total rooms and the number available rooms.

        Args:
            available_rooms (int): The current count of available rooms.
            total_rooms(int):The number of the total rooms.
        """
        return self.total_rooms - self.available_rooms

    @abstractmethod
    def get_location(self):
        """
        Abstract method to get location of hotel.

        This method should be implemented by the concrete hotel classes.

        Returns:
        str:The remaining name of Hotel.
        str:The remaining name of track.
        """
    def get_attributes_by_value_type(self, value_type):
        """
        Return a dictionary of attributes and their values that match the
        specified value type.

        Args:
        value_type(type): The type of value to match.

        Returns:
        dict: A dictionary of attributes and their values that have the
        specified value type.
        """
        return {attr: value for attr, value in self.__dict__.items()
                if isinstance(value, value_type)}
