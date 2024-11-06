#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel, Base
from models.city import City
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Represents a state for a MySQL database."""
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if storage_type != 'db':
        @property
        def cities(self):
            """Returns a list of City instances with state_id equal to the current State id."""
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
