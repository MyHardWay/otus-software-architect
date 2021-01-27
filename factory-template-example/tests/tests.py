import ast
import unittest
import os, sys

path_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src'
sys.path.append(path_)

from main import main

input_file = os.path.dirname(os.path.abspath(__file__)) + '/test.txt'
output_file = os.path.dirname(os.path.abspath(__file__)) + '/result.txt'

class MainTests(unittest.TestCase):

    def test_selection_sort(self):

        result = [1, 2, 6, 8]
        main(3, input_file, output_file)
        result_list, result_method = self.get_result_tuple(output_file)
        self.assertTrue(result_list == result)
        self.assertTrue(result_method == 'Сортировка выбором')

    def test_insert_sort(self):
        result = [1, 2, 6, 8]
        main(1, input_file, output_file)
        result_list, result_method = self.get_result_tuple(output_file)
        self.assertTrue(result_list == result)
        self.assertTrue(result_method == 'Сортировка вcтавками')

    def test_merge_sort(self):
        result = [1, 2, 6, 8]
        main(2, input_file, output_file)
        result_list, result_method = self.get_result_tuple(output_file)
        self.assertTrue(result_list == result)
        self.assertTrue(result_method == 'Сортировка слиянием')

    def get_result_tuple(self, output_file):
        with open(output_file) as f:
            sorted_list = ast.literal_eval(f.readline())
            result_method = f.readline()
        return sorted_list, result_method


if __name__ == "__main__":
    unittest.main()
