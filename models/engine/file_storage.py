#!/usr/bin/python3
"""fileStorage """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """FileStorage class"""

    
        
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        return (FileStorage.__objects)

    def new(self, obj):
        """new"""
        obj_class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """save"""
        objects_copy = FileStorage.__objects
        objects_dict = {
            obj: objects_copy[obj].to_dict() for obj in objects_copy.keys()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """reload"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
