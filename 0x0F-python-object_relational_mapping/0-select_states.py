#!/usr/bin/python3
"""Script that lists all states from the hbtn_0e_0_usa database"""

import MYSQLdb
from sys import argv

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * \
            FROM states \
            ORDER BY states.id ASC")
    [print(state) for state in c.fetchall()]
