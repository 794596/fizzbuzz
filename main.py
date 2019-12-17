

FIZZ = 3
BUZZ = 5


def fizzbuzz(integer):
    if (integer % FIZZ == 0) & (integer % BUZZ == 0):
        return "fizzbuzz"
    elif integer % FIZZ == 0:
        return "fizz"
    elif integer % BUZZ == 0:
        return "buzz"
    else:
        return integer


string = []
for i in range(0, 31):
    if i <= 30:
        string.append(str(fizzbuzz(i)))

print(", ".join(string))


