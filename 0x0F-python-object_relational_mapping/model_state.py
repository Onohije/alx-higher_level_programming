#!/usr/bin/python3
"""Contains the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Defines a city of a state, extends the Base
    class from SQLAlchemy's declarative_base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', backref='cities')
