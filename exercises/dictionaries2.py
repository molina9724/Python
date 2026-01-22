# ======================================================================
# DICTIONARY EXERCISES - PROGRESSIVE DIFFICULTY
# ======================================================================

# ----------------------------------------------------------------------
# SECTION 1: BASIC DICTIONARY OPERATIONS (Warm-up)
# ----------------------------------------------------------------------

# Exercise 1: Creating and Accessing Dictionaries
#
# 1. Create a dictionary called 'book' with keys: "title", "author", "year", "pages"
#    Use any values you want
# 2. Print the entire dictionary
# 3. Access and print the "title"
# 4. Access and print the "year"
# 5. Try to access a key that doesn't exist using .get() with a default value
#
# Write your code for Exercise 1 below:

# book = {"title": "1984", "author": "George Orwell",
#         "year": 1948, "pages": 120}

# print(book)
# print(book["title"])
# print(book["year"])

# print(book.get("coauthor", "No coauthor this time"))

# ----------------------------------------------------------------------
# Exercise 2: Adding and Modifying Items
#
# 1. Create a dictionary: prices = {"apple": 1.50, "banana": 0.75}
# 2. Print the original dictionary
# 3. Add a new item: "orange" with price 2.00
# 4. Modify the price of "apple" to 1.75
# 5. Print the updated dictionary
#
# Write your code for Exercise 2 below:

# prices = {"apple": 1.50, "banana": 0.75}
# print(prices)
# prices["oranges"] = 2.00
# prices["apple"] = 1.75

# print(prices)


# ----------------------------------------------------------------------
# Exercise 3: Removing Items
#
# 1. Create a dictionary: stock = {"apples": 50, "bananas": 30, "oranges": 20, "grapes": 15}
# 2. Remove "bananas" using del
# 3. Remove "oranges" using .pop() and print the removed value
# 4. Print the final dictionary
#
# Write your code for Exercise 3 below:

# stock = {"apples": 50, "bananas": 30, "oranges": 20, "grapes": 15}

# del stock["bananas"]
# removed = stock.pop("oranges")
# print(removed)
# print(stock)

# ----------------------------------------------------------------------
# SECTION 2: DICTIONARY METHODS (Building Understanding)
# ----------------------------------------------------------------------

# Exercise 4: Using .keys(), .values(), .items()
#
# 1. Create a dictionary: grades = {"Math": 85, "English": 92, "Science": 78, "History": 88}
# 2. Get all the keys and print them
# 3. Get all the values and print them
# 4. Get all the items (key-value pairs) and print them
# 5. Convert the keys to a list and print it
# 6. Convert the values to a list and print it
#
# Write your code for Exercise 4 below:

# grades = {"Math": 85, "English": 92, "Science": 78, "History": 88}

# print(grades.keys())
# print(grades.values())
# print(grades.items())

# key_list = list(grades.keys())
# print(key_list)
# value_list = list(grades.values())
# print(value_list)

# ----------------------------------------------------------------------
# Exercise 5: Simple Iteration
#
# 1. Create a dictionary: temperatures = {"Monday": 72, "Tuesday": 75, "Wednesday": 68, "Thursday": 70}
# 2. Loop through and print each KEY only
# 3. Loop through and print each VALUE only (use .values())
# 4. Loop through and print each key-value pair in format: "Monday: 72"
#
# Write your code for Exercise 5 below:

# temperatures = {"Monday": 72, "Tuesday": 75, "Wednesday": 68, "Thursday": 70}

# for key in temperatures:
#     print(key)

# for value in temperatures.values():
#     print(value)

# for key, value in temperatures.items():
#     print(f"{key}: {value}")

# ----------------------------------------------------------------------
# Exercise 6: Membership Testing
#
# 1. Create a dictionary: menu = {"burger": 8.99, "pizza": 12.99, "salad": 6.99}
# 2. Check if "burger" is in the dictionary (print True or False)
# 3. Check if "taco" is in the dictionary (print True or False)
# 4. Check if the price 12.99 is in the VALUES (print True or False)
# 5. Use an if statement to safely print the price of "burger" only if it exists
#
# Write your code for Exercise 6 below:

