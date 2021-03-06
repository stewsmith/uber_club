import MySQLdb
import relations
from deejays import Deejay
from bartenders import Bartender
from drinkers import Drinker
from night_clubs import Night_Club
from beers import Beer
from database import Database

def add_deejays(db):
    cursor = db.cursor()
    num = input("Enter number of DJs: ")

    i = 0
    while i < num:
        deejay = Deejay.generate()
        name = deejay.name
        genre = deejay.genre
        booking_cost = deejay.booking_cost

        try:
            cursor.execute("""INSERT INTO deejays(name, genre, booking_cost)
                           VALUES(%s, %s, %s)""",
                           (name, genre, booking_cost))
            print name, genre, booking_cost
        except MySQLdb.IntegrityError:
            i -= 1
        i += 1

    db.commit()


def add_bartenders(db):
    cursor = db.cursor()
    num = input("Enter number of bartenders: ")

    i = 0
    while i < num:
        bartender = Bartender.generate()
        name = bartender.name
        gender = bartender.gender
        age = bartender.age

        try:
            cursor.execute("""INSERT INTO bartenders(name, gender, age)
                           VALUES(%s, %s, %s)""",
                           (name, gender, age))
            print name, gender, age
        except MySQLdb.IntegrityError:
            i -= 1
        i += 1

    db.commit()


def add_drinkers(db):
    cursor = db.cursor()
    num = input("Enter number of drinkers: ")

    i = 0
    while i < num:
        drinker = Drinker.generate()
        name = drinker.name
        addr = drinker.addr
        city = drinker.city
        gender = drinker.gender
        phone = drinker.phone
        age = drinker.age

        try:
            cursor.execute("""INSERT INTO drinkers(name, addr, city,
                                                gender, phone, age)
                           VALUES(%s, %s, %s, %s, %s, %s)""",
                           (name, addr, city, gender, phone, age))
            print name, addr, city, gender, phone, age
        except MySQLdb.IntegrityError:
            i -= 1
        i += 1

    db.commit()


def add_night_clubs(db):
    cursor = db.cursor()
    num = input("Enter number of night clubs: ")

    i = 0
    while i < num:
        night_club = Night_Club.generate()
        name = night_club.name
        addr = night_club.addr
        city = night_club.city
        phone = night_club.phone
        nc_license = night_club.license  # license is a python variable

        try:
            cursor.execute("""INSERT INTO night_clubs(name, addr, city,
                                                    phone, license)
                           VALUES(%s, %s, %s, %s, %s)""",
                           (name, addr, city, phone, nc_license))
            print name, addr, city, phone, nc_license
        except MySQLdb.IntegrityError:
            i -= 1
        i += 1

    db.commit()


def add_beers(db):
    cursor = db.cursor()
    num = input("Enter number of beers (max is 476): ")

    i = 0
    while i < num:
        beer = Beer.generate()
        name = beer.name
        manf = beer.manf

        try:
            cursor.execute("""INSERT INTO beers(name, manf)
                           VALUES(%s, %s)""",
                           (name, manf))
            print name, manf
        except MySQLdb.IntegrityError:
            i -= 1
        i += 1
    db.commit()


def main():
    db = Database().connect()
    add_deejays(db)
    add_bartenders(db)
    add_drinkers(db)
    add_night_clubs(db)
    add_beers(db)
    relations.create_relations()
    db.close()


if __name__ == "__main__":
    main()
