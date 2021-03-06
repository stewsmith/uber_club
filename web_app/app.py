from flask import Flask, render_template, request, jsonify
from database import Database
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    db = Database().connect()
    data = db.select("SELECT name FROM night_clubs")
    db.close()
    return render_template('index.html', data=data)


@app.route('/nightclub', methods=['GET'])
def got_nightclub():
    db = Database().connect()
    night_club = request.args['night_club']
    bartenders = db.select("""SELECT bartender FROM works_at
                           WHERE night_club='%s'""" % night_club)
    beers = db.select("""SELECT beer FROM sells
                      WHERE night_club='%s'""" % night_club)
    db.close()
    #print night_club, bartenders, beers
    return render_template('results.html', night_club=night_club,
                           bartenders=bartenders, beers=beers)


def str_to_date(str_date):
    d = map(int, str_date.split("-"))
    date = datetime.date(d[0], d[1], d[2])
    return date


@app.route('/pumped', methods=['POST'])
def pumped():
    db = Database().connect()
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
                                  """ % (night_club, day_of_week,
                                         format_list(beers))
    top_three_bartenders_query = """SELECT bartender
                                    FROM( SELECT bartender
                                    FROM served s
                                    WHERE night_club='%s'
                                    AND DAYOFWEEK(date)=%s
                                    GROUP BY bartender
                                    ORDER BY avg(tip) DESC) a
                                    WHERE a.bartender in (%s)
                                    LIMIT 3
                                    """ % (night_club, day_of_week,
                                           format_list(bartenders))
    avg_age_on_date_query = """SELECT avg(a) FROM(
                               SELECT date, avg(age) as a
                               FROM (SELECT drinker, date
                               FROM frequented
                               WHERE night_club='%s' AND DAYOFWEEK(date)=%s
                               ORDER BY date) r1, drinkers d
                               WHERE r1.drinker=d.name
                               GROUP BY date) r2;
                               """ % (night_club, day_of_week)
    recommended_deejay_query = """SELECT deejay
                                  FROM (SELECT * FROM performed_at p
                                  WHERE night_club='%s'
                                  AND DAYOFWEEK(date)=%s) a, frequented f
                                  WHERE f.night_club='%s' AND f.date=a.date
                                  GROUP BY f.date
                                  ORDER BY count(drinker) * cover_fee DESC
                                  LIMIT 1""" % (night_club, day_of_week, night_club)
    queries = [num_drinkers_query, avg_cover_fee_revenue_query,
               avg_num_men_query, avg_num_women_query,
               bottom_three_beers_query, top_three_bartenders_query,
               avg_age_on_date_query, recommended_deejay_query]

    num_drinkers_on_date = int(db.select(num_drinkers_query)[0])
    avg_cover_fee_revenue = int(db.select(avg_cover_fee_revenue_query)[0])
    avg_num_men = int(db.select(avg_num_men_query)[0])
    avg_num_women = int(db.select(avg_num_women_query)[0])
    MF_ratio = "%.2f" % (avg_num_men / float(avg_num_men + avg_num_women))
    avg_age_on_date = int(db.select(avg_age_on_date_query)[0])
    bottom_three_beers = db.select(bottom_three_beers_query)
    top_three_bartenders = db.select(top_three_bartenders_query)
    recommended_cover_fee = avg_cover_fee_revenue / num_drinkers_on_date
    recommended_deejay = db.select(recommended_deejay_query)[0]

    dj_genre_query = """SELECT genre
                        FROM deejays
                        WHERE name='%s'""" % (recommended_deejay)
    dj_genre = db.select(dj_genre_query)[0]

    # print num_drinkers_on_date
    # print avg_cover_fee_revenue
    # print recommended_cover_fee
    # print avg_num_men
    # print avg_num_women
    # print avg_age_on_date
    # print bottom_three_beers
    # print top_three_bartenders

    data = {
        "num_drinkers_on_date": num_drinkers_on_date,
        "avg_cover_fee_revenue": avg_cover_fee_revenue,
        "recommended_cover_fee": recommended_cover_fee,
        "avg_num_men": avg_num_men,
        "avg_num_women": avg_num_women,
        "MF_ratio": MF_ratio,
        "avg_age_on_date": avg_age_on_date,
        "bottom_three_beers": bottom_three_beers,
        "top_three_bartenders": top_three_bartenders,
        "recommended_dj": recommended_deejay,
        "dj_genre": dj_genre,
        "queries": queries
    }
    db.close()
    return jsonify(data)


def format_list(list):
    res = ""
    for el in list:
        res += "\"%s\", " % el
    return res[0:-2]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(host='0.0.0.0', port=5000, debug=True)
