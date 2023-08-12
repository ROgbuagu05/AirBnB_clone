#!/usr/bin/python3
'''Command line interpreter'''
import cmd
import sys
import re
import models
from check_type import check_type
from cmd_parser import cmd_parser
from unquote import unquote
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_dict = {"BaseModel": BaseModel, "User": User, "City": City,
              "Review": Review, "State": State, "Amenity": Amenity,
              "Place": Place}


class HBNBCommand(cmd.Cmd):
    '''A class defining a CLI object'''

    prompt = "(hbnb) "

    def emptyline(self):
        '''Do nothing if no command and/or argument is entered'''
        pass

    def default(self, line):
        '''This method is called if there is no do_(line) method available'''
        command_list = ["all", "create", "delete", "show", "update", "count"]
        args = cmd_parser(line)
        
        # if there is no valid class name in (line) print error message
        if args == 1:
            print("*** Unknown syntax: {}".format(line))
            return False

        # call do_* method based on class name found in (line)
        command = re.split(' ', args, 1)
        if command[0] in command_list:
            if args.startswith(command_list[0]):
                self.do_all(command[1])
            elif args.startswith(command_list[1]):
                self.do_create(command[1])
            elif args.startswith(command_list[2]):
                self.do_delete(command[1])
            elif args.startswith(command_list[3]):
                self.do_show(command[1])
            elif args.startswith(command_list[4]):
                self.do_update(command[1])
            else:
                self.do_count(command[1])
            return False

    def do_quit(self, line):
        '''Do method to exit CLI'''
        sys.exit(0)

    def help_quit(self):
        print("Usage: quit")
        print("-- eg. q (Alternative Usage)")
        print("-- exits program")

    def do_EOF(self, line):
        '''Do method for EOF condition'''
        return True

    def help_EOF(self):
        print("Usage: <ctrl-d> or automatic when EOF is reached")
        print("-- Allows user to exit CLI cleanly")

    def do_create(self, args):
        '''Do method to create a new instance based on class name'''
        cmd_args = args.split()
        if cmd_args == []:
            print("** class name missing **")
        elif cmd_args[0] not in class_dict:
            print("** class doesn't exist **")
        else:
            obj = class_dict[cmd_args[0]]()
            print(obj.id)
            obj.save()

    def help_create(self):
        print("Usage: create <class constructor>")
        print("-- eg. create BaseModel")
        print("-- Creates a class object and displays object id")

    def do_show(self, args):
        '''Do method that displays an instance of class'''
        cmd_args = args.split()
        if cmd_args == []:
            print("** class name missing **")
        elif cmd_args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            models.storage.reload()
            storage = models.storage.all()
            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key in storage:
                s = "{}".format(storage[key])
                print(s)
            else:
                print("** no instance found **")

    def help_show(self):
        print("Usage: show <class Constructor> <obj.id>")
        print("-- eg. show BaseModel 1234-1234-1234")
        print("-- Prints the string representation of the object")

    def do_delete(self, args):
        '''Do method to delete an instance of class'''
        cmd_args = args.split()
        if cmd_args == []:
            print("** class name missing **")
        elif cmd_args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            storage = models.storage.all()
            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key in storage:
                del storage[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def help_delete(self):
        print("Usage: delete <class name> <obj.id>")
        print("-- eg. delete BaseModel 1234-1234-1234")
        print("-- eg. d Basemodel 1234-1234-1234(alternative)")
        print("-- Deletes the object")

    def do_all(self, args):
        '''DO method that displays all instances of all classes or all
        instances of a specified class'''
        models.storage.reload()
        storage = models.storage.all()
        list_objs = []
        if args and args not in class_dict:
            print("** class doesn't exist **")
        elif args:
            cmd_arg = args.split()
            for key, value in storage.items():
                key_string = key.split('.')
                if key_string[0] in class_dict and key_string[0] == cmd_arg[0]:
                    list_objs.append(str(storage[key]))
            print(list_objs)
        else:
            for key, value in storage.items():
                list_objs.append(str(storage[key]))
            print(list_objs)

    def help_all(self):
        print("Usage: all <class name>(optional)")
        print("-- eg. all")
        print("-- eg. all BaseModel")
        print("-- Prints a list of all instances or all instances of class")

    def do_update(self, args):
        '''Do method that updates the attribute of an instance of class'''
        cmd_args = args.split()
        storage = models.storage.all()
        if cmd_args == []:
            print("** class name missing **")
        elif cmd_args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(cmd_args[0], cmd_args[1]) not in storage:
            print("** no instance found **")
        elif len(cmd_args) < 3:
            print("** attribute name missing **")
        elif len(cmd_args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            new_arg = unquote(cmd_args[3])
            instance = storage[key].__dict__
            if cmd_args[2] in instance:
                valtype = type(instance[cmd_args[2]])
                storage[key].__dict__[cmd_args[2]] = valtype(new_arg)
            else:
                storage[key].__dict__[cmd_args[2]] = check_type(new_arg)
            storage[key].__dict__[cmd_args[2]] = new_arg
            models.storage.save()

    def help_update(self):
        print("Usage: update <class name> <obj.id> <attribute> <attr value>")
        print("-- eg. update User 1234-1234 first_name \"John\"")
        print("-- Updates the object attribute if it exists")
        print("-- Adds new attribute to object if attribute does not exist")

    def do_count(self, arg):
        '''Counts all instance of class name(arg)'''
        models.storage.reload()
        storage = models.storage.all()
        count = 0
        for key, value in storage.items():
            key_list = key.split('.')
            if key_list[0] == arg:
                count += 1
        print(count)                

    do_q = do_quit
    do_d = do_delete

    def postloop(self):
        '''Code to run at end of loop'''
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
