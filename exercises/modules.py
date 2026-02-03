# ======================================================================
# 🐍 PYTHON MODULES - PRACTICE EXERCISES
# ======================================================================
# Topic: Importing and Using Modules
# Instructions: Complete each exercise, then uncomment tests to verify
# ======================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Basic Import and Use
# 1. Import the 'math' module
# 2. Create a function get_square_root(number)
# 3. Use math.sqrt() to calculate the square root
# 4. Return the result
#
# Test: get_square_root(144) -> 12.0
# Test: get_square_root(25) -> 5.0
# Test: get_square_root(2) -> 1.4142135623730951
# Edge: get_square_root(0) -> 0.0
# Edge: get_square_root(1) -> 1.0
# ----------------------------------------------------------------------

# Write your code below:

# import math


# def get_square_root(number):
#     return math.sqrt(number)


# # Test your solution:
# print("🟢 get_square_root(144):", get_square_root(144))  # -> 12.0
# print("🟢 get_square_root(25):", get_square_root(25))    # -> 5.0
# print("🟢 get_square_root(2):", get_square_root(2))      # -> 1.4142...
# print("🟢 get_square_root(0):", get_square_root(0))      # -> 0.0
# print("🟢 get_square_root(1):", get_square_root(1))      # -> 1.0


# ----------------------------------------------------------------------
# 🟢 EASY 2: Import with Alias
# 1. Import the 'datetime' module with alias 'dt'
# 2. Create a function get_current_year()
# 3. Use dt.date.today() to get today's date
# 4. Return the year from that date using .year attribute
#
# Test: get_current_year() -> 2025 (or current year)
# ----------------------------------------------------------------------

# Write your code below:

# import datetime as dt
# def get_current_year():
#     return dt.date.today()

# Test your solution:
# print("🟢 get_current_year():", get_current_year())  # -> 2025


# ----------------------------------------------------------------------
# 🟢 EASY 3: From Import Syntax
# 1. From the 'random' module, import only 'randint'
# 2. Create a function roll_dice()
# 3. Use randint(1, 6) to simulate a dice roll
# 4. Return the result
#
# Test: roll_dice() -> number between 1 and 6
# Note: Result will vary each time (it's random!)
# ----------------------------------------------------------------------

# Write your code below:

# from random import randint

# def roll_dice():
#     return randint(1,6)

# Test your solution:
# print("🟢 roll_dice():", roll_dice())  # -> 1-6
# print("🟢 roll_dice():", roll_dice())  # -> 1-6
# print("🟢 roll_dice():", roll_dice())  # -> 1-6


# ----------------------------------------------------------------------
# 🟢 EASY 4: Import Multiple Items
# 1. From the 'math' module, import 'pi' and 'ceil' in ONE line
# 2. Create a function circle_area_rounded(radius)
# 3. Calculate area using: pi * radius ** 2
# 4. Use ceil() to round UP to nearest integer
# 5. Return the rounded result
#
# Test: circle_area_rounded(5) -> 79
# Test: circle_area_rounded(1) -> 4
# Test: circle_area_rounded(2.5) -> 20
# Edge: circle_area_rounded(0) -> 0
# ----------------------------------------------------------------------

# Write your code below:

# from math import pi
# from math import ceil

# def circle_area_rounded(radius):
#     return ceil(pi*radius**2)

# Test your solution:
# print("🟢 circle_area_rounded(5):", circle_area_rounded(5))      # -> 79
# print("🟢 circle_area_rounded(1):", circle_area_rounded(1))      # -> 4
# print("🟢 circle_area_rounded(2.5):", circle_area_rounded(2.5))  # -> 20
# print("🟢 circle_area_rounded(0):", circle_area_rounded(0))      # -> 0


# ----------------------------------------------------------------------
# 🟡 MEDIUM 1: Working with Multiple Modules
# 1. Import 'math' module
# 2. Import 'random' module
# 3. Create a function random_circle_area()
# 4. Generate random radius between 1 and 10 using random.randint()
# 5. Calculate area using math.pi * radius ** 2
# 6. Return a tuple: (radius, area)
#
# Test: random_circle_area() -> (radius, area) where radius is 1-10
# Note: Results will vary (random radius)
# ----------------------------------------------------------------------

# Write your code below:

