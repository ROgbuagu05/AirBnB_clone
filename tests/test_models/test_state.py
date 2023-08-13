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

    def test_instantiation(self):
        '''Tests instantiation'''
        self.assertTrue(isinstance(self.one, State))

    def test_field_attributes(self):
        '''Tests field attributes of State class'''
        self.one.name = "KZN"
        self.assertEqual(self.one.name, "KZN")
        self.assertTrue(isinstance(self.one.name, str))
