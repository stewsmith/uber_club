import MySQLdb
import datetime
import random
from database import Database
from deejays import Deejay


def create_performed_at():
    db = Database().connect()
    cursor = db.cursor()

    night_clubs = db.select("SELECT name FROM night_clubs")
    deejays = map(lambda d: Deejay(d[0], d[1], d[2]), db.select("SELECT * FROM deejays"))

    initial_date = datetime.date(2012, 1, 1)
    for i in range(365):
        curr_date = initial_date + datetime.timedelta(days=i)
        #Night_clubs only open on thur, fri, sat
        if curr_date.weekday() in [3, 4, 5]:
            for night_club in night_clubs:
                i, num_deejays = 0, random.randint(1, 2)
                while i < num_deejays:
                    #if Saturday then 50% chance of getting House DJ
                    if curr_date.weekday() == 6 and random.randint(0, 1) == 0:
                        house_deejays = filter(lambda d: d.genre == 'House', deejays)
                        deejay = house_deejays[random.randint(0, len(house_deejays) - 1)]
                    else:
                        deejay = deejays[random.randint(0, len(deejays) - 1)]
                    try:

                        date_str = curr_date.strftime("%Y-%m-%d")
                        cursor.execute("""INSERT INTO performed_at(deejay, night_club, date)
                                    VALUES(%s, %s, %s)""", (deejay.name, night_club, date_str))
                        print (deejay.name, night_club, date_str)
                    except MySQLdb.IntegrityError:
                        i -= 1
                    i += 1
    db.commit()
    db.close()


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
    create_performed_at()
