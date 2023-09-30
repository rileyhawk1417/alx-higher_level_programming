#!/usr/bin/python3
"""
List States and Cities from the database
<state id>: <state name>
<tabulation><city id>: <city name>
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker as create_session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    sql_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
    Base.metadata.create_all(sql_engine)
    InitSession = create_session(bind=sql_engine)
    session = InitSession()

    states = session.query(City).order_by(City.id)
    for city in states:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
