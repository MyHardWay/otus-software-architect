from multiprocessing import Queue, cpu_count, Process

from common import is_matrix_same_dimension, get_matrix_dimension


def multiprocess_multiply(matrix_1: list, matrix_2:list, process_num: int):
    tasks = Queue()
    res = Queue()

    if not is_matrix_same_dimension(matrix_1, matrix_2):
        return False

    calculate_process = [Process(target=calculate, args=[tasks, res]) for i in range(process_num)]

    N, M = get_matrix_dimension(matrix_1)
    res_lst = [[None] * N] * M

    for i in range(N):
        for j in range(M):
            tasks.put((i, j, matrix_1[i][j], matrix_2[i][j]))

    for w in calculate_process:
        w.start()

    for i in calculate_process:
        i.join()

    while not res.empty():
        i, j, elem = res.get()
        res_lst[i][j] = elem
    return res_lst


def calculate(req_queue: Queue, res_queue: Queue):
    while not req_queue.empty():
        elements = req_queue.get()
        i, j, elem_1, elem_2 = elements
        elem = elem_1 * elem_2
        res_queue.put((i, j, elem))


if __name__ == '__main__':

    CORE_COUNT = cpu_count()

    a = [[2, 2], [3, 3]]
    b = [[4, 1], [5, 6]]
    res = multiprocess_multiply(a, b, CORE_COUNT)
    print(res)

