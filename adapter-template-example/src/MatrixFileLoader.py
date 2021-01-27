from IMatrixFileLoader import IMatrixFileLoader
from common import get_files_directory

class MatrixFileLoader(IMatrixFileLoader):

    def get_file(self):
        return get_files_directory() + 'F0.txt'