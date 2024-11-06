#!/usr/bin/python3
"""Defines the State class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """Represents a state for MySQL database."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Return the list of City instances with state_id matching current state id."""
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]
