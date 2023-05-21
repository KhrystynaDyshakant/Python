from models.Hotel import Hotel
class LuxuryHotel(Hotel):
    """
     A class inheriting from the Hotel class.
    """
    def __init__(self, name, total_rooms, available_rooms, rating, number_of_spa_rooms, number_of_service):
        """
       Initialize a ResortHotel object with the specified attributes.

       Args:
          name(str):The name of the hotel
          total_rooms(int):The number of the total rooms.
          available_rooms(int):The number of the available rooms.
          rating(int):This is a rating of hotels.
          number_of_spa_rooms(int):The number of spa rooms.
          number_of_service(int):The number of service.
        """

        super().__init__(name, total_rooms, available_rooms, rating)
        self.number_of_spa_rooms = number_of_spa_rooms
        self.number_of_service = number_of_service

    def __str__(self):
      return f"""Name:{self.name}, Total Rooms: {self.total_rooms},
    Available Rooms: {self.available_rooms}, Rating: {self.rating},
    Number Of Spa Rooms: {self.number_of_spa_rooms},
    Number Of Service: {self.number_of_service}"""

    def __repr__(self):
      return f"LuxuryHotel='{self.name}', total_rooms={self.total_rooms}, available_rooms={self.available_rooms}, rating={self.rating}, number_of_spa_rooms={self.number_of_spa_rooms}, number_of_service={self.number_of_service}"

    def get_location():
       """
       Abstract method to get location of hotel.

        This method should be implemented by the concrete hotel classes.

       """
       return None 
