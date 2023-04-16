#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
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
    c.execute("SELECT * \
                FROM states \
                ORDER BY states.id ASC")

    for state in c.fetchall():
        if state[1].startswith(N):
            print(state)

    c.close()
    db.close()
