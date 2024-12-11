from src.day_11 import stone_splitter


def test_0_stones_become_1():
    input = [0, 0, 0]
    output = stone_splitter(input, 1)
    assert output == 3

def test_even_digit_stones_are_split():
    input = [10, 0, 0]
    output = stone_splitter(input, 1)
    assert output == 4

def test_multiple_cases_with_single_blink():
    input = [0, 1, 10, 99, 999]
    output = stone_splitter(input, 1)
    assert output == 7

def test_multiple_cases_with_multiple_blinks():
    input = [125, 17]
    output = stone_splitter(input, 5)
    assert output == 13

