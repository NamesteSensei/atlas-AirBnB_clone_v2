#!/usr/bin/python3
"""This module defines the City class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """Represents a city for a MySQL database"""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
