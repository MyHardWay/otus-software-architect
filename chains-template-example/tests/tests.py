import unittest
import os, sys


path_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src'
sys.path.append(path_)

from XmlHandler import XmlHandler
from TxtHandler import TxtHandler
from JsonHandler import JsonHandler
from CsvHandler import CsvHandler


class MainTests(unittest.TestCase):

    def setUp(self):
        self.h1, self.h2, self.h3, self.h4 = XmlHandler(), TxtHandler(), JsonHandler(), CsvHandler()
        self.h1.set_next(self.h2)
        self.h2.set_next(self.h3)
        self.h3.set_next(self.h4)
        self.files_dict = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/tests/test_data/'
        self.output_file = self.files_dict + 'result.res'
        open(self.output_file, 'w').close()

    def test_xml(self):
        file_name = self.files_dict + 'Test.xml'
        self.h1.handle(file_name, self.output_file)
        with open(self.output_file, 'r') as f:
            content = f.readline()
        self.assertTrue('XmlHandler' in content)

    def test_json(self):
        file_name = self.files_dict + 'Test.json'
        self.h1.handle(file_name, self.output_file)
        with open(self.output_file, 'r') as f:
            content = f.readline()
        self.assertTrue('JsonHandler' in content)

    def test_txt(self):
        file_name = self.files_dict + 'Test.txt'
        self.h1.handle(file_name, self.output_file)

        with open(self.output_file, 'r') as f:
            content = f.readline()
        self.assertTrue('TxtHandler' in content)

    def test_csv(self):
        file_name = self.files_dict + 'Test.csv'
        self.h1.handle(file_name, self.output_file)

        with open(self.output_file, 'r') as f:
            content = f.readline()
        self.assertTrue('CsvHandler' in content)

if __name__ == "__main__":
    unittest.main()
