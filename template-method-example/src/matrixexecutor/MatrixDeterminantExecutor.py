from .IMatrixExecutor import AbstractMatrixExecutor


class MatrixDeterminantExecutor(AbstractMatrixExecutor):

    def execute(self, file_path):
        matrix = self.data_loader.load_data(file_path)
        return self._produce_determinant(matrix)

    def _produce_determinant(self, matrix, total=0):
        indices = list(range(len(matrix)))
        if len(matrix) == 2 and len(matrix[0]) == 2:
            val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return val
        for fc in indices:
            As = matrix[:]
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1:]

            sign = (-1) ** (fc % 2)  # F)
            sub_det = self._produce_determinant(As)
            total += sign * matrix[0][fc] * sub_det
        return total