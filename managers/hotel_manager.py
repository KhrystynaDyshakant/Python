"""
HotelManager class
"""
class HotelManager:
    """
    HotelManager class
    """
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

# pylint: disable=line-too-long
    def find_hotel_with_available_rooms(self, available_rooms):
        """
        Find hotels with available rooms.

        Args:
            available_rooms(int):The available rooms to find.

        Returns:
            list:A list of hotels with available rooms.
        """
        filtered_hotels = list(filter(lambda hotel: hotel.available_rooms == available_rooms, self.hotels))

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

    def __len__(self):
        """
        Get the number of hotels in the manager.

        Returns:
            int: The number of hotels.
        """
        return len(self.hotels)

    def __getitem__(self, index):
        """
        Get the hotel at the specified index.

        Args:
            index (int): The index of the hotel.

        Returns:
            Hotel: The hotel at the specified index.
        """
        return self.hotels[index]

    def __iter__(self):
        """
        Iterate over the hotels in the manager.

        Returns:
            iter: An iterator over the hotels.
        """
        return iter(self.hotels)

    def get_locations(self):
        """
        Get the locations of all hotels in the manager.

        Returns:
            list: A list of locations of the hotels.
        """
        locations = [hotel.get_location() for hotel in self.hotels]
        return locations

    def enumerate_hotels(self):
        """
        Enumerate the hotels in the manager.

        Returns:
            list: A list of tuples containing the hotel and its index.
        """
        enumerated_hotels = list(enumerate(self.hotels))
        return enumerated_hotels

    def zip_with_get_location(self):
        """
        Zip the hotels with the result of calling get_location() for each hotel.

        Returns:
            list: A list of tuples containing the hotel and its location.
        """
        zipped_results = list(zip(self.hotels, [hotel.get_location() for hotel in self.hotels]))
        return zipped_results

    def check_condition(self, condition):
        """
        Checks if all objects in the manager satisfy a certain condition and if any object satisfies the condition.

        Args:
            condition (callable): The condition to check. It should be a function that takes an object as an argument and returns a boolean value.

        Returns:
            dict: A dictionary containing the results of the checks. The keys are "all" and "any" with corresponding boolean values.
        """
        all_result = all(condition(hotel) for hotel in self.hotels)
        any_result = any(condition(hotel) for hotel in self.hotels)

        results = {"all": all_result, "any": any_result}
        return results # pylint: disable=C0305
