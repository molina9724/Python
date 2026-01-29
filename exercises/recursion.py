# ============================================================================
# RECURSION EXERCISES (R1-R20) - FIGURE IT OUT YOURSELF!
# ============================================================================
# Focus: Understanding recursion, base cases, recursive calls
# You get WHAT to do, not HOW to do it!
# ============================================================================

# ----------------------------------------------------------------------
# Exercise R1: Basic Recursion - Countdown
# 1. Create a recursive function called countdown that takes a number n
# 2. It should print each number from n down to 1, then print "Done!"
# 3. Base case: when n reaches 0, print "Done!" and stop
# 4. Test with countdown(5)
#
# Expected:
# 5
# 4
# 3
# 2
# 1
# Done!

# Write your code for Exercise R1 below:


# ----------------------------------------------------------------------
# Exercise R2: Sum of Numbers
# 1. Create a recursive function called sum_to_n that takes a number n
# 2. It should return the sum of all numbers from 1 to n
# 3. Base case: when n is 1, you know the answer without recursion
# 4. Test with sum_to_n(5)
#
# Expected: 15

# Write your code for Exercise R2 below:


# ----------------------------------------------------------------------
# Exercise R3: Factorial
# 1. Create a recursive function called factorial that takes n
# 2. Factorial means: 5! = 5 × 4 × 3 × 2 × 1
# 3. Base case: 0! and 1! both equal 1
# 4. Test with factorial(5)
#
# Expected: 120

# Write your code for Exercise R3 below:


# ----------------------------------------------------------------------
# Exercise R4: Power Function
# 1. Create a recursive function called power that takes base and exponent
# 2. Calculate base raised to the power of exponent (base^exponent)
# 3. Base case: any number to the power of 0 equals 1
# 4. Think: 2^5 = 2 × 2^4
# 5. Test with power(2, 5)
#
# Expected: 32

# Write your code for Exercise R4 below:


# ----------------------------------------------------------------------
# Exercise R5: Fibonacci Sequence
# 1. Create a recursive function called fibonacci that takes n
# 2. Return the nth number in the Fibonacci sequence
# 3. Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
# 4. Base cases: 1st number is 0, 2nd number is 1
# 5. Each other number is the sum of the previous two
# 6. Test with fibonacci(7)
#
# Expected: 8

# Write your code for Exercise R5 below:


# ----------------------------------------------------------------------
# Exercise R6: Count Digits
# 1. Create a recursive function called count_digits that takes a number n
# 2. Count how many digits are in the number
# 3. Base case: single digit numbers (less than 10) have 1 digit
# 4. Hint: You can remove the last digit with n // 10
# 5. Test with count_digits(12345)
#
# Expected: 5

# Write your code for Exercise R6 below:


# ----------------------------------------------------------------------
# Exercise R7: Sum of Digits
# 1. Create a recursive function called sum_digits that takes a number n
# 2. Return the sum of all digits in the number
# 3. Base case: single digit numbers
# 4. Hint: n % 10 gives you the last digit, n // 10 removes it
# 5. Test with sum_digits(12345)
#
# Expected: 15

# Write your code for Exercise R7 below:


# ----------------------------------------------------------------------
# Exercise R8: Reverse a String
# 1. Create a recursive function called reverse_string that takes a string s
# 2. Return the string reversed
# 3. Base case: strings with 0 or 1 characters are already "reversed"
# 4. Think about taking characters from the end and building backwards
# 5. Test with reverse_string("hello")
#
# Expected: olleh

# Write your code for Exercise R8 below:


# ----------------------------------------------------------------------
# Exercise R9: Is Palindrome
# 1. Create a recursive function called is_palindrome that takes a string s
# 2. Return True if the string reads the same forwards and backwards
# 3. Base case: strings with 0 or 1 characters are palindromes
# 4. Check if first and last characters match, then check the middle
# 5. Test with is_palindrome("racecar") and is_palindrome("hello")
#
# Expected:
# True
# False

# Write your code for Exercise R9 below:


# ----------------------------------------------------------------------
# Exercise R10: Sum of List
# 1. Create a recursive function called sum_list that takes a list of numbers
# 2. Return the sum of all numbers in the list
# 3. Base case: empty list sums to 0
# 4. Think: sum = first element + sum of the rest
# 5. Test with sum_list([1, 2, 3, 4, 5])
#
# Expected: 15

