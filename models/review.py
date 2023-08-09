#!/usr/bin/python3
'''A module defining a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''A class defining a Review object'''

    place_id = ""
    user_id = ""
    text = ""
