#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            cities = relationship('City', backref='state', cascade='all')
            return cities
        else:
            from models import storage
            cities = storage.all(City)
            return {city_id: city_obj for city_id, city_obj in cities.items()
                    if city_obj.state_id == self.id}
