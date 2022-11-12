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
    query_part_1 = "SELECT * FROM states WHERE name = "
    query_part_2 = "'{}' ORDER BY states.id".format(argv[4])
    cursor.execute(query_part_1 + query_part_2)
    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
