#!/usr/bin/python3
'''Module containing the class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''class defining a User object'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
