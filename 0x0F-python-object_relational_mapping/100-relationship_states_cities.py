#!/usr/bin/python3
"""
Add a new city & state linked to each other in
the database
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

    state = State(name="California")
    city = City(name="San Fransisco")
    session.cities.append(city)
    session.commit()
    session.close()
