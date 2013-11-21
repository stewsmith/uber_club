import random
import MySQLdb

def db_select(query):
    db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                         user="csuser",
                         passwd="cs97f462",
                         db="nightclubconsultants")

    cursor = db.cursor()
    cursor.execute(query)

    ans = []
    for row in list(cursor.fetchall()):
        ans.append(row[0])

    db.close()
    return ans

def create_sells():
    beers = db_select("SELECT name FROM beers")
    night_clubs = db_select("SELECT name FROM night_clubs")

    db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                         user="csuser",
                         passwd="cs97f462",
                         db="nightclubconsultants")

    cursor = db.cursor()

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

    db.close()


