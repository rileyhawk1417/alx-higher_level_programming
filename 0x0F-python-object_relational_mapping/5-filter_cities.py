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
    selector.execute("SELECT cities.name FROM cities \
    LEFT JOIN states ON states.id = cities.state_id \
    WHERE states.name LIKE BINARY (%s) \
    ORDER BY cities.id ASC", (given_state_name,))
    sql_table = selector.fetchall()

    end_cities = ""
    start_cities = ""

    for row in sql_table:
        start_cities = start_cities + end_cities + row[0]
        end_cities = ", "
    print(start_cities)
    selector.close()
    sql_db.close()
