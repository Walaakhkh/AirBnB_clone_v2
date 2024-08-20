#!/usr/bin/python3
import cmd
from models import storage
import models
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        
        # Create a new instance of the specified class
        new_instance = models.classes[class_name]()
        
        # Parse parameters
        for param in args[1:]:
            if "=" not in param:
                continue
            key, value = param.split("=", 1)
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace("_", " ").replace('\\"', '"')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue

            # Set attribute if it exists
            if hasattr(new_instance, key):
                setattr(new_instance, key, value)

        # Save the new instance
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        # Your existing code for do_show

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        # Your existing code for do_destroy

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        # Your existing code for do_all

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        # Your existing code for do_update

    def emptyline(self):
        """Override the default behavior of repeating the last command when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
