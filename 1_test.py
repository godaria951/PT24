import unittest

def multiply_string(s, n):
    return s * n

class TestMultiplyString(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual(multiply_string("Hello World ", 5), "Hello World Hello World Hello World Hello World Hello World ")

if __name__ == "__main__":
    unittest.main()
