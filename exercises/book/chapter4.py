def add(number1, number2):
    total = number1
    for i in range(number2):
        total = plus_one(number2)
    return total


def plus_one(number):
    return number + 1


print(add(8, 9))
