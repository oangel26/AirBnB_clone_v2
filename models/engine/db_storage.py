#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from sqlalchemy import (create_engine)
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """This class manages storage of hbnb models in database format"""
    __engine = None
    __session = None

    def __init__(self):
		"""Returns a dictionary of models currently in storage"""
		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'), os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB'), pool_pre_ping=True)
		Base.metadata.create_all(DBStorage.__engine)
		Session=sessionmaker(bind=engine)
        self.__session=Session()

		if os.getenv('HBNB_ENV') == 'test':
			self.__table__.drop(DBStorage.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if cls is None:
			new_dict={}
			for q in self.__session.query().all():
                k='{}.{}'.format(q.__class__.__name__, q.id)
				new_dict[k]=q
			return new_dict

        for q in self.__session.query(cls).all():
                k='{}.{}'.format(q.__class__.__name__, q.id)
				new_dict[k]=q
			return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
		if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
		self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
			self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from database"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

		Base.metadata.create_all(DBStorage.__engine)

        session_factory=sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session=scoped_session(session_factory)
		self.__session=Session()
