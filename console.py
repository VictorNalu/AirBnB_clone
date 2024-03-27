#!/usr/bin/python3
"""Console module."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print('** class name missing **')
            return
        try:
            class_name = arg.split()[0]
            if class_name not in globals():
                print('** class doesn\'t exist **')
                return
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        if not arg:
            print('** class name missing **')
            return
        try:
            args = arg.split()
            class_name = args[0]
            if class_name not in globals():
                print('** class doesn\'t exist **')
                return
            if len(args) < 2:
                print('** instance id missing **')
                return
            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key not in storage.all():
                print('** no instance found **')
                return
            print(storage.all()[key])
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print('** class name missing **')
            return
        try:
            args = arg.split()
            class_name = args[0]
            if class_name not in globals():
                print('** class doesn\'t exist **')
                return
            if len(args) < 2:
                print('** instance id missing **')
                return
            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key not in storage.all():
                print('** no instance found **')
                return
            del storage.all()[key]
            storage.save()
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Print all string representation of all instances."""
        try:
            if not arg:
                print("** class name missing **")
                return

            class_name = arg.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            all_instances = storage.all()[class_name].values()
            print(all_instances)

        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print('** class name missing **')
            return
        try:
            args = arg.split()
            class_name = args[0]
            if class_name not in globals():
                print('** class doesn\'t exist **')
                return
            if len(args) < 2:
                print('** instance id missing **')
                return
            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key not in storage.all():
                print('** no instance found **')
                return
            if len(args) < 3:
                print('** attribute name missing **')
                return
            attribute_name = args[2]
            if len(args) < 4:
                print('** value missing **')
                return
            attribute_value = args[3]
            instance = storage.all()[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except Exception as e:
            print(e)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End of file."""
        print()
        return True

    def emptyline(self):
        """Empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
