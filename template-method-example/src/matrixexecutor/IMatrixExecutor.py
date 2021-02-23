from abc import ABC, abstractmethod


class AbstractMatrixExecutor(ABC):

    def __init__(self, data_loader):
        self.data_loader = data_loader()

    @abstractmethod
    def execute(self):
        pass
