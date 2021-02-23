import argparse
import json
import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from matrixexecutor.MatrixSumExecutor import  MatrixSumExecutor
from matrixexecutor.MatrixDeterminantExecutor import MatrixDeterminantExecutor
from matrixexecutor.MatrixTransponateExecutor import MatrixTransponateExecutor
from matrixdataloader.SingleMatrixFileDataLoader import SingleMatrixFileDataLoader
from matrixdataloader.PairMatrixFileDataLoader import PairMatrixFileDataLoader



def main(operation_method, input_file, output_file):
    print('Start. Reading from {0}, method_id {1}, save to {2}'.format(operation_method, input_file, output_file))

    if operation_method == 1:
        matrix_executor = MatrixSumExecutor(PairMatrixFileDataLoader)
    elif operation_method == 2:
        matrix_executor = MatrixDeterminantExecutor(SingleMatrixFileDataLoader)
    elif operation_method == 3:
        matrix_executor = MatrixTransponateExecutor(SingleMatrixFileDataLoader)
    else:
        print('Unsupported method')
        return

    result = matrix_executor.execute(input_file)
    print('Write to file...')
    try:
        with open(output_file, 'w') as f:
            f.write(json.dumps(result))
    except FileNotFoundError:
        print('Output directory doesnt exists')
        return
    print('Done.')


if __name__ == '__main__':

    print(*[[1,3], [4,5]])

    parser = argparse.ArgumentParser(description='Programm for sorting array from a file.')
    parser.add_argument('operation_method', metavar='operation_method', type=int, choices=[1, 2, 3],
                        help='Operation method. 1 - sum matrix, 2 - find determinant, 3 - transponate')
    parser.add_argument('input_file', metavar='input_file', type=str,
                        help='Input file full path')
    parser.add_argument('output_file', metavar='output_file', type=str,
                        help='Output file full path')
    args = parser.parse_args()
    main(args.operation_method, args.input_file, args.output_file)