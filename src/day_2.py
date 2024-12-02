def check_safe_report_count(input_list):
    safe_count = 0

    for list in input_list:
        difference_list = [b - a for a, b in zip(list[:-1], list[1:])]

        if (
        (all(x<0 for x in difference_list) or all(x>0 for x in difference_list))
        and all(abs(x)<=3 for x in difference_list)):
            safe_count += 1
        else:
            safe_count += 0

    return safe_count

# invoking function with input file
with open('inputs/day_2.txt') as f:
    lines = [line.rstrip() for line in f]

list_string = [line.split() for line in lines]

list_int = []
for line in list_string:
    list_int.append([int(x) for x in line])

check_safe_report_count(list_int)