import unittest
from mock import Mock
from sample_payload import *
from request_parser import RequestParser

class RequestParserTest(unittest.TestCase):
    def setUp(self):
        self.env = {}
        self.env['wsgi.input'] = Mock()

    def test_detects_modified_files_in_single_commit(self):
        self.env['wsgi.input'].read.return_value = simple_payload
        self.request_parser = RequestParser(self.env)
        self.request = self.request_parser.parse()

        modified_files = set(['file4.py', 'file3.py'])
        self.assertEquals(self.request.modified_files, modified_files)

    def test_same_modified_file_is_detected_only_once_in_multiple_commits(self):
        self.env['wsgi.input'].read.return_value = complex_payload
        self.request_parser = RequestParser(self.env)
        self.request = self.request_parser.parse()

        modified_files = set(['file4.py', 'file3.py', 'file5.py'])
        self.assertEquals(self.request.modified_files, modified_files)


