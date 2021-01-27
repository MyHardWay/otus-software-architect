import unittest
import os, sys

path_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src'
sys.path.append(path_)

from common import get_files_directory
from MatrixGenerator import MatrixGenerator
from MatrixProccessor import MatrixProccessor
from MatrixGeneratorAdapter import MatrixGeneratorAdapter
from MatrixFileLoader import MatrixFileLoader

class MainTests(unittest.TestCase):

    def test_file_loader_interface(self):
        file_loader = MatrixFileLoader()
        res_file = file_loader.get_file()
        self.assertTrue(res_file == get_files_directory() + 'F0.txt')


    def test_matrix_generator(self):
        generator = MatrixGenerator()
        file_name = generator.execute_matrix_generator()

        self.assertTrue(isinstance(generator.matrix_a, list))
        self.assertTrue(len(generator.matrix_a) == 3)
        self.assertTrue(len(generator.matrix_a[0]) == 3)
        self.assertTrue(file_name == get_files_directory() + 'F2.txt')


    def test_matrix_proccessor(self):
        file_loader = MatrixFileLoader()
        proccessor = MatrixProccessor(file_loader)
        sum_matrix = proccessor.proccess_matrix_summary()
        self.assertTrue(sum_matrix == [[4324, 13791, 12028], [8254, 6508, 9696], [12156, 11515, 11991]])


    def test_matrix_adapter(self):
        generator = MatrixGenerator()
        adapter = MatrixGeneratorAdapter(generator)
        file_name = adapter.get_file()
        self.assertTrue(file_name == get_files_directory() + 'F2.txt')


if __name__ == "__main__":
    unittest.main()
