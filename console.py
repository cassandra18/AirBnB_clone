#!/usr/bin/python3
"""A simple command interpreter module."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def arg_handler(arg):
    """Parse an argument into a list of tokens.
    Args:
        arg (str): The argument to parse.
    Returns:
        list: A list of tokens.
    """
    curlybraces = re.search(r"\{(.*?)\}", arg)
    sq_brackets = re.search(r"\[(.*?)\]", arg)
    if curlybraces is None:
        if sq_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            tokens_list = split(arg[:sq_brackets.span()[0]])
            parsed_tokens = [i.strip(",") for i in tokens_list]
            parsed_tokens.append(sq_brackets.group())
            return parsed_tokens
    else:
        tokens_list = split(arg[:curlybraces.span()[0]])
        parsed_tokens = [i.strip(",") for i in tokens_list]
        parsed_tokens.append(curlybraces.group())
        return parsed_tokens


class HBNBCommand(cmd.Cmd):
    """
    A simple command interpreter for the AirBnB_clone project
    """

    prompt = "(hbnb) "
    __valid_classes = {
        "BaseModel",
        "Review",
        "Amenity",
        "User",
        "Place",
        "City",
        "State"
    }

    def default(self, arg):
        """Default behavior for invalid input."""
        cmd_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        result = re.search(r"\.", arg)
        if result is not None:
            arglist = [arg[:result.span()[0]], arg[result.span()[1]:]]
            result = re.search(r"\((.*?)\)", arglist[1])
            if result is not None:
                command = [arglist[1][:result.span()[0]], result.group()[1:-1]]
                if command[0] in cmd_dict.keys():
                    cmd_args = "{} {}".format(arglist[0], command[1])
                    return cmd_dict[command[0]](cmd_args)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Handle end-of-file input (Ctrl+D) to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Move to the next line when you press enter without a command."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class and print its ID."""
        arglist = arg_handler(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arglist[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Display the string representation of a class instance.
        """
        arglist = arg_handler(arg)
        obj_dict = storage.all()
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglist[0], arglist[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arglist[0], arglist[1])])

    def do_destroy(self, arg):
        """
        Delete a class instance by id."""
        arglist = arg_handler(arg)
        obj_dict = storage.all()
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglist[0], arglist[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arglist[0], arglist[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representations of class instances."""
        arglist = arg_handler(arg)
        if len(arglist) > 0 and arglist[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        else:
            objlist = []
            for obj in storage.all().values():
                if len(arglist) > 0 and arglist[0] == obj.__class__.__name__:
                    objlist.append(obj.__str__())
                elif len(arglist) == 0:
                    objlist.append(obj.__str__())
            print(objlist)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        arglist = arg_handler(arg)
        occurrence = 0
        for obj in storage.all().values():
            if arglist[0] == obj.__class__.__name__:
                occurrence += 1
        print(occurrence)

    def do_update(self, arg):
        """Update a class instance with a new attribute or value."""
        arglist = arg_handler(arg)
        obj_dict = storage.all()

        if len(arglist) == 0:
            print("** class name missing **")
            return False
        if arglist[0] not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
            return False
        if len(arglist) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arglist[0], arglist[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arglist) == 2:
            print("** attribute name missing **")
            return False
        if len(arglist) == 3 and not isinstance(eval(arglist[2]), dict):
            print("** value missing **")
            return False

        if len(arglist) == 4:
            obj = obj_dict["{}.{}".format(arglist[0], arglist[1])]
            if arglist[2] in obj.__class__.__dict__.keys():
                type_value = type(obj.__class__.__dict__[arglist[2]])
                obj.__dict__[arglist[2]] = type_value(arglist[3])
            else:
                obj.__dict__[arglist[2]] = arglist[3]
        elif isinstance(eval(arglist[2]), dict):
            obj = obj_dict["{}.{}".format(arglist[0], arglist[1])]
            for key, value in eval(arglist[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {
                            str, int, float}):
                    type_value = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = type_value(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
