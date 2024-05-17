#!/usr/bin/python3

import json
import os
from base_model import BaseModel


class FileStorage:
    
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    
    Attributes:
        __file_path: a path to the JSON file
        __objects: store all objects by <class name>.id
        
    Mathods:
        all: returns the dictionary __objects
        new: sets in __objects the obj with key <obj class name>.id
        save: serializes __objects to the JSON file (path: __file_path)
        reload: deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists;
        otherwise, does nothing. 
        If the file doesn’t exist, no exception would be raised)
    """
    
    __file_path = "file.json"
    __objects = {}
    
    """creating class attributes"""
    def all(self):
        """Instance methods returns the dictionary"""
        return (self.__objects)
    
    def new(self, obj):
        """Adds a new objects to the dictionary"""
        if obj not in self.objects:
            key = ("{}.{}".format(obj.__class__.__name__, obj.id))
            self.__objects[key] = obj
            
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {k: v.to_dict() for k, v in self.objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dictionary, file)
            
    def reload(self):
        """deserializing the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    instance_dict = json.load(file)
                
                for key, data in instance_dict.items():
                    key_class = data.get('__class__')
                    if key_class:
                        class_name = globals().get(key_class)
                        if class_name:
                            obj = class_name(**data)
                            self.__objects[key] = obj
                            
            except Exception:
                pass