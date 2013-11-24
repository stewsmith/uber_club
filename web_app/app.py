from flask import Flask, render_template, request, jsonify
from database import Database
import datetime

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


def str_to_date(str_date):
    d = map(lambda x: int(x), str_date.split("-"))
    date = datetime.date(d[0], d[1], d[2])
    return date

@app.route('/pumped', methods=['POST'])
def pumped():
    json = request.get_json()
    night_club = json['night_club']
    bartenders = json['bartenders']
    date = str_to_date(json['date'])
    day_of_week = date.weekday() + 2
    beers = json['beers']
    # DAYOFWEEK(date)=7 is Saturday in SQL
    num_drinkers_query = """SELECT AVG(num)
                            FROM (SELECT COUNT(*) as num, date
                            FROM frequented
                            WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                            GROUP BY date) a;""" % (night_club, day_of_week)
    avg_cover_fee_revenue_query = """SELECT AVG(revenue)
                             FROM (SELECT COUNT(*) as num, date,
                             COUNT(*)*cover_fee AS revenue, cover_fee
                             FROM frequented
                             WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                             GROUP BY date) a;""" % (night_club, day_of_week)
    avg_num_men_query = """SELECT AVG(num)
                           FROM (SELECT COUNT(*) AS num, date
                           FROM frequented f
                           WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                           AND f.drinker IN (SELECT name FROM drinkers WHERE gender='M')
                           GROUP BY date) a;""" % (night_club, day_of_week)
    avg_num_women_query = """SELECT AVG(num)
                             FROM (SELECT COUNT(*) AS num, date
                             FROM frequented f
                             WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                             AND f.drinker IN (SELECT name FROM drinkers WHERE gender='F')
                             GROUP BY date) a;""" % (night_club, day_of_week)
    bottom_three_beers_query = """SELECT beer
                                  FROM (SELECT beer
                                  FROM served s
                                  WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                                  GROUP BY beer
                                  ORDER BY count(*) ASC) a
                                  WHERE a.beer in (%s)
                                  LIMIT 3;
                                  """ % (night_club, day_of_week, format_list(beers))
    top_three_bartenders_query = """SELECT bartender
                                    FROM( SELECT bartender
                                    FROM served s
                                    WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                                    GROUP BY bartender
                                    ORDER BY avg(tip) DESC) a
                                    WHERE a.bartender in (%s)
                                    LIMIT 3
                                    """ % (night_club, day_of_week, format_list(bartenders))
    avg_age_on_date_query = """SELECT avg(a) FROM(
                               SELECT date, avg(age) as a
                               FROM (SELECT drinker, date
                               FROM frequented
                               WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                               ORDER BY date) r1, drinkers d
                               WHERE r1.drinker=d.name
                               GROUP BY date) r2;""" % (night_club, day_of_week)

    num_drinkers_on_date = int(db.select(num_drinkers_query)[0])
    avg_cover_fee_revenue = int(db.select(avg_cover_fee_revenue_query)[0])
    avg_num_men = int(db.select(avg_num_men_query)[0])
    avg_num_women = int(db.select(avg_num_women_query)[0])
    avg_age_on_date = int(db.select(avg_age_on_date_query)[0])
    bottom_three_beers = db.select(bottom_three_beers_query)
    top_three_bartenders = db.select(top_three_bartenders_query)
    recommended_cover_fee = avg_cover_fee_revenue / num_drinkers_on_date
    print num_drinkers_on_date
    print avg_cover_fee_revenue
    print recommended_cover_fee
    print avg_num_men
    print avg_num_women
    print avg_age_on_date
    print bottom_three_beers
    print top_three_bartenders
    return "OK", 200

def format_list(list):
    res = ""
    for el in list:
        res += "'%s', " % el
    return res[0:-2]

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
