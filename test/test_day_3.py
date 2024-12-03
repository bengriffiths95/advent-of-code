from src.day_3 import sum_valid_multiplications


def test_sums_correctly_when_given_valid_basic_string():
    test_string = 'mul(2,4)'
    assert sum_valid_multiplications(test_string) == 8

    test_string = 'mul(10,10)'
    assert sum_valid_multiplications(test_string) == 100

    test_string = 'testmul(10,10)'
    assert sum_valid_multiplications(test_string) == 100

def test_ignores_numbers_when_not_preceded_by_mul():
    test_string = '(2,4)'
    assert sum_valid_multiplications(test_string) == 0

def test_ignores_numbers_if_non_round_brackets_used():
    test_string = 'mul[2,4]'
    assert sum_valid_multiplications(test_string) == 0

    test_string = 'mul(2,4]'
    assert sum_valid_multiplications(test_string) == 0

    test_string = 'mul(2,4}'
    assert sum_valid_multiplications(test_string) == 0

def test_ignores_numbers_if_spaces_present_inside_brackets():
    test_string = 'mul( 2 , 4 )'
    assert sum_valid_multiplications(test_string) == 0
    
    test_string = 'mul(2 , 4 )'
    assert sum_valid_multiplications(test_string) == 0

def test_ignores_numbers_if_other_characters_used():
    test_string = 'mul(2*4)'
    assert sum_valid_multiplications(test_string) == 0

    test_string = 'mul(2,4!)'
    assert sum_valid_multiplications(test_string) == 0

def test_sums_correctly_with_multiple_valid_number_pairs_in_string():
    test_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)'
    assert sum_valid_multiplications(test_string) == 33

def test_ignores_numbers_if_only_1_number_between_parentheses():
    test_string = 'mul(4)'
    assert sum_valid_multiplications(test_string) == 0
