#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import City
from models.__init__ import storage

class State(BaseModel, Base):
    """ State class """    
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """ FileStorage relationship between cities and state"""
        city_list = []
        for v in storage.__objects.values():
            if "state_id" in v.keys():
                if v["state_id"] == self.id:
                    city_list.append(v)
        return city_list
