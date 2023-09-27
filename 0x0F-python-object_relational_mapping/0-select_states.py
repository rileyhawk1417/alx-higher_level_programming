#!/usr/bin/python3
"""Select all states from database"""
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

    selector = sql_db.cursor()
    selector.execute("SELECT * FROM states")
    sql_table = selector.fetchall()

    for rows in sql_table:
        print(rows)
    selector.close()
    sql_db.close()
