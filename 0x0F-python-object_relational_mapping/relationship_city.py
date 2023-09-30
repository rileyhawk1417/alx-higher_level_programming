#!/usr/bin/python3
"""City model that will be used with SQLAlchemy"""

from sqlalchemy import \
    Column, ForeignKey,\
    Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """City class inherits from Delcarative Base
    then links to MYSQL table 'cities'
    Attr:
        id Integer
        name String
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
