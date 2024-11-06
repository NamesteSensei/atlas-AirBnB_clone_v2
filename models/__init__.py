#!/usr/bin/python3
"""Module initializer for storage"""

from os import getenv

# Select storage type based on environment variable
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
