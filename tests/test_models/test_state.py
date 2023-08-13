#!/usr/bin/python3
'''Module to test State class'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''CLass that tests State class'''

    def setUp(self):
        '''Set up instances for testing'''
        self.one = State()

    def tearDown(self):
        '''Destroy instances once tests are done'''
        del self.one

    def test_class_docs(self):
        '''Test to see if class documentation exists'''
        self.assertTrue(self.one.__doc__)

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

    def test_instantiation(self):
        '''Tests instantiation'''
        self.assertTrue(isinstance(self.one, State))

    def test_field_attributes(self):
        '''Tests field attributes of State class'''
        self.one.name = "KZN"
        self.assertEqual(self.one.name, "KZN")
        self.assertTrue(isinstance(self.one.name, str))
