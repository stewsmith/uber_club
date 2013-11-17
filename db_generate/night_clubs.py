import random
import cities
from faker import Faker

class Night_Club:
    def __init__(self, name, addr, city, phone, license):
        self.name = name
        self.addr = addr
        self.city = city
        self.phone = phone
        self.license = license

def generate():
    night_clubs = []
    num = input("Enter number of night clubs: ")

    fake = Faker()

    for i in range(num):
        name = ""
        addr = fake.street_address()
        city = cities.get_random()
        phone = fake.random_number(digits=10)
        license = ''.join(random.choice('0123456789ABCDEF') for i in range(8))

        night_club = Night_Club(name, addr, city, phone, license)
        night_clubs.append(night_club)

    return night_clubs



