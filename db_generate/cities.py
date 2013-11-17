import random

def get_random():
    cities = ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco',
              'Fresno', 'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield',
              'Anaheim', 'Santa Ana', 'Riverside', 'Stockton', 'Chula Vista',
              'Fremont', 'Irvine', 'San Bernadino', 'Modesto', 'Oxnard', 'Fontana']
    return cities[random.randint(0, len(cities))]

