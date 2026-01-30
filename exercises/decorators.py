# ============================================================================
# DECORATOR EXERCISES (D1-D15)
# ============================================================================
# Focus: Understanding decorators, wrapper functions, @syntax, nesting
# ============================================================================

# ----------------------------------------------------------------------
# Exercise D1: Your First Decorator
# Create a decorator called uppercase_decorator that:
# - Takes a function as input
# - Returns a wrapper that converts the function's result to uppercase
# - The original function returns a string
#
# Test it on this function:
# def greet():
#     return "hello world"
#
# Expected after decoration:
# greet() → "HELLO WORLD"

# Write your code below:


# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         lower = result.upper()
#         return lower
#     return wrapper


# @uppercase_decorator
# def greet():
#     return "hello world"


# print(greet())

# ----------------------------------------------------------------------
# Exercise D2: Using @ Syntax
# Take your uppercase_decorator from D1
# Apply it using @decorator syntax to a function called say_name
# that returns "john doe"
#
# Expected:
# say_name() → "JOHN DOE"

# Write your code below:

# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         lower = result.upper()
#         return lower
#     return wrapper


# @uppercase_decorator
# def say_name():
#     return "jhon doe"


# print(say_name())

# ----------------------------------------------------------------------
# Exercise D3: Before and After
# Create a decorator called announce that:
# - Prints "Starting..." before the function runs
# - Runs the original function
# - Prints "Finished!" after the function runs
#
# Test it on:
# @announce
# def do_work():
#     print("Working...")
#
# Expected output:
# Starting...
# Working...
# Finished!

# Write your code below:

# def announce(func):
#     def wrapper():
#         print("Starting...")
#         func()
#         print("Finished")
#     return wrapper


# @announce
# def do_work():
#     print("Working...")


# do_work()

# ----------------------------------------------------------------------
# Exercise D4: Decorator with Function Arguments
# Create a decorator called double_result that:
# - Takes a function that accepts arguments
# - Returns double the result of that function
#
# Hint: Your wrapper needs to accept *args, **kwargs
#
# Test it on:
# @double_result
# def add(a, b):
#     return a + b
#
# Expected:
# add(3, 4) → 14  (because (3+4)*2 = 14)

# Write your code below:

# def double_result(func):
#     def wrapper(*args, **kwargs):
#         total = func(*args, **kwargs)
#         total *= 2
#         return total
#     return wrapper


# @double_result
# def add(a, b):
#     return a+b


# print(add(3, 4))

# ----------------------------------------------------------------------
# Exercise D5: Multiple Functions, One Decorator
# Create a decorator called add_stars that:
# - Adds "***" before and after the function's return value
#
# Apply it to TWO different functions:
# - greet(name) that returns f"Hello, {name}"
# - farewell(name) that returns f"Goodbye, {name}"
#
# Expected:
# greet("Alice") → "*** Hello, Alice ***"
# farewell("Bob") → "*** Goodbye, Bob ***"

# Write your code below:

# def add_stars(func):
#     def wrapper(*args):
#         split_word = func(*args).split()
#         split_word.append(" ***")
#         split_word.insert(0, "*** ")
#         joined_word = " ".join(split_word)
#         print(joined_word)
#     return wrapper


# @add_stars
# def greet_name(name, lastname):
#     return f"Hello, {name} {lastname}"


# @add_stars
# def farewell(name, lastname):
#     return f"Goodbye, {name} {lastname}"


# greet_name("Alice", "Estrada")
# farewell("Bob", "Arteaga")

# ----------------------------------------------------------------------
# Exercise D6: Stacking Decorators - Order Matters
# Create two decorators:
# - bold: wraps result in <b>result</b>
# - italic: wraps result in <i>result</i>
#
# Apply them in this order:
# @bold
# @italic
# def get_text():
#     return "Hello"
#
# What will get_text() return?
# Predict first, then test!
#
# Your prediction: ???

