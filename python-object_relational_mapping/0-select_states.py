#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
""" documentation """

cur = conn.cursor()
""" documentation """

cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
""" documentation """

query_rows = cur.fetchall()
""" documentation """

for row in query_rows:
    """ documentation """
    print(row)
    
cur.close()
""" documentation """
conn.close()
""" documentation """