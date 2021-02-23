import ast

from .IMatrixDataLoader import AbstractMatrixDataLoader


class PairMatrixFileDataLoader(AbstractMatrixDataLoader):

    def load_data(self, file_path):
        try:
            with open(file_path) as f:
                matrix_a = ast.literal_eval(f.readline())
                matrix_b = ast.literal_eval(f.readline())
        except FileNotFoundError:
            return
        return matrix_a, matrix_b
