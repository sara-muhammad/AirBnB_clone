#!/usr/bin/python3
"""Module for console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """
        End of file (Ctrl+D) signal to exit the program.
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True
    def help_quit(self, arg):
        """
        print help message to exit the program.
        """
        print("Quit command to exit the program")
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
