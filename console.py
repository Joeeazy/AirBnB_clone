#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
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
        """ quit to exit the program """
    def do_quit(self, string):
        print("Exiting HBNB")
        return True

        """ EOF to exit when CTRL + D is called
        """
    def do_EOF(self, string):
        print("Exit")
        return True

        """ shouldn’t execute anything """
    def emptyline(self):
        pass

    """ Creates a new instance of the basemodel class,
        saves it (to the JSON file) and prints the id 
    """
    def do_create(self, string):
        # if class name is missing
        if not string:
            print("** class name missing **")
            return
        new_data = shlex.split(string)

        # If the class name doesn’t exist
        if new_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        created_instance = HBNBCommand.my_dict[new_data[0]]()
        created_instance.save()
        print(created_instance.id)

        """
        Prints the string representation of an 
        instance based on the class name and id
        """
    def do_show(self, string):
        toks = shlex.split(string)
        if len(toks) == 0:
            print("** class name missing **")
            return
        if toks[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(toks) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        new_dict = storage.all()
        key = toks[0] + "." + toks[1]
        if key in new_dict:
            id_instance = str(new_dict[key])
            print(id_instance)
        else:
            print("** no instance found **")


        """
        Deletes an instance based on the class name 
        and id (save the change into the JSON file)
        """
    def do_destroy(self, string):
        toks = shlex.split(string)
        if len(toks) == 0:
            print("** class name missing **")
            return
        if toks[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(toks) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        new_dict = storage.all()
        key = toks[0] + "." + toks[1]
        if key in new_dict:
            del new_dict[key]
            storage.save()
        else:
            print("** no instance found **")

        """
        Prints all string representation
        of all instances based or not on the class name
        """
    def do_all(self, string):
        storage.reload()
        my_list = []
        objs_dict = storage.all()
        if not string:
            for key in objs_dict:
                my_list.append(str(obs_dict[key]))
            print(json.dumps(my_list))
            return
        toks = shlex.split(string)
        if toks[0] in HBNBCommand.my_dict.keys():
            for key in objs_dict:
                if toks[0] in key:
                    my_list.append(str(objs_dict[key]))
            print(json.dumps(my_list))
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()



