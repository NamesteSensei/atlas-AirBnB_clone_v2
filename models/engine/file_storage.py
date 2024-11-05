#!/usr/bin/python3
"""FileStorage class for storage management in JSON format"""

import json

class FileStorage:
    """Handles long-term storage of all class instances in JSON format"""

    # other methods like all(), new(), save(), reload() go here

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()
