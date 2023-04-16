#!/usr/bin/python3
"""Script that takes state as an argument and
lists all cities using the database hbtn_0e_4_usa
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
    c.execute("SELECT cities.name \
            FROM cities INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC", [argv[4]])

    print(", ".join([state[0] for state in c.fetchall()]))

    c.close()
    db.close()
