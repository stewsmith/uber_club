import MySQLdb

class Database:
    def __init__(self):
        self.db = None

    def connect(self):
        db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                             user="csuser",
                             passwd="cs97f462",
                             db="nightclubconsultants")
        self.db = db
        return self

    def select(self, query):
        """Return array of the rows of a 'SELECT attr FROM table' query."""
        cursor = self.db.cursor()
        cursor.execute(query)
        res = []
        for row in list(cursor.fetchall()):
            res.append(row[0])

        return res

    def cursor(self):
        return self.db.cursor()

    def close(self):
        self.db.close()
