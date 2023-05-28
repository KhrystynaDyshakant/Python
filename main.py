"""
main.
"""
from managers.hotel_manager import HotelManager
from models.resort_hotel import ResortHotel
from models.motel import Motel
from models.luxury_hotel import LuxuryHotel
from models.eco_hotel import EcoHotel

manager = HotelManager()
manager.add_hotel(ResortHotel("Grand", 5, 2, 3, 5, 8, 1))
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



# Список результатів виконання методу get_location()
get_location_results = [hotel.get_location() for hotel in manager]

print("Results of get_location() method:")
for result in get_location_results:
    print(result)

print("\n")

# Склейка об'єкта з його порядковим номером в списку
enumerated_hotels = [(index, hotel) for index, hotel in enumerate(manager)]# pylint: disable=R1721

print("Enumerated hotels:")
for index, hotel in enumerated_hotels:
    print(f"Index: {index}, Hotel: {hotel}")

print("\n")

# Склейка об'єкта з результатом виконання методу get_location()
zip_results = [(hotel, hotel.get_location()) for hotel in manager]

print("Zip results (hotel and get_location() method):")
for result in zip_results:
    print(result)

print("\n")

# Повертає словник з усіма ключами та значеннями атрибутів обʼєкта
hotel = ResortHotel("Grand", 4, 2, 3, 4, 8, 1)
attributes = hotel.get_attributes_by_value_type(str)
print("\nList of attributes by value type str:")
print(attributes)

# Перевірка умови за допомогою функцій all() та any()
all_condition = all(hotel.available_rooms > 0 for hotel in manager)
any_condition = any(hotel.rating > 3 for hotel in manager)

print(f"All condition: {all_condition}")
print(f"Any condition: {any_condition}")
