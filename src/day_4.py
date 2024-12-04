import re
import numpy as np


def word_count(matrix):
    matches_count = 0
    enumerated_list = []
    for row in matrix:
        enumerated_list.append(list(enumerate(row)))

    # checking horizonal matches
    for row in matrix:
        row_joined = ''.join(row)
        matches = re.findall(r'SAMX|XMAS', row_joined)
        if matches:
            matches_count += len(matches)

    # checking vertical matches
    transposed_matrix = []
    for i in range(len(matrix[0])):
        transposed_column = []
        for row in matrix:
            transposed_column.append(row[i])
        transposed_matrix.append(transposed_column)

    for row in transposed_matrix:
        row_joined = ''.join(row)
        matches = re.findall(r'SAMX|XMAS', row_joined)
        if matches:
            matches_count += len(matches)

    # checking diagonal matches
    matrix_np = np.array(matrix)
    matrix_diag = [np.diag(matrix_np[-1:-matrix_np.shape[0]-1:-1,:], i).tolist() for i in range(-matrix_np.shape[0]+1,matrix_np.shape[0])]
    for row in matrix_diag:
        row_joined = ''.join(row)
        matches = re.findall(r'SAMX|XMAS', row_joined)
        if matches:
            matches_count += len(matches)

    flipped_matrix_np = matrix_np[:, ::-1]
    flipped_matrix_diag = [np.diag(flipped_matrix_np[-1:-flipped_matrix_np.shape[0]-1:-1,:], i).tolist() for i in range(-flipped_matrix_np.shape[0]+1,flipped_matrix_np.shape[0])]
    for row in flipped_matrix_diag:
        row_joined = ''.join(row)
        matches = re.findall(r'SAMX|XMAS', row_joined)
        if matches:
            matches_count += len(matches)

    return matches_count

