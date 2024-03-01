import unittest
from lab

def multiply_string(string, n):
    return string * n

class TestStringMultiplier(unittest.TestCase):
    
    def test_multiply_string(self):
        self.assertEqual(multiply_string("Hello World ", 5), "Hello World Hello World Hello World Hello World Hello World ")
        self.assertEqual(multiply_string("Test ", 3), "Test Test Test ")
        self.assertEqual(multiply_string("123", 0), "")
        self.assertEqual(multiply_string("", 10), "")

if __name__ == '__main__':
    unittest.main()
