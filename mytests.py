import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(main.fizzbuzz(1), 1)

    def test_multiple_of_three(self):
        self.assertEqual(main.fizzbuzz(3), "fizz")

    def test_multiple_of_five(self):
        self.assertEqual(main.fizzbuzz(5), "buzz")

    def test_multiple_of_three_and_five(self):
        self.assertEqual(main.fizzbuzz(15), "fizzbuzz")


if __name__ == '__main__':
    unittest.main()
