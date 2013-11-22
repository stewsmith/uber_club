import names
import random

class Deejay:
    def __init__(self, name, genre, booking_cost):
        self.name = name
        self.genre = genre
        self.booking_cost = booking_cost

    @staticmethod
    def generate():
        BOOKING_COST_MIN = 700
        BOOKING_COST_MAX = 1100

        GENRES = ["House", "Trance", "Neurofunk", "Chillwave", "Futurepop",
                "Cybergrind", "Dubstep", "Brostep", "Jungle", "Techno",
                "Club", "Rave", "Disco", "Skweee", "Funk", "Electronica"]

        name = "DJ " + names.get_last_name()
        genre = GENRES[random.randint(0, len(GENRES) - 1)]
        if random.randint(0, 10) == 0:
            genre = "House"
        booking_cost = random.randint(BOOKING_COST_MIN, BOOKING_COST_MAX)

        if (genre == "House"):
            booking_cost += random.randint(300, 500)

        dj = Deejay(name, genre, booking_cost)
        return dj
