# ============================================================================
# RECURSION EXERCISES (R1-R20) - FIGURE IT ALL OUT YOURSELF!
# ============================================================================
# Focus: Understanding recursion - YOU find the base case AND recursive logic
# No hand-holding! You got this! 💪
# ============================================================================

# ----------------------------------------------------------------------
# Exercise R1: Countdown
# Create a recursive function called countdown that takes a number n
# It should print each number from n down to 1, then print "Done!"
# Test with countdown(5)
#
# Expected:
# 5
# 4
# 3
# 2
# 1
# Done!

# Write your code for Exercise R1 below:

# def countdown(n):
#     if n == 0:
#         print("Done")
#     else:
#         print(n)
#         return countdown(n-1)


# countdown(5)

# ----------------------------------------------------------------------
# Exercise R2: Sum of Numbers
# Create a recursive function called sum_to_n that takes a number n
# Return the sum of all numbers from 1 to n
# Test with sum_to_n(5)
#
# Expected: 15

# Write your code for Exercise R2 below:

# def sum_to_n(n):
#     if n == 0:
#         return 0
#     else:
#         return n+sum_to_n(n-1)


# print(sum_to_n(5))

# ----------------------------------------------------------------------
# Exercise R3: Factorial
# Create a recursive function called factorial that takes n
# Calculate n! (n factorial = n × (n-1) × (n-2) × ... × 1)
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
# Exercise R4: Power Function
# Create a recursive function called power that takes base and exponent
# Calculate base raised to the power of exponent
# Test with power(2, 5)
#
# Expected: 32

# Write your code for Exercise R4 below:

# def power(base, exponent):
#     if base == 0 and exponent != 0:
#         return 0
#     elif exponent == 0:
#         return 1
#     else:
#         return base*power(base, exponent-1)


# print(power(0, 4))

# ----------------------------------------------------------------------
# Exercise R5: Fibonacci Sequence
# Create a recursive function called fibonacci that takes n
# Return the nth number in the Fibonacci sequence
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
# Test with fibonacci(7)
#
# Expected: 8

# Write your code for Exercise R5 below:

def fibonacci(n):
    if n <= 0:
        print("N must be >1")
    elif n == 1:
        print(0)
    else:
        x = 0
        y = 1
        z = x+y
        for i in range(3, n):
            x = y
            y = z
            z = x+y
        return z


print(fibonacci(8))


# ----------------------------------------------------------------------
# Exercise R6: Count Digits
# Create a recursive function called count_digits that takes a number n
# Count how many digits are in the number
# Test with count_digits(12345)
#
# Expected: 5

# Write your code for Exercise R6 below:


# ----------------------------------------------------------------------
# Exercise R7: Sum of Digits
# Create a recursive function called sum_digits that takes a number n
# Return the sum of all digits in the number
# Test with sum_digits(12345)
#
# Expected: 15

# Write your code for Exercise R7 below:


# ----------------------------------------------------------------------
# Exercise R8: Reverse a String
# Create a recursive function called reverse_string that takes a string s
# Return the string reversed
# Test with reverse_string("hello")
#
# Expected: olleh

# Write your code for Exercise R8 below:


# ----------------------------------------------------------------------
# Exercise R9: Is Palindrome
# Create a recursive function called is_palindrome that takes a string s
# Return True if the string reads the same forwards and backwards
# Test with is_palindrome("racecar") and is_palindrome("hello")
#
# Expected:
# True
# False

# Write your code for Exercise R9 below:


# ----------------------------------------------------------------------
# Exercise R10: Sum of List
# Create a recursive function called sum_list that takes a list of numbers
# Return the sum of all numbers in the list
# Test with sum_list([1, 2, 3, 4, 5])
#
# Expected: 15

# Write your code for Exercise R10 below:


# ----------------------------------------------------------------------
# Exercise R11: Find Maximum in List
# Create a recursive function called find_max that takes a list of numbers
# Return the largest number in the list
# Test with find_max([3, 7, 2, 9, 1, 5])
#
# Expected: 9

# Write your code for Exercise R11 below:


# ----------------------------------------------------------------------
# Exercise R12: Count Occurrences
# Create a recursive function called count_occurrences
# Takes a list and a target value
# Return how many times target appears in the list
# Test with count_occurrences([1, 2, 3, 2, 4, 2], 2)
#
# Expected: 3

# Write your code for Exercise R12 below:


# ----------------------------------------------------------------------
# Exercise R13: Flatten Nested List
# Create a recursive function called flatten that takes a nested list
# Return a single flat list with all elements
# Test with flatten([1, [2, 3], [4, [5, 6]]])
#
# Expected: [1, 2, 3, 4, 5, 6]

# Write your code for Exercise R13 below:


# ----------------------------------------------------------------------
# Exercise R14: Binary Search
# Create a recursive function called binary_search
# Takes: sorted list, target value, start index, end index
# Return the index where target is found, or -1 if not found
# Test with binary_search([1, 3, 5, 7, 9, 11], 7, 0, 5)
#
# Expected: 3

# Write your code for Exercise R14 below:


# ----------------------------------------------------------------------
# Exercise R15: GCD (Greatest Common Divisor)
# Create a recursive function called gcd that takes two numbers a and b
# Find the largest number that divides both a and b evenly
# Test with gcd(48, 18)
#
# Expected: 6

# Write your code for Exercise R15 below:


# ----------------------------------------------------------------------
# Exercise R16: Print List in Reverse
# Create a recursive function called print_reverse that takes a list
# Print all elements in reverse order (one per line)
# Test with print_reverse([1, 2, 3, 4, 5])
#
# Expected:
# 5
# 4
# 3
# 2
# 1

# Write your code for Exercise R16 below:


# ----------------------------------------------------------------------
# Exercise R17: Tower of Hanoi
# Create a recursive function called hanoi
# Takes: number of disks (n), source rod, destination rod, auxiliary rod
# Print the moves needed to transfer all disks from source to destination
# Rules: only one disk at a time, larger disk never on smaller disk
# Test with hanoi(3, 'A', 'C', 'B')
#
# Expected:
# Move disk from A to C
# Move disk from A to B
# Move disk from C to B
# Move disk from A to C
# Move disk from B to A
# Move disk from B to C
# Move disk from A to C

# Write your code for Exercise R17 below:


# ----------------------------------------------------------------------
# Exercise R18: Generate All Subsets
# Create a recursive function called subsets that takes a list
# Return a list of all possible subsets (the power set)
# Test with subsets([1, 2, 3])
#
# Expected: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

# Write your code for Exercise R18 below:


# ----------------------------------------------------------------------
# Exercise R19: String Permutations
# Create a recursive function called permutations that takes a string
# Return a list of all possible arrangements of the characters
# Test with permutations("abc")
#
# Expected: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Write your code for Exercise R19 below:


# ----------------------------------------------------------------------
# Exercise R20: Recursive vs Iterative Comparison
# Create TWO functions to calculate sum from 1 to n:
# - sum_recursive(n) using recursion
# - sum_iterative(n) using a for loop
# Both should return the same result
# Test both with n = 100
#
# Expected:
# 5050
# 5050

# Write your code for Exercise R20 below:


# ============================================================================
# END OF RECURSION EXERCISES
# ============================================================================
