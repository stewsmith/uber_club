import names
import random

BOOKING_COST_MIN = 700
BOOKING_COST_MAX = 1100

GENRES = ["House", "Trance", "Neurofunk", "Chillwave", "Futurepop",
          "Cybergrind", "Dubstep", "Brostep", "Jungle", "Techno",
          "Club", "Rave", "Disco", "Skweee", "Funk", "Electronica"]

class Deejay:
    def __init__(self, name, genre, booking_cost):
        self.name = name
        self.genre = genre
        self.booking_cost = booking_cost

def generate():
    djs = []
    num = input("Enter number of DJs: ")

    for i in range(num):
        name = "DJ " + names.get_last_name()
        genre = GENRES[random.randint(0, len(GENRES) - 1)]
        booking_cost = random.randint(BOOKING_COST_MIN, BOOKING_COST_MAX)

        if (genre == "House"):
            booking_cost += random.randint(200, 300)

        dj = Deejay(name, genre, booking_cost)

        djs.append(dj)

    return djs