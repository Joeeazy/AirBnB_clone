#!/usr/bin/python3
"""
import Module for the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represention of a city.
    Attributes:
        state_id: The state id.
        name: empty string of the city's name.
    """

    state_id = ""
    name = ""