# Write your code for Exercise R10 below:


# ----------------------------------------------------------------------
# Exercise R11: Find Maximum in List
# 1. Create a recursive function called find_max that takes a list of numbers
# 2. Return the largest number in the list
# 3. Base case: list with one element - that's the max
# 4. Compare first element with the max of the remaining elements
# 5. Test with find_max([3, 7, 2, 9, 1, 5])
#
# Expected: 9

# Write your code for Exercise R11 below:


# ----------------------------------------------------------------------
# Exercise R12: Count Occurrences
# 1. Create a recursive function called count_occurrences
# 2. Takes a list and a target value
# 3. Return how many times target appears in the list
# 4. Base case: empty list has 0 occurrences
# 5. Check first element, then count in the rest
# 6. Test with count_occurrences([1, 2, 3, 2, 4, 2], 2)
#
# Expected: 3

# Write your code for Exercise R12 below:


# ----------------------------------------------------------------------
# Exercise R13: Flatten Nested List
# 1. Create a recursive function called flatten that takes a nested list
# 2. Return a single flat list with all elements
# 3. Base case: if item is not a list, it's already flat
# 4. If item is a list, flatten it recursively
# 5. Test with flatten([1, [2, 3], [4, [5, 6]]])
#
# Expected: [1, 2, 3, 4, 5, 6]

# Write your code for Exercise R13 below:


# ----------------------------------------------------------------------
# Exercise R14: Binary Search (Recursive)
# 1. Create a recursive function called binary_search
# 2. Takes: sorted list, target value, start index, end index
# 3. Return the index where target is found, or -1 if not found
# 4. Base case: if start > end, target not found
# 5. Find middle element, compare with target, search appropriate half
# 6. Test with binary_search([1, 3, 5, 7, 9, 11], 7, 0, 5)
#
# Expected: 3

# Write your code for Exercise R14 below:


# ----------------------------------------------------------------------
# Exercise R15: GCD (Greatest Common Divisor)
# 1. Create a recursive function called gcd that takes two numbers a and b
# 2. Find the largest number that divides both a and b
# 3. Base case: if b is 0, the GCD is a
# 4. Use the Euclidean algorithm: gcd(a, b) = gcd(b, remainder of a/b)
# 5. Test with gcd(48, 18)
#
# Expected: 6

# Write your code for Exercise R15 below:


# ----------------------------------------------------------------------
# Exercise R16: Print List in Reverse
# 1. Create a recursive function called print_reverse that takes a list
# 2. Print all elements in reverse order (one per line)
# 3. Base case: empty list, nothing to print
# 4. Think: print the rest first, THEN print the first element
# 5. Test with print_reverse([1, 2, 3, 4, 5])
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
# 1. Create a recursive function called hanoi
# 2. Takes: number of disks (n), source rod, destination rod, auxiliary rod
# 3. Print the moves needed to transfer all disks from source to destination
# 4. Rules: only one disk at a time, larger disk never on smaller disk
# 5. Base case: moving 1 disk is simple - just move it
# 6. For n disks: move n-1 to auxiliary, move largest to destination, move n-1 to destination
# 7. Test with hanoi(3, 'A', 'C', 'B')
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
# 1. Create a recursive function called subsets that takes a list
# 2. Return a list of all possible subsets (the power set)
# 3. Base case: subset of empty list is [[]]
# 4. For each element: include it or don't include it in subsets
# 5. Test with subsets([1, 2, 3])
#
# Expected: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

# Write your code for Exercise R18 below:


# ----------------------------------------------------------------------
# Exercise R19: String Permutations
# 1. Create a recursive function called permutations that takes a string
# 2. Return a list of all possible arrangements of the characters
# 3. Base case: permutation of single character is just that character
# 4. For each character: make it first, then permute the rest
# 5. Test with permutations("abc")
#
# Expected: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Write your code for Exercise R19 below:


# ----------------------------------------------------------------------
# Exercise R20: Recursive vs Iterative Comparison
# 1. Create TWO functions to calculate sum from 1 to n:
#    - sum_recursive(n) using recursion
#    - sum_iterative(n) using a for loop
# 2. Both should return the same result
# 3. Test both with n = 100
# 4. Print both results
#
# Expected:
# 5050
# 5050

# Write your code for Exercise R20 below:


# ============================================================================
# END OF RECURSION EXERCISES
# ============================================================================