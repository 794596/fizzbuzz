FIZZ_CONSTANT = 3
BUZZ_CONSTANT = 5


def fizz_buzz(number):
    if (number % FIZZ_CONSTANT == 0) & (number % BUZZ_CONSTANT == 0):
        return "FizzBuzz"
    elif number % FIZZ_CONSTANT == 0:
        return "Fizz"
    elif number % BUZZ_CONSTANT == 0:
        return "Buzz"
    else:
        return number


def string_fizz_buzz(maximum):
    string = []
    for integer in range(0, (maximum+1)):
        string.append(str(fizz_buzz(integer)))

    print(", ".join(string))


string_fizz_buzz(40)
