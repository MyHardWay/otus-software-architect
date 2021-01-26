from .iSortFactory import ISortFactory

class InsertSort(ISortFactory):

    def sort(self, input_list: list) -> list:
        sorted_list = input_list[:]
        for i in range(1, len(sorted_list)):
            key = sorted_list[i]
            j = i - 1
            while j >= 0 and key < sorted_list[j]:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
                sorted_list[j + 1] = key
        return sorted_list

    def get_sort_method(self):
        return 'Сортировка вcтавками'
