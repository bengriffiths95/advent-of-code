from itertools import product


def check_equations(input_list):

    numbers_string = [str(x) for x in input_list[1:]]
    equation_string = '+'.join(numbers_string)
    equation_list = list('+'.join(numbers_string))
    
    if eval(equation_string) == input_list[0]:
        return input_list[0]
    else:
        for _ in range(0,(len(numbers_string) * 2)):
            for index, i in enumerate(equation_list):
                if i == '+':
                    equation_list.pop(index)
                    equation_list.insert(index, '*')
                equation_string = ''.join(equation_list)
                if eval(equation_string) == input_list[0]:
                    return input_list[0]
            if eval(equation_string) == input_list[0]:
                return input_list[0]
    return

# each equation is a list inside a nested list
# take index 0
# loop through indexes 1 to -1, trying every combination of + and * until index 0 is equalled.
# add this value to the running total
# if no matches move on to the next list