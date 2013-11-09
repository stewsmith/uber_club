import MySQLdb
import names

conn = MySQLdb.connect(host="cs336-23.cs.rutgers.edu",
                       user="csuser",
                       passwd="cs97f462",
                       db="csuser")

curr = conn.cursor()

numrows = 1000

for i in range(numrows):
    curr.execute("INSERT INTO stem VALUE (%s)", names.get_full_name())
    conn.commit()

conn.close()
