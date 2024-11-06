#!/usr/bin/python3
"""This module defines a base class for all models in our application"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

Base = declarative_base()

class BaseModel:
    """A base class for all HBNB models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Converts instance into dict format"""
        dictionary = {key: value for key, value in self.__dict__.items()}
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
