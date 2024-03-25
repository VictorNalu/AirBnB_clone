#!/usr/bin/python3
"""fileStorage """
import json
import os


class FileStorage:
    """FileStorage class"""

    def __init__(self):
        """Constructor"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """all method"""
        return self.__objects

    def new(self, obj):
        """new"""
        obj_class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(obj_class_name, obj.id)
        self.__objects[obj_key] = obj.to_dict()

    def save(self):
        """save"""
        obj_dict = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(obj_dict)

    def reload(self):
        """reload"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = file.read()

                self.__objects = json.loads(obj_dict)
