from src.day_6 import guard_position


def test_function_correctly_tracks_route_with_no_obstacles():
    input =    [['.','.','.','.'],
                ['.','.','.','.'],
                ['.','.','.','.'],
                ['.','^','.','.']]
    output = guard_position(input)
    assert output == 4

def test_function_correctly_tracks_route_with_one_obstacle():
    input =    [['.','.','.','.'],
                ['.','#','.','.'],
                ['.','.','.','.'],
                ['.','^','.','.']]
    output = guard_position(input)
    assert output == 4

def test_function_correctly_tracks_route_with_two_obstacles():
    input =    [['#','.','.','.'],
                ['.','.','.','#'],
                ['.','.','.','.'],
                ['^','.','.','.']]
    output = guard_position(input)
    assert output == 7

def test_function_correctly_tracks_route_with_three_obstacles():
    input =    [['#','.','.','.'],
                ['.','.','.','#'],
                ['.','.','.','.'],
                ['^','.','#','.']]
    output = guard_position(input)
    assert output == 7

def test_real_example():
    input =    [['.','.','.','.','#','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','#'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','#','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','#','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','#','.','.','^','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','#','.'],
                ['#','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','#','.','.','.']]
    output = guard_position(input)
    assert output == 41

def test_guard_can_correctly_exit_via_left_hand_side():
    input =    [['.','.','.','.','.'],
                ['.','.','#','.','.'],
                ['.','.','^','.','#'],
                ['.','.','.','#','.'],
                ['.','.','.','.','.']]
    output = guard_position(input)
    assert output == 4
