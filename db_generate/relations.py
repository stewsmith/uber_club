import MySQLdb
import random
from database import Database


def create_likes():
    db = Database().connect()
    cursor = db.cursor()

    drinkers = db.select("SELECT name FROM drinkers")
    beers = db.select("SELECT name FROM beers")

    # Every drinker likes between 1-7 beers
    for drinker in drinkers:
        i, num = 0, random.randint(1, 7)
        while i < num:
            beer = beers[random.randint(0, len(beers) - 1)]
            try:
                cursor.execute("""INSERT INTO likes(drinker, beer)
                               VALUES(%s, %s)""", (drinker, beer))
                print drinker, beer
            except MySQLdb.IntegrityError:
                i -= 1
            i += 1

    db.commit()
    db.close()


def create_works_at():
    db = Database().connect()
    cursor = db.cursor()

    bartenders = db.select("SELECT name FROM bartenders")
    night_clubs = db.select("SELECT name FROM night_clubs")

    #Between 3 and 12 bartenders per night_club
    for night_club in night_clubs:
        i = 0
        num = random.randint(3, 12)
        while i < num:
            bartender = bartenders[random.randint(0, len(bartenders) - 1)]

            try:
                cursor.execute("""INSERT INTO works_at(bartender, night_club)
                               VALUES(%s, %s)""",
                               (bartender, night_club))
                print bartender, night_club
            except MySQLdb.IntegrityError:
                i -= 1

            i += 1

    db.commit()
    db.close()


def create_sells():
    db = Database().connect()
    cursor = db.cursor()

    beers = db.select("SELECT name FROM beers")
    night_clubs = db.select("SELECT name FROM night_clubs")

    #Between 10 and 15 beers sold per night_club
    for night_club in night_clubs:
        i = 0
        num = random.randint(10, 15)
        while i < num:
            beer = beers[random.randint(0, (len(beers) - 1))]

            try:
                price = random.randint(5, 13)
                cursor.execute("""INSERT INTO sells(beer, price, night_club)
                               VALUES(%s, %s, %s)""",
                               (beer, price, night_club))
                print beer, price, night_club
            except MySQLdb.IntegrityError:
                i -= 1

            i += 1

    db.commit()
    db.close()

def create_relations():
    create_likes()
    create_works_at()
    create_sells()
