#!/usr/bin/python3
"""DBStorage module for managing MySQL storage of objects"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
import os

class DBStorage:
    """Interacts with the MySQL database for storage and retrieval"""
    
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{os.getenv('HBNB_MYSQL_USER')}:{os.getenv('HBNB_MYSQL_PWD')}"
            f"@{os.getenv('HBNB_MYSQL_HOST')}/{os.getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the current session"""
        objects = {}
        if cls:
            results = self.__session.query(cls).all()
        else:
            results = self.__session.query(State).all() + self.__session.query(City).all()
        for obj in results:
            key = f"{obj.__class__.__name__}.{obj.id}"
            objects[key] = obj
        return objects

    def new(self, obj):
        """Add an object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes in the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()
