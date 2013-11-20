import random
import cities
from faker import Faker

def generate_name():
    rand_adj = ""
    rand_animal = ""

    animalPresent = random.randint(1, 10)
    if(animalPresent> 3):
        animals = open("../scrape/animals.txt", "r")
        animals_lines = animals.readlines()
        i = random.randint(0, len(animals_lines))
        rand_animal = animals_lines[i].strip().capitalize()
        animals.close()

    adjectivePresent = 10
    if rand_animal: adjectivePresent = random.randint(1, 10)
    if(adjectivePresent > 3):
        adjs = open("../scrape/adjectives.txt", "r")
        adjs_lines = adjs.readlines()
        i = random.randint(0, len(adjs_lines))
        rand_adj = adjs_lines[i].strip().capitalize()
        adjs.close()


    if rand_adj and rand_animal:
        name = "The %s %s" % (rand_adj, rand_animal)
    elif rand_adj:
        name = "The %s" % (rand_adj)
    elif rand_animal:
        name = "The %s" % (rand_animal)


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



