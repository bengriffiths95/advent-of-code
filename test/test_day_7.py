from src.day_7 import check_equations

def test_calculates_correctly_when_valid_addition_equation_given():
    input = [29, 10, 19]
    output = check_equations(input)
    assert output == 29

def test_calculates_correctly_when_longer_valid_addition_equation_given():
    input = [100, 50, 30, 10, 10]
    output = check_equations(input)
    assert output == 100

def test_calculates_correctly_when_valid_multiplication_equation_given():
    input = [190, 10, 19]
    output = check_equations(input)
    assert output == 190

def test_calculates_correctly_with_mix_of_add_and_multiply():
    input = [125, 10, 10, 25]
    output = check_equations(input)
    assert output == 125

def test_calculates_correctly_with_complex_mixture():
    input = [292, 11, 6, 16, 20]
    output = check_equations(input)
    assert output == 292

