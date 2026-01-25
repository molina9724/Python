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

# ============================================================================
# FUNCTIONS REINFORCEMENT EXERCISES (FR1-FR15)
# ============================================================================
# Focus: Functions chapter concepts where you needed help
# - Using map() and filter() correctly
# - Passing functions as arguments
# - Returning functions
# - Storing functions in dictionaries
# - Lambda functions (bonus - related to map/filter)
# - Reading instructions carefully
# ============================================================================

# ----------------------------------------------------------------------
# Exercise FR1: Basic map() Pattern
# 1. Create a function called add_ten that takes a number and returns number + 10
# 2. Create a list: nums = [5, 15, 25, 35]
# 3. Use map() to apply add_ten to all numbers
# 4. Convert to list and print
#
# Expected: [15, 25, 35, 45]

# Write your code for Exercise FR1 below:

# def add_ten(number):
#     return number+10

# nums = [5, 15, 25, 35]
# plus_ten = list(map(add_ten, nums))
# print(plus_ten)

# ----------------------------------------------------------------------
# Exercise FR2: Basic filter() Pattern
# 1. Create a function called is_positive that takes a number and returns True if > 0
# 2. Create a list: nums = [-5, 3, -2, 8, -1, 10]
# 3. Use filter() to get only positive numbers
# 4. Convert to list and print
#
# Expected: [3, 8, 10]

# Write your code for Exercise FR2 below:

# def is_positive(number):
#     return True if number > 0 else False


# nums = [-5, 3, -2, 8, -1, 10]
# only_positive = list(filter(is_positive, nums))
# print(only_positive)

# ----------------------------------------------------------------------
# Exercise FR3: map() with Strings
# 1. Create a function called get_length that takes a string and returns its length
# 2. Create a list: words = ["hi", "hello", "hey", "goodbye"]
# 3. Use map() to get the length of each word
# 4. Convert to list and print
#
# Expected: [2, 5, 3, 7]

# Write your code for Exercise FR3 below:

# def get_length(string):
#     return len(string)


# words = ["hi", "hello", "hey", "goodbye"]
# length_words = list(map(len, words))
# print(length_words)

# ----------------------------------------------------------------------
# Exercise FR4: filter() with Strings
# 1. Create a function called starts_with_h that takes a string
#    and returns True if it starts with 'h'
# 2. Create a list: words = ["hello", "world", "hi", "python", "hey"]
# 3. Use filter() to get only words starting with 'h'
# 4. Convert to list and print
#
# Expected: ['hello', 'hi', 'hey']

# Write your code for Exercise FR4 below:

# def starts_with_h(string):
#     return True if string[0] == "h" else False


# words = ["hello", "world", "hi", "python", "hey"]
# only_h = list(filter(starts_with_h, words))
# print(only_h)

# ----------------------------------------------------------------------
# Exercise FR5: Passing a Function as Argument
# 1. Create a function called square that takes x and returns x ** 2
# 2. Create a function called cube that takes x and returns x ** 3
# 3. Create a function called apply_operation that takes:
#    - operation (a function)
#    - number (a number)
#    It should call operation on number and return the result
# 4. Test: print(apply_operation(square, 5))
# 5. Test: print(apply_operation(cube, 3))
#
# Expected:
# 25
# 27

# Write your code for Exercise FR5 below:

# def square(number):
#     return number**2


# def cube(number):
#     return number**3

# def apply_operation(operation, number):
#     return operation(number)

# print(apply_operation(square, 5))
# print(apply_operation(cube, 3))

# ----------------------------------------------------------------------
# Exercise FR6: Returning a Function
# 1. Create a function called make_multiplier that takes a number n
# 2. Inside it, create a function called multiplier that takes x and returns x * n
# 3. Return the multiplier function
# 4. Call: times_five = make_multiplier(5)
# 5. Call: print(times_five(10))
# 6. Call: times_three = make_multiplier(3)
# 7. Call: print(times_three(10))
#
# Expected:
# 50
# 30

# Write your code for Exercise FR6 below:

# def make_multiplier(n):
#     def multiplier(x):
#         return x*n
#     return multiplier


# times_five = make_multiplier(5)
# print(times_five(10))

# times_three = make_multiplier(3)
# print(times_three(10))

