import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(main.fizz_buzz(1), 1)

    def test_multiple_of_three(self):
        self.assertEqual(main.fizz_buzz(3), "Fizz")

    def test_multiple_of_five(self):
        self.assertEqual(main.fizz_buzz(5), "Buzz")

    def test_multiple_of_three_and_five(self):
        self.assertEqual(main.fizz_buzz(15), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
