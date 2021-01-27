import ast

from common import save_matrix, remove_file, get_files_directory


class MatrixProccessor():

    def __init__(self, file_loader):
        self.file_loader = file_loader


    def _sum_matrix(self, matrix_a, matrix_b):
        result = []
        for sublist in zip(matrix_a, matrix_b):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return result

    def _read_matrix(self, file_name):
        try:
            with open(file_name, 'r') as f:
                matrix_a = ast.literal_eval(f.readline())
                matrix_b = ast.literal_eval(f.readline())
        except (FileNotFoundError):
            print('Output directory doesnt exists')
            return
        return matrix_a, matrix_b


    def proccess_matrix_summary(self):
        print('Read matrix...')
        file_name = self.file_loader.get_file()
        res = self._read_matrix(file_name)
        if not res:
            return
        print('Sum matrix')
        matrix_a, matrix_b = res
        file_name = get_files_directory() + 'F1.txt'
        new_matrix = self._sum_matrix(matrix_a, matrix_b)
        print('Saving to file...')
        remove_file(file_name)
        save_matrix(file_name, new_matrix)
        return new_matrix


if __name__ == '__main__':
    proccessor = MatrixProccessor()
    proccessor.proccess_matrix_summary()
