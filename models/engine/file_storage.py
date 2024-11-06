#!/usr/bin/python3
"""FileStorage module for managing JSON storage of objects"""

import json
from models.base_model import BaseModel
from models.state import State
# Add other imports as necessary for the project

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects in storage"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file at __file_path"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass

    def close(self):
        """Calls reload() for deserializing the JSON file to objects"""
        self.reload()
