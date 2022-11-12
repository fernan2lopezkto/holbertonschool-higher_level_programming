#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    password=argv[2],
    database=argv[3]
    )

cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
result = cursor.fetchall()

for row in result:
    print(row)