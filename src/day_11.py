from copy import deepcopy

def stone_splitter(input_list, number_blinks):
    transformed_list = {0: deepcopy(input_list)}
    for i in range(0, number_blinks):
        current_list = []
        for item in transformed_list[i]:
            if item == 0:
                current_list.append(1)
            elif len(str(item)) % 2 == 0:
                current_list.append(int(str(item)[0:len(str(item))//2]))
                current_list.append(int(str(item)[len(str(item))//2:]))
            else:
                current_list.append(item*2024)
        transformed_list[i+1] = current_list

    return len(transformed_list[number_blinks])


# invoking function with input files
with open('inputs/day_11.txt') as f:
    input = f.read()
    list_input_str = input.split()
    list_input = [int(x) for x in list_input_str]

print(stone_splitter(list_input, 75))

