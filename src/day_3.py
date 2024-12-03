import re


def sum_valid_multiplications(input_string):
    total = 0
    extracted_values = re.findall(r'(?<=mul\()[\d,]+(?=\))', input_string)
    if extracted_values:
        string_list = [x.split(',') for x in extracted_values]
        int_list = [[int(x) for x in list] for list in string_list]
        for list in int_list:
            if len(list) == 2:
                total += list[0] * list[1]
    return total

# invoking function with input file
with open('inputs/day_3.txt')as f:
    input_data = f.read()

print(sum_valid_multiplications(input_data))