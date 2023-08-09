#!/usr/bin/python3
'''A module containing a BaseModel class'''

import json
import models
import uuid
from datetime import datetime


class BaseModel:
    '''A class that defines a BaseModel object'''

    def __init__(self, *args, **kwargs):
        '''Constructor method for BaseModel class'''

        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)       # updates __objects var of storage
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
        var = self.__class__.__name__
        return "[{}] ({}) {}".format(var, self.id, self.__dict__)

    def save(self):
        '''Method that updates the updated_at attribute'''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        '''Returns the key/values of __dict__ of the instance'''
        temp = self.__dict__
        temp["__class__"] = "{}".format(self.__class__.__name__)
        if isinstance(temp["created_at"], datetime):        
            temp["created_at"] = self.created_at.isoformat()
        if isinstance(temp["updated_at"], datetime):
            temp["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