# ----------------------------------------------------------------------
# Exercise FR7: Function with Multiple Default Parameters
# 1. Create a function called create_user that takes:
#    - name (required)
#    - age (default: 18)
#    - country (default: "USA")
# 2. It should return a string: "name, age, from country"
# 3. Test with: create_user("Alice")
# 4. Test with: create_user("Bob", 25)
# 5. Test with: create_user("Charlie", 30, "Canada")
# 6. Print all three results
#
# Expected:
# Alice, 18, from USA
# Bob, 25, from USA
# Charlie, 30, from Canada

# Write your code for Exercise FR7 below:

# def create_user(name, age=18, country="USA"):
#     return (f"{name}, {age}, from {country}")


# print(create_user("Alice"))
# print(create_user("Bob", 25))
# print(create_user("Charlie", 30, "Canada"))

# ----------------------------------------------------------------------
# Exercise FR8: Combining map() and filter()
# 1. Create a function called is_even that returns True if number is even
# 2. Create a function called square that returns number squared
# 3. Create a list: numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# 4. First, use filter() to get only even numbers
# 5. Then, use map() to square those even numbers
# 6. Convert to list and print
#
# Expected: [4, 16, 36, 64]
# (2²=4, 4²=16, 6²=36, 8²=64)

# Write your code for Exercise FR8 below:

# def is_even(number):
#     return number % 2 == 0


# def square(number):
#     return number**2


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = filter(is_even, numbers)
# square_numbers = map(square, even_numbers)
# final_list = list(square_numbers)
# print(final_list)

# ----------------------------------------------------------------------
# Exercise FR9: Function that Returns Multiple Functions
# 1. Create a function called get_math_operations that takes no parameters
# 2. Inside, define three functions:
#    - add(a, b) returns a + b
#    - subtract(a, b) returns a - b
#    - multiply(a, b) returns a * b
# 3. Return all three functions as a tuple
# 4. Call: add_func, sub_func, mul_func = get_math_operations()
# 5. Test each function and print results
#
# Expected:
# 15  (from add_func(10, 5))
# 5   (from sub_func(10, 5))
# 50  (from mul_func(10, 5))

# Write your code for Exercise FR9 below:

# def get_math_operations():
#     def add(a, b):
#         return a+b

#     def subtract(a, b):
#         return a-b

#     def multiply(a, b):
#         return a*b
#     return add, subtract, multiply


# add_func, sub_func, mul_func = get_math_operations()
# print(add_func(5, 5))
# print(sub_func(5, 5))
# print(mul_func(5, 5))

# ----------------------------------------------------------------------
# Exercise FR10: Using Lambda with map()
# 1. Create a list: numbers = [1, 2, 3, 4, 5]
# 2. Use map() with a lambda function to add 5 to each number
#    Syntax: lambda x: x + 5
# 3. Convert to list and print
#
# Expected: [6, 7, 8, 9, 10]
#
# Lambda is an anonymous function - you don't need to define it separately!

# Write your code for Exercise FR10 below:

# numbers = [1, 2, 3, 4, 5]
# add_five = map(lambda x: x+5, numbers)
# my_list = list(add_five)
# print(my_list)

# ----------------------------------------------------------------------
# Exercise FR11: Using Lambda with filter()
# 1. Create a list: numbers = [10, 15, 20, 25, 30, 35, 40]
# 2. Use filter() with a lambda function to get numbers > 25
# 3. Convert to list and print
#
# Expected: [30, 35, 40]

# Write your code for Exercise FR11 below:

# numbers = [10, 15, 20, 25, 30, 35, 40]
# my_list = list(filter(lambda x: x > 25, numbers))
# print(my_list)

# ----------------------------------------------------------------------
# Exercise FR12: Function that Modifies Behavior Based on Parameter
# 1. Create a function called create_greeting that takes a style parameter
#    - If style is "formal", return a function that says "Good day, {name}"
#    - If style is "casual", return a function that says "Hey {name}!"
# 2. Test: formal_greet = create_greeting("formal")
# 3. Test: casual_greet = create_greeting("casual")
# 4. Print: formal_greet("Alice")
# 5. Print: casual_greet("Bob")
#
# Expected:
# Good day, Alice
# Hey Bob!

# Write your code for Exercise FR12 below:

# def create_greeting(style):
#     if style == "formal":
#         return lambda name: f"Good day, {name}"
#     else:
#         return lambda name: f"Hey {name}!"


# formal_greet = create_greeting("formal")
# casual_greet = create_greeting("casual")

# print(formal_greet("Alice"))
# print(casual_greet("Bob"))

