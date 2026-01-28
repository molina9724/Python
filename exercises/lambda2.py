# ============================================================================
# ADVANCED LAMBDA PRACTICE (AL1-AL20)
# ============================================================================
# Focus: More complex scenarios, combining concepts, real-world applications
# ============================================================================

# ----------------------------------------------------------------------
# Exercise AL1: Lambda with String Methods
# 1. Create a list: emails = ["ALICE@EMAIL.COM", "bob@email.com", "CHARLIE@EMAIL.COM"]
# 2. Use map() with a lambda to convert all emails to lowercase
# 3. Convert to list and print
#
# Expected: ['alice@email.com', 'bob@email.com', 'charlie@email.com']

# Write your code for Exercise AL1 below:

# emails = ["ALICE@EMAIL.COM", "bob@email.com", "CHARLIE@EMAIL.COM"]
# lower_emails = list(map(lambda x:x.lower(), emails))
# print(lower_emails)

# ----------------------------------------------------------------------
# Exercise AL2: Filter and Transform
# 1. Create a list: prices = [10.50, 25.00, 5.75, 30.00, 15.25]
# 2. Use filter() to get prices >= 15
# 3. Use map() to apply 10% discount (multiply by 0.9)
# 4. Convert to list and print
#
# Expected: [22.5, 27.0, 13.725]

# Write your code for Exercise AL2 below:

# prices = [10.50, 25.00, 5.75, 30.00, 15.25]
# plus_fifteen = filter(lambda x: x >= 15, prices)
# discount = list(map(lambda x: x*0.9, plus_fifteen))
# print(discount)

# ----------------------------------------------------------------------
# Exercise AL3: Lambda with List of Tuples - Extract Specific Data
# 1. Create a list: people = [("Alice", 30, "Engineer"), ("Bob", 25, "Designer"), ("Charlie", 35, "Manager")]
# 2. Use map() with a lambda to extract only names and ages as tuples
# 3. Convert to list and print
#
# Expected: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# Write your code for Exercise AL3 below:

# people = [("Alice", 30, "Engineer"), ("Bob", 25,
#                                       "Designer"), ("Charlie", 35, "Manager")]
# names = list(map(lambda x: (x[0], x[1]), people))
# print(names)

# ----------------------------------------------------------------------
# Exercise AL4: Complex Filter Condition
# 1. Create a list: words = ["apple", "application", "apricot", "banana", "avocado"]
# 2. Use filter() to get words that:
#    - Start with 'a' AND
#    - Have more than 5 letters
# 3. Convert to list and print
#
# Expected: ['application', 'apricot', 'avocado']

# Write your code for Exercise AL4 below:

# words = ["apple", "application", "apricot", "banana", "avocado"]
# a_five = list(filter(lambda x: x[0] == "a" and len(x) > 5, words))

# ----------------------------------------------------------------------
# Exercise AL5: Sort by Multiple Criteria - Descending and Ascending
# 1. Create a list: scores = [("Alice", 85, 20), ("Bob", 92, 18), ("Charlie", 85, 22), ("David", 92, 19)]
#    Format: (name, score, age)
# 2. Sort by score (highest first), then by age (youngest first)
# 3. Print the sorted list
#
# Expected: [('Bob', 92, 18), ('David', 92, 19), ('Alice', 85, 20), ('Charlie', 85, 22)]

# Write your code for Exercise AL5 below:

# scores = [("Alice", 85, 20), ("Bob", 92, 18),
#           ("Charlie", 85, 22), ("David", 92, 19)]
# scores.sort(key=lambda x: (-x[1], x[2]))
# print(scores)

# ----------------------------------------------------------------------
# Exercise AL6: Lambda with Dictionary Values
# 1. Create a dictionary: inventory = {"apple": 50, "banana": 0, "orange": 30, "grape": 0, "mango": 20}
# 2. Use filter() on inventory.items() to get only items with quantity > 0
# 3. Convert back to a dictionary using dict()
# 4. Print the result
#
# Expected: {'apple': 50, 'orange': 30, 'mango': 20}

