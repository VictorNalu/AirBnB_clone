#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    This class represents a simple file-based storage mechanism for managing objects.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary containing objects indexed by a combination
                          of their class name and ID.

    Methods:
        all(self):
            Returns all objects stored in the __objects dictionary.

        new(self, obj):
            Adds a new object to the __objects dictionary.

        save(self):
            Saves objects from __objects to the JSON file specified by __file_path.

        reload(self):
            Loads objects from the JSON file specified by __file_path into __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the __objects dictionary.

        Returns:
            dict: A dictionary containing all objects stored in __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added to __objects.
        """
        obj_class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Saves objects from __objects to the JSON file specified by __file_path.
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Loads objects from the JSON file specified by __file_path into __objects.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        inst = cls(**value)
                        FileStorage.__objects[key] = inst
                except Exception:
                    pass

