# ============================================================================
# RECURSION - BUILDING ON COUNTDOWN PATTERN
# ============================================================================

# ----------------------------------------------------------------------
# REFERENCE: Countdown (You already understand this!)
#
# def countdown(n):
#     if n == 0:           # Base case
#         print("Done!")
#     else:
#         print(n)         # Do work
#         countdown(n-1)   # Recurse with n-1
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Exercise R1: Count UP instead of down
# Create a function called countup that takes n
# It should print from 1 up to n, then print "Done!"
#
# Pattern is SAME as countdown, but think:
# - What's your base case? (When do you stop?)
# - Do you print BEFORE or AFTER the recursive call?
#
# Test with countup(5)
#
# Expected:
# Done!
# 1
# 2
# 3
# 4
# 5

# Write your code for Exercise R1 below:

# def countup(n):
#     if n == 0:
#         print("Done!")
#     else:
#         countup(n-1)
#         print(n)


# countup(5)

# ----------------------------------------------------------------------
# Exercise R2: Sum from 1 to n
# Create a function called sum_to_n that takes n
# Return the sum of numbers from 1 to n
#
# Same pattern as countdown, but:
# - Instead of PRINTING, you're RETURNING a number
# - Base case: What's the sum when n is 1? Just return 1!
# - Recursive: return n + sum_to_n(n-1)
#
# Think: sum_to_n(5) = 5 + sum_to_n(4)
#        sum_to_n(4) = 4 + sum_to_n(3)
#        ...
#        sum_to_n(1) = 1  (base case!)
#
# Test with sum_to_n(5)
#
# Expected: 15

# Write your code for Exercise R2 below:

# def sum_to_n(n):
#     if n == 1:
#         return 1
#     else:
#         return n+sum_to_n(n-1)


# print(sum_to_n(5))

# ----------------------------------------------------------------------
# Exercise R3: Factorial
# Create a function called factorial that takes n
# Return n! = n × (n-1) × (n-2) × ... × 1
#
# Same pattern, but multiply instead of add:
# - Base case: 1! = 1 (also 0! = 1)
# - Recursive: return n * factorial(n-1)
#
# Think: factorial(5) = 5 * factorial(4)
#        factorial(4) = 4 * factorial(3)
#        ...
#        factorial(1) = 1  (base case!)
#
# Test with factorial(5)
#
# Expected: 120

# Write your code for Exercise R3 below:

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# ----------------------------------------------------------------------
# Exercise R4: Print a string n times
# Create a function called print_n_times that takes a string and n
# Print the string n times
#
# Same countdown pattern:
# - Base case: when n is 0, stop (don't print anything)
# - Recursive: print the string, then call with n-1
#
# Test with print_n_times("Hello", 3)
#
# Expected:
# Hello
# Hello
# Hello

# Write your code for Exercise R4 below:

# def print_n_times(a_string, n):
#     if n==0:
#         return
#     else:
#         print(a_string)
#         print_n_times(a_string, n-1)

# print_n_times("Hello", 3)

# ----------------------------------------------------------------------
# Exercise R5: Power function
# Create a function called power that takes base and exponent
# Calculate base^exponent
#
# Same pattern:
# - Base case: anything^0 = 1
# - Recursive: base^exponent = base * base^(exponent-1)
#
# Think: power(2, 5) = 2 * power(2, 4)
#        power(2, 4) = 2 * power(2, 3)
#        ...
#        power(2, 0) = 1  (base case!)
#
# Test with power(2, 5)
#
# Expected: 32

# Write your code for Exercise R5 below:

# def power(base, exponent):
#     if (exponent == 0):
#         return 1
#     else:
#         return base*power(base, exponent-1)


# print(power(2, 5))
# print(power(2, 0))
# print(power(0, 2))
# print(power(0, 0))

# ============================================================================
# END - If you got these, you understand recursion! 🔥
# ============================================================================
