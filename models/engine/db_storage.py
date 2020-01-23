#!/usr/bin/python3
""" Database storage """

from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

classes = {User, State, City, Amenity, Place, Review}


class DBStorage:
    """ Database storage class """

    __engine = None
    __session = None

    def __init__(self):
        """ init """
        self.__engine = create_engine(
            "mysql+mysqldb://" + getenv("HBNB_MYSQL_USER") +
            ":" + getenv("HBNB_MYSQL_PWD") +
            "@" + getenv("HBNB_MYSQL_HOST") +
            "/" + getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ get all items with a certain class """
        ret = {}
        if cls:
            for x in self.__session.query(cls).all():
                ret[cls.__name__+"."+x.id] = x
        else:  # if no class passed, get everything
            for c in classes:
                ret.update(self.all(c))
        return ret

    def close(self):
        self.__session.remove()

    def new(self, obj):
        """ add object to session """
        self.__session.add(obj)

    def save(self):
        """ save changes """
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload from database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )()
