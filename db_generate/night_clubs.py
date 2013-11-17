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

    @staticmethod
    def generate():
        fake = Faker()

        name = ""
        addr = fake.street_address()
        city = cities.get_random()
        phone = fake.random_number(digits=10)
        license = ''.join(random.choice('0123456789ABCDEF') for i in range(8))

        night_club = Night_Club(name, addr, city, phone, license)
        return night_club



