#!/usr/bin/python3
"""Fetch a single state from the database"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker as create_session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    sql_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(sql_engine)
    InitSession = create_session(bind=sql_engine)
    session = InitSession()
    states = session.query(State).first()

    if not states:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
