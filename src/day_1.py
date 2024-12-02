def find_total_distance(list1, list2):
    total_distance = 0
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    for index, item in enumerate(sorted_list1):
        total_distance += abs(item - sorted_list2[index])
        
    return total_distance

# invoking function with input list
with open('inputs/day_1.txt') as f:
    lines = [line.rstrip() for line in f]

input_list_1 = []
input_list_2 = []

for line in lines:
    line_split = line.split('   ')
    input_list_1.append(int(line_split[0]))
    input_list_2.append(int(line_split[1]))

find_total_distance(input_list_1, input_list_2)