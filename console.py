#!/usr/bin/python3

"""This program defines the HBnB console"""

import cmd
from shlex import split

class HBNBCommand(cmd.Cmd):
    
    """This class contains the entry point for th command interpreter
    """
    
    """custom prompt"""
    prompt = '(hbnb) '
    
    def do_quit(self, line):
        """used to quit the interactive mode of the console
        Usage: input 'quit' to exit the console
        """    
        return True
    
    def do_EOF(self, line):
        """Force exi the console

        Usage:
            use ctr + d or c to force exit the console
        """
        print("")
        return True
    
    def emptyline(self):
        """return a new line when an empty line + ENTER is used
        Execute:
            Does not execute anything
        """
        pass
    
    """Updating command interpreter (console.py) to have known commands"""
    
    def d0_create(self, line_arg):
        pass
    
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()