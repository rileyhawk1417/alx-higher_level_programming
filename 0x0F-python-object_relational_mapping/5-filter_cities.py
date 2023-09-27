#!/usr/bin/python3
"""Get all cities, with states from Database"""
import MySQLdb
import sys

if __name__ == "__main__":
    sql_db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    given_state_name = sys.argv[4]
    selector = sql_db.cursor()
    query = "SELECT cities.name, FROM cities \
    LEFT JOIN states ON states.id = cities.state_id \
    WHERE states.name LIKE BINARY (%s) \
    ORDER BY cities.id ASC".format(given_state_name)
    selector.execute(query)
    sql_table = selector.fetchall()

    for rows in sql_table:
        print(rows)
    selector.close()
    sql_db.close()
