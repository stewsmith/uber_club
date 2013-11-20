from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

def queryDB():
    db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                         user="csuser",
                         passwd="cs97f462",
                         db="nightclubconsultants")

    cursor = db.cursor()

    query = "SELECT name FROM night_clubs"
    cursor.execute(query)
    ans = []
    for row in list(cursor.fetchall()):
        ans += list(row)
    return ans

@app.route("/")
def index():
    data = queryDB()
    print data
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
