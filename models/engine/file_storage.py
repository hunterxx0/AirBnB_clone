#!/usr/bin/python3
""" Base class """
import json
from os import path
import datetime
import copy
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        x = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[x] = obj

    def save(self):
        if self.__file_path:
            dt = {}
            for key, value in FileStorage.__objects.items():
                dt[key] = value.to_dict()
            j_str = json.dumps(dt)
            with open(self.__file_path, mode='w', encoding='utf-8') as f:
                f.write(j_str)

    def reload(self):
        if FileStorage.__file_path and path.exists(
                FileStorage.__file_path
        ) and path.getsize(FileStorage.__file_path):
            with open(self.__file_path, encoding='utf-8') as f:
                tmp = json.loads(f.read())
                for key, value in tmp.items():
                    FileStorage.__objects[key] = eval(
                        value["__class__"])(**value)
