def get_matrix_dimension(matrix: list):
    try:
        N, M = len(matrix), len(matrix[0])
    except IndexError:
        return None
    return (N, M)


def is_matrix_same_dimension(*args) -> bool:
    N, M = None, None
    for i in args:
        dimension = get_matrix_dimension(i)
        if not dimension or (N != dimension[0] and N) or (M != dimension[1] and M):
            return False
        N, M = dimension
    return True

