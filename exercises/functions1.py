# Exercise F1: Create Your First Function
# 1. Create a function called greet that takes one parameter: name
# 2. The function should print "Hello, {name}!"
# 3. Call the function with your name
# 4. Call it again with a different name
#
# Expected output:
# Hello, Alice!
# Hello, Bob!

# Write your code for Exercise F1 below:

# def greet(name):
#     print(f"Hello {name}!")

# greet("Carl")
# greet("Johnson")

# ----------------------------------------------------------------------
# Exercise F2: Function with Return Value
# 1. Create a function called double that takes one parameter: number
# 2. The function should RETURN the number multiplied by 2
# 3. Call the function with 5 and print the result
# 4. Call it with 10 and store the result in a variable, then print it
#
# Expected output:
# 10
# 20

# Write your code for Exercise F2 below:

# def double(number):
#     return number*2

# print(double(5))
# x = double(10)
# print(x)

# ----------------------------------------------------------------------
# Exercise F3: Function with Multiple Parameters
# 1. Create a function called add that takes two parameters: a and b
# 2. The function should return the sum of a and b
# 3. Call the function with different numbers and print results
# 4. Try: add(3, 5), add(10, 20), add(7, 8)
#
# Expected output:
# 8
# 30
# 15

# Write your code for Exercise F3 below:

# def add(a,b):
#     return a+b

# print(add(3, 5))
# print(add(10, 20))
# print(add(7, 8))

# ----------------------------------------------------------------------
# Exercise F4: Assign Function to Variable
# 1. Create a function called square that returns x ** 2
# 2. Assign this function to a variable called my_func
# 3. Call my_func(5) and print the result
# 4. Print the type of my_func
#
# Expected output:
# 25
# <class 'function'>

# Write your code for Exercise F4 below:

# def square(number):
#     return number**2

# my_func = square
# print(my_func(5))
# print(type(my_func))

# ----------------------------------------------------------------------
# Exercise F5: Pass Function as Argument
# 1. Create a function called cube that returns x ** 3
# 2. Create a function called apply_twice that takes two parameters:
#    - func (a function)
#    - value (a number)
# 3. apply_twice should call func on value, then call func on that result
# 4. Call apply_twice(cube, 2) and print the result
#
# Expected output:
# 512
# Explanation: cube(2) = 8, then cube(8) = 512

# Write your code for Exercise F5 below:

# def cube(number):
#     return number**3


# def apply_twice(func, value):
#     return func(func(value))


# print(apply_twice(cube, 2))

# ----------------------------------------------------------------------
# Exercise F6: Store Functions in a Dictionary
# 1. Create three functions:
#    - add(a, b) returns a + b
#    - subtract(a, b) returns a - b
#    - multiply(a, b) returns a * b
# 2. Store them in a dictionary called operations with keys: 'add', 'subtract', 'multiply'
# 3. Use the dictionary to call operations['add'](10, 5)
# 4. Print the result
#
# Expected output:
# 15

# Write your code for Exercise F6 below:

# def add(a, b):
#     return a+b


# def subtract(a, b):
#     return a-b


# def multiply(a, b):
#     return a*b


# my_dic = {"add": add, "subtract": subtract, "multiply": multiply}
# print(my_dic["add"](10, 5))
# print(my_dic["subtract"](10, 5))
# print(my_dic["multiply"](10, 5))

# ----------------------------------------------------------------------
# Exercise F7: Return a Function
# 1. Create a function called get_operation that takes one parameter: op_name
# 2. Inside, create a dictionary mapping 'double' to a function that doubles
#    and 'triple' to a function that triples
# 3. Return the function based on op_name
# 4. Call: my_op = get_operation('double'), then print my_op(5)
#
# Expected output:
# 10

# Write your code for Exercise F7 below:

# def get_operation(op_name):
#     my_dic = {"double": double, "triple": triple}
#     return my_dic[op_name]


# def double(number):
#     return number*2


# def triple(number):
#     return number*3


# my_operation = get_operation("double")
# print(my_operation(5))

# ----------------------------------------------------------------------
# Exercise F8: Using Built-in all()
# 1. Create a list: numbers = [2, 4, 6, 8, 10]
# 2. Use all() to check if all numbers are even (use a generator expression)
# 3. Print the result
# 4. Try with numbers2 = [2, 4, 5, 8] and print that result
#
# Expected output:
# True
# False

# Write your code for Exercise F8 below:

# numbers = [2, 4, 6, 8, 10]
# numbers2 = [2, 4, 5, 8]

# print(all(num % 2 == 0 for num in numbers))
# print(all(num % 2 == 0 for num in numbers2))

