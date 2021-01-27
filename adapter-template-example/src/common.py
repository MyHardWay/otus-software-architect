import json
import os


def save_matrix(file_name, matrix):
    try:
        with open(file_name, 'a') as f:
            f.write(json.dumps(matrix))
            f.write('\n')
    except FileNotFoundError:
        print('Output directory doesnt exists')
        return


def remove_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        return


def get_files_directory():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/'