# Write your code below:

# def bold(func):
#     def wrapper():
#         text = func()
#         bold_text = f"<b>{text}</b>"
#         return bold_text
#     return wrapper


# def italic(func):
#     def wrapper():
#         text = func()
#         bold_text = f"<i>{text}</i>"
#         return (bold_text)
#     return wrapper


# @bold
# @italic
# def get_text():
#     return "Hello"


# print(get_text())

# ----------------------------------------------------------------------
# Exercise D7: Timing Decorator
# Create a decorator called timer that:
# - Records the time before the function runs
# - Runs the function
# - Records the time after
# - Prints how long it took
#
# Hint: import time, use time.time()
#
# Test it on:
# @timer
# def slow_function():
#     time.sleep(1)
#     return "Done"
#
# Expected output:
# Function took 1.00 seconds

# Write your code below:

# import time


# def timer(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()
#         print(end-start)
#         return result
#     return wrapper


# @timer
# def slow_function():
#     time.sleep(1)
#     return "Done"


# print(slow_function())

# ----------------------------------------------------------------------
# Exercise D8: Validation Decorator
# Create a decorator called positive_only that:
# - Checks if all arguments are positive numbers
# - If yes, runs the function
# - If no, prints "Error: All arguments must be positive!" and returns None
#
# Test it on:
# @positive_only
# def multiply(a, b):
#     return a * b
#
# Expected:
# multiply(3, 4) → 12
# multiply(-3, 4) → prints error, returns None

# Write your code below:

# def positive_only(func):
#     def wrapper(*args):
#         if all(x >= 0 for x in args):
#             return func(*args)
#         else:
#             print("Error: All arguments must be positive!")
#     return wrapper


# @positive_only
# def multiply(a, b):
#     return a*b


# print(multiply(3, 4))
# print(multiply(0, 4))
# multiply(-5, 4)
# multiply(5, -4)

# ----------------------------------------------------------------------
# Exercise D9: Call Counter Decorator
# Create a decorator called count_calls that:
# - Keeps track of how many times the decorated function is called
# - Prints the call number each time
#
# Hint: Use nonlocal to maintain state!
#
# Test it on:
# @count_calls
# def say_hi():
#     print("Hi!")
#
# Expected:
# say_hi()  # Call #1 \n Hi!
# say_hi()  # Call #2 \n Hi!
# say_hi()  # Call #3 \n Hi!

# Write your code below:


# def count_calls(func):
#     number = 0

#     def wrapper():
#         nonlocal number
#         number += 1
#         print(f"Call #{number}")
#         func()
#     return wrapper


# @count_calls
# def say_hi():
#     print("Hi!")


# say_hi()
# say_hi()
# say_hi()


# ----------------------------------------------------------------------
# Exercise D10: Repeat Decorator
# Create a decorator called repeat_twice that:
# - Runs the decorated function twice
#
# Test it on:
# @repeat_twice
# def greet(name):
#     print(f"Hello, {name}!")
#
# Expected:
# greet("Alice")
# Hello, Alice!
# Hello, Alice!

# Write your code below:

# def repeat_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper


# @repeat_twice
# def greet(name):
#     print(f"Hello, {name}!")


# greet("Alice")

# ----------------------------------------------------------------------
# Exercise D11: Decorator with Arguments - Repeat N Times
# Create a decorator FACTORY called repeat that:
# - Takes a number n as argument
# - Returns a decorator that repeats the function n times
#
# Test it on:
# @repeat(3)
# def say_hello():
#     print("Hello!")
#
# Expected:
# say_hello()
# Hello!
# Hello!
# Hello!

# Write your code below:

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator


# @repeat(3)
# def say_hello():
#     print("Hello!")

# say_hello()

