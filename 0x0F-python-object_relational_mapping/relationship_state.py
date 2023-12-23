#!/usr/bin/python3
"""relationship state"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class with id and name attrs of each state
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                autoincrement="auto"
                )
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")
