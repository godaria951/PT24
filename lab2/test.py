from my_module import divide

def test_divide_positive_numbers():
    result = divide(10, 2)
    assert result == 5.0

def test_divide_by_zero():
    result = divide(10, 0)
    assert result == "Ділення на нуль неможливе"
