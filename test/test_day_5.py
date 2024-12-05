from src.day_5 import correctly_ordered

with open('inputs/day_5_testing.txt') as f:
    first_section_list_str = [line.rstrip().split('|') for line in f]
    first_section_list = [[int(item) for item in list] for list in first_section_list_str]

def test_returns_correct_count_from_basic_true_example():
    second_section_list = [[75, 29, 13]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 29

    second_section_list = [[75,47,61,53,29]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 61

def test_returns_correct_count_from_basic_false_example():
    second_section_list = [[61, 13, 29]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 0

    second_section_list = [[75,97,47,61,53]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 0

    second_section_list = [[97,13,75,29,47]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 0

def test_returns_correct_count_from_multi_line_input():
    second_section_list = [[75, 29, 13],[75,47,61,53,29]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 90

    second_section_list = [[61, 13, 29],[75, 29, 13],[75,47,61,53,29]]
    output = correctly_ordered(first_section_list, second_section_list)
    assert output == 90