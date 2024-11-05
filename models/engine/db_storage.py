#!/usr/bin/python3
"""DBStorage class for storage management with MySQL database"""

from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """Handles long-term storage of all class instances with a MySQL database"""

    # other methods like all(), new(), save(), reload() go here

    def close(self):
        """Removes the current SQLAlchemy session"""
        self.__session.remove()
