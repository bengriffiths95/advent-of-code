from src.day_9 import disk_fragmenter

def test_basic_example():
    input = '12345'
    output = disk_fragmenter(input)
    assert output == 60

def xtest_more_complex_example():
    input = '2333133121414131402'
    output = disk_fragmenter(input)
    assert output == 1928

def xtest_more_complex_example_2():
    input = '1010101010101010101010'
    output = disk_fragmenter(input)
    assert output == 385
