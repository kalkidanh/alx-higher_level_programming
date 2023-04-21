#!/usr/bin/python3
"""Script that returns a list of all cities on the DB"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Gets the state of the DB"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(City.state_id == State.id)
    for city, state in query.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name)i)

    session.commit()
    session.close()
