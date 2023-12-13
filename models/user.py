#!/usr/bin/python3
"""
Import Module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that handles the
    following users' information
    email, pwd, f_name and l_name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
