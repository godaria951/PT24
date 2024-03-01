def repeat_string(string, n):
    return string * n

def test_repeat_string():
    n = 5
    string = "Hello World "
    expected_result = "Hello World Hello World Hello World Hello World Hello World "
    assert repeat_string(string, n) == expected_result
pytest lab.py