# menu = {"burger": 8.99, "pizza": 12.99, "salad": 6.99}
# print("burger" in menu)
# print("taco" in menu)
# print(12.99 in menu.values())

# if "burger" in menu:
#     print(menu["burger"])

# ----------------------------------------------------------------------
# SECTION 3: WORKING WITH DICTIONARY VALUES (Gradual Complexity)
# ----------------------------------------------------------------------

# Exercise 7: Dictionaries with List Values
#
# 1. Create a dictionary where values are lists:
#    student = {"name": "Alex", "grades": [85, 90, 78, 92], "subjects": ["Math", "English", "Science", "History"]}
# 2. Print the student's name
# 3. Print all the grades
# 4. Print the first grade (index 0)
# 5. Print the last subject (index -1)
# 6. Add a new grade (88) to the grades list
# 7. Print the updated dictionary
#
# Write your code for Exercise 7 below:

# student = {"name": "Alex", "grades": [85, 90, 78, 92], "subjects": [
#     "Math", "English", "Science", "History"]}
# print(student["name"])
# print(student["grades"])
# print(student["grades"][0])
# print(student["subjects"][-1])

# student["grades"].append(88)
# print(student)

# ----------------------------------------------------------------------
# Exercise 8: Simple Nested Dictionary (One Level)
#
# 1. Create a nested dictionary:
#    person = {
#        "name": "Sarah",
#        "age": 28,
#        "address": {"street": "123 Main St", "city": "Boston", "zip": "02101"}
#    }
# 2. Print the person's name
# 3. Print the person's age
# 4. Print the entire address dictionary
# 5. Print just the city from the address
# 6. Print just the zip code from the address
#
# Write your code for Exercise 8 below:

# person = {"name": "Sarah",
#           "age": 28,
#           "address": {"street": "123 Main St", "city": "Boston", "zip": "02101"}}

# print(person["name"])
# print(person["age"])
# print(person["address"])
# print(person["address"]["city"])
# print(person["address"]["zip"])


# ----------------------------------------------------------------------
# Exercise 9: Modifying Nested Values
#
# 1. Create the same nested dictionary from Exercise 8
# 2. Change the person's age to 29
# 3. Change the city to "Cambridge"
# 4. Add a new key "state" with value "MA" to the address dictionary
# 5. Print the entire updated dictionary
#
# Write your code for Exercise 9 below:

# person = {
#     "name": "Sarah",
#     "age": 28,
#     "address": {"street": "123 Main St", "city": "Boston", "zip": "02101"}
# }

# person["age"] = 29
# person["address"]["city"] = "Cambridge"
# person["address"]["state"] = "MA"

# print(person)

# ----------------------------------------------------------------------
# SECTION 4: COUNTING PATTERNS (Building the Skill)
# ----------------------------------------------------------------------

# Exercise 10: Manual Counting - Method 1 (if/else)
#
# 1. Create a list: colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
# 2. Create an empty dictionary called color_counts
# 3. Loop through the colors list
# 4. For each color, check if it's already in color_counts:
#    - If NOT in dictionary: set its count to 1
#    - If already in dictionary: add 1 to its count
# 5. Print the final counts
#
# Write your code for Exercise 10 below:

# colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
# color_counts = {}

# for color in colors:
#     if color not in color_counts:
#         color_counts[color] = 1
#     else:
#         color_counts[color] += 1

# print(color_counts)

# ----------------------------------------------------------------------
# Exercise 11: Manual Counting - Method 2 (.get())
#
# 1. Create the same list: colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
# 2. Create an empty dictionary called color_counts
# 3. Loop through the colors list
# 4. For each color, use .get() to get current count (default 0), then add 1
# 5. Print the final counts
# 6. Compare: is the result the same as Exercise 10?
#
# Write your code for Exercise 11 below:

# colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
# color_counts = {}

# for color in colors:
#     color_counts[color] = color_counts.get(color, 0) + 1

# print(color_counts)

