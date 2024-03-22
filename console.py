#!/usr/bin/python3
"""The console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Custom Console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the interpreter with ctrl+d"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
