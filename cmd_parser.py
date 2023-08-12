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
    arg_list = re.split('\.', arg, 1)
    arg_list[1] = re.sub(r'[(]', ' ', arg_list[1])
    arg_list[1] = re.sub(r'[),]', '', arg_list[1])
    new_arg = arg_list[1].split()
    new_arg.insert(1, arg_list[0])

    new_format = new_arg[0]
    if len(new_arg) > 1:
        for i in new_arg[1:]:
            new_format += ' ' + i

    return new_format
