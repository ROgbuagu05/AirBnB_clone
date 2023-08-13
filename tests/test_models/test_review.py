#!/usr/bin/python3
'''Module to test City class'''
import unittest
from models.review import Review
from datetime import datetime


class TestCity(unittest.TestCase):
    '''A class that tests the City class'''

    def setUp(self):
        '''Set up instance to test City class'''
        self.one = Review()

    def tearDown(self):
        '''Destroy instance once tests are done'''
        del self.one

    def test_class_docs(self):
        '''Tests to see if City class documentation exists'''
        self.assertTrue(self.one.__doc__)

    def test_method_docs(self):
        '''Tests to see if CIty class methods documentation exits'''
        self.assertTrue(self.one.save.__doc__)
        self.assertTrue(self.one.to_dict.__doc__)

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
        self.assertTrue(self.one, Review)

    def test_field_attributes(self):
        '''Tests field attributes of City class'''
        self.one.place_id = "1234-1234"
        self.one.user_id = "1234"
        self.one.text = "Durban"
        self.assertEqual(self.one.place_id, "1234-1234")
        self.assertEqual(self.one.user_id, "1234")
        self.assertEqual(self.one.text, "Durban")
        self.assertTrue(isinstance(self.one.place_id, str))
        self.assertTrue(isinstance(self.one.user_id, str))
        self.assertTrue(isinstance(self.one.text, str))
        self.assertTrue(isinstance(self.one.id, str))
        self.assertTrue(isinstance(self.one.created_at, datetime))
        self.assertTrue(isinstance(self.one.updated_at, datetime))
