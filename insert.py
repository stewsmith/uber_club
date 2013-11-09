import MySQLdb

conn = MySQLdb.connect(host= "cs336-23.cs.rutgers.edu",
                user="csuser",
                passwd="cs97f462",
                db="csuser")

curr = conn.cursor()

curr.execute("""INSERT INTO stem VALUE (%s)""",(90))
conn.commit()

conn.close()
