from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    def all(self, cls=None):
        # Your existing implementation
        pass

    def new(self, obj):
        # Your existing implementation
        pass

    def save(self):
        # Your existing implementation
        pass

    def delete(self, obj=None):
        # Your existing implementation
        pass

    def reload(self):
        # Your existing implementation
        pass

    def close(self):
        if self.__session:
            self.__session.close()

