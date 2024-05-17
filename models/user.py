#!/usr/bin/python3

"""A class user that inherits from BaseModel"""

from base_model import BaseModel


class User(BaseModel):
    
    """This user inherits from Basemodel
    
    Attributes:
        email: empty string
        password: empty string
        first_name: empty string
        last_name: empty string
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""