#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Gets all states from the database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
