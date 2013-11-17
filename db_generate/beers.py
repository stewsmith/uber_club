import random

NUM_BEER_MAX = 100  # Depending on http://www.fin.gov.on.ca/en/lists/bwt/beer.html

class Beer:
    def __init__(self, name, manf):
        self.name = name
        self.manf = manf

    @staticmethod
    def generate():
        return
        # TODO scrape data from:
        # http://www.fin.gov.on.ca/en/lists/bwt/beer.html
