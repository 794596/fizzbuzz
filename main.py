"""
print a string with the numbers between 1 and the maximum separated by ", ".
If a number is a multiple of 3, it is replaced by fizz.
If a number is a multiple of 5, it is replaced by buzz.
If a number is a multiple of both 3 and 5, it is replaced by FizzBuzz
Otherwise the number is returned.
"""
FIZZ_CONSTANT = 3
BUZZ_CONSTANT = 5


def fizz_buzz(number):
    """
    returns FizzBuzz if number is a multiple of 5 and 3,
    returns Fizz if number is a multiple of 5,
    returns Buzz if number is a multiple of 3,
    returns the number of it is none of the above.

    parameters:
        number (int): number to be determined what is returned

    return:
        str: value related to the number in fizzbuzz

    """
    try:
        return "Fizz"*(number % 3 == 0)+"Buzz"*(number % 5 == 0) or str(number)
    except TypeError:
        return None


def string_fizz_buzz(maximum):
    """
    iterates through the range 0 to maximum calls the "fizz_buzz" function adds to string.
    Prints out the string.

    Parameter:
        maximum (int): number for loop iterates to.

    Return:
        none

    """
    string = []
    for integer in range(0, (maximum+1)):
        string.append(str(fizz_buzz(integer)))

    print(", ".join(string))


string_fizz_buzz(40)
