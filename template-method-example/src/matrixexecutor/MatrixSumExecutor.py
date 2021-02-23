from .IMatrixExecutor import AbstractMatrixExecutor


class MatrixSumExecutor(AbstractMatrixExecutor):

    def execute(self, file_path):
        matrix_a, matrix_b = self.data_loader.load_data(file_path)
        return self._sum_matrix(matrix_a, matrix_b)

    def _sum_matrix(self, matrix_a, matrix_b):
        result = []
        for sublist in zip(matrix_a, matrix_b):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return result
