#!/usr/bin/python3
'''Contains a function that removes double quotation marks from a string'''
import re


def unquote(arg):
    '''Function that checks if there are literal double quotation marks at
    the beginning and ending a string and removes the double quotation
    marks from the end and beginning of string

    Args:
        arg: A list of string objects

    Returns:
        The arg string without double quotation marks at the beginning and
        ending of the string
    '''
    arg_one = ""
    arg_two = ""

    # if arg[3] is a single word in quotes
    if arg[3].startswith('"') and arg[3].endswith('"'):
        new = re.sub('"', '', arg[3])
        return new
    elif arg[3].startswith('"'):
        arg_one = arg[3]
        for i in arg[4:]:
            arg_one += " " + i
            if '"' in i:
                break
        if arg_one.startswith('"') and arg_one.endswith('"'):
            new = re.sub('"', '', arg_one)
            return new
        else:
            return arg[3]
    else:
        return arg
