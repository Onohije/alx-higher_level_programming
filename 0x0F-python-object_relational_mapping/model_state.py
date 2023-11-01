#!/usr/bin/python3
"""
This script defines a State class and a Base
class to work with SQLAlchemy ORM.
It also creates the necessary database tables
based on the defined classes.
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class representing a state, with each instances
    with its own unique id and name."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
