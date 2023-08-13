#!/usr/bin/python3
'''Module to test City class'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''A class that tests the City class'''

    def setUp(self):
        '''Set up instance to test City class'''
        self.one = City()

    def tearDown(self):
        '''Destroy instance once tests are done'''
        del self.one

    def test_class_docs(self):
        '''Tests to see if City class documentation exists'''
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
        self.assertTrue(self.one, City)

    def test_field_attributes(self):
        '''Tests field attributes of City class'''
        self.one.state_id = "1234-1234"
        self.one.name = "Durban"
        self.assertEqual(self.one.state_id, "1234-1234")
        self.assertEqual(self.one.name, "Durban")
        self.assertTrue(isinstance(self.one.state_id, str))
        self.assertTrue(isinstance(self.one.name, str))
