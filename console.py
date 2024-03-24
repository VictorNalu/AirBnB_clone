#!/usr/bin/python3
"""The console"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Custom Console"""

    prompt = "(hbnb) "
    valid_classes = [
        "BaseModel",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the interpreter with ctrl+d"""
        return True

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = models.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show command to print string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            models.storage.save()

    def do_all(self, arg):
        """All command to print all string representations of instances"""
        objects = models.storage.all()
        if not arg:
            print([str(objects[obj]) for obj in objects])
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(objects[obj]) for obj in objects if arg in obj])

    def do_update(self, arg):
        """Update command to update an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            setattr(objects[key], args[2], args[3])
            models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
