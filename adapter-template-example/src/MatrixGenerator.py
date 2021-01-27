import random

from common import save_matrix, remove_file, get_files_directory

class MatrixGenerator():

    def __init__(self):
        self.file_name = get_files_directory() + 'F2.txt'
        self.matrix_a = []
        self.matrix_b = []

    def _gen_matrix(self):
        new_matrix = []
        for i in range(3):
            sub_array = []
            for j in range(3):
                sub_array.append(random.randint(1, 10000))
            new_matrix.append(sub_array)
        return new_matrix

    def execute_matrix_generator(self):
        print('Gen matrix...')
        self.matrix_a = self._gen_matrix()
        self.matrix_b = self._gen_matrix()
        remove_file(self.file_name)
        print('Saving to file...')
        save_matrix(self.file_name, self.matrix_a)
        save_matrix(self.file_name, self.matrix_b)
        return self.file_name

if __name__ == '__main__':
    generator = MatrixGenerator()
    generator.execute_matrix_generator()
