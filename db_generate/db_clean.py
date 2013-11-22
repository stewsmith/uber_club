import MySQLdb

db = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                     user="csuser",
                     passwd="cs97f462",
                     db="nightclubconsultants")

cursor = db.cursor()
cursor.execute("TRUNCATE TABLE bartenders")
cursor.execute("TRUNCATE TABLE beers")
cursor.execute("TRUNCATE TABLE deejays")
cursor.execute("TRUNCATE TABLE drinkers")
cursor.execute("TRUNCATE TABLE frequented")
cursor.execute("TRUNCATE TABLE likes")
cursor.execute("TRUNCATE TABLE night_clubs")
cursor.execute("TRUNCATE TABLE performed_at")
cursor.execute("TRUNCATE TABLE sells")
cursor.execute("TRUNCATE TABLE served")
cursor.execute("TRUNCATE TABLE works_at")

db.commit()
db.close()
