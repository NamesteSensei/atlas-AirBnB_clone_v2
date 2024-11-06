#!/usr/bin/python3
"""This module instantiates a storage object based on environment settings"""

from os import getenv

# Import the storage engines conditionally
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Call reload to load data or setup database
storage.reload()
