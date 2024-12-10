from src.day_10 import trail_finder

def test_1_trailhead_example():
    input =  '''...0...
                ...1...
                ...2...
                65.3456
                7.....7
                8.....8
                9.....9'''
    input_split = input.split()
    output = trail_finder(input_split)
    assert output == 1

def test_2_trailhead_example():
    input =  '''...0...
                ...1...
                ...2...
                6543456
                7.....7
                8.....8
                9.....9'''
    input_split = input.split()
    output = trail_finder(input_split)
    assert output == 2

def test_complex_trailhead_example():
    input =  '''..90..9
                ...1.98
                ...2..7
                6543456
                765.987
                876....
                987....'''
    input_split = input.split()
    output = trail_finder(input_split)
    assert output == 4

def test_complex_trailhead_example_2():
    input =  '''89010123
                78121874
                87430965
                96549874
                45678903
                32019012
                01329801
                10456732'''
    input_split = input.split()
    output = trail_finder(input_split)
    assert output == 36
