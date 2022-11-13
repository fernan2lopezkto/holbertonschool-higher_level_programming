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

    '''
    select = "SELECT cities.name "
    fromm = "FROM cities "
    iner = "INNER JOIN states "
    onn = "ON cities.state_id = states.id AND states.name = %s", (argv[4], )
    ordr = "ORDER BY cities.id;"
    '''

    cursor.execute("SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
            AND states.name = %s ORDER BY cities.id ASC", (argv[4], ))
    result = cursor.fetchall()

    count = 0

    for row in result:
        print(row[0], end="")
        count += 1
        if count < len(result):
            print(end=", ")
