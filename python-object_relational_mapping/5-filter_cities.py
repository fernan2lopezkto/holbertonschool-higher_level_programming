#!/usr/bin/python3
""" Write a scriptss """

import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
        )

    cursor = db.cursor()

    select = "SELECT cities.name "
    fromm = "FROM cities "
    iner = "INNER JOIN states "
    onn = "ON cities.state_id = states.id "
    ordr = "ORDER BY cities.id;"

    cursor.execute(select + fromm + iner + onn + ordr)
    result = cursor.fetchall()

    for row in result:
        print(row, end="")
