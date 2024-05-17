#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel():
    """_summary_
    """
    
    def __init__(self, *args, **kwargs):
        
        """Creating a basemodel from dictionary"""
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    continue
                setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        
    # Printing information for the instance attributes 
    def __str__(self):
        
        """should return [<class name>] (<self.id>) <self.__dict__>"""
        return(self.__class__.__name__, self.id, self.__dict__)
    
    # creating some public instances
    
    def save(self):
        """ makes updated_at valid to current datetime"""
        updated_at = datetime.now()
        
    def to_dict(self):
        """creating an empty dict"""
        all_keys_values_dict = {}
        
        """ Using self.__dict__ to retun only only sets instances"""
        all_keys_values_dict.update(self.__dict__)
        
        """Adding a key __class__ with class name of the object"""
        all_keys_values_dict["__class__"] = self.__class__.__name__
        
        """Converting created_at and updated_at to isoformat"""
        all_keys_values_dict["created_at"] = all_keys_values_dict["created_at"].isoformat()
        all_keys_values_dict["update_at"] = all_keys_values_dict["update_at"].isoformat()
        
        """returning the dictionary containing all keys and values"""
        return (all_keys_values_dict)