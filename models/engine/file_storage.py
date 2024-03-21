#!/usr/bin/python3
"""Filestorage class"""
import sys
import json



class FileStorage:
    """A class for (de)serialisation to and from a JSON file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                loaded_objects = json.load(f)
                for key, obj_dict in loaded_objects.items():  # Iterate over key-value pairs
                    class_name, obj_id = key.split('.')
                    module_name = "models.base_model"
                    if module_name in sys.modules:
                        module = sys.modules[module_name]
                    else:
                        module = __import__(module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
            
                