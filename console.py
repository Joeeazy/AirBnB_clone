#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ The entry point of the cmd interpreter """
    prompt = '(hbnb) ' # The custom prompt
    my_dict = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place,
        "Review": Review
            }
    def do_quit(self, arg):
        """ quit to exit the program """
        print("Exiting HBNB")
        return True

    def do_EOF(self, arg):
        """ EOF to exit when CTRL + D is called
        """
        print("Exit")
        return True

    def emptyline(self):
        """ shouldn’t execute anything """
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()



