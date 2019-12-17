import unittest
import main


class TestFizzBuzz(unittest.TestCase):
    def test_number(self):
        test_cases = [
            {
                "name": "Simple number test 1",
                "input": 1,
                "expected": "1"
            },
            {
                "name": "Simple number test 2",
                "input": 2,
                "expected": "2"
            },
            {
                "name": "Simple number test 3",
                "input": 997,
                "expected": "997"
            },
            {
                "name": "Test imput of none",
                "input": None,
                "expected": None
            },
            {
                "name": "test input of string",
                "input": "word",
                "expected": None
            }
        ]
        for test_case in test_cases:
            assert test_case["expected"] == main.fizz_buzz(test_case["input"]), test_case["name"]

    def test_multiple_of_3(self):
        test_cases = [
            {
                "name": "test multiple of three 1",
                "input": 3,
                "expected": "Fizz"
            },
            {
                "name": "test multiple of three 2",
                "input": 6,
                "expected": "Fizz"
            },
            {
                "name": "test multiple of three 3",
                "input": 999,
                "expected": "Fizz"
            },
            {
                "name": "test multiple of three with string",
                "input": "999",
                "expected": None
            }
        ]
        for test_case in test_cases:
            assert test_case["expected"] == main.fizz_buzz(test_case["input"]), test_case["name"]

    def test_multiple_of_five(self):
        self.assertEqual(main.fizz_buzz(5), "Buzz")

    def test_multiple_of_three_and_five(self):
        self.assertEqual(main.fizz_buzz(15), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