# ----------------------------------------------------------------------
# Exercise FR13: Using all() with a Custom Function
# 1. Create a function called is_passing that takes a score and returns True if >= 60
# 2. Create a list: scores = [75, 82, 90, 68]
# 3. Use all() with a generator expression to check if all scores are passing
#    Hint: all(is_passing(score) for score in scores)
# 4. Print the result
# 5. Try with: scores2 = [75, 55, 90, 68]
# 6. Print that result
#
# Expected:
# True
# False

# Write your code for Exercise FR13 below:

# def is_passing(score):
#     return score >= 60


# scores = [75, 82, 90, 68]
# result = all(is_passing(score) for score in scores)
# print(result)

# scores2 = [75, 55, 90, 68]
# result2 = all(is_passing(score) for score in scores2)
# print(result2)

# ----------------------------------------------------------------------
# Exercise FR14: Using any() with a Custom Function
# 1. Create a function called is_excellent that takes a score and returns True if >= 90
# 2. Create a list: scores = [75, 82, 85, 68]
# 3. Use any() to check if any score is excellent
# 4. Print the result
# 5. Try with: scores2 = [75, 92, 85, 68]
# 6. Print that result
#
# Expected:
# False
# True

# Write your code for Exercise FR14 below:

# def is_excellent(score):
#     return score >= 90


# scores = [75, 82, 85, 68]
# results = any(is_excellent(score) for score in scores)
# print(results)

# scores2 = [75, 92, 85, 68]
# results2 = any(is_excellent(score) for score in scores2)
# print(results2)

# ----------------------------------------------------------------------
# Exercise FR15: Comprehensive Function Challenge
# 1. Create a function called process_numbers that takes:
#    - numbers (a list)
#    - operation (a function)
#    - filter_func (a function, default: None)
# 2. If filter_func is provided, first filter the numbers
# 3. Then apply operation to the (filtered) numbers using map()
# 4. Return the result as a list
# 5. Test with:
#    - process_numbers([1,2,3,4,5], lambda x: x*2)
#    - process_numbers([1,2,3,4,5], lambda x: x*2, lambda x: x > 2)
# 6. Print both results
#
# Expected:
# [2, 4, 6, 8, 10]  (all doubled)
# [6, 8, 10]  (only >2, then doubled: 3*2=6, 4*2=8, 5*2=10)

# Write your code for Exercise FR15 below:

# def process_numbers(numbers, operation, filter_func=None):
#     if filter_func is not None:
#         numbers = filter(filter_func, numbers)
#     return list(map(operation, numbers))


# number1 = process_numbers([1, 2, 3, 4, 5], lambda x: x*2)
# print(number1)

# number2 = process_numbers([1, 2, 3, 4, 5], lambda x: x*2, lambda x: x > 2)
# print(number2)

# ----------------------------------------------------------------------
# REVIEW SESSION: Generators & Lambdas
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Review 1: Generator Expressions with any()
# 1. Create a list of names: ["Alice", "Bob", "Charlie", "Dave"]
# 2. Define a helper function `starts_with_z(name)` that returns True if name starts with "Z"
# 3. Use any() with a generator expression to check if ANY name starts with "Z"
#    (Do NOT use square brackets [])
# 4. Print the result (Should be False)
# 5. Add "Zack" to the list and run the check again (Should be True)

# Write your code for Review 1 below:


# ----------------------------------------------------------------------
# Review 2: Generator Expressions with all()
# 1. Create a list of temperatures: [98.6, 99.5, 102.0, 98.2]
# 2. Use all() with a lambda inside the generator to check if ALL temps are < 100
#    (Syntax: all(lambda_logic(t) for t in temps) ... wait, you don't need a separate function!)
#    (Try writing the condition directly: t < 100 for t in temps)
# 3. Print the result (Should be False)

# Write your code for Review 2 below:


# ----------------------------------------------------------------------
# Review 3: The "Greedy" Lambda Fix
# 1. Create a function `get_multiplier(kind)`
# 2. If kind is "double", return a lambda that multiplies by 2
# 3. If kind is "triple", return a lambda that multiplies by 3
# 4. IMPORTANT: Do not try to put the if/else inside one lambda line.
#    Use a standard if/else block to return the correct lambda.
# 5. Test:
#    doubler = get_multiplier("double")
#    print(doubler(10))  -> Should be 20
#    tripler = get_multiplier("triple")
#    print(tripler(10))  -> Should be 30

# Write your code for Review 3 below:
