#!/usr/bin/python3

"""A class city that inherits from BaseModel"""

from base_model import BseModel


class City(BaseModel):
    
    """Inherits from basemodel

    Attributes:
        state_id: it would be the state.id
        name: empty string
    """
    
    state_id = ""
    name = ""
