from src.day_1 import find_total_distance


def test_returns_correct_difference_when_one_number_provided():
    list1 = [2]
    list2 = [5]
    output = find_total_distance(list1, list2)
    assert output == 3

def test_returns_correct_difference_when_two_numbers_provided():
    list1 = [2, 4]
    list2 = [5, 6]
    output = find_total_distance(list1, list2)
    assert output == 5

def test_returns_correct_difference_when_larger_number_list_position_changes():
    list1 = [2, 6]
    list2 = [5, 4]
    output = find_total_distance(list1, list2)
    assert output == 3

def test_returns_correct_difference_when_longer_lists_provided():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    output = find_total_distance(list1, list2)
    assert output == 11

# invoking function with input list
with open('inputs/day_1.txt') as f:
    lines = [line.rstrip() for line in f]

input_list_1 = []
input_list_2 = []

for line in lines:
    line_split = line.split('   ')
    input_list_1.append(int(line_split[0]))
    input_list_2.append(int(line_split[1]))

print(find_total_distance(input_list_1, input_list_2))