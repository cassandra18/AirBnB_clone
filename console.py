#!/usr/bin/python3
"""The console contains the entry point of the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import json


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class is a subclass of the Cmd class.
    Cmd provides a framework for writing line-oriented command interpreters.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """The quit command is used to exit the console."""
        return True

    def do_EOF(self, arg):
        """EOF is used to exit the program."""
        print()
        return True

    def emptyline(self):
        """Move to the next line when you press enter without a command."""
        pass

    def do_create(self, arg):
        """Create a new instance of the BaseModel class.
        Save the new instance to JSON file and print the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            model_class = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        new_instance = model_class()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Print the string representation of and instance.
        Based of the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            model_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        if class_name not in globals() or not issubclass(
               globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return

        instance_key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()

        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.
        Save changes to JSON file."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) == 0:
            print("** class name missing  **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in globals():
            print("** Class doesn't exist **")
            return

        instance_key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()

        if instance_key not in instances:
            print("** No instance found **")
            return

        del instances[instance_key]
        storage.save()

    def do_all(self, arg):
        """Print the string representation of all instances.
        Based on or not on the class name."""

        model_classes = {
               "BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review
            }
        if not arg:
            instances = storage.all().values()
            print([str(instance) for instance in instances])
        elif arg in model_classes:
            model_class = model_classes[arg]
            instances = storage.all().values()
            filtered_inst = [str(instance) for instance in instances
                             if isinstance(instance, model_class)]
            print(filtered_inst)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute, saving on JSON file"""
        arg = args.split()
        found = False

        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            instance_key = "{}.{}".format(arg[0], arg[1])
            for key, obj in storage.all().items():
                if key == instance_key:
                    att_val_idx = len(arg[0]) + len(arg[1]) + len(arg[2]) + 3
                    value = args[att_val_idx:]
                    if args[att_val_idx] == "\"":
                        att_val_idx += 1
                        value = args[att_val_idx:-1]
                    if hasattr(obj, arg[2]):
                        value = type(getattr(obj, arg[2]))(args[att_val_idx:])
                    setattr(obj, arg[2], value)
                    found = True
                    storage.save()
                    break
            if not found:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
