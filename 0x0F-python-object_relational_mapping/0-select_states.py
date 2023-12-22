#!/usr/bin/python3
"""script lists all states from a database"""

import MySQLdb
import sys

if __name__ == "__main__":
    
    database = MySQLdb.Connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3],
                               port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for row in states:
        print(row)
