# ============================================================================
# LEGB NAMESPACE EXERCISES (NS1-NS10)
# ============================================================================
# Focus: Understanding scope, LEGB rule, global/nonlocal keywords
# ============================================================================

# ----------------------------------------------------------------------
# Exercise NS1: Predict the Output - Local vs Global
# Look at this code and predict what it will print.
# Then run it to check your answer.
#
# Code:
# x = 100

# def test():
#     x = 50
#     print(x)

# test()
# print(x)
#
# What will this print?
# Write your prediction as a comment, then uncomment and run the code.


# Your prediction: 50
# test() will print: 50
# print(x) will print: 100

# Uncomment to test:
# x = 100
# def test():
#     x = 50
#     print(x)
# test()
# print(x)


# ----------------------------------------------------------------------
# Exercise NS2: Fix the Code - Modify Global Variable
# This code is trying to modify the global variable count
# But it doesn't work! Fix it using the 'global' keyword.
#
# Current code (broken):
# count = 0
#
# def increment():
#     count = count + 1
#
# increment()
# print(count)  # Should print 1, but gives an error!

# Write your fixed code below:

# count = 0

# def increment():
#     global count
#     count = count + 1

# increment()
# print(count)  # Should print 1, but gives an error!


# ----------------------------------------------------------------------
# Exercise NS3: Predict the Output - Enclosing Scope
# Predict what this will print:
#
# Code:
# def outer():
#     message = "outer"
#
#     def inner():
#         print(message)
#
#     inner()
#
# outer()
#
# What will print? Write your prediction, then test.

# Your prediction: outer

# Uncomment to test:
# def outer():
#     message = "outer"
#     def inner():
#         print(message)
#     inner()
# outer()


# ----------------------------------------------------------------------
# Exercise NS4: Fix the Code - Modify Enclosing Variable
# This code tries to modify a variable from the enclosing scope
# It doesn't work! Fix it using the 'nonlocal' keyword.
#
# Current code (broken):
# def outer():
#     count = 0
#
#     def inner():
#         count = count + 1
#         print(count)
#
#     inner()
#     print(count)  # Should print 1
#
# outer()

# Write your fixed code below:

# def outer():
#     count = 0

#     def inner():
#         nonlocal count
#         count = count + 1
#         print(count)

#     inner()
#     print(count)  # Should print 1

# outer()

# ----------------------------------------------------------------------
# Exercise NS5: Predict the Output - LEGB in Action
# Predict what each print statement will output:
#
# Code:
# x = "global"
#
# def outer():
#     x = "enclosing"
#
#     def inner():
#         x = "local"
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
# outer()
# print("global:", x)

# Your predictions:
# inner: local
# outer: enclosing
# global: global

# Uncomment to test:
# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()
# print("global:", x)


# ----------------------------------------------------------------------
# Exercise NS6: Create a Counter Function
# Create a function called make_counter() that returns an inner function
# The inner function should increment and return a count each time it's called
# Use enclosing scope to maintain the count
#
# Example usage:
# counter = make_counter()
# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3

# Write your code below:

# count = 0

# def make_counter():
#     def counter():
#         global count
#         count+=1
#         print(count)
#     counter()

# make_counter()
# make_counter()
# make_counter()

# ----------------------------------------------------------------------
# Exercise NS7: Predict the Output - Tricky Scope
# This one is tricky! Predict what happens:
#
# Code:
# x = 10
#
# def test():
#     print(x)
#     x = 20
#
# test()
#
# Will this:
# A) Print 10
# B) Print 20
# C) Give an error
#
# Your prediction: A
# Why? (write your reasoning) - Global x=10

# Uncomment to test:
# x = 10
# def test():
#     print(x)
#     x = 20
# test()


# ----------------------------------------------------------------------
# Exercise NS8: Fix the Scope Issue
# This code has a scope problem. Fix it so it prints the global x,
# then creates a local x.
#
# Current code (broken):
# x = 10
#
# def test():
#     print(x)  # Want to print global x (10)
#     x = 20    # Then create local x
#     print(x)  # Print local x (20)
#
# test()

# Write your fixed code below:
# Hint: You might need to use a different variable name or approach

# x=10

# def test():
#     global x
#     print(x)  # Want to print global x (10)
#     x = 20    # Then create local x
#     print(x)  # Print local x (20)


# test()

# ----------------------------------------------------------------------
# Exercise NS9: Built-in Namespace - Don't Shadow!
# This code accidentally shadows a built-in function.
# Identify the problem and fix it.
#
# Code:
# list = [1, 2, 3, 4, 5]
# sum = 0
#
# for num in list:
#     sum = sum + num
#
# print(sum)
#
# # Later in the code...
# new_list = list(range(5))  # This will fail!
# total = sum([1, 2, 3])     # This will fail too!
#
# What's the problem? How would you fix it?

# Your explanation: ???

# Write better code below:

# my_list = [1, 2, 3, 4, 5]
# total_sum = 0

# for num in my_list:
#     total_sum = total_sum + num

# print(total_sum)

# # Later in the code...
# new_list = list(range(5))
# total = [1, 2, 3]
# another_total = sum(total)

# ----------------------------------------------------------------------
# Exercise NS10: Create a Bank Account (Practical Application)
# Create a function called create_account(initial_balance)
# It should return a dictionary with three functions:
# - deposit(amount): adds to balance
# - def deposit(amount):
# - get_balance(): returns current balance
#
# Use enclosing scope to keep the balance private!
#
# Example usage:
# account = create_account(100)
# account['deposit'](50)
# account['withdraw'](30)
# print(account['get_balance']())  # Should print 120

# Write your code below:

# def create_account(initial_balance):
#     def deposit(amount):
#         account["balance"] += amount

#     def withdraw(amount):
#         account["balance"] -= amount

#     def get_balance():
#         return account["balance"]

#     account = {"balance": initial_balance, "deposit": deposit,
#                "withdraw": withdraw, "get_balance": get_balance}

#     return account


# account = create_account(100)
# account["deposit"](50)
# account["withdraw"](30)
# print(account['get_balance']())

# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# ----------------------------------------------------------------------
# Exercise NS11 (BONUS): Explain This Behavior
# Run this code and explain why it behaves this way:
#
# Code:
# funcs = []
#
# for i in range(3):
#     def func():
#         print(i)
#     funcs.append(func)
#
# for f in funcs:
#     f()
#
# Why does it print what it prints? Because it initializes func for every i in the for, so 
# How would you fix it to print 0, 1, 2? 

# Your explanation: ???

# Uncomment to test:
# funcs = []
# for i in range(3):
#     def func(x=i):
#         print(x)
#     funcs.append(func)
# for f in funcs:
#     f()


# ----------------------------------------------------------------------
# Exercise NS12 (BONUS): Multiple Enclosing Scopes
# Predict the output:
#
# Code:
# x = "global"
#
# def level1():
#     x = "level1"
#
#     def level2():
#         x = "level2"
#
#         def level3():
#             print(x)
#
#         level3()
#
#     level2()
#
# level1()

# Your prediction: level2

# Uncomment to test:
# x = "global"
# def level1():
#     x = "level1"
#     def level2():
#         x = "level2"
#         def level3():
#             print(x)
#         level3()
#     level2()
# level1()


# ============================================================================
# END OF LEGB NAMESPACE EXERCISES
# ============================================================================