# Write your code for Exercise AL6 below:

# inventory = {"apple": 50, "banana": 0, "orange": 30, "grape": 0, "mango": 20}
# bigger_than_zero = dict(filter(lambda x: x[1] > 0, inventory.items()))

# ----------------------------------------------------------------------
# Exercise AL7: Map with Index - Enumerate
# 1. Create a list: words = ["python", "is", "awesome"]
# 2. Use map() with lambda on enumerate(words) to create strings: "index: word"
# 3. Convert to list and print
#
# Expected: ['0: python', '1: is', '2: awesome']

# Write your code for Exercise AL7 below:

# words = ["python", "is", "awesome"]
# my_list = list(map(lambda x: x, enumerate(words)))
# print(my_list)

# ----------------------------------------------------------------------
# Exercise AL8: Nested Lambda - Transform Nested Data
# 1. Create a list: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 2. Use map() with a lambda to double each number in each sublist
#    Hint: You'll need map inside map
# 3. Convert outer and inner to lists and print
#
# Expected: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

# Write your code for Exercise AL8 below:

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# double = list(
#     map(lambda lists: list(map(lambda element: element*2, lists)), matrix))
# print(double)

# ----------------------------------------------------------------------
# Exercise AL9: Filter with Complex Dictionary Condition
# 1. Create a list of dictionaries:
#    employees = [
#        {"name": "Alice", "salary": 50000, "department": "IT"},
#        {"name": "Bob", "salary": 60000, "department": "HR"},
#        {"name": "Charlie", "salary": 55000, "department": "IT"},
#        {"name": "David", "salary": 45000, "department": "HR"}
#    ]
# 2. Use filter() to get IT employees with salary > 50000
# 3. Convert to list and print
#
# Expected: [{'name': 'Charlie', 'salary': 55000, 'department': 'IT'}]

# Write your code for Exercise AL9 below:

# employees = [
#     {"name": "Alice", "salary": 50000, "department": "IT"},
#     {"name": "Bob", "salary": 60000, "department": "HR"},
#     {"name": "Charlie", "salary": 55000, "department": "IT"},
#     {"name": "David", "salary": 45000, "department": "HR"}
# ]

# it_fifty = list(filter(lambda person: (
#     person["department"] == "IT" and person["salary"] > 50000), employees))
# print(it_fifty)

# ----------------------------------------------------------------------
# Exercise AL10: Reduce to Calculate Average
# 1. Import reduce from functools
# 2. Create a list: numbers = [10, 20, 30, 40, 50]
# 3. Use reduce() to sum all numbers
# 4. Divide by the length to get average
# 5. Print the average
#
# Expected: 30.0

# Write your code for Exercise AL10 below:

# from functools import reduce
# numbers = [10, 20, 30, 40, 50]
# result = reduce(lambda x, y: (x+y), numbers)
# total = result/len(numbers)
# print(total)

# ----------------------------------------------------------------------
# Exercise AL11: Lambda with zip()
# 1. Create two lists:
#    names = ["Alice", "Bob", "Charlie"]
#    scores = [85, 92, 78]
# 2. Use map() with lambda on zip(names, scores) to create strings: "name: score"
# 3. Convert to list and print
#
# Expected: ['Alice: 85', 'Bob: 92', 'Charlie: 78']

# Write your code for Exercise AL11 below:

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# task = list(map(lambda x: f"{x[0]}: {x[1]}", zip(names, scores)))
# print(task)

# ----------------------------------------------------------------------
# Exercise AL12: Sort Dictionary by Value Length
# 1. Create a dictionary: data = {"a": "apple", "b": "banana", "c": "cat", "d": "dog"}
# 2. Sort the items by the LENGTH of the value (shortest first)
# 3. Convert back to dictionary using dict()
# 4. Print the result
#
# Expected: {'c': 'cat', 'd': 'dog', 'a': 'apple', 'b': 'banana'}