# import math
# import random

# def random_circle_area():
#     return math.pi*random.randint(1,10)**2

# Test your solution:
# print("🟡 random_circle_area():", random_circle_area())
# print("🟡 random_circle_area():", random_circle_area())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 2: Using the os.path Module
# 1. From 'os.path' import 'basename' and 'splitext'
# 2. Create a function get_file_info(filepath)
# 3. Use basename() to get just the filename from a path
# 4. Use splitext() to separate name and extension
# 5. Return a dictionary: {"name": name, "extension": extension}
#
# Test: get_file_info("/home/user/document.txt")
#       -> {"name": "document", "extension": ".txt"}
# Test: get_file_info("image.png")
#       -> {"name": "image", "extension": ".png"}
# Test: get_file_info("/folder/script.py")
#       -> {"name": "script", "extension": ".py"}
# Edge: get_file_info("noextension")
#       -> {"name": "noextension", "extension": ""}
# ----------------------------------------------------------------------

# Write your code below:

# from os.path import basename
# from os.path import splitext


# def get_file_info(filepath):
#     filename = basename(filepath)
#     name, extension = splitext(filename)
#     return {"name": name, "extension": extension}


# # Test your solution:
# print("🟡 get_file_info('/home/user/document.txt'):",
#       get_file_info("/home/user/document.txt"))
# print("🟡 get_file_info('image.png'):", get_file_info("image.png"))
# print("🟡 get_file_info('/folder/script.py'):",
#       get_file_info("/folder/script.py"))
# print("🟡 get_file_info('noextension'):", get_file_info("noextension"))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 3: Date Formatting with datetime
# 1. Import 'datetime' from the 'datetime' module
# 2. Create a function format_date(year, month, day)
# 3. Create a datetime object using datetime(year, month, day)
# 4. Return the date formatted as "Day, Month DD, YYYY"
#    Hint: use .strftime("%A, %B %d, %Y")
#
# Test: format_date(2025, 1, 15) -> "Wednesday, January 15, 2025"
# Test: format_date(2000, 12, 25) -> "Monday, December 25, 2000"
# Test: format_date(1999, 7, 4) -> "Sunday, July 04, 1999"
# ----------------------------------------------------------------------


# Write your code below:

# from datetime import datetime


# def format_date(year, month, day):
#     old_format = datetime(year, month, day)
#     new_format = old_format.strftime("%A, %B %d, %Y %")
#     return new_format


# # Test your solution:
# print("🟡 format_date(2025, 1, 15):", format_date(2025, 1, 15))
# print("🟡 format_date(2000, 12, 25):", format_date(2000, 12, 25))
# print("🟡 format_date(1999, 7, 4):", format_date(1999, 7, 4))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: String Module Constants
# 1. Import 'string' module
# 2. Create a function analyze_text(text)
# 3. Count how many characters are:
#    - letters (use string.ascii_letters)
#    - digits (use string.digits)
#    - punctuation (use string.punctuation)
# 4. Return a dictionary with the counts
#
# Test: analyze_text("Hello, World! 123")
#       -> {"letters": 10, "digits": 3, "punctuation": 2}
# Test: analyze_text("abc")
#       -> {"letters": 3, "digits": 0, "punctuation": 0}
# Test: analyze_text("!@#")
#       -> {"letters": 0, "digits": 0, "punctuation": 3}
# Edge: analyze_text("")
#       -> {"letters": 0, "digits": 0, "punctuation": 0}
# ----------------------------------------------------------------------

# Write your code below:

# import string


# def analyze_text(text):
#     letters = 0
#     digits = 0
#     punctuation = 0
#     for char in text:
#         if char in string.ascii_letters:
#             letters += 1
#         elif char in string.digits:
#             digits += 1
#         elif char in string.punctuation:
#             punctuation += 1
#     info = {"letters": letters, "digits": digits, "punctuation": punctuation}
#     return info


# # Test your solution:
# print("🟡 analyze_text('Hello, World! 123'):",
#       analyze_text("Hello, World! 123"))
# print("🟡 analyze_text('abc'):", analyze_text("abc"))
# print("🟡 analyze_text('!@#'):", analyze_text("!@#"))
# print("🟡 analyze_text(''):", analyze_text(""))


