#!/usr/bin/python3
'''A module containing a BaseModel class'''

from datetime import datetime
import json
import uuid


class BaseModel:
    '''A class that defines a BaseModel object'''

    def __init__(self, *args, **kwargs):
        '''Constructor method for BaseModel class'''

        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
        else:
            # if dictionary is not none or not empty
            for key, value in kwargs.items():
                # exclude __class__ attr
                if key != "__class__":
                    # set attr for each key/value pair in kwargs
                    if key in ["created_at", "updated_at"]:
                        self.__setattr__(key, datetime.fromisoformat(value))
                    else:
                        self.__setattr__(key, value)

    def __str__(self):
        '''String representation of BaseModel object'''
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        '''Method that updates the updated_at attribute'''
        self.updated_at = datetime.today()

    def to_dict(self):
        '''Returns the key/values of __dict__ of the instance'''
        self.__dict__["__class__"] = "BaseModel"
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
