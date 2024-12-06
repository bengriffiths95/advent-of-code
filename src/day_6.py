from copy import deepcopy


def change_direction(current_direction):
    if current_direction == 'up':
        return 'right'
    if current_direction == 'right':
        return 'down'
    if current_direction == 'down':
        return 'left'
    if current_direction == 'left':
        return 'up'

def guard_position(input_matrix):
    matrix = deepcopy(input_matrix)
    for index, list in enumerate(matrix):
        try:
            if list.index('^') >= 0:
                pos1 = index
                pos2 = list.index('^')
        except Exception:
            continue

    searching = True
    current_direction = 'up'

    while searching == True:
        try:
            if current_direction == 'up':
                next_pos1, next_pos2 = pos1-1, pos2
            elif current_direction == 'right':
                next_pos1, next_pos2 = pos1, pos2+1
            elif current_direction == 'down':
                next_pos1, next_pos2 = pos1+1, pos2
            elif current_direction == 'left':
                next_pos1, next_pos2 = pos1, pos2-1
        
            if next_pos1 == -1 or next_pos2 == -1:
                matrix[pos1].pop(pos2)
                matrix[pos1].insert(pos2, 'X')
                searching = False                
            elif matrix[next_pos1][next_pos2] == '.' or matrix[next_pos1][next_pos2] == 'X':
                matrix[pos1].pop(pos2)
                matrix[pos1].insert(pos2, 'X')
                pos1 = next_pos1
                pos2 = next_pos2
            elif matrix[next_pos1][next_pos2] == '#':
                matrix[pos1].pop(pos2)
                matrix[pos1].insert(pos2, 'X')
                current_direction = change_direction(current_direction)
            else:
                matrix[pos1].pop(pos2)
                matrix[pos1].insert(pos2, 'X')
                searching = False
        except:
            matrix[pos1].pop(pos2)
            matrix[pos1].insert(pos2, 'X')
            searching = False

# invoking function with input files
with open('inputs/day_6.txt') as f:
    input_list_str = [line.rstrip().split(',') for line in f]
    input_list = [list(line[0]) for line in input_list_str]

print(guard_position(input_list))