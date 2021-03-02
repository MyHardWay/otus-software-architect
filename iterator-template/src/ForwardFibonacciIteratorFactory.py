from AbstractIteratorFactory import AbstractIteratorFactory
from ForwardFibonacciIterator import ForwardFibonachiIterator


class ForwardFibonacciIteratorFactory(AbstractIteratorFactory):

    def create_iterator(self):
        return ForwardFibonachiIterator