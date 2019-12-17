FIZZ_CONSTANT = 3
BUZZ_CONSTANT = 5


def fizz_buzz(number):
    """
    Returns fizzbuzz if number is a multiple of 5 and 3,
    returns fizz if number is a multiple of 5,
    returns buzz if number is a multiple of 3,
    returns the number of it is none of the above.

    """
    if (number % FIZZ_CONSTANT == 0) & (number % BUZZ_CONSTANT == 0):
        return "FizzBuzz"
    elif number % FIZZ_CONSTANT == 0:
        return "Fizz"
    elif number % BUZZ_CONSTANT == 0:
        return "Buzz"
    else:
        return number


def string_fizz_buzz(maximum):
    """
    Iterates through the range 0 to maximum calls the "fizz_buzz" function adds to string.
    prints out the string.
    """
    string = []
    for integer in range(0, (maximum+1)):
        string.append(str(fizz_buzz(integer)))

    print(", ".join(string))


string_fizz_buzz(40)
