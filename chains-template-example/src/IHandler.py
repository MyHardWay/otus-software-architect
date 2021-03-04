from abc import ABC, abstractmethod


class IHandler(ABC):

    @abstractmethod
    def set_next(self):
        pass

    @abstractmethod
    def handle(self):
        pass

