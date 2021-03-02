from AbstractIteratorFactory import AbstractIteratorFactory
from BackwardFibonacciIterator import BackwardFibonacciIterator


class BackwardFibonacciIteratorFactory(AbstractIteratorFactory):

    def create_iterator(self):
        return BackwardFibonacciIterator