# ----------------------------------------------------------------------
# Exercise 12: Manual Counting - Method 3 (.setdefault())
#
# 1. Create the same list: colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
# 2. Create an empty dictionary called color_counts
# 3. Loop through the colors list
# 4. For each color:
#    - Use .setdefault() to ensure it exists with value 0
#    - Then add 1 to it
# 5. Print the final counts
# 6. Compare: is the result the same as Exercises 10 and 11?
#
# Write your code for Exercise 12 below:

# colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
# color_counts = {}

# for color in colors:
#     color_counts.setdefault(color, 0)
#     color_counts[color] += 1

# print(color_counts)

# ----------------------------------------------------------------------
# SECTION 5: DICTIONARY COMPREHENSIONS (Gradual Introduction)
# ----------------------------------------------------------------------

# Exercise 13: Simple Dictionary Comprehension
#
# 1. Create a dictionary of numbers 1-5 and their squares using a comprehension:
#    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# 2. Print the dictionary
# 3. Create a dictionary of numbers 1-10 and their cubes (x**3)
# 4. Print that dictionary
#
# Write your code for Exercise 13 below:

# square = {x: x**2 for x in range(1, 6)}
# print(square)

# cubes = {x: x**3 for x in range(1, 11)}
# print(cubes)

# ----------------------------------------------------------------------
# Exercise 14: Dictionary Comprehension from a List
#
# 1. Create a list: words = ["cat", "elephant", "dog", "butterfly"]
# 2. Create a dictionary where:
#    - Keys are the words
#    - Values are the length of each word
#    Use a dictionary comprehension
# 3. Print the dictionary
#
# Write your code for Exercise 14 below:

# words = ["cat", "elephant", "dog", "butterfly"]
# my_dic = {word: len(word) for word in words}
# print(my_dic)

# ----------------------------------------------------------------------
# Exercise 15: Dictionary Comprehension with Condition
#
# 1. Create a dictionary of numbers 1-10 and their squares (like Exercise 13)
# 2. But ONLY include even numbers
#    Result should be: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# 3. Print the dictionary
#
# Write your code for Exercise 15 below:

# my_dic = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# print(my_dic)

# ----------------------------------------------------------------------
# Exercise 16: Transforming an Existing Dictionary
#
# 1. Create a dictionary: prices = {"apple": 2.00, "banana": 1.50, "orange": 3.00}
# 2. Create a NEW dictionary with a 10% discount (multiply by 0.9)
#    Use a dictionary comprehension with .items()
# 3. Print both the original and discounted dictionaries
#
# Write your code for Exercise 16 below:

# prices = {"apple": 2.00, "banana": 1.50, "orange": 3.00}
# ten_discount = {fruit: price*0.9 for fruit, price in prices.items()}

# print(prices)
# print(ten_discount)

# ----------------------------------------------------------------------
# SECTION 6: COMBINING CONCEPTS (Slightly More Complex)
# ----------------------------------------------------------------------

# Exercise 17: Filtering a Dictionary
#
# 1. Create a dictionary: scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}
# 2. Create a NEW dictionary with only scores >= 90
#    Use a dictionary comprehension with an if condition
# 3. Print the filtered dictionary
# 4. Print how many students scored >= 90 (use len())
#
# Write your code for Exercise 17 below:

# scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}
# only_high = {key: value for key, value in scores.items() if value >= 90}
# print(only_high)
# print(len(only_high))

# ----------------------------------------------------------------------
# Exercise 18: Combining Two Lists into a Dictionary
#
# 1. Create two lists:
#    names = ["Alice", "Bob", "Charlie"]
#    ages = [25, 30, 35]
# 2. Combine them into a dictionary using zip() and dict()
# 3. Print the dictionary
# 4. Now do the same thing using a dictionary comprehension with zip()
# 5. Print that dictionary (should be the same)
#
# Write your code for Exercise 18 below:

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]

# mixed = dict(zip(names, ages))
# print(type(mixed))

# mixed2 = {key: value for key, value in zip(names, ages)}
# print(mixed)
# print(mixed2)

