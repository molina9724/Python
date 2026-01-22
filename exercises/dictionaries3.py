# Exercise B1: Warm-Up - Double All Values
# 1. Create a dictionary: prices = {"apple": 2.50, "banana": 1.00, "orange": 3.00}
# 2. Create a NEW dictionary where all prices are doubled
#    Use a dictionary comprehension
# 3. Print both dictionaries
#
# Expected output:
# Original: {'apple': 2.5, 'banana': 1.0, 'orange': 3.0}
# Doubled: {'apple': 5.0, 'banana': 2.0, 'orange': 6.0}

# Write your code for Exercise B1 below:

# prices = {"apple": 2.50, "banana": 1.00, "orange": 3.00}
# double = {key: value*2 for key, value in prices.items()}

# print(prices)
# print(double)

# ----------------------------------------------------------------------
# Exercise B2: Using .get() in Comprehension
# 1. Create two dictionaries:
#    stock = {"apple": 50, "banana": 30, "orange": 20}
#    sold = {"apple": 10, "banana": 5, "grape": 3}
# 2. Create a NEW dictionary showing remaining stock
#    Use a dictionary comprehension with .get()
#    Only include items that are IN stock (ignore grape)
# 3. Print the result
#
# Expected: {'apple': 40, 'banana': 25, 'orange': 20}

# Write your code for Exercise B2 below:

# stock = {"apple": 50, "banana": 30, "orange": 20}
# sold = {"apple": 10, "banana": 5, "grape": 3}

# remaining = {key: stock.get(key) - sold.get(key, 0) for key in stock.keys()}
# print(remaining)

# ----------------------------------------------------------------------
# Exercise B3: Filter and Transform
# 1. Create a dictionary: temps = {"Mon": 72, "Tue": 85, "Wed": 68, "Thu": 90, "Fri": 78}
# 2. Create a NEW dictionary with:
#    - Only days where temp >= 75
#    - Convert Fahrenheit to Celsius: (F - 32) * 5/9
# 3. Print the result with temperatures rounded to 1 decimal
#
# Expected: {'Tue': 29.4, 'Thu': 32.2, 'Fri': 25.6}

# Write your code for Exercise B3 below:

# temps = {"Mon": 72, "Tue": 85, "Wed": 68, "Thu": 90, "Fri": 78}

# only_high = {key: (value-32)*5/9 for key,
#              value in temps.items() if value >= 75}

# for day, temp in only_high.items():
#     print(f"{day} - {temp:.1f}")

# ----------------------------------------------------------------------
# Exercise B4: .setdefault() Practice
# 1. Create a list of tuples:
#    purchases = [("Alice", "apple"), ("Bob", "banana"), ("Alice", "orange"),
#                 ("Charlie", "apple"), ("Bob", "apple")]
# 2. Create a dictionary where:
#    - Keys are customer names
#    - Values are LISTS of items they bought
#    Use .setdefault() in a loop (NOT comprehension)
# 3. Print the result
#
# Expected: {'Alice': ['apple', 'orange'], 'Bob': ['banana', 'apple'],
#            'Charlie': ['apple']}

# Write your code for Exercise B4 below:

# purchases = [("Alice", "apple"), ("Bob", "banana"), ("Alice", "orange"),
#              ("Charlie", "apple"), ("Bob", "apple")]

# my_dic = {}
# for person, fruit in purchases:
#     # if person not in my_dic:
#     #     my_dic[person] = [fruit]
#     # else:
#     #     my_dic[person].append(fruit)

#     my_dic.setdefault(person, []).append(fruit)


# print(my_dic)

# ----------------------------------------------------------------------
# Exercise B5: Combining with .get()
# 1. Create two dictionaries:
#    week1 = {"apples": 20, "bananas": 15, "oranges": 10}
#    week2 = {"apples": 15, "bananas": 10, "grapes": 5}
# 2. Create a NEW dictionary with TOTAL sales (add the values)
#    Use a dictionary comprehension
#    Include ALL items from both dictionaries
# 3. Print the result
#
# Expected: {'apples': 35, 'bananas': 25, 'oranges': 10, 'grapes': 5}

# Write your code for Exercise B5 below:

# week1 = {"apples": 20, "bananas": 15, "oranges": 10}
# week2 = {"apples": 15, "bananas": 10, "grapes": 5}

# all_keys = week1 | week2

# total = {key: week1.get(key, 0) + week2.get(key, 0)
#          for key in all_keys.keys()}

# ----------------------------------------------------------------------
# Exercise B6: Transform Keys
# 1. Create a dictionary: grades = {"alice": 85, "bob": 92, "charlie": 78}
# 2. Create a NEW dictionary where:
#    - Keys are capitalized (first letter uppercase)
#    - Values stay the same
# 3. Print the result
#
# Expected: {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Write your code for Exercise B6 below:

# grades = {"alice": 85, "bob": 92, "charlie": 78}
# names_list = {name.title(): grade for name, grade in grades.items()}

# ----------------------------------------------------------------------
# Exercise B7: Nested Comprehension
# 1. Create a dictionary:
#    students = {"Alice": [85, 90, 78], "Bob": [92, 88, 95], "Charlie": [78, 82, 80]}
# 2. Create a NEW dictionary where:
#    - Keys are student names
#    - Values are their HIGHEST grade (use max())
# 3. Print the result
#
# Expected: {'Alice': 90, 'Bob': 95, 'Charlie': 82}

# Write your code for Exercise B7 below:

# students = {"Alice": [85, 90, 78], "Bob": [92, 88, 95], "Charlie": [78, 82, 80]}
# highest = {key: max(grades) for key,grades in students.items()}

# ----------------------------------------------------------------------
# Exercise B8: Multiple Conditions
# 1. Create a dictionary:
#    products = {"apple": 2.50, "banana": 1.00, "orange": 3.00, "grape": 4.50, "mango": 5.00}
# 2. Create a NEW dictionary with:
#    - Only items that cost between $2.00 and $4.00 (inclusive)
#    - Apply a 10% discount to those items
# 3. Print the result
#
# Expected: {'apple': 2.25, 'orange': 2.7}

# Write your code for Exercise B8 below:

# products = {"apple": 2.50, "banana": 1.00,
#             "orange": 3.00, "grape": 4.50, "mango": 5.00}
# new_dic = {key: price*0.9 for key, price in products.items() if price >=
#            2 and price <= 4}

# ----------------------------------------------------------------------
# Exercise B9: Swap Keys and Values
# 1. Create a dictionary: codes = {"A": 1, "B": 2, "C": 3}
# 2. Create a NEW dictionary where keys and values are swapped
#    Use a dictionary comprehension
# 3. Print the result
#
# Expected: {1: 'A', 2: 'B', 3: 'C'}

# Write your code for Exercise B9 below:

# codes = {"A": 1, "B": 2, "C": 3}
# inverted = {value: key for key, value in codes.items()}

# ----------------------------------------------------------------------
# Exercise B10: Complex Grouping with Comprehension
# 1. Create a list of tuples:
#    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 85), ("Eve", 92)]
# 2. Create a dictionary where:
#    - Keys are the scores
#    - Values are LISTS of names with that score
#    Use a dictionary comprehension (challenge!)
# 3. Print the result
#
# Expected: {85: ['Alice', 'David'], 92: ['Bob', 'Eve'], 78: ['Charlie']}

# Write your code for Exercise B10 below:

# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78),
#           ("David", 85), ("Eve", 92)]

# my_dic = {}
# for name, score in scores:
#     my_dic.setdefault(score, []).append(name)