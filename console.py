#!/usr/bin/python3
""" The Console """
import cmd
import uuid
import copy
import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    """ The Airbnb Project Console."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, l):
        """Creates a New instance of a given class"""
        classes = [
            "BaseModel", "User", "State",
            "City", "Amenity", "Place", "Review"
        ]
        line = l.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] in classes:
            tmp = eval(line[0])()
            tmp.save()
            print(tmp.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, l):
        """Prints the string representation of an instance\
based on the class name and id"""
        classes = [
            "BaseModel", "User", "State",
            "City", "Amenity", "Place", "Review"
        ]
        line = l.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif len(line) == 2:
            tmp = line[0] + "." + line[1]
            if tmp in storage.all():
                print(storage.all()[tmp])
            else:
                print("** no instance found **")

    def do_destroy(self, l):
        """Deletes an instance based on the class name and id"""
        classes = [
            "BaseModel", "User", "State",
            "City", "Amenity", "Place", "Review"
        ]
        line = l.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif len(line) == 2:
            tmp = line[0] + "." + line[1]
            if tmp in storage.all():
                del storage.all()[tmp]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, l):
        """Prints all string representation of all instances"""
        line = l.split()
        str_list = []
        for key in storage.all():
            cls, _, _ = key.partition(".")
            if len(line) == 1:
                if line[0] == cls:
                    str_list.append(storage.all()[key].__str__())
            else:
                str_list.append(storage.all()[key].__str__())
        print(str_list)

    def do_update(self, l):
        """Updates an instance based on the class name and id"""
        line = l.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif len(line) == 2:
            dt = ""
            for key, value in storage.all().items():
                if line[1] in key and line[0] in key:
                    dt = key
            if len(dt) == 0:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        elif len(line) >= 4:
            base = ""
            idnum = ""
            for key, value in storage.all().items():
                if line[1] in key and line[0] in key:
                    if is_int(line[3]):
                        line[3] = int(line[3])
                    elif is_float(line[3]):
                        line[3] = float(line[3])
                    else:
                        tmp = str(line[3])
                        if tmp[0] in '"\'' and tmp[-1] in '"\'':
                            tmp = tmp[1:-1]
                        line[3] = tmp
                    if line[2][0] in '"\'' and line[2][-1] in '"\'':
                        line[2] = line[2][1:-1]
                    value.__dict__[str(line[2])] = line[3]
                    storage.save()
                    base = 1
                    idnum = 1
                    break
                else:
                    if line[0] in key:
                        base = key
                    if line[1] in key:
                        idnum = key
            if type(base) is int and type(idnum) is int:
                pass
            elif len(base) == 0:
                print("** class doesn't exist **")
            elif len(idnum) == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
