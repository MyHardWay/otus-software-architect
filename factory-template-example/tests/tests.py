import ast
import unittest
import sys
sys.path.append('../')

from src.main import main

class MainTests(unittest.TestCase):

    def test_selection_sort(self):
        input_file = 'test.txt'
        output_file = 'result.txt'
        result = [1, 2, 6, 8]
        main(3, input_file, output_file)
        result_list, result_method = self.get_result_tuple(output_file)
        self.assertTrue(result_list == result)
        self.assertTrue(result_method == 'Сортировка выбором')

    def test_insert_sort(self):
        input_file = 'test.txt'
        output_file = 'result.txt'
        result = [1, 2, 6, 8]
        main(1, input_file, output_file)
        result_list, result_method = self.get_result_tuple(output_file)
        self.assertTrue(result_list == result)
        self.assertTrue(result_method == 'Сортировка вcтавками')

    def test_merge_sort(self):
        input_file = 'test.txt'
        output_file = 'result.txt'
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
