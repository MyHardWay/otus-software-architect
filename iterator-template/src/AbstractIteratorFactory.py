from abc import ABC, abstractmethod


class AbstractIteratorFactory(ABC):

    @abstractmethod
    def create_iterator(self):
        pass
