#!/usr/bin/python3
"""DBStorage engine class"""

from sqlalchemy import create_engine
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {'User': User, 'Place': Place, 'State': State,
           'City': City, 'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """create database engine"""
    __engine = None
    __session = None

    def __init__(self):
        """create engine from sqlalchemy"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all
        objects depending of the class name (argument cls)"""
        objs = {}
        if cls:
            for row in self.__session.query(cls).all():
                objs.update({'{}.{}'.
                             format(type(row).__name__, row.id): row})
        else:
            for key, value in classes.items():
                for row in self.__session.query(value).all():
                    objs.update({'{}.{}'.
                                 format(type(row).__name__, row.id): row})
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            cls = classes[type(obj).__name__]
            self.__session.query(cls).filter(cls.id == obj.id).delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        self.__session = scoped_session(self.__session)

    def close(self):
        """ close db session """
        self.__session.remove()
