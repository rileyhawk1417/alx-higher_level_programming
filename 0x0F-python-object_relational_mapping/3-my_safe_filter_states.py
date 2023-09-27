#!/usr/bin/python3
"""Filter states from user input & display all values"""
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
    query = "SELECT * FROM states WHERE name = (%s)\
    ORDER BY states.id ASC".format(given_state_name)
    selector.execute(query)
    sql_table = selector.fetchall()

    for rows in sql_table:
        print(rows)
    selector.close()
    sql_db.close()
