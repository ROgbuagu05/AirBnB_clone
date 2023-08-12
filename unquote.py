#!/usr/bin/python3
'''Contains a function that removes double quotation marks from a string'''
import re


def unquote(arg):
    '''Function that checks if there are literal double quotation marks at
    the beginning and ending a string and removes the double quotation
    marks from the end and beginning of string

    Args:
        arg: A string object

    Returns:
        The arg string without double quotation marks at the beginning and
        ending of the string
    '''
    if arg.startswith('"') and arg.endswith('"'):
        new = re.sub('"', '', arg)
        return new
    else:
        return arg
