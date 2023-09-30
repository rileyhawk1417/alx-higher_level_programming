#!/usr/bin/python3
"""
Fetch states.id that match the state.name from the user
from the database
"""

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

    states = session.query(State).filter(State.name.like(sys.argv[4]))
    if states.count() != 1 or not states:
        print("Not found")
    else:
        print("{}".format(states.first().id))
