#!/usr/bin/python3
"""This program defines the HBnB console"""

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


def parse(line):
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(line)]
        else:
            lexer = split(line[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(line[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    
    prompt = '(hbnb) '
    
    def emptyline(self):
        """Do nothing if empty line is passed"""
        pass
    
    def do_quit(self, line):
        """Use the command 'quit' to exit"""
        return True
    
    def do_EOF(self, line):
        """Use ctr + D or C to exit"""
        print("")
        return True
    
    """"Adding new commands to enhance it functionality"""
    
    def do_create(self, line):
        """'create', creates a new instance of 
        BaseModel and prints its 'id'"""
        
        line_index = parse(line)
        if len(line_index) == 0:
            print("** class name m[issing **")
            
        elif line_index[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            
        else:
            print(eval(line_index[0])().id)
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
