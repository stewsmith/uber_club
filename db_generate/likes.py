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
