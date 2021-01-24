from multiprocessing import Queue, cpu_count, Process

from common import is_matrix_same_dimension, get_matrix_dimension


def multiprocess_multiply(matrix_1: list, matrix_2:list):
    tasks = Queue()
    res = Queue()
    CORE_COUNT = cpu_count()

    if not is_matrix_same_dimension(matrix_1, matrix_2):
        return False

    N, M = get_matrix_dimension(matrix_1)
    res_lst = [[0 for x in range(N)] for y in range(M)]

    calculate_process = [Process(target=calculate, args=[tasks, res, matrix_1, matrix_2]) for i in range(CORE_COUNT)]

    for i in range(N):
        for j in range(M):
            tasks.put((i, j))

    for w in calculate_process:
        w.start()

    for i in calculate_process:
        i.join()

    while not res.empty():
        i, j, elem = res.get()
        res_lst[i][j] = elem
    return res_lst


def calculate(req_queue: Queue, res_queue: Queue, matrix_1, matrix_2):
    while not req_queue.empty():
        indexes = req_queue.get()
        i, j = indexes
        elem = 0
        for k in range(len(matrix_2)):
            elem += (matrix_1[i][k] * matrix_2[k][j])
        res_queue.put((i, j, elem))
