# ============================================================================
# LAMBDA FUNCTIONS EXERCISES (L1-L15)
# ============================================================================
# Focus: Lambda functions, map(), filter(), reduce(), and sorting with lambdas
# ============================================================================

# ----------------------------------------------------------------------
# Exercise L1: Basic Lambda Function
# 1. Create a lambda function that takes x and returns x * 2
# 2. Assign it to a variable called double
# 3. Call double(5) and print the result
# 4. Call double(10) and print the result
#
# Expected:
# 10
# 20

# Write your code for Exercise L1 below:

# def double(x): return x*2


# print(double(5))
# print(double(10))


# ----------------------------------------------------------------------
# Exercise L2: Lambda with Two Arguments
# 1. Create a lambda function that takes a and b and returns a + b
# 2. Assign it to a variable called add
# 3. Call add(3, 7) and print the result
# 4. Call add(10, 20) and print the result
#
# Expected:
# 10
# 30

# Write your code for Exercise L2 below:

# add = lambda a,b:a+b
# print(add(3,7))
# print(add(10,20))

# ----------------------------------------------------------------------
# Exercise L3: Lambda with map()
# 1. Create a list: numbers = [1, 2, 3, 4, 5]
# 2. Use map() with a lambda to square each number
# 3. Convert to list and print
#
# Expected: [1, 4, 9, 16, 25]

# Write your code for Exercise L3 below:

# numbers = [1,2,3,4,5]
# square = list(map(lambda x:x**2, numbers))

# ----------------------------------------------------------------------
# Exercise L4: Lambda with filter()
# 1. Create a list: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2. Use filter() with a lambda to get only odd numbers
# 3. Convert to list and print
#
# Expected: [1, 3, 5, 7, 9]

# Write your code for Exercise L4 below:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd = list(filter(lambda x:x%2!=0, numbers))
# print(odd)


# ----------------------------------------------------------------------
# Exercise L5: Sorting with Lambda - FIRST TIME
# 1. Create a list: pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
# 2. Sort the list by the SECOND element (the string) using .sort() with key parameter
# 3. Print the sorted list
#
# Hint: pairs.sort(key=lambda x: x[1])
#
# Expected: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Write your code for Exercise L5 below:

pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=lambda x: x[1])
print(pairs)

# ----------------------------------------------------------------------
# Exercise L6: Sorting with Lambda - Practice (NO HINT)
# 1. Create a list: words = ["python", "is", "awesome", "fun"]
# 2. Sort the list by word length using sorted() with key parameter
# 3. Print the sorted list
#
# Expected: ['is', 'fun', 'python', 'awesome']

# Write your code for Exercise L6 below:

words = ["python", "is", "awesome", "fun"]
words.sort(key=lambda x: len(x))
print(words)

# ----------------------------------------------------------------------
# Exercise L7: Lambda vs Regular Function
# 1. Create a regular function called multiply that takes x and y and returns x * y
# 2. Create a lambda function that does the same thing, assign to multiply_lambda
# 3. Test both with multiply(3, 4) and multiply_lambda(3, 4)
# 4. Print both results
#
# Expected:
# 12
# 12

# Write your code for Exercise L7 below:


# ----------------------------------------------------------------------
# Exercise L8: map() with Lambda - Practice (NO HINT)
# 1. Create a list: names = ["alice", "bob", "charlie"]
# 2. Use map() with a lambda to capitalize each name
# 3. Convert to list and print
#
# Expected: ['Alice', 'Bob', 'Charlie']

# Write your code for Exercise L8 below:


# ----------------------------------------------------------------------
# Exercise L9: filter() with Lambda - Multiple Conditions (NO HINT)
# 1. Create a list: numbers = [5, 12, 17, 8, 23, 14, 30]
# 2. Use filter() with a lambda to get numbers that are:
#    - Greater than 10 AND
#    - Even (divisible by 2)
# 3. Convert to list and print
#
# Expected: [12, 14, 30]

# Write your code for Exercise L9 below:


