#!/usr/bin/python3
"""DBStorage class for storage management with MySQL database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv

class DBStorage:
    """Handles long-term storage of all class instances with a MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

    # other methods like all(), new(), save(), reload() go here

    def close(self):
        """Removes the current SQLAlchemy session"""
        self.__session.remove()
