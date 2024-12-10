def wrapper_func(grid, row_index, col_index, current_num):

    running_total = 0

    def explore_grid(grid, row_index, col_index, current_num, visited):
        nonlocal running_total

        if (row_index, col_index) in visited:
            return
        visited.add((row_index, col_index))

        try:
            if current_num == 9:
                running_total += 1
            if grid[row_index+1][col_index] == current_num+1:
                explore_grid(grid, row_index+1, col_index, current_num+1, visited)
            if grid[row_index-1][col_index] == current_num+1:
                explore_grid(grid, row_index-1, col_index, current_num+1, visited)
            if grid[row_index][col_index+1] == current_num+1:
                explore_grid(grid, row_index, col_index+1, current_num+1, visited)
            if grid[row_index][col_index-1] == current_num+1:
                explore_grid(grid, row_index, col_index-1, current_num+1, visited)
        except IndexError:
            pass
    
    explore_grid(grid, row_index, col_index, current_num, set())
    return running_total

def trail_finder(input_matrix):
    input_matrix_list = [[int(character) if character != '.' else character for character in row ] for row in input_matrix]
    running_total = 0
    for row_index, row in enumerate(input_matrix_list):
        for column_index, item in enumerate(row):
            if item == 0:
                total_paths = 0
                total_paths += wrapper_func(input_matrix_list, row_index, column_index, 0)
                if total_paths > 0:
                    running_total += total_paths
    return running_total
