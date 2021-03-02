import argparse

from BackwardFibonacciIterator import BackwardFibonacciIteratorFactory
from ForwardFibonacciIterator import ForwardFibonachiIteratorFactory
from FibonacciCollection import FibonacciCollection


def main(output_file, fibonacci_count, reverse):
    print('Start. Writting {0} of fibonacci sequence with reverse {1} to {2}'.format(output_file,
                                                                                    fibonacci_count, reverse))
    if reverse == 1:
        factory = BackwardFibonacciIteratorFactory()
    elif reverse == 2:
        factory = ForwardFibonachiIteratorFactory()
    iterator = factory.create_iterator()
    collection = FibonacciCollection(iterator, fibonacci_count)
    for i in collection:
        try:
            with open(output_file, 'a') as f:
                f.write(str(i) + '\n')
        except FileNotFoundError:
            print('Output directory doesnt exists')
            return
    print('Done.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program for sorting array from a file.')
    parser.add_argument('fibonacci_count', metavar='fibonacci_count', type=int,
                        help='Set fibonacci count')
    parser.add_argument('output_file', metavar='input_file', type=str,
                        help='Input file full path')
    parser.add_argument('reverse', metavar='reverse', type=int, choices=[1, 2],
                        help='1 - Use reverse, 2 - Doesnt use.')
    args = parser.parse_args()
    main(args.output_file, args.fibonacci_count, args.reverse)
