#!/usr/bin/python3
"""
Fetch the City by State from the database
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker as create_session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    sql_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(sql_engine)
    InitSession = create_session(bind=sql_engine)
    session = InitSession()

    state_city = session.query(State, City).\
        join(City, State.id == City.state_id).\
        order_by(City.id)
    for state, city, in state_city:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
