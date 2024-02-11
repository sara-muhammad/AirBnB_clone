#!/usr/bin/python3
"""This is the File Storage module"""
import json
import os
from models.base_model import BaseModel

class FileStorage():
    """the file storage class"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key 
        <obj class name>.id
        """
        cls_name = obj.__class__.__name__
        key = "{}.{}".format(cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """return the __objects"""
        return FileStorage.__objects
    


    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)

        """
        new_dict = FileStorage.__objects
        dict_form = {}
        for i in new_dict.items():
            dict_form[i] = new_dict[i].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dumps( dict_form, file)

    def reload(self):
        """
        deserializes the JSON file
        """

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    new_dict = json.load(file)
                    for k, v in new_dict.items():
                        class_name, obj_id = k.split('.')

                        cls = eval(class_name)

                        instance = cls(**v)

                        FileStorage.__objects[k] = instance
                except FileNotFoundError:
                    return

    