#!/usr/bin/python3
"""Defines the State class for HBNB project"""

from models.base_model import BaseModel
from models import storage_type
from models.city import City

class State(BaseModel):
    """State class representing a state in the database"""

    name = ""

    if storage_type != 'db':
        @property
        def cities(self):
            """Returns list of City instances with state_id equal to the current State.id"""
            return [city for city in storage.all(City).values() if city.state_id == self.id]
