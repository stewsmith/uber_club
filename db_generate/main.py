import MySQLdb
import deejays
import bartenders
import drinkers
import night_clubs
import beers

db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                     user="csuser",
                     passwd="cs97f462",
                     db="nightclubconsultants")

cursor = db.cursor()

def add_deejays():
    arr = deejays.generate()

    for i in range(len(arr)):
        name = arr[i].name
        genre = arr[i].genre
        booking_cost = arr[i].booking_cost

        cursor.execute("""INSERT IGNORE INTO deejays(name, genre, booking_cost)
                          VALUES(%s, %s, %s)""",
                          (name, genre, booking_cost))
        print name, genre, booking_cost

    db.commit()


def add_bartenders():
    arr = bartenders.generate()

    for i in range(len(arr)):
        name = arr[i].name
        gender = arr[i].gender
        age = arr[i].age

        cursor.execute("""INSERT IGNORE INTO bartenders(name, gender, age)
                          VALUES(%s, %s, %s)""",
                          (name, gender, age))
        print name, gender, age

    db.commit()


def add_drinkers():
    arr = drinkers.generate()

    for i in range(len(arr)):
        name = arr[i].name
        addr = arr[i].addr
        city = arr[i].city
        gender = arr[i].gender
        phone = arr[i].phone
        age = arr[i].age

        cursor.execute("""INSERT IGNORE INTO drinkers(name, addr, city,
                                                      gender, phone, age)
                          VALUES(%s, %s, %s, %s, %s, %s)""",
                          (name, addr, city, gender, phone, age))

        print name, addr, city, gender, phone, age

    db.commit()


def add_night_clubs():
    arr = night_clubs.generate()

    for i in range(len(arr)):
        name = arr[i].name
        addr = arr[i].addr
        city = arr[i].city
        phone = arr[i].phone
        license = arr[i].license

        cursor.execute("""INSERT IGNORE INTO night_clubs(name, addr, city,
                                                         phone, license)
                       VALUES(%s, %s, %s, %s, %s)""",
                       (name, addr, city, phone, license))

        print name, addr, city, phone, license

    db.commit()


def add_beers():
    db.commit()


def main():
    add_deejays()
    add_bartenders()
    add_drinkers()
    add_night_clubs()
    add_beers()
    db.close()


if __name__ == "__main__":
    main()
