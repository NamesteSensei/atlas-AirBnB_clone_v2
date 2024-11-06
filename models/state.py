#!/usr/bin/python3
"""State module containing the State class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """Represents a state in the database"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Return list of City instances linked to the current State"""
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]
