#!/usr/bin/python3
"""Contains class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """ updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict

    def __str__(self):
        """String representation of the BaseModel class"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
