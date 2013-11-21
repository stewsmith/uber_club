import random
import MySQLdb
from database import Database

def create_sells():
    db = Database().connect()
    cursor = db.cursor()

    beers = db.select("SELECT name FROM beers")
    night_clubs = db.select("SELECT name FROM night_clubs")

    #Between 10 and 15 beers sold per night_club
    for night_club in night_clubs:
        j = 0
        num = random.randint(10, 15)
        while j < num:
            beer = beers[random.randint(0, (len(beers) - 1))]

            try:
                price = random.randint(5, 13)
                cursor.execute("""INSERT INTO sells(beer, price, night_club)
                            VALUES(%s, %s, %s)""",
                            (beer, price, night_club))
                print beer, price, night_club
            except MySQLdb.IntegrityError:
                j -= 1

            j +=1

    db.commit()
    db.close()


