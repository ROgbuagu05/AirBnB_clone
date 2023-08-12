#!/usr/bin/python3
'''A module containing the obj_parser function'''
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


def obj_parser(obj):
    '''Takes in obj which is a dictionary containing the dictionaries
    of objects and creates an instance from these dictionaries and returns
    the instances in a dictionary'''
    new_obj = {}
    for key, value in obj.items():

        if value["__class__"] == "BaseModel":
            new_obj[key] = BaseModel(**value)
        elif value["__class__"] == "User":
            new_obj[key] = User(**value)
        elif value["__class__"] == "State":
            new_obj[key] = State(**value)
        elif value["__class__"] == "City":
            new_obj[key] = City(**value)
        elif value["__class__"] == "Amenity":
            new_obj[key] = Amenity(**value)
        elif value["__class__"] == "Review":
            new_obj[key] = Review(**value)
        elif value["__class__"] == "Place":
            new_obj[key] = Place(**value)
    return new_obj
