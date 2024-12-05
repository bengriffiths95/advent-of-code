from src.day_4 import word_count
import pytest

@pytest.mark.skip
class TestHorizontalMatching:
    def test_function_correctly_counts_forward_horizontal_matches(self):
        list = [['.','.','X','.','.','.'],
                ['.','S','A','A','X','.'],
                ['.','.','.','.','A','.'],
                ['X','M','A','S','.','S'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 1

    def test_function_correctly_counts_backward_horizontal_matches(self):
        list = [['.','.','X','.','.','.'],
                ['.','S','A','M','X','.'],
                ['.','A','.','.','.','.'],
                ['X','A','A','S','.','S'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 1

    def test_function_correctly_counts_two_matches_in_same_row(self):
        list = [['X','M','A','S','.','S'],
                ['.','S','A','A','X','.'],
                ['.','.','.','.','A','.'],
                ['X','M','A','S','.','S'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 2

@pytest.mark.skip
class TestVerticalMatching:
    def test_function_correctly_counts_downward_vertical_matches(self):
        list = [['.','.','X','X','.','.'],
                ['.','.','A','M','X','.'],
                ['.','A','.','A','A','.'],
                ['X','A','A','S','.','.'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 1

    def test_function_correctly_counts_upward_vertical_matches(self):
        list = [['.','.','X','X','.','S'],
                ['.','.','A','M','X','A'],
                ['.','A','.','A','A','M'],
                ['X','A','A','S','.','X'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 2

    def test_function_correctly_counts_two_matches_in_same_column(self):
        list = [['.','.','X','X','.','S'],
                ['.','.','A','M','X','A'],
                ['.','A','.','A','A','M'],
                ['X','A','A','S','.','X'],
                ['X','A','A','S','.','S'],
                ['X','A','A','S','.','A'],
                ['X','A','A','S','.','M'],
                ['X','A','A','S','.','X'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 3

class TestDiagonalMatching:
    def xtest_function_correctly_counts_diagonal_first_direction(self):
        list = [['.','.','.','.','X','.'],
                ['.','.','.','M','.','.'],
                ['.','.','A','.','.','.'],
                ['.','S','.','.','.','.'],
                ['.','.','.','.','.','.']]
        output = word_count(list)
        assert output == 1

    def xtest_function_correctly_counts_diagonal_second_direction(self):
        list = [['.','.','X','.','.','.'],
                ['.','.','.','M','.','.'],
                ['.','.','.','.','A','.'],
                ['.','.','.','.','.','S'],
                ['.','.','.','.','.','.']]
        output = word_count(list)
        assert output == 1

    def xtest_function_correctly_counts_diagonal_backwards(self):
        list = [['.','.','.','.','.','.'],
                ['.','.','.','.','S','.'],
                ['.','.','.','A','.','.'],
                ['.','.','M','.','.','.'],
                ['.','X','.','.','.','.']]
        output = word_count(list)
        assert output == 1

    def test_function_correctly_counts_multiple_diagonal(self):
        list = [['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],          
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','X'], 
                ['.','.','.','.','.','.','.','.','M','.'],
                ['.','.','.','.','.','.','.','A','.','.'],
                ['.','.','.','.','.','.','S','.','.','.'],
                ['.','.','.','.','.','A','.','.','.','.'],
                ['.','.','.','.','M','.','.','.','.','.'],
                ['.','.','.','X','.','.','.','.','.','.']]
        output = word_count(list)
        assert output == 2

class TestFullWordsearch:
    def test_function_correctly_counts_matches_from_test_data(self):
        with open('inputs/day_4_testing.txt') as f:
            list = [[line.rstrip()] for line in f]

        print(list)
        output = word_count(list)
        assert output == 18
