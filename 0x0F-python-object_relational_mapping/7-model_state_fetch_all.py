#!/usr/bin/python3
"""Script that returns a list of all states from the DB"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name == "__main__":
    """Gets the state of the DB"""
    engine = create_engine('mysql+mysqldb://{}:[]@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