# ----------------------------------------------------------------------
# Exercise L10: Sorting Dictionaries with Lambda - FIRST TIME
# 1. Create a list of dictionaries:
#    students = [
#        {"name": "Alice", "grade": 85},
#        {"name": "Bob", "grade": 92},
#        {"name": "Charlie", "grade": 78}
#    ]
# 2. Sort by grade (highest first) using sorted() with key and reverse parameters
# 3. Print the sorted list
#
# Hint: sorted(students, key=lambda x: x["grade"], reverse=True)
#
# Expected: [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85},
#            {'name': 'Charlie', 'grade': 78}]

# Write your code for Exercise L10 below:


# ----------------------------------------------------------------------
# Exercise L11: Lambda with Multiple Operations (NO HINT)
# 1. Create a list: numbers = [1, 2, 3, 4, 5]
# 2. Use map() with a lambda to:
#    - Multiply each number by 2
#    - Then add 10
# 3. Convert to list and print
#
# Expected: [12, 14, 16, 18, 20]

# Write your code for Exercise L11 below:


# ----------------------------------------------------------------------
# Exercise L12: Combining map() and filter() with Lambdas (NO HINT)
# 1. Create a list: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2. First, use filter() with a lambda to get only even numbers
# 3. Then, use map() with a lambda to square those numbers
# 4. Convert to list and print
#
# Expected: [4, 16, 36, 64, 100]

# Write your code for Exercise L12 below:


# ----------------------------------------------------------------------
# Exercise L13: Lambda with Conditional Expression - FIRST TIME
# 1. Create a list: numbers = [-5, 3, -2, 8, -1, 10]
# 2. Use map() with a lambda that:
#    - Returns the number if it's positive
#    - Returns 0 if it's negative
# 3. Convert to list and print
#
# Hint: lambda x: x if x > 0 else 0
#
# Expected: [0, 3, 0, 8, 0, 10]

# Write your code for Exercise L13 below:


# ----------------------------------------------------------------------
# Exercise L14: Sorting with Multiple Keys - FIRST TIME
# 1. Create a list of tuples:
#    data = [("Alice", 25), ("Bob", 30), ("Charlie", 25), ("David", 30)]
# 2. Sort by age first, then by name (both ascending)
# 3. Print the sorted list
#
# Hint: key=lambda x: (x[1], x[0])
#
# Expected: [('Alice', 25), ('Charlie', 25), ('Bob', 30), ('David', 30)]

# Write your code for Exercise L14 below:


# ----------------------------------------------------------------------
# Exercise L15: Practical Lambda - Processing Data (NO HINT)
# 1. Create a list of dictionaries:
#    products = [
#        {"name": "apple", "price": 2.50, "quantity": 10},
#        {"name": "banana", "price": 1.00, "quantity": 5},
#        {"name": "orange", "price": 3.00, "quantity": 0},
#        {"name": "grape", "price": 4.00, "quantity": 8}
#    ]
# 2. Use filter() with a lambda to get only products in stock (quantity > 0)
# 3. Use map() with a lambda to get just the names of those products
# 4. Convert to list and print
#
# Expected: ['apple', 'banana', 'grape']

# Write your code for Exercise L15 below:


# ============================================================================
# BONUS: reduce() Function (Optional - Advanced)
# ============================================================================

# ----------------------------------------------------------------------
# Exercise L16 (BONUS): Using reduce() with Lambda - FIRST TIME
# 1. Import reduce from functools
# 2. Create a list: numbers = [1, 2, 3, 4, 5]
# 3. Use reduce() with a lambda to multiply all numbers together
# 4. Print the result
#
# Hint: from functools import reduce
#       reduce(lambda x, y: x * y, numbers)
#
# Expected: 120

# Write your code for Exercise L16 below:


# ----------------------------------------------------------------------
# Exercise L17 (BONUS): reduce() to Find Maximum (NO HINT)
# 1. Import reduce from functools
# 2. Create a list: numbers = [3, 7, 2, 9, 1, 5]
# 3. Use reduce() with a lambda to find the maximum number
# 4. Print the result
#
# Expected: 9

# Write your code for Exercise L17 below:


# ============================================================================
# END OF LAMBDA FUNCTIONS EXERCISES
# ============================================================================
