from .iSortFactory import ISortFactory

class SelectionSort(ISortFactory):

    def sort(self, input_list: list) -> list:
        sorted_list = input_list[:]
        for i in range(len(sorted_list)):
            min_idx = i
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[min_idx] > sorted_list[j]:
                    min_idx = j
            sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
        return sorted_list

    def get_sort_method(self):
        return 'Сортировка выбором'
