def add(number1, number2):
    total = number1
    for i in range(number2):
        total = plus_one(total)
    return total


def plus_one(number):
    return number+1


def multiply(number1, number2):
    total = 0
    for i in range(number2):
        total = add(total, number1)
    return total


def tick_tock(seconds):
    for element in range(seconds):
        if element % 2 == 0:
            print("Tick...")
        else:
            print("Tock...")


def collatz(number):
    if number % 2 == 0:
        result = number//2
    else:
        result = 3 * number + 1
    print(result)
    return result


try:
    n = int(2)
    while n != 1:
        n = collatz(n)
except (TypeError, ValueError):
    print("It must be an integer")
