#!/usr/bin/python3
"""Select all states from database"""
import MySQLdb
import sys


def get_states(user_name, pass_word, database):
    """Function that gets all the states"""
    try:
        sql_db = MySQLdb.connect(
            host='localhost',
            user=user_name,
            passwd=pass_word,
            db=database,
            port=3306
        )
        selector = sql_db.cursor()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to MySQL server.")
        print("MySQL ERROR {}: {}".format(e.args[0], e.args[1]))

    try:
        selector.execute("SELECT * FROM states")
        sql_table = selector.fetchall()
        for rows in sql_table:
            print(rows)

    except MySQLdb.Error as e:
        print("MySQL ERROR {}: {}".format(e.args[0], e.args[1]))

    finally:
        selector.close()
        sql_db.close()


usage_msg = "Usage: python script.py <mysql_username>"
usage_msg += " <mysql_password> <database_name>"

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print(usage_msg)
    else:
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3],
        get_states(user, passwd, db)
