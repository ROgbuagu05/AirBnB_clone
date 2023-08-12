#!/usr/bin/python3
'''Test module to test file_storage.py and obj_parser.py'''
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.engine.obj_parser import obj_parser


class TestFileStorage(unittest.TestCase):
    '''Class for testing file_storage.py and obj_parser.py'''

    def setUp(self):
        '''Set up instances in order to run tests'''

        self.store = FileStorage()
        self.one = BaseModel()

    def tearDown(self):
        '''Delete instances once tests are done'''

        del (self.store)
        del (self.one)

    def test_for_class_docs(self):
        '''Tests to see if class documentation is present'''

        self.assertIsNotNone(self.__doc__)

    def test_for_method_docs(self):
        '''Tests to see if method documentation is present'''

        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_instantiation(self):
        '''Tests to see if object is of class FileStorage'''
        self.assertTrue(isinstance(self.store, FileStorage))

    def test_all(self):
        '''Tests the all method'''
        self.assertTrue(isinstance(self.store.all(), dict))
        with self.assertRaises(AttributeError):
            FileStorage.all(24)

    def test_new(self):
        '''Tests the new method'''
        objects = self.store.all()
        self.two = BaseModel()
        self.store.new(self.two)
        # check if new object was added into __objects
        # self.assertEqual(len(self.store.all()), len(objects) + 1)
        # check if object id exists in __objects
        key = "{}.{}".format("BaseModel", self.two.id)
        self.assertTrue(key in objects)



