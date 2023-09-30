#!/usr/bin/python3
"""State model that will be used with SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inherits from Delcarative Base
    then links to MYSQL table 'states'
    Attr:
        id Integer
        name String
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
