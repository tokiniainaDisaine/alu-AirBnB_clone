#!/usr/bin/python3
"""
doc: to do later
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Base class for all AirBnB clone models"""
    user_id = ""
    place_id = ""
    text = ""