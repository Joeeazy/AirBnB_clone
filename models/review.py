#!/usr/bin/python3
"""
import Module for the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of review Attributes =
        place_id: The Place id.
        user_id: The User id.
        text: The text of the review done.
    """

    place_id = ""
    user_id = ""
    text = ""
