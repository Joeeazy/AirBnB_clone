#!/usr/bin/python3
"""
Module for handling data serialization and deserialization
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage class manages the storage, 
    serialization, and deserialization of data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
        Adds an object to the __objects dictionary with a key formatted as 
        <object class name>.id.
        """
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the __objects dictionary, 
        providing access to all stored objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes the __objects dictionary into JSON format and 
        saves it to the file specified by __file_path.
        """
        all_objects = FileStorage.__objects

        obj_dict = {}

        for obj_key in all_objects.keys():
            obj_dict[obj_key] = all_objects[obj_key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to restore objects.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