# ----------------------------------------------------------------------
# Exercise 19: Grouping Data (Practical Example)
#
# 1. Create a list of tuples: students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("David", "C"), ("Eve", "B")]
#    Each tuple is (name, grade)
# 2. Create an empty dictionary called grade_groups
# 3. Loop through the students list
# 4. For each student:
#    - Get the grade (second item in tuple)
#    - If grade not in dictionary, create an empty list for it
#    - Append the student's name to that grade's list
# 5. Print the final dictionary
#    Should look like: {"A": ["Alice", "Charlie"], "B": ["Bob", "Eve"], "C": ["David"]}
#
# Write your code for Exercise 19 below:

# ----------------------------------------------------------------------
# Exercise 20: Word Frequency Counter
#
# 1. Create a string: text = "the cat and the dog and the bird"
# 2. Split it into words using .split()
# 3. Count how many times each word appears (use any counting method you prefer)
# 4. Print the word counts
# 5. Find and print the most common word (the one with highest count)
#    Hint: You can use max() with .values() to find the highest count,
#          then loop to find which key has that count
#
# Write your code for Exercise 20 below:

# ----------------------------------------------------------------------
# SECTION 7: CHALLENGE EXERCISES (Putting It All Together)
# ----------------------------------------------------------------------

# Exercise 21: Inventory Management
#
# 1. Create a dictionary: inventory = {"apples": 50, "bananas": 30, "oranges": 20}
# 2. Create a dictionary: sales = {"apples": 15, "bananas": 10, "grapes": 5}
# 3. Update the inventory by subtracting the sales
#    - For items in both dictionaries, subtract the sale amount
#    - For items only in sales (like grapes), ignore them (can't sell what you don't have)
# 4. Print the updated inventory
# 5. Add a new item "grapes": 25 to inventory
# 6. Print the final inventory
#
# Write your code for Exercise 21 below:

# ----------------------------------------------------------------------
# Exercise 22: Student Grade Statistics
#
# 1. Create a dictionary: students = {
#        "Alice": [85, 90, 78],
#        "Bob": [92, 88, 95],
#        "Charlie": [78, 82, 80]
#    }
# 2. For each student, calculate and print their average grade
#    Format: "Alice: 84.33"
# 3. Create a NEW dictionary where:
#    - Keys are student names
#    - Values are their average grades
# 4. Print this new dictionary
# 5. Find and print the student with the highest average
#
# Write your code for Exercise 22 below:

# ----------------------------------------------------------------------
# Exercise 23: Merging Dictionaries with Conflict Resolution
#
# 1. Create two dictionaries:
#    dict1 = {"a": 1, "b": 2, "c": 3}
#    dict2 = {"b": 20, "c": 30, "d": 4}
# 2. Merge them using the | operator (dict2 values win for conflicts)
# 3. Print the merged dictionary
# 4. Now merge them the opposite way (dict1 values win)
# 5. Print that merged dictionary
# 6. Compare: what's different?
#
# Write your code for Exercise 23 below:

# ----------------------------------------------------------------------
# Exercise 24: Building a Phone Book
#
# 1. Create an empty dictionary called phonebook
# 2. Add these entries:
#    "Alice": "555-1234"
#    "Bob": "555-5678"
#    "Charlie": "555-9012"
# 3. Print the entire phonebook
# 4. Look up and print Bob's number
# 5. Try to look up "David" using .get() with default "Not found"
# 6. Update Alice's number to "555-0000"
# 7. Remove Charlie from the phonebook
# 8. Print the final phonebook
#
# Write your code for Exercise 24 below:

# ----------------------------------------------------------------------
# Exercise 25: Advanced Counting - Letter Frequency
#
# 1. Create a string: text = "hello world"
# 2. Create an empty dictionary called letter_counts
# 3. Loop through each character in the string
# 4. Count each letter (skip spaces)
# 5. Print the letter counts
# 6. Find and print the most common letter
# 7. BONUS: Convert all letters to lowercase first so 'H' and 'h' count as the same
#
# Write your code for Exercise 25 below:

# ======================================================================
# END OF EXERCISES
# ======================================================================
#
# Tips for success:
# - Start from Exercise 1 and work your way through
# - Don't skip exercises - each builds on previous concepts
# - If you get stuck, try to break the problem into smaller steps
# - Test your code frequently with print statements
# - Compare similar exercises (like 10, 11, 12) to see different approaches
#
# You've got this! 🚀
# ======================================================================