# ----------------------------------------------------------------------
# Exercise F9: Using Built-in any()
# 1. Create a list: scores = [45, 67, 89, 52, 73]
# 2. Use any() to check if any score is above 80
# 3. Print the result
# 4. Use any() to check if any score is above 95
# 5. Print that result
#
# Expected output:
# True
# False

# Write your code for Exercise F9 below:

# scores = [45, 67, 89, 52, 73]
# print(any(score>80 for score in scores))
# print(any(score>95 for score in scores))

# ----------------------------------------------------------------------
# Exercise F10: Combining Functions and Dictionaries
# 1. Create a list of numbers: nums = [1, 2, 3, 4, 5]
# 2. Create a function called apply_to_all that takes:
#    - a function
#    - a list
# 3. It should return a NEW list with the function applied to each element
# 4. Test it with a square function: apply_to_all(square, nums)
# 5. Print the result
#
# Expected output:
# [1, 4, 9, 16, 25]

# Write your code for Exercise F10 below:

# nums = [1, 2, 3, 4, 5]


# def square(number):
#     return number**2


# def apply_to_all(function, list):
#     return [function(item) for item in list]


# print(apply_to_all(square, [1, 2, 3, 4, 5]))

# ----------------------------------------------------------------------
# Exercise F11: Function with Default Parameter
# 1. Create a function called greet_with_title that takes two parameters:
#    - name
#    - title (with default value "Mr.")
# 2. Return a string: "{title} {name}"
# 3. Call it with just a name: greet_with_title("Smith")
# 4. Call it with both: greet_with_title("Smith", "Dr.")
# 5. Print both results
#
# Expected output:
# Mr. Smith
# Dr. Smith

# Write your code for Exercise F11 below:

# def greet_with_title(name, title="Mr."):
#     return (f"{title} {name}")


# print(greet_with_title("Smith"))
# print(greet_with_title("Smith", "Dr."))

# ----------------------------------------------------------------------
# Exercise F12: Function that Returns Multiple Values
# 1. Create a function called get_stats that takes a list of numbers
# 2. Return three values: min, max, and average (use built-in functions)
# 3. Call it with [10, 20, 30, 40, 50]
# 4. Unpack the results into three variables and print them
#
# Expected output:
# Min: 10
# Max: 50
# Average: 30.0

# Write your code for Exercise F12 below:

# def get_stats(list):
#     return min(list), max(list), sum(list)/len(list)

# min, max, avg = get_stats([10, 20, 30, 40, 50])
# print(min)
# print(max)
# print(avg)

# ----------------------------------------------------------------------
# Exercise F13: Using map() with a Function
# 1. Create a list: prices = [10, 20, 30, 40]
# 2. Create a function called add_tax that adds 10% to a price
# 3. Use map() to apply add_tax to all prices
# 4. Convert the result to a list and print it
#
# Expected output:
# [11.0, 22.0, 33.0, 44.0]

# Write your code for Exercise F13 below:

# prices = [10, 20, 30, 40]


# def add_tax(price):
#     return price * 1.1


# result = map(add_tax, prices)
# result_list = list(result)
# print(result_list)

# ----------------------------------------------------------------------
# Exercise F14: Using filter() with a Function
# 1. Create a list: ages = [12, 18, 25, 16, 30, 14, 21]
# 2. Create a function called is_adult that returns True if age >= 18
# 3. Use filter() to get only adult ages
# 4. Convert to a list and print it
#
# Expected output:
# [18, 25, 30, 21]

# Write your code for Exercise F14 below:

# ages = [12, 18, 25, 16, 30, 14, 21]

# def is_adult(age):
#     return True if age>=18 else False

# result = filter(is_adult, ages)
# result_list = list(result)
# print(result_list)

# ----------------------------------------------------------------------
# Exercise F15: Calculator with Function Dictionary
# 1. Create a calculator dictionary with functions for: add, subtract, multiply, divide
# 2. Create a function called calculate that takes: operation, a, b
# 3. It should look up the operation in the dictionary and call it
# 4. Test all four operations and print results
#
# Expected output:
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0

# Write your code for Exercise F15 below:

# def add(a, b):
#     return a+b


# def subtract(a, b):
#     return a-b


# def multiply(a, b):
#     return a*b


# def divide(a, b):
#     return a/b


# def calculate(operation, a, b):
#     my_dic = {"add": add, "subtract": subtract,
#               "multiply": multiply, "divide": divide}
#     return my_dic[operation](a, b)


# print(calculate("add", 10, 5))
# print(calculate("subtract", 10, 5))
# print(calculate("multiply", 10, 5))
# print(calculate("divide", 10, 5))
