#!/usr/bin/python3
"""script lists all states from a database"""

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    
    if len(argv) != 4:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    dataBase = argv[3]

    database = MySQLdb.Connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3],
                               port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for row in states:
        print(row)
