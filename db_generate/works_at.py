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

def create_works_at():
    bartenders = db_select("SELECT name FROM bartenders")
    night_clubs = db_select("SELECT name FROM night_clubs")

    db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                         user="csuser",
                         passwd="cs97f462",
                         db="nightclubconsultants")

    cursor = db.cursor()

    #Between 3 and 12 bartenders per night_club
    for night_club in night_clubs:
        j = 0
        num = random.randint(3, 12)
        while j < num:
            bartender = bartenders[random.randint(0, (len(bartenders) - 1))]

            try:
                cursor.execute("""INSERT INTO works_at(bartender, night_club)
                            VALUES(%s, %s)""",
                            (bartender, night_club))
                print bartender, night_club
            except MySQLdb.IntegrityError:
                j -= 1

            j +=1

    db.close()


