import time


start_time = time.time()

def correctly_ordered(first_section_list, second_section_list):

    return_total = 0
    for i in range(0,len(second_section_list)):
        rules_list = []
        for num in second_section_list[i]:
            temp_list = []
            for list in first_section_list:
                if list[0] == num:
                    temp_list.append(list[1])
            rules_list.append(temp_list)
        
        for num in second_section_list[i]:
            rules_list_flat = [x for sublist in rules_list for x in sublist]
            if num in rules_list_flat:
                to_add = 0
                break
            else:
                middle = int((len(second_section_list[i])-1)/2)
                to_add = second_section_list[i][middle]
            rules_list.pop(0)
        return_total += to_add

    return return_total

# invoking function with input files
with open('inputs/day_5_section_1.txt') as f:
    first_section_list_str = [line.rstrip().split('|') for line in f]
    first_section_list = [[int(item) for item in list] for list in first_section_list_str]

with open('inputs/day_5_section_2.txt') as f:
    second_section_list_str = [line.rstrip().split(',') for line in f]
    second_section_list = [[int(item) for item in list] for list in second_section_list_str]

print(correctly_ordered(first_section_list, second_section_list))
print("Process finished in %s seconds" % (time.time() - start_time))
