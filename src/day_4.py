import re
from pprint import pprint

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
    
        # row_values = list(zip(*row))[1]
        # row_joined = ''.join(row_values)

    return matches_count

