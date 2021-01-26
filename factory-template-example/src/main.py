import argparse
import json
import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from concretesortfactory.insertSort import InsertSort
from concretesortfactory.mergeSort import MergeSort
from concretesortfactory.selectionSort import SelectionSort


def main(sort_method, input_file, output_file):
    print('Proccessing...')
    print('Read list..')
    try:
        with open(input_file) as f:
            unsorted_list = json.load(f)
    except FileNotFoundError:
        print('Input file doesnt exists')
        return

    print('Setting sort method...')
    if sort_method == 1:
        sort_executor = InsertSort()
    elif sort_method == 2:
        sort_executor = MergeSort()
    elif sort_method == 3:
        sort_executor = SelectionSort()
    else:
        print('Unsupported sort method')
        return

    print('Sorting...')
    sorted_list = sort_executor.sort(unsorted_list)

    print('Write to file...')
    try:
        with open(output_file, 'w') as f:
            f.write(json.dumps(sorted_list))
            f.write('\n')
            f.write(sort_executor.get_sort_method())
    except FileNotFoundError:
        print('Output directory doesnt exists')
        return

    print('Done.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Programm for sorting array from a file.')
    parser.add_argument('sort_method', metavar='sort_method', type=int, choices=[1, 2, 3],
                        help='Sort method. 1 - insertSort, 2 - mergeSort, 3 - selectionSort')
    parser.add_argument('input_file', metavar='input_file', type=str,
                        help='Input file full path')
    parser.add_argument('output_file', metavar='output_file', type=str,
                        help='Output file full path')
    args = parser.parse_args()
    main(args.sort_method, args.input_file, args.output_file)
