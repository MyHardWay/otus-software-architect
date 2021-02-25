import ast
import unittest
import os, sys

proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_ = proj_path + '/src'
sys.path.append(path_)

from BackwardFibonacciIterator import BackwardFibonacciIterator
from ForwardFibonacciIterator import ForwardFibonachiIterator
from FibonacciCollection import FibonacciCollection


class MainTests(unittest.TestCase):


    def test_forward_fibonacci(self):
        iterator = ForwardFibonachiIterator
        collection = FibonacciCollection(iterator, 5)
        for i in collection:
            print(i)
        calculated_result = list([i for i in collection])
        result = [0, 1, 1, 2, 3, 5]
        self.assertTrue(calculated_result == result)

    def test_backward_fibonacci(self):
        iterator = BackwardFibonacciIterator
        collection = FibonacciCollection(iterator, 5)
        calculated_result = list([int(i) for i in collection])
        result = [5, 3, 2, 1, 1, 0]
        self.assertTrue(calculated_result == result)



if __name__ == "__main__":
    unittest.main()