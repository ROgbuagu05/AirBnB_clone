#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import json
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = arg[:brackets.span()[0]].split()
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = arg[:curly_braces.span()[0]].split()
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Class that defines the command interpreter
    """
    prompt = "(hbnb) "
    __classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
    }

    def emptyline(self):
        """Does nothing when an empty line is entered"""
        pass

    def default(self, arg):
        """Default behavior for cmd module on an nvalid input"""
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = arg.split(".", 1)
            command = re.search(r"(\w+)\((.*?)\)", argl[1])
            if command is not None:
                 cmd_name = command.group(1)
                 cmd_arg = command.group(2)
                 if cmd_name in argdict:
                     call = "{} {}".format(argl[0], cmd_arg)
                     return argdict[cmd_name](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exits the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is encountered"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            print(f"Created instance with id: {new_instance.id}")
            storage.save()

    def do_show(self, arg):
        """Print the string representation of a class instance for a given id."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) < 2:
            print("** class name and instance id missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) < 3:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) < 2:
            print("** class name and instance id missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
                print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Print all instances or instances of a specific class."""
        argl = parse(arg)
        objl = []

        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(argl) == 0 or argl[0] == obj.__class__.__name__:
                    objl.append(str(obj))
            print(objlist)

    def do_update(self, arg):
        """Update an instance based on its ID."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
