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
         """Deserialize the JSON file to objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = key.split('.')[0]
                    if cls_name in globals():
                        cls = globals()[cls_name]
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
        pass

    def delete(self, obj=None):
        # Your existing implementation
        pass

    def close(self):
        """Calls reload() to deserialize the JSON file to objects"""
        self.reload()
