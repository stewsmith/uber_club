import random

class Beer:
    def __init__(self, name, manf):
        self.name = name
        self.manf = manf

    @staticmethod
    def generate():
        f = open('../scrape/manf_beer.txt', 'r')
        lines = f.readlines()
        randLine = random.randint(0, len(lines))
        manf, name = lines[randLine].strip().split('|')

        beer = Beer(name, manf)

        f.close()
        return beer
