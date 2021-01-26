from .iSortFactory import ISortFactory

class MergeSort(ISortFactory):

    def sort(self, input_list: list) -> list:
        sorted_list = input_list[:]
        if len(sorted_list) > 1:
            mid = len(sorted_list) // 2
            lefthalf, righthalf = sorted_list[:mid], sorted_list[mid:]

            self.sort(lefthalf)
            self.sort(righthalf)

            i, j, k = 0, 0 , 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    sorted_list[k] = lefthalf[i]
                    i += 1
                else:
                    sorted_list[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                sorted_list[k] = lefthalf[i]
                i, k = i + 1, k + 1

            while j < len(righthalf):
                sorted_list[k] = righthalf[j]
                j, k = j + 1, k + 1
        return sorted_list

    def get_sort_method(self):
        return 'Сортировка слиянием'
