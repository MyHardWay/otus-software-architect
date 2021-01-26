from abc import ABC, abstractmethod


class ISortFactory(ABC):

    @abstractmethod
    def sort(self, input_list: list) -> list:
        pass

    @abstractmethod
    def get_sort_method(self) -> str:
        pass
