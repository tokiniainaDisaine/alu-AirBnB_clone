#!/usr/bin/python3
"""
doc: to do later
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Base class for all AirBnB clone models"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