# ----------------------------------------------------------------------
# 🔴 HARD 1: Password Generator Using Multiple Modules
# 1. Import 'string' module
# 2. Import 'random' module
# 3. Create a function generate_password(length)
# 4. Password must contain at least:
#    - 1 uppercase letter (string.ascii_uppercase)
#    - 1 lowercase letter (string.ascii_lowercase)
#    - 1 digit (string.digits)
#    - 1 special character (string.punctuation)
# 5. Fill remaining length with random chars from all categories
# 6. Shuffle the password and return as string
#
# Test: generate_password(8) -> 8-char password with all requirements
# Test: generate_password(12) -> 12-char password with all requirements
# Test: len(generate_password(10)) -> 10
# Edge: generate_password(4) -> minimum valid password
# Validation: Password should contain mixed characters
# ----------------------------------------------------------------------

# Write your code below:

# import string
# import random


# def generate_password(length):
#     uppercase = random.choice(string.ascii_uppercase)
#     lowercase = random.choice(string.ascii_lowercase)
#     digit = random.choice(string.digits)
#     special = random.choice(string.punctuation)

#     password_list = [uppercase, lowercase, digit, special]

#     all_chars = string.ascii_letters + string.digits + string.punctuation

#     for _ in range(length - 4):
#         password_list.append(random.choice(all_chars))

#     random.shuffle(password_list)

#     return "".join(password_list)


# Test your solution:
# print("🔴 generate_password(8):", generate_password(8))
# print("🔴 generate_password(12):", generate_password(12))
# print("🔴 len(generate_password(10)):", len(generate_password(10)))  # -> 10


# ----------------------------------------------------------------------
# 🔴 HARD 2: Statistics Calculator
# 1. From 'statistics' import: mean, median, mode, stdev
# 2. Create a function calculate_stats(numbers)
# 3. Return a dictionary with:
#    - "mean": average of numbers
#    - "median": middle value
#    - "mode": most common value (handle StatisticsError if no mode)
#    - "std_dev": standard deviation (only if len > 1, else None)
#    - "range": max - min
#
# Test: calculate_stats([1, 2, 2, 3, 4])
#       -> {"mean": 2.4, "median": 2, "mode": 2, "std_dev": ~1.14, "range": 3}
# Test: calculate_stats([5, 5, 5])
#       -> {"mean": 5, "median": 5, "mode": 5, "std_dev": 0.0, "range": 0}
# Edge: calculate_stats([10])
#       -> {"mean": 10, "median": 10, "mode": 10, "std_dev": None, "range": 0}
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 calculate_stats([1, 2, 2, 3, 4]):", calculate_stats([1, 2, 2, 3, 4]))
# print("🔴 calculate_stats([5, 5, 5]):", calculate_stats([5, 5, 5]))
# print("🔴 calculate_stats([10]):", calculate_stats([10]))


# ----------------------------------------------------------------------
# 🔴 HARD 3: File Path Builder (Cross-Platform)
# 1. Import 'os' module
# 2. Create a function build_path(*parts)
# 3. Use os.path.join() to combine all path parts
# 4. Use os.path.normpath() to normalize the path
# 5. Return a dictionary with:
#    - "full_path": the complete normalized path
#    - "directory": just the directory (os.path.dirname)
#    - "filename": just the filename (os.path.basename)
#    - "exists": whether the path exists (os.path.exists)
#
# Test: build_path("home", "user", "documents", "file.txt")
#       -> {"full_path": "home/user/documents/file.txt", ...}
# Test: build_path(".", "data", "test.csv")
#       -> {"full_path": "data/test.csv", ...}
# Note: Path separator may vary by OS (/ or \)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 build_path('home', 'user', 'documents', 'file.txt'):")
# print("  ", build_path("home", "user", "documents", "file.txt"))
# print("🔴 build_path('.', 'data', 'test.csv'):")
# print("  ", build_path(".", "data", "test.csv"))


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# 🟢 EASY (4):    Basic import, alias, from import, multiple imports
# 🟡 MEDIUM (4):  Multiple modules, os.path, datetime, string
# 🔴 HARD (3):    Password generator, statistics, path builder
#
# Modules You'll Practice:
# - math          - datetime       - random
# - os / os.path  - string         - statistics
# ======================================================================
