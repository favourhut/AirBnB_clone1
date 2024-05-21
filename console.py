#!/usr/bin/python3

"""This program defines the HBnB console"""

import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    
    """This class contains the entry point for th command interpreter
    """

    """custom prompt"""
    prompt = '(hbnb) '
    
    """calling basemodel classes"""
    valid_classes = ["BaseModel"]
    
    def do_quit(self, line_arg):
        """used to quit the interactive mode of the console
        Usage: input 'quit' to exit the console
        """    
        return True
    
    def do_EOF(self, line_arg):
        """Force exit the console
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
    
    """Updating command interpreter (console.py) to have moreknown commands"""
    
    def do_create(self, line_arg):
        """
        Create new instance of basemodel and saves it id
        Args:
            line_arg (string): line arguments in the console
        """
        
        input_commands = split(line_arg)
        if len(input_commands) == 0:
            print("** class name missing **")
            
        elif input_commands[0] not in self.valid_classes:
            print("** class name doesn't exist **")
            
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            
    def do_show(self, line_arg):
        
        """Prints the string representation of an 
        instance based on the class name and id
        """
        
        input_commands = split(line_arg)
        
        if len(input_commands) == 0:
            print("** class name missing **")
            
        elif input_commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
            
        elif len(input_commands) < 2:
            print("** instance id missing**")
            
        else:
            """fetching all objects from storage"""
            all_obejcts = storage.all()
            
            key = "{}.{}".format(input_commands[0], input_commands[1])
            
            if key in all_obejcts:
                print([all_obejcts[key]])   
            else:
                print("** no instance found **")
                
    def do_destroy(self, line_arg):
        
        """Deletes an instance based on the class name and id
        """
        input_commands = split(line_arg)
        
        if len(input_commands) == 0:
            print("** class name missing **")
              
        elif input_commands not in self.valid_classes:
            print("** class doesn't exist **")
            
        elif len(input_commands) < 2:
            print("** instance id missing**")
            
        else:
            all_objects = storge.all()  
            key = "{}.{}".format(input_commands[0], input_commands[1])
            
            if key in all_objects:
                del all_objects[key]
                storage.save()
                
            else:
                print("** no instance found **")
                
    def do_all(self, line_arg):
        
        """Prints all string representation of all instances 
        based or not on the class name
        """
        
        """retrieving all objects"""
        all_objects = storage.all()
        
        input_commands = split(line_arg)
        
        if len(line_arg) == 0:
            for key, value in all_objects.items():
                print(str(value))
                
        elif input_commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
            
        else:
            for key, value in all_objects,items():
                if key.split(',') == input_commands[0]:
                    print(str(value))
                    
                    
    def do_update(self, line_arg):
        """_ Updates an instance based on the class name 
        and id by adding or updating attribute 
        """
        
        input_commands = split(line_arg)
        
        if len(input_commands) == 0:
            print("** class name missing **")
            
        elif line_arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        
        elif len(input_commands) < 2:
            print("** instance id missing **")
        
        else:
            all_objects = storage.all()
            
            key = "{}.{}".format(input_commands[0], input_commands[1])
            
            if key not in all_objects:
                print("** no instance found **")
            elif len(input_commands) < 3:
                print("** attribute name missing **")
                
            elif len(input_commands < 4):
                print("** value missing **")
                
            else:
                update_obj = all_objects[key]
                
                attr_name = input_commands[2]
                attr_value = input_commands[3]
                
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                
                setattr(update_obj, attr_name, attr_value)
                    
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()