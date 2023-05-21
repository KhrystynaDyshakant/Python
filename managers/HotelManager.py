from models.Hotel import Hotel
from models.ResortHotel import ResortHotel
from models.Motel import Motel
from models.LuxuryHotel import LuxuryHotel
from models.EcoHotel import EcoHotel

class HotelManager:
    
    def __init__(self):
        """
        Initialize a HotelManager object.

        Initialixes an emty list of hotels.
        """

        self.hotels = []

    def add_hotel(self, hotel):
         """
         Add a hotel to the manager.

         Args:
           hotel(Hotel):The hotel to be added.
         """
         self.hotels.append(hotel)
         

    def find_hotel_with_available_rooms(self, available_rooms):
        """
        Find hotels with available rooms.

        Args:
            available_rooms(int):The available rooms to find.

        Returns:
            list:A list of hotels with available rooms.
        """
            
        filtered_hotels = list(filter(lambda hotel:hotel.available_rooms==available_rooms, self.hotels))
        return filtered_hotels

    def find_hotel_with_rating_more_than(self, rating):
         """
         Find hotels with more rating.

         Args:
           rating(int):The rating to filter hotels.

         Returns:
           list:A list of hotels with more rating.
         """
         filtered_hotels = list(filter(lambda hotel:hotel.rating>rating, self.hotels))
         return filtered_hotels
          
