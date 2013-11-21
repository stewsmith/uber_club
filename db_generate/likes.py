import MySQLdb
import random

db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                     user="csuser",
                     passwd="cs97f462",
                     db="nightclubconsultants")
cursor = db.cursor()

def db_select(query):
    cursor.execute(query)
    res = []
    for row in list(cursor.fetchall()):
        res.append(row[0])

    return res


def create_likes():
    drinkers = db_select("SELECT name FROM drinkers")
    beers = db_select("SELECT name FROM beers")

    for i in range(len(drinkers)):
        drinker = drinkers[i]

        j, num = 0, random.randint(1, 7)
        while j < num:
            beer = beers[random.randint(0, len(beers) - 1)]
            try:
                cursor.execute("""INSERT INTO likes(drinker, beer)
                               VALUES(%s, %s)""", (drinker, beer))
                print drinker, beer
            except MySQLdb.IntegrityError:
                j -= 1
            j += 1

    db.close()
