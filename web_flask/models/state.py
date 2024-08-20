from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def cities(self):
        """ Returns a list of City objects linked to the State """
        from models import storage
        if storage.__class__.__name__ == "FileStorage":
            # For file storage
            return [city for city in storage.all(City).values()
                   if city.state_id == self.id]
        elif storage.__class__.__name__ == "DBStorage":
            # For DB storage
            return self.cities
