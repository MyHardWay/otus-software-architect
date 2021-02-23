from abc import ABC, abstractmethod

class AbstractMatrixDataLoader(ABC):

    @abstractmethod
    def load_data(self, file_path):
        pass