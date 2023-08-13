#!/usr/bin/python3
'''Module to test Place class'''
import unittest
from models.place import Place
from datetime import datetime


class TestCity(unittest.TestCase):
    '''A class that tests the City class'''

    def setUp(self):
        '''Set up instance to test City class'''
        self.one = Place()

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
        self.assertTrue(self.one, Place)

    def test_field_attributes(self):
        '''Tests field attributes of City class'''
        self.one.city_id = "1234-1234"
        self.one.user_id = "1234"
        self.one.name = "Town"
        self.one.description = "Cabin"
        self.one.number_rooms = 2
        self.one.number_bathrooms = 1
        self.one.max_guest = 4
        self.one.price_by_night = 1000
        self.one.latitude = 20.4
        self.one.longitude = 34.7
        self.one.amenity_ids = ["wifi", "games"]

        self.assertEqual(self.one.city_id, "1234-1234")
        self.assertEqual(self.one.user_id, "1234")
        self.assertEqual(self.one.name, "Town")
        self.assertEqual(self.one.description, "Cabin")
        self.assertEqual(self.one.number_rooms, 2)
        self.assertEqual(self.one.number_bathrooms, 1)
        self.assertEqual(self.one.max_guest, 4)
        self.assertEqual(self.one.price_by_night, 1000)
        self.assertEqual(self.one.latitude, 20.4)
        self.assertEqual(self.one.longitude, 34.7)
        self.assertEqual(self.one.amenity_ids, ["wifi", "games"])

        self.assertTrue(isinstance(self.one.city_id, str))
        self.assertTrue(isinstance(self.one.user_id, str))
        self.assertTrue(isinstance(self.one.name, str))
        self.assertTrue(isinstance(self.one.description, str))
        self.assertTrue(isinstance(self.one.number_rooms, int))
        self.assertTrue(isinstance(self.one.number_bathrooms, int))
        self.assertTrue(isinstance(self.one.max_guest, int))
        self.assertTrue(isinstance(self.one.price_by_night, int))
        self.assertTrue(isinstance(self.one.latitude, float))
        self.assertTrue(isinstance(self.one.longitude, float))
        self.assertTrue(isinstance(self.one.amenity_ids, list))
        self.assertTrue(isinstance(self.one.id, str))
        self.assertTrue(isinstance(self.one.created_at, datetime))
        self.assertTrue(isinstance(self.one.updated_at, datetime))
