class Hotel:
    instance = None

    def __init__(self, name="Zirka", totalRooms=4, availableRooms=5, rating=5):
        self.name = name
        self.totalRooms = totalRooms
        self.availableRooms = availableRooms
        self.rating = rating

    @staticmethod
    def getInstance():
        if Hotel.instance is None:
            Hotel.instance = Hotel()
        return Hotel.instance

    def bookRoom(self):
        if self.availableRooms > 0:
            self.availableRooms -= 1

    def releaseRoom(self):
        self.availableRooms += 1

    def getAvailableRooms(self):
        return self.availableRooms

    def getBookedRoomsCount(self):
        return self.totalRooms - self.availableRooms

    def __str__(self):
        return f"Hotel: {self.name}, Total Rooms: {self.totalRooms}, Available Rooms: {self.availableRooms}, Rating: {self.rating}"


hotel1 = Hotel()
hotel2 = Hotel("Grand", 100, 80, 4)
hotel3 = Hotel.getInstance()
hotel4 = Hotel.getInstance()
hotels = [hotel1, hotel2, hotel3, hotel4]

for hotel in hotels:
    print(hotel)




