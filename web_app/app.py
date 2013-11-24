from flask import Flask, render_template, request, jsonify
from database import Database

db = Database().connect()
app = Flask(__name__)

@app.route("/")
def index():
    data = db.select("SELECT name FROM night_clubs")
    return render_template('index.html', data=data)

@app.route('/clubs', methods=['GET'])
def my_form_post():
    night_club = request.args.get('name')
    bartenders = db.select("""SELECT bartender FROM works_at
                           WHERE night_club='%s'""" % night_club)
    beers = db.select("""SELECT beer FROM sells
                           WHERE night_club='%s'""" % night_club)
    ret_data = {"bartenders": bartenders, "beers": beers}
    return jsonify(ret_data)

@app.route('/pumped', methods=['POST'])
def pumped():
    night_club = request.form['night_club']
    bartenders = request.form['bartenders']
    date = request.form['date']
    beers = request.form['beers']
    print "------------y-----------------"
    print night_club, bartenders, date, beers
    return "OK", 200

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
