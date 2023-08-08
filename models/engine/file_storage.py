#!/usr/bin/python3
'''Module containing FileStorage class'''
import json
from models.engine.obj_parser import obj_parser


class FileStorage:
    '''A class that serializes and deserializes to and from a json string'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns private class attribute __objects'''
        return self.__objects

    def new(self, obj):
        '''sets obj key in __objects'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serialize object to json file'''
        # first convert BaseModel object's to dict and store in new_obj
        new_obj = {}
        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()

        # Serialize new_obj to json file
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_obj, f)

    def reload(self):
        '''Deserialize json string from file'''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                # Deserialize json file to dict containing dicts(new_objs)
                new_objs = json.load(f)

                # Instantiate all objects from new_objs
                self.__objects = obj_parser(new_objs)
        except Exception:
            pass
