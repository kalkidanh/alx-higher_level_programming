#!/usr/bin/python3
"""Script that lists all states from the hbtn_0e_0_usa database"""

import MYSQLdb
from sys import argv

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
