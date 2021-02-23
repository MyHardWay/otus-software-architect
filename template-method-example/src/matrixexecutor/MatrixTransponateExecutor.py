from .IMatrixExecutor import AbstractMatrixExecutor


class MatrixTransponateExecutor(AbstractMatrixExecutor):

    def execute(self, file_path):
        matrix = self.data_loader.load_data(file_path)
        print(file_path)
        print('here')
        print(matrix)
        return self._transponate_matrix(matrix)

    def _transponate_matrix(self, matrix):
        return [list(i) for i in zip(*matrix)]

