import names
import random
from faker import Faker

DRINKER_AGE_MIN = 21
DRINKER_AGE_MAX = 60

class Drinker:
    def __init__(self, name, addr, city, gender, phone, age):
        self.name = name
        self.addr = addr
        self.city = city
        self.gender = gender
        self.phone = phone
        self.age = age

def generate():
    drinkers = []
    num = input("Enter number of drinkers: ")

    fake = Faker()

    for i in range(num):
        is_male = True if random.randint(0, 1) == 0 else False

        name = names.get_full_name(gender=('male' if is_male else 'female'))
        addr = fake.street_address()
        city = fake.city()
        gender = 'M' if is_male else 'F'
        phone = fake.random_number(digits=10)
        age = random.randint(DRINKER_AGE_MIN, DRINKER_AGE_MAX)

        drinker = Drinker(name, addr, city, gender, phone, age)
        drinkers.append(drinker)

    return drinkers
