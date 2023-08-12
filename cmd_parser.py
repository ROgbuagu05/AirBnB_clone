#!/usr/bin/python3
'''Module containing a function that parser's a string
and returns a reformatted string'''
import re


def cmd_parser(arg):
    '''Re-formats a string

    Args:
        arg: a string to be formatted

    Return:
        Formatted string
    '''

    class_list = ["Amenity", "BaseModel", "City", "Place", "Review",
                  "State", "User"]

    # Split class name from rest of argument
    arg_list = arg.split('.')

    # if a valid class name is not given, return 1
    if arg_list[0] not in class_list:
        return (1)

    # if a valid class name was given, continue processing arg
    arg_list[1] = re.sub(r'[(]', ' ', arg_list[1])
    arg_list[1] = re.sub(r'[),]', '', arg_list[1])
    new_arg = arg_list[1].split()
    new_arg.insert(1, arg_list[0])

    # begin reformatting string
    new_format = new_arg[0]
    if len(new_arg) > 1:
        for i in new_arg[1:]:
            new_format += ' ' + i

    return new_format
