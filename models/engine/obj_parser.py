#!/usr/bin/python3
'''A module containing the obj_parser function'''
from models.base_model import BaseModel


def obj_parser(obj):
    '''Takes in obj which is a dictionary containing the dictionaries
    of objects and creates an instance from these dictionaries and returns
    the instances in a dictionary'''
    new_obj = {}
    for key, value in obj.items():

        if value["__class__"] == "BaseModel":
            tmp = BaseModel(**value)
            new_obj[key] = tmp

    return new_obj
