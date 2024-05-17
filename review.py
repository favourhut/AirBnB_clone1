#!/usr/bin/python3

"""class that inherits from basemodel"""

from base_model import BaseModel


class Review(BaseModel):
    """creating public class attribute
    
    Attributes:
        place_id: empty string
        user_id: empty string
        text: empty string
    """
    
    place_id = ""
    user_id = ""
    text = ""