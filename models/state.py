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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all')
    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """ Get a list of City instances
                that linked with the current state
            """
            from models import storage
            cities = storage.all(City)
            return [city_obj for city_id, city_obj in cities.items()
                    if city_obj.state_id == self.id]
