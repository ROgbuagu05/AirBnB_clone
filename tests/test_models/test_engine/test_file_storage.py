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
        self.store2 = FileStorage()
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
        # Test len of self.__objects before new method is called
        objects = self.store.all()
        self.assertEqual(len(objects), 2)

        # Test len of self.__objects after new method is called
        self.two = BaseModel()
        self.store.new(self.two)
        objects = self.store.all()
        self.assertEqual(len(objects), 3)

        # check if object id exists in __objects
        key = "{}.{}".format("BaseModel", self.two.id)
        self.assertTrue(key in objects)

    def test_save(self):
        '''Tests the save method'''
        # save to file
        self.store.new(self.one)
        self.store.save()

        # open file to check if object BaseModel has been saved
        key = "{}.{}".format("BaseModel", self.one.id)
        with open("file.json", "r", encoding="utf-8") as f:
            json_str = f.read()
            # check if <class>.<obj.id> is in file
            self.assertTrue(key in json_str)

    def test_reload(self):
        '''Tests the reload method'''
        # check len of self.__objects before reload is called
        self.assertEqual(len(self.store.all()), 3)

        # store object to file using json
        self.store.new(self.one)
        self.store.save()

        # reload object from file
        objects = self.store.reload()
        self.assertTrue(isinstance(objects, dict))
        self.assertEqual(objects, self.store.all())
        with self.assertRaises(TypeError):
            self.store.reload("Hello")

    def test_class_field_attributes(self):
        '''Tests the field attributes for the class'''

        self.store.new(self.one)
        # check attribute types
        self.assertTrue(isinstance(self.store._FileStorage__file_path, str))
        self.assertTrue(isinstance(self.store._FileStorage__objects, dict))

        self.three = BaseModel()
        self.store.new(self.three)
        key = "{}.{}".format("BaseModel", self.three.id)
        # check value of attribute
        self.assertEqual(self.store._FileStorage__file_path, "file.json")
        self.assertTrue(key in self.store._FileStorage__objects)
