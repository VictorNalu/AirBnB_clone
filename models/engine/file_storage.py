#!/usr/bin/python3
"""fileStorage """
import json
import os
import models


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        return FileStorage.__objects

    def new(self, obj):
        """new"""
        obj_class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[obj_key] = obj

    def save(self):
        """save"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """reload"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
