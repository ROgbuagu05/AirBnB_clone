#!/usr/bin/python3
'''Contains a function that converts the argument passed into a float
int or string type. Selection is based on regex patterns'''
import re


def check_type(arg):
    '''Checks arg variable and returns arg casted into a new type
    if criteria is met

    args:
        arg: a string variable

    Returns:
        arg casted to a float if possible
        arg casted to an int if possible
        arg as a string if the above is not possible
    '''
    pattern2 = re.search(r'^[\d]+\.[\d]+$', arg)
    pattern3 = re.search(r'^\d+$', arg)

    if pattern2:
        return float(arg)
    elif pattern3:
        return int(arg)
    else:
        return arg
