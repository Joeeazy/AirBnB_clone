#!/usr/bin/pytho3
"""
Imports the uuid module for generating unique identifiers
datetime class for working with dates and times as dt
"""
from uuid import uuid4
from datetime import datetime as dt
import models


# Defines the BaseModel class
class BaseModel:
    """
    an __init__ method
    that initializes the instance with a
    unique id, creation timestamp (created_at),
    and update timestamp (updated_at).
    """
    def __init__(self, **key_args):
        utc_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = dt.utcnow()
        self.updated_at = dt.utcnow()

        if key_args:
            for key, value in key_args.items():
                if key == "__class__":
                    continue

                if key in {"created_at", "updated_at"}:
                    setattr(self, key, dt.strptime(value, utc_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    """
    A __str__ method to provide a string representation of the object.
    It prints the class name, id, and the object's dictionary.
    """
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    """
    A save method that updates the updated_at attribute
    to the current timestamp.
    """
    def save(self):
        self.updated_at = dt.utcnow()
        models.storage.save()

    """
    A to_dict method that converts the object into a dictionary. 
    it includes class information, creation and
    update timestamps formatted as strings.
    """
    def to_dict(self):
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()

        return result_dict
