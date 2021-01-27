import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from MatrixProccessor import MatrixProccessor
from MatrixGeneratorAdapter import MatrixGeneratorAdapter
from MatrixGenerator import MatrixGenerator
from MatrixFileLoader import MatrixFileLoader


def main():
    print('Matrix proccessing from F0.txt')
    file_loader = MatrixFileLoader()
    proccessor = MatrixProccessor(file_loader)
    proccessor.proccess_matrix_summary()
    print('Done.')

    print('Matrix proccessing via Adapter')
    generator = MatrixGenerator()
    adapter = MatrixGeneratorAdapter(generator)
    proccessor = MatrixProccessor(adapter)
    proccessor.proccess_matrix_summary()
    print('Done.')


if __name__ == '__main__':
    main()
