from src.day_2 import check_safe_report_count


def test_marked_safe_if_all_increasing_numbers():
    list = [[1, 2, 3, 4, 5]]
    output = check_safe_report_count(list)
    assert output == 1

def test_marked_safe_if_all_decreasing_numbers():
    list = [[5, 4, 3, 2, 1]]
    output = check_safe_report_count(list)
    assert output == 1

def test_marked_unsafe_if_any_two_consecutive_numbers_same():
    list = [[5, 4, 4, 2, 1]]
    output = check_safe_report_count(list)
    assert output == 0

def test_marked_unsafe_if_any_two_consecutive_numbers_greater_than_3_difference():
    list = [[10, 8, 3, 2, 1]]
    output = check_safe_report_count(list)
    assert output == 0

def test_function_correctly_counts_multiple_lists():
    list = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1],[10, 8, 3, 2, 1]]
    output = check_safe_report_count(list)
    assert output == 2