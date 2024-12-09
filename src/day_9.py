from string import punctuation


def disk_fragmenter(number_input):

    # unmap the blocks
    disk_unmapped_list = []
    last_id = 0
    for index, num in enumerate(number_input):
        if index % 2 == 0:
            for _ in range(0, int(num)):
                disk_unmapped_list.append(last_id)
            last_id += 1
        if index % 2 != 0:
            for _ in range(0, int(num)):
                disk_unmapped_list.append('.')
    
    print('step 1 complete')
    print(disk_unmapped_list)

    # move the blocks
    last_value_index = len(disk_unmapped_list) -1
    for index, item in enumerate(disk_unmapped_list):
        flag = True
        while flag:
            if isinstance(disk_unmapped_list[last_value_index], str):
                last_value_index -= 1
            else:
                flag = False
        if item == '.':
            disk_unmapped_list[index] = disk_unmapped_list[last_value_index]
            disk_unmapped_list[last_value_index] = '.'
            last_value_index -= 1
        
        disk_unmapped_str = "".join(str(x) for x in disk_unmapped_list)
        disk_unmapped_str_stripped =  disk_unmapped_str.rstrip(punctuation)
        if '.' not in disk_unmapped_str_stripped:
            break

    print('step 2 complete')

    # calculate the total
    return_total = 0
    for index, item in enumerate(disk_unmapped_list):
        if type(item) == int:
            return_total += (item * index)
    
    return return_total

# invoking function with input files
with open('inputs/day_9.txt') as f:
    input = f.read()

print(disk_fragmenter(input))