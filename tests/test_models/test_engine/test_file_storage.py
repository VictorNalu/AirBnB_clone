#!/usr/bin/python3
"""FileStorage module"""

import json
import os


class FileStorage:
    """FileStorage class for handling file operations"""

    def __init__(self):
        """Initialize FileStorage"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects"""
        obj_class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(obj_class_name, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serialize __objects to JSON and save to file"""
        obj_dict = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(obj_dict)

    def reload(self):
        """Deserialize JSON from file and reload __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = file.read()
                self.__objects = json.loads(obj_dict)
