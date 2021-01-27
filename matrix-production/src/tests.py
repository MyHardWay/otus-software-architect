import unittest
from main import multiprocess_multiply
import os, sys

path_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_)


class MainTests(unittest.TestCase):

    def test_multiply_result(self):
        matrix_a = [[2, 2], [3, 3]]
        matrix_b = [[4, 1], [5, 6]]
        calculated_result = multiprocess_multiply(matrix_a, matrix_b)
        result = [[18, 14], [27, 21]]
        self.assertTrue(calculated_result == result)

    def test_different_dimension(self):
        matrix_a = [[2, 2, 3], [3, 3]]
        matrix_b = [[4, 1], [5, 6]]
        calculated_result = multiprocess_multiply(matrix_a, matrix_b)
        self.assertTrue(calculated_result == False)

    def test_empty_matrix(self):
        matrix_a = []
        matrix_b = []
        calculated_result = multiprocess_multiply(matrix_a, matrix_b)
        self.assertTrue(calculated_result == False)

if __name__ == "__main__":
    unittest.main()