# ----------------------------------------------------------------------
# Exercise D12: Decorator with Arguments - Prefix
# Create a decorator factory called prefix that:
# - Takes a string prefix as argument
# - Returns a decorator that adds that prefix to the function's result
#
# Test it on:
# @prefix("Mr. ")
# def get_name():
#     return "Smith"
#
# Expected:
# get_name() → "Mr. Smith"

# Write your code below:

# def prefix(prefix):
#     def decorator(func):
#         def wrapper():
#             full_name = prefix + func()
#             return full_name
#         return wrapper
#     return decorator


# @prefix("Mr. ")
# def get_name():
#     return "Smith"


# print(get_name())

# ----------------------------------------------------------------------
# Exercise D13: Cache/Memoization Decorator
# Create a decorator called cache that:
# - Stores results of function calls
# - If called with same arguments again, returns cached result
# - Prints "Calculating..." when actually running the function
# - Prints "Using cache..." when using cached result
#
# Hint: Use a dictionary to store results
#
# Test it on:
# @cache
# def expensive_function(n):
#     print("Calculating...")
#     return n * n
#
# Expected:
# expensive_function(5)  # Calculating... → 25
# expensive_function(5)  # Using cache... → 25
# expensive_function(3)  # Calculating... → 9

# Write your code below:

# def cache(func):
#     cache_dict = {}

#     def decorator(n):
#         if n in cache_dict:
#             print(f"Using cache... {cache_dict[n]}")
#             return cache_dict[n]
#         else:
#             cache_dict[n] = func(n)
#             print(cache_dict[n])
#             return cache_dict[n]
#     return decorator


# @cache
# def expensive_function(n):
#     print("Calculating...")
#     return n*n


# expensive_function(5)
# expensive_function(5)
# expensive_function(3)

# ----------------------------------------------------------------------
# Exercise D14: Debug Decorator
# Create a decorator called debug that:
# - Prints the function name
# - Prints the arguments it received
# - Runs the function
# - Prints the result
# - Returns the result
#
# Test it on:
# @debug
# def add(a, b):
#     return a + b
#
# Expected output:
# add(3, 5)
# Calling: add
# Arguments: (3, 5)
# Result: 8
# → returns 8

# Write your code below:

# def debug(func):
#     def wrapper(*args):
#         print(f"Calling: {func.__name__}")
#         print(f"Arguments: {args}")
#         result = func(*args)
#         print(f"Result: {result}")
#         return result
#     return wrapper


# @debug
# def add(a, b):
#     return a + b


# add(3, 5)

# ----------------------------------------------------------------------
# Exercise D15: Practical Application - Login Required
# Create a decorator called login_required that:
# - Takes a function that has a 'user' parameter
# - If user is None, prints "Please login first!" and returns None
# - Otherwise, runs the function normally
#
# Test it on:
# @login_required
# def view_profile(user):
#     return f"Profile of {user}"
#
# Expected:
# view_profile(None) → prints "Please login first!", returns None
# view_profile("Alice") → "Profile of Alice"

# Write your code below:

# def login_required(func):
#     def wrapper(user):
#         if user is None:
#             print("Please login first!")
#             return None
#         else:
#             print(func(user))
#             return func(user)
#     return wrapper


# @login_required
# def view_profile(user):
#     return f"Profile of {user}"


# view_profile("Alice")
# view_profile(None)

# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# ----------------------------------------------------------------------
# Exercise D16 (BONUS): Combine Everything
# Create a function that:
# - Is timed (shows execution time)
# - Is counted (shows call number)
# - Is cached (stores results)
#
# Stack three decorators in the right order!
#
# Think about: Which decorator should be closest to the function?

# Write your code below:


# ----------------------------------------------------------------------
# Exercise D17 (BONUS): Decorator Class
# Research: Decorators can also be classes!
# Create a class-based decorator called Repeat that:
# - Takes n in __init__
# - Implements __call__ to repeat the function n times
#
# This is advanced! Try if you're curious!

# Write your code below:


# ============================================================================
# END OF DECORATOR EXERCISES
# ============================================================================
