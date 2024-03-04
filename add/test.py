from my module import pytest

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ділення на нуль неможливе"

def test_divide_non_zero():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == "Ділення на нуль неможливе"
