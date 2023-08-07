#!/usr/bin/python3
'''Unittest module to test BaseModel class'''
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBase(unittest.TestCase):
    '''Test class to test BaseModel'''

    def setUp(self):
        '''Set up instances in order to run tests'''

        self.one = BaseModel()
        self.two = BaseModel(None)
        self.three = BaseModel()
        self.three.name = "Kivashan"
        self.three.number = 98

    def tearDown(self):
        '''Tear down instances from setUp method'''

        del (self.one)
        del (self.two)
        del (self.three)

    def test_for_class_docs(self):
        '''Tests to see if class documentation is present'''

        self.assertIsNotNone(self.__doc__)

    def test_for_method_docs(self):
        '''Tests to see if method documentation exists for methods
        contained in the class'''

        self.assertIsNotNone(self.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instantiation(self):
        '''Tests instances of Base class'''
        self.assertTrue(isinstance(self.one, BaseModel))
        self.assertTrue(isinstance(self.two, BaseModel))
        self.assertTrue(isinstance(self.three, BaseModel))

    def test_save_method(self):
        '''Tests if the save method updates attr updated_at'''

        val1 = self.one.updated_at
        self.one.save()
        self.assertNotEqual(val1, self.one.updated_at)

    def test_to_dict_method(self):
        '''Tests to_dict method'''

        new_dict = self.one.to_dict()
        self.assertTrue(isinstance(new_dict, dict))
        self.assertTrue(isinstance(new_dict["created_at"], str))
        self.assertTrue(isinstance(new_dict["updated_at"], str))
        self.assertTrue(new_dict["__class__"])

    def test_field_attributes(self):
        '''Tests any class or instance attributes'''

        self.assertTrue(isinstance(self.one.id, str))
        self.assertTrue(isinstance(self.one.created_at, datetime))
        self.assertTrue(isinstance(self.one.updated_at, datetime))
        # test created_at and updated_at when instance is created
        self.assertEqual(self.one.created_at, self.one.updated_at)
