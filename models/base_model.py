#!/usr/bin/python3
'''A module containing a BaseModel class'''

from datetime import datetime
import json
import uuid

class BaseModel:
	'''A class that defines a BaseModel object'''

	def __init__(self, *args, **kwargs):
		'''Constructor method for BaseModel class'''

		self.id = str(uuid.uuid4())
		self.created_at = datetime.today()
		self.updated_at = self.created_at

	def __str__(self):
		'''String representation of BaseModel object'''
		return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

	def save(self):
		'''Method that updates the updated_at attribute'''
		self.updated_at = datetime.today()

	def to_dict(self):
		'''Returns the key/values of __dict__ of the instance'''
		self.__dict__["__class__"] = "BaseModel"
		self.__dict__["created_at"] = self.created_at.isoformat()	# change attr to str type
		self.__dict__["updated_at"] = self.updated_at.isoformat()	# change attr to str type
		return self.__dict__
