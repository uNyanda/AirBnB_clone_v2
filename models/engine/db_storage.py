#!/usr/bin/python3
""" DBStorage engine """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects of a class. If cls=None, query all types """
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """ Add object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from current database session if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in database & current session """
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
