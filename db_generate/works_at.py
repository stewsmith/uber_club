import random
import MySQLdb
from database import Database

def create_works_at():
    db = Database().connect()
    cursor = db.cursor()

    bartenders = db.select("SELECT name FROM bartenders")
    night_clubs = db.select("SELECT name FROM night_clubs")

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
