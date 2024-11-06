#!/usr/bin/python3
"""FileStorage class for managing JSON storage."""
import json
from models.state import State
from models.city import City
# Other imports as needed

class FileStorage:
    """Handles storage of all class instances with JSON files."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        # Return dictionary of objects by class or all objects if cls is None

    def new(self, obj):
        # Add object to storage dictionary

    def save(self):
        # Serialize __objects to JSON file

    def reload(self):
        # Deserialize JSON file to __objects

    def close(self):
        """Deserializes the JSON file to objects."""
        self.reload()
