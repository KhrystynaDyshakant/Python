"""
main
"""
from managers.hotel_manager import HotelManager
from models.resort_hotel import ResortHotel
from models.motel import Motel
from models.luxury_hotel import LuxuryHotel
from models.eco_hotel import EcoHotel

manager = HotelManager()
manager.add_hotel(ResortHotel("Grand", 4, 2, 3, 4, 8, 1))
manager.add_hotel(Motel("Tracl", 1, 2, 4, 17, 210, "Lviv", "Sokal",
                        "Lviv-Sokal"))
manager.add_hotel(LuxuryHotel("Lion", 5, 14, 1, 4, 1))
manager.add_hotel(EcoHotel("Flower", 2, True, 0, 1, 1))
manager.add_hotel(ResortHotel("Zirka", 4, 5, 4, 1, 2, 3))
manager.add_hotel(Motel("Track1", 1, 2, 4, 4, 14, "Sokal", "Chervonograd",
                        "Sokal-Chervonograd"))
manager.add_hotel(LuxuryHotel("Astra", 4, 11 ,4, 2, 1))
manager.add_hotel(EcoHotel("Tree", 5, False, 1, 5, 1))

hotels_with_available_rooms = manager.find_hotel_with_available_rooms(5)
print("Hotels with available rooms 5:")
for hotel in hotels_with_available_rooms:
    print(hotel)

print("\n")

hotels_with_rating_more_than = manager.find_hotel_with_rating_more_than(3)
print("Hotels with rating more than 3:")
for hotel in hotels_with_rating_more_than:
    print(hotel)

print("\n")
