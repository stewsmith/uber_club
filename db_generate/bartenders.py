import names
import random

class Bartender:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def generate():
        AGE_MIN = 18
        AGE_MAX = 45

        is_male = True if random.randint(0, 1) == 0 else False

        name = names.get_full_name(gender=('male' if is_male else 'female'))
        gender = 'M' if is_male else 'F'
        age = random.randint(AGE_MIN, AGE_MAX)

        bartender = Bartender(name, gender, age)
        return bartender
