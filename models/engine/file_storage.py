#!/usr/bin/python3
"""Filestorage class"""
import json
import models

import sys


class FileStorage:
    """A class for (de)serialisation to and from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(
                FileStorage.__file_path,
                "r",
            ) as f:
                FileStorage.__loaded_objects = json.load(f)
                for key, obj_dict in FileStorage.__loaded_objects.items():
                    class_name = obj_dict["__class__"]
                    class_ = getattr(models, class_name)
                    obj = class_(
                        **obj_dict
                    )  # Instantiate object with deserialized data
                    FileStorage.__objects[key] = (
                        obj  # Add object to __objects dictionary
                    )
        except FileNotFoundError:
            pass
