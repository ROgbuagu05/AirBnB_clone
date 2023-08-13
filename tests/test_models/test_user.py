#!/usr/bin/python3
'''Module to test the User class'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Class to test User class'''

    def setUp(self):
        '''Set up instances for test cases'''
        self.one = User()

    def tearDown(self):
        '''Destroy instances once tests are done'''
        del self.one

    def test_class_docs(self):
        '''Test to see if class documentation exists'''
        self.assertTrue(self.one.__doc__)

    def test_field_attributes(self):
        '''Test field attributes of User class'''
        self.one.email = "bvk@email.com"
        self.one.first_name = "Kivashan"
        self.one.last_name = "Brandon"
        self.one.password = "abc"

        self.assertEqual(self.one.email, "bvk@email.com")
        self.assertEqual(self.one.first_name, "Kivashan")
        self.assertEqual(self.one.last_name, "Brandon")
        self.assertEqual(self.one.password, "abc")

        self.assertTrue(isinstance(self.one.email, str))
        self.assertTrue(isinstance(self.one.first_name, str))
        self.assertTrue(isinstance(self.one.last_name, str))
        self.assertTrue(isinstance(self.one.password, str))

    def test_instantiation(self):
        '''Tests instantiation of User class'''

        self.assertTrue(self.one, User)
