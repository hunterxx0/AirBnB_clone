#!/usr/bin/python3
""" Base class """
import uuid
import datetime


class BaseModel:
    """ BaseModel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value, _, us = value.partition(".")
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT\
%H:%M:%S')
                        us = int(us.rstrip("Z"), 10)
                        value = value + datetime.timedelta(microseconds=us)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        dt = dict(self.__dict__)
        dt['created_at'] = self.created_at.isoformat()
        dt['updated_at'] = self.updated_at.isoformat()
        dt["__class__"] = "BaseModel"
        return dt