# AirBnB_clone

The AirBnB clone project is our first attempt to build a full website. This project is a simple copy of the AirBnB website.

This is the first part of the project and here we are working on `THE CONSOLE`. In this project we will:

1. Create our data model
2. Manage (create, update, destroy, etc) objects via a console / command interpreter
3. Store and persist objects to a file (JSON file)

To explain in more technical terms:

> The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won’t have to pay attention (take care) of how your objects are stored.This abstraction will also allow us to change the type of storage easily without updating all of our codebase. The console will be a tool to validate this storage engine.

For this project we will be using the `Command interpreter or cmd module`.
The cmd module contains one public class, Cmd, designed to be used as a base class for command processors such as interactive shells and other command interpreters. By default it uses `readline` for interactive prompt handling, command line editing, and command completion.

## How does the cmd work?

The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler. Input lines are parsed into two parts. The command, and any other text on the line. If the user enters a command `foo bar`, and your class includes a method named `do_foo()`, it is called with `"bar"` as the only argument.

The end-of-file marker is dispatched to do_EOF(). If a command handler returns a true value, the program will exit cleanly. So to give a clean way to exit your interpreter, make sure to implement do_EOF() and have it return True.

Here is an example of how to use the command interpeter:

This simple example program supports the “greet” command:

```python
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
```

By running it interactively, we can demonstrate how commands are dispatched as well as show of some of the features included in Cmd for free.

```
$ python cmd_simple.py
(Cmd)
```

The first thing to notice is the command prompt, (Cmd). The prompt can be configured through the attribute prompt. If the prompt changes as the result of a command processor, the new value is used to query for the next command.

```
(Cmd) help

Undocumented commands:
======================
EOF  greet  help
```

The help command is built into Cmd. With no arguments, it shows the list of commands available. If you include a command you want help on, the output is more verbose and restricted to details of that command, when available.

If we use the greet command, do_greet() is invoked to handle it:

```
(Cmd) greet
hello
```

If your class does not include a specific command processor for a command, the method default() is called with the entire input line as an argument. The built-in implementation of default() reports an error.

(Cmd) foo \*\*\* Unknown syntax: foo
Since do_EOF() returns True, typing Ctrl-D will drop us out of the interpreter.

```
(Cmd) ^D$

```

N/B: Notice that no newline is printed, so the results are a little messy.

Here is another example. This version of the example includes a few enhancements to eliminate some of the annoyances and add help for the greet command.

```python
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print "hi,", person
        else:
            print 'hi'

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
```

First, let’s look at the help. The docstring added to do_greet() becomes the help text for the command:

```
$ python cmd_arguments.py
(Cmd) help

Documented commands (type help ):
========================================
greet

Undocumented commands:
======================
EOF  help

(Cmd) help greet
greet [person]
        Greet the named person
```

The output shows one optional argument to the greet command, person. Although the argument is optional to the command, there is a distinction between the command and the callback method. The method always takes the argument, but sometimes the value is an empty string. It is left up to the command processor to determine if an empty argument is valid, or do any further parsing and processing of the command. In this example, if a person’s name is provided then the greeting is personalized.

```
(Cmd) greet Alice
hi, Alice
(Cmd) greet
hi
```

Whether an argument is given by the user or not, the value passed to the command processor does not include the command itself. That simplifies parsing in the command processor, if multiple arguments are needed.

You can find more examples of the command interpreter implementation on [Cmd][def]

[def]: https://pymotw.com/2/cmd/
