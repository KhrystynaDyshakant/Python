class Hotel:
    __instance = None

    def __init__(self, name="Zirka", total_rooms=4, available_rooms=5, rating=5):
        self._name = name
        self._total_rooms = total_rooms
        self._available_rooms = available_rooms
        self._rating = rating

    @staticmethod
    def get_instance():
        if not Hotel.__instance:
            Hotel.__instance = Hotel()
        return Hotel.__instance

    def book_room(self):
        if self._available_rooms > 0:
            self._available_rooms -= 1

    def release_room(self):
        self._available_rooms += 1

    def get_booked_rooms_count(self):
        return self._total_rooms - self._available_rooms
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = new_name
        
    @property
    def total_rooms(self):
        return self._total_rooms
    
    @total_rooms.setter
    def total_rooms(self, total_rooms):
        self._total_rooms = new_total_rooms
        
    @property
    def available_rooms(self):
        return self._available_rooms
    
    @available_rooms.setter
    def available_rooms(self, available_rooms):
        self._available_rooms = new_available_rooms
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        self._rating = new_rating

    def __str__(self):
        return f"Hotel: {self._name}, Total Rooms: {self._total_rooms}, Available Rooms: {self._available_rooms}, Rating: {self._rating}"

hotel1 = Hotel()
hotel2 = Hotel("Grand", 100, 80, 4)
hotel3 = Hotel.get_instance()
hotel4 = Hotel.get_instance()
hotels = [hotel1, hotel2, hotel3, hotel4]

for hotel in hotels:
    print(hotel)
