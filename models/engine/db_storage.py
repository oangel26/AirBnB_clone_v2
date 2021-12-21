#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from sqlalchemy import (create_engine)
import os


class DBStorage:
    """This class manages storage of hbnb models in database format"""
    __engine = None
    __session = None

    def __init__(self):
		"""Returns a dictionary of models currently in storage"""
		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'), os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB'), pool_pre_ping=True)
		Base.metadata.create_all(DBStorage.__engine)

		if os.getenv('HBNB_ENV') == 'test':
			self.__table__.drop(DBStorage.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        if cls is not None:
            for k, v in DBStorage.__session.items():
                if k.split('.')[0] == cls.__name__:
                    new_dict[k] = v
            return new_dict
        return DBStorage.__session

    def new(self, obj):
        """Add the object to the current database session"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Commit all changes of the current database session"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(DBStorage.__session)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            key = "{}.{}".format(obj.to_dict()['__class__'], obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
