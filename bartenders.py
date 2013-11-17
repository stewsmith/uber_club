import names
import random

BARTENDER_AGE_MIN = 18
BARTENDER_AGE_MAX = 45

class Bartender:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

def generate():
    bartenders = []
    num = input("Enter number of bartenders: ")

    for i in range(num):
        is_male = True if random.randint(0, 1) == 0 else False

        name = names.get_full_name(gender=('male' if is_male else 'female'))
        gender = 'M' if is_male else 'F'
        age = random.randint(BARTENDER_AGE_MIN, BARTENDER_AGE_MAX)

        bartender = Bartender(name, gender, age)
        bartenders.append(bartender)

    return bartenders
