#!/usr/bin/python3
'''Test module to test file_storage.py and obj_parser.py'''
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    '''Class for testing file_storage.py and obj_parser.py'''

    def setUp(self):
        '''Set up instances in order to run tests'''
        self.storage = FileStorage()

    def tearDown(self):
        '''Delete instances once tests are done'''
        del (self.storage)

    def test_for_class_docs(self):
        '''Tests to see if class documentation is present'''

        self.assertIsNotNone(self.__doc__)
