from abc import ABC, abstractmethod


class IFibonacciIterator(ABC):

    @abstractmethod
    def is_last(self, value):
        pass

    @abstractmethod
    def __next__(self):
        pass
