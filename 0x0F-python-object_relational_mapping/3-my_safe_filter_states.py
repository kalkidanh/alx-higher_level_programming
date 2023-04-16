#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
that matches a giver argument protected from SQL injection attacks
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
                WHERE name LIKE BINARY %(state_namae)s \
                ORDER BY states.id ASC", {'state_name': argv[4]})

    for state in c.fetchall():
        print(state)

    c.close()
    db.close()
