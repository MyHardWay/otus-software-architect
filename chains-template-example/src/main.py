import argparse
import os

from XmlHandler import XmlHandler
from TxtHandler import TxtHandler
from JsonHandler import JsonHandler
from CsvHandler import CsvHandler


def main(files_directory: str, output_file: str) -> None:
    paths = [os.path.join(files_directory, fn) for fn in next(os.walk(files_directory))[2]]
    h1, h2, h3, h4 = XmlHandler(), TxtHandler(), JsonHandler(), CsvHandler()
    h1.set_next(h2)
    h2.set_next(h3)
    h3.set_next(h4)
    for path in paths:
        h1.handle(path, output_file)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Programm for sorting array from a file.')
    parser.add_argument('files_directory', metavar='files_directory', type=str,
                        help='Set the input directory')
    parser.add_argument('output_file', metavar='output_file', type=str,
                        help='Set the output file')
    args = parser.parse_args()
    main(args.files_directory, args.output_file)
