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
                class_name, BaseModel):
            print("** class doesn't exist **")
            return

        instance_key = f("{class_name}.{instance_id}")
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
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            model_class = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        if class_name not in globals() or not issubclass(
                model_class, BaseModel):
            print("** class doesn't exist **")
            return

        instance_key = f("{class_name}.{instance_id}")
        instances = storage.all()
        if instance_key in instances:
            del instances[instance_key]
            storage.save()
            return
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Print the string representation of all instances.
        Based on or not on the class name."""
        if not arg:
            instances = storage.all().values()
            print([str(instance) for instance in instances])
        else:
            try:
                model_class = eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return

            if arg not in globals() or not issubclass(model_class, BaseModel):
                print("** class doesn't exist **")
                return

            instances = storage.all().values()
            filtered_inst = [str(instance) for instance in instances
                             if isinstance(instance, model_class)]
            print(filtered_inst)

    def do_update(self, arg):
        """Updates an instance based on class name and id.
        Save the change into the JSON file."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance_key = f("{class_name}.{instance_id}")
        instances = storage.all()

        if instance_key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        try:
            model_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        instance = instances[instance_key]
        if not hasattr(instance, attribute_name):
            print("** attribute name missing **")
            return

        attribute_type = type(getattr(instance, attribute_name))
        try:
            casted_value = attribute_type(attribute_value)
        except ValueError:
            print("** value missing **")
            return

        setattr(instance, attribute_name, casted_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