# Write your code for Exercise AL12 below:

# data = {"a": "apple", "b": "banana", "c": "cat", "d": "dog"}

# data_list = list(data.items())

# data_list.sort(key=lambda x: len(x[1]))

# my_dict = dict(data_list)
# print(my_dict)

# ----------------------------------------------------------------------
# Exercise AL13: Filter None Values
# 1. Create a list: data = [1, None, 3, None, 5, 0, None, 7]
# 2. Use filter() with a lambda to remove None values (keep everything else, including 0)
# 3. Convert to list and print
#
# Expected: [1, 3, 5, 0, 7]

# Write your code for Exercise AL13 below:


# ----------------------------------------------------------------------
# Exercise AL14: Map with Multiple Lists using zip()
# 1. Create three lists:
#    a = [1, 2, 3]
#    b = [4, 5, 6]
#    c = [7, 8, 9]
# 2. Use map() with lambda on zip(a, b, c) to sum corresponding elements
# 3. Convert to list and print
#
# Expected: [12, 15, 18]

# Write your code for Exercise AL14 below:


# ----------------------------------------------------------------------
# Exercise AL15: Complex Sorting - Custom Logic
# 1. Create a list: numbers = [15, -3, 42, -8, 23, -15, 7]
# 2. Sort by absolute value (smallest to largest)
# 3. Print the sorted list
#
# Expected: [-3, 7, -8, 15, -15, 23, 42]

# Write your code for Exercise AL15 below:


# ----------------------------------------------------------------------
# Exercise AL16: Reduce with Strings
# 1. Import reduce from functools
# 2. Create a list: words = ["Python", "is", "really", "awesome"]
# 3. Use reduce() to concatenate all words with spaces
# 4. Print the result
#
# Expected: Python is really awesome

# Write your code for Exercise AL16 below:


# ----------------------------------------------------------------------
# Exercise AL17: Filter and Map Chain - Real World
# 1. Create a list of dictionaries:
#    transactions = [
#        {"id": 1, "amount": 100, "status": "completed"},
#        {"id": 2, "amount": 50, "status": "pending"},
#        {"id": 3, "amount": 200, "status": "completed"},
#        {"id": 4, "amount": 75, "status": "failed"}
#    ]
# 2. Filter only "completed" transactions
# 3. Map to get only the amounts
# 4. Convert to list and print
#
# Expected: [100, 200]

# Write your code for Exercise AL17 below:


# ----------------------------------------------------------------------
# Exercise AL18: Sort with Custom Comparison
# 1. Create a list: words = ["apple", "Banana", "cherry", "Date"]
# 2. Sort case-insensitively (all lowercase for comparison)
# 3. Print the sorted list
#
# Expected: ['apple', 'Banana', 'cherry', 'Date']

# Write your code for Exercise AL18 below:


# ----------------------------------------------------------------------
# Exercise AL19: Reduce to Find Longest String
# 1. Import reduce from functools
# 2. Create a list: words = ["hi", "hello", "hey", "goodbye", "greetings"]
# 3. Use reduce() with a lambda to find the longest word
# 4. Print the result
#
# Expected: greetings

# Write your code for Exercise AL19 below:


# ----------------------------------------------------------------------
# Exercise AL20: Comprehensive Challenge
# 1. Create a list of dictionaries:
#    students = [
#        {"name": "Alice", "grades": [85, 90, 78]},
#        {"name": "Bob", "grades": [92, 88, 95]},
#        {"name": "Charlie", "grades": [70, 75, 72]},
#        {"name": "David", "grades": [88, 85, 90]}
#    ]
# 2. Use map() to calculate average grade for each student
# 3. Use filter() to get students with average >= 85
# 4. Use map() to extract just their names
# 5. Convert to list and print
#
# Expected: ['Alice', 'Bob', 'David']

# Write your code for Exercise AL20 below:


# ============================================================================
# END OF ADVANCED LAMBDA PRACTICE
# ============================================================================
