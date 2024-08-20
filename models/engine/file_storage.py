#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        # Your existing implementation
        pass

    def new(self, obj):
        # Your existing implementation
        pass

    def save(self):
        # Your existing implementation
        pass

    def reload(self):
        # Your existing implementation
        pass

    def delete(self, obj=None):
        # Your existing implementation
        pass

    def close(self):
        self.reload()
