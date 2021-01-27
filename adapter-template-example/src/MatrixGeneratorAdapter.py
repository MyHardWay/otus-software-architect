from IMatrixFileLoader import IMatrixFileLoader
from MatrixGenerator import MatrixGenerator

class MatrixGeneratorAdapter(IMatrixFileLoader):
    def __init__(self, generator: MatrixGenerator):
        self.generator = generator

    def get_file(self):
        file_name = self.generator.execute_matrix_generator()
        return file_name