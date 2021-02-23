import ast

from .IMatrixDataLoader import AbstractMatrixDataLoader


class SingleMatrixFileDataLoader(AbstractMatrixDataLoader):

    def load_data(self, file_path):
        try:
            with open(file_path) as f:
                matrix_a = ast.literal_eval(f.readline())
        except FileNotFoundError:
            return
        return matrix_a
