import random
import cities
from faker import Faker

def generate_name():
    adjs = open("../scrape/adjectives.txt", "r")
    adjs_lines = adjs.readlines()
    i = random.randint(0, len(adjs_lines))
    rand_adj = adjs_lines[i].strip().capitalize()

    animals = open("../scrape/animals.txt", "r")
    animals_lines = animals.readlines()
    i = random.randint(0, len(animals_lines))
    rand_animal = animals_lines[i].strip().capitalize()

    name = "The %s %s" % (rand_adj, rand_animal)

    adjs.close()
    animals.close()
    return name


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

        name = generate_name()
        addr = fake.street_address()
        city = cities.get_random()
        phone = fake.random_number(digits=10)
        license = ''.join(random.choice('0123456789ABCDEF') for i in range(8))

        night_club = Night_Club(name, addr, city, phone, license)
        return night_club



