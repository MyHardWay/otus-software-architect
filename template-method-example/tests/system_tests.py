import ast
import unittest
import os, sys

proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_ = proj_path + '/src'
sys.path.append(path_)

from main import main


class MainTests(unittest.TestCase):

    def test_matrix_summary(self):
        input_file = proj_path + '/tests/testing_data/input_multi_data.txt'
        output_file = proj_path + '/tests/testing_data/ouput_sumary.sample'
        main(1, input_file, output_file)
        with open(output_file) as f:
            calculated_result = ast.literal_eval(f.readline())
        result = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        self.assertTrue(calculated_result == result)

    def test_matrix_determinant(self):
        input_file = proj_path + '/tests/testing_data/input_single_data.txt'
        output_file = proj_path + '/tests/testing_data/ouput_determinant.sample'
        main(2, input_file, output_file)
        with open(output_file) as f:
            calculated_result = ast.literal_eval(f.readline())
        result = 0
        self.assertTrue(calculated_result == result)

    def test_matrix_transparent(self):
        input_file = proj_path + '/tests/testing_data/input_single_data.txt'
        output_file = proj_path + '/tests/testing_data/ouput_transparent.sample'
        main(3, input_file, output_file)
        with open(output_file) as f:
            calculated_result = ast.literal_eval(f.readline())
        result = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertTrue(calculated_result == result)

if __name__ == "__main__":
    unittest.main()