from abc import ABC, abstractmethod

class IMatrixFileLoader(ABC):

    @abstractmethod
    def get_file(self):
        pass