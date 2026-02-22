# ======================================================================
# 🐍 CHAPTER 9: TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS
# ======================================================================
# Based on: Automate the Boring Stuff with Python, 3rd Edition
# Topics: re module, compile, search, findall, sub, groups,
#         character classes, quantifiers, greedy/lazy, anchors
# ======================================================================

import re


# =====================================================================
#                    SECTION 1: BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: First Regex - Find a Phone Number
# Use re.compile() and search() to find a phone number
# in the format XXX-XXX-XXXX
#
# Steps: import re → compile pattern → search → group()
#
# Test: find_phone("Call me at 415-555-1234 tomorrow") -> "415-555-1234"
# Test: find_phone("No number here") -> None
# ----------------------------------------------------------------------

# message = "Call me at 415-555-1234 tomorrow. 415-555-9999 is my office."

# # Write your code below:

# pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
# result = pattern.search(message)

# # Test your solution:
# if result:
#     print("🟢 Found:", result.group())
# else:
#     print("Not found")


# ----------------------------------------------------------------------
# 🟢 EASY 2: Find ALL Phone Numbers
# Use findall() instead of search() to find ALL phone numbers
# in a string, not just the first one
#
# Test: "Call 415-555-1234 or 415-555-9999" -> ['415-555-1234', '415-555-9999']
# ----------------------------------------------------------------------

# message = "Call 415-555-1234 or 415-555-9999. Also try 800-123-4567."

# # Write your code below:

# pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
# results = pattern.findall(message)

# # Test your solution:
# print("🟢 All phones:", results)


# ----------------------------------------------------------------------
# 🟢 EASY 3: Grouping with Parentheses
# Use groups to separate area code from the rest of the number
# Pattern: (XXX)-(XXX-XXXX)
#
# Test: "415-555-1234" -> group(1)="415", group(2)="555-1234"
# ----------------------------------------------------------------------

# phone = "My number is 415-555-1234."

# # Write your code below:

# pattern = re.compile(r"(\d{3})-(\d{3}-\d{4})")
# results = pattern.search(phone)

# area_code = results.group(1)
# number = results.group(2)

# # Test your solution:
# print("🟢 Area code:", area_code)
# print("🟢 Number:", number)


# =====================================================================
#                    SECTION 2: CHARACTER CLASSES & QUANTIFIERS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 4: The Pipe Character - Match Alternatives
# Use the | (pipe) to match either "cat" or "dog" in a string
# search() returns the FIRST match found
#
# Test: "I have a cat and a dog" -> first match is "cat"
# Test: "I have a dog and a cat" -> first match is "dog"
# ----------------------------------------------------------------------

# text1 = "I have a cat and a dog"
# text2 = "I have a dog and a cat"

# # Write your code below:

# pattern = re.compile(r"cat|dog")
# result1 = pattern.search(text1)
# result1 = result1.group()
# result2 = pattern.search(text2)
# result2 = result2.group()

# # Test your solution:
# print("🟢 Text1 first match:", result1)
# print("🟢 Text2 first match:", result2)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 5: Character Classes - Find Vowels and Consonants
# Use character classes to find all vowels and all non-vowels in a string
#
# Test: "RoboCop eats BABY FOOD." ->
#   vowels: ['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']
# ----------------------------------------------------------------------

# text = "RoboCop eats BABY FOOD."

# # Write your code below:

# vowels_pattern = re.compile(r"[aeiouAEIOU]")
# vowels = vowels_pattern.findall(text)

# consonants_pattern = re.compile(r"[^aeiouAEIOU]")
# consonants = consonants_pattern.findall(text)

# # Test your solution:
# print("🟡 Vowels:", vowels)
# print("🟡 Consonants:", consonants)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: Shorthand Classes - Extract Data
# Use shorthand character classes to
# find all "number word" patterns like "12 drummers", "11 pipers"
#
# Test: "12 drummers, 11 pipers, 10 lords" ->
#   ['12 drummers', '11 pipers', '10 lords']
# ----------------------------------------------------------------------

# text = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"

# # Write your code below:

# pattern = re.compile(r"\d{1,2}\s+\w+")
# matches = pattern.findall(text)

# # Test your solution:
# print("🟡 Matches:", matches)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 7: Optional Matching with ?
# Create a regex that matches phone numbers WITH or WITHOUT area code
#
# Test: "415-555-1234" -> match
# Test: "555-1234" -> match
# ----------------------------------------------------------------------

# phone1 = "My number is 415-555-1234"
# phone2 = "My number is 555-1234"

# # Write your code below:

# pattern = re.compile(r"(\d{3}-)?\d{3}-\d{4}")

# match1 = pattern.search(phone1)
# match1 = match1.group()
# match2 = pattern.search(phone2)
# match2 = match2.group()

# # Test your solution:
# print("🟡 With area code:", match1)
# print("🟡 Without area code:", match2)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 8: Quantifiers - Exact, Range, Unlimited
# Practice {n}, {n,m}, *, +
# a) Match exactly 3 digits
# b) Match 3 to 5 "Ha"
# c) Match "Bat" followed by zero or more "man"
# d) Match "Bat" followed by one or more "man"
#
# Test: "HaHaHaHaHa" greedy -> "HaHaHaHaHa" (matches max)
# Test: "HaHaHaHaHa" lazy -> "HaHaHa" (matches min)
# ----------------------------------------------------------------------

# Write your code below:

# pattern_a = re.compile(r"(\d{3})")
# pattern_b = re.compile(r"(Ha){3,5}")
# pattern_c = re.compile(r"Bat(man)*")
# pattern_d = re.compile(r"Bat(man)+")

# # Test your solution:
# print("🟡 a) 3 digits in '12345':", pattern_a.search("12345").group())
# print("🟡 b) 3-5 Ha in 'HaHaHaHaHa':", pattern_b.search("HaHaHaHaHa").group())
# print("🟡 c) Bat+0 man in 'Bat':", pattern_c.search("Bat").group())
# print("🟡 c) Bat+0 man in 'Batman':", pattern_c.search("Batman").group())
# print("🟡 c) Bat+0 man in 'Batmanmanman':", pattern_c.search("Batmanmanman").group())
# print("🟡 d) Bat+1 man in 'Bat':", pattern_d.search("Bat"))
# print("🟡 d) Bat+1 man in 'Batman':", pattern_d.search("Batman").group())
# print("🟡 d) Bat+1 man in 'Batmanmanman':", pattern_d.search("Batmanmanman").group())


# =====================================================================
#                    SECTION 3: ADVANCED PATTERNS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 MEDIUM 9: Anchors - Start (^) and End ($)
# a) Match strings that START with "Hello"
# b) Match strings that END with a digit
# c) Match strings that are ENTIRELY digits
#
# Test: "Hello, world!" starts with Hello -> True
# Test: "Your number is 42" ends with digit -> True
# Test: "1234567890" is all digits -> True
# Test: "12345xyz67890" is all digits -> False
# ----------------------------------------------------------------------

# texts = [
#     "Hello, world!",
#     'He said "Hello."',
#     "Your number is 42",
#     "Your number is forty two.",
#     "1234567890",
#     "12345xyz67890",
# ]

# Write your code below:


# Test your solution:


# ----------------------------------------------------------------------
# 🟡 MEDIUM 10: Word Boundaries (\b)
# Use \b to find words that START with "cat"
# Then use \B to find "cat" in the MIDDLE of words
#
# Test: "The cat found a catapult catalog in the catacombs."
#   words starting with cat -> ['cat', 'catapult', 'catalog', 'catacombs']
#
# Test: "certificate" cat in middle -> ['cat']
# Test: "catastrophe" cat in middle -> [] (cat is at the start, not middle)
# ----------------------------------------------------------------------

# text = "The cat found a catapult catalog in the catacombs."

# Write your code below:


# Test your solution:
# print("🟡 Words starting with cat:", results)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 11: Substitution with sub()
# Use sub() to:
# a) Replace "Agent Name" with "CENSORED"
# b) Replace "Agent Name" but keep the first letter: "A****"
#
# Hint for b): Use groups and back references (\1)
#
# Test a): "Agent Alice contacted Agent Bob." -> "CENSORED contacted CENSORED."
# Test b): "Agent Alice contacted Agent Bob." -> "A**** contacted B****."
# ----------------------------------------------------------------------

# text = "Agent Alice contacted Agent Bob."

# Write your code below:


# Test your solution:
# print("🟡 Censored:", censored)
# print("🟡 Partially censored:", partially_censored)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 12: Case-Insensitive and DOTALL
# a) Create a case-insensitive regex to match "robocop"
#    regardless of casing
# b) Use re.DOTALL to make . match newlines too
#
# Test a): "RoboCop" -> match, "ROBOCOP" -> match, "robocop" -> match
# Test b): "Line1\nLine2" with .* and re.DOTALL -> matches everything
# ----------------------------------------------------------------------

# texts = ["RoboCop is cool", "ROBOCOP protects", "Have you seen robocop?"]

# Write your code below:


# Test your solution:
# for t in texts:
#     print(f"🟡 Found in '{t}':", result)


# =====================================================================
#                    SECTION 4: PRACTICE PROGRAMS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 13: Greedy vs Lazy - HTML Tag Matching
# Given an HTML-like string, match ONLY the first tag using lazy matching
# Then match EVERYTHING between first < and last > using greedy matching
#
# Test greedy: "<To serve man> for dinner.>" -> "<To serve man> for dinner.>"
# Test lazy:   "<To serve man> for dinner.>" -> "<To serve man>"
# ----------------------------------------------------------------------

# html = "<To serve man> for dinner.>"

# Write your code below:


# Test your solution:
# print("🔴 Greedy:", greedy_result)
# print("🔴 Lazy:", lazy_result)


# ----------------------------------------------------------------------
# 🔴 HARD 14: Email Validator
# Write a regex that matches valid email addresses
# Format: username@domain.extension
# - Username: letters, digits, dots, underscores, hyphens
# - Domain: letters, digits, hyphens
# - Extension: 2-4 letters
#
# Test: "user@email.com" -> match
# Test: "first.last@company.co.uk" -> match
# Test: "invalid@.com" -> no match
# Test: "@no-user.com" -> no match
# ----------------------------------------------------------------------

# emails = [
#     "user@email.com",
#     "first.last@company.co",
#     "my_name123@domain.org",
#     "invalid@.com",
#     "@no-user.com",
#     "spaces in@email.com",
#     "normal@test.info",
# ]

# Write your code below:


# Test your solution:
# for email in emails:
#     print(f"🔴 {email}: {'✅ Valid' if is_valid else '❌ Invalid'}")


# ----------------------------------------------------------------------
# 🔴 HARD 15: Strong Password Detection
# Write a function that uses regex to check if a password is strong:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
#
# Hint: It's easier to test against MULTIPLE regex patterns
# instead of one giant regex
#
# Test: "HelloWorld1" -> Strong
# Test: "hello" -> Weak (short, no uppercase, no digit)
# Test: "ALLCAPS123" -> Weak (no lowercase)
# Test: "Password1" -> Strong
# ----------------------------------------------------------------------

# passwords = [
#     "HelloWorld1",
#     "hello",
#     "ALLCAPS123",
#     "Password1",
#     "short1A",
#     "longpasswordwithoutdigits",
#     "12345678",
#     "Str0ngP@ss",
# ]

# Write your code below:


# Test your solution:
# for pwd in passwords:
#     print(f"🔴 '{pwd}': {'💪 Strong' if is_strong else '👎 Weak'}")


# ----------------------------------------------------------------------
# 🔴 HARD 16: Regex strip() Method
# Write a function that does the same thing as strip()
# - If no second argument: remove whitespace from start and end
# - If second argument given: remove those characters from start and end
#
# Use regex with ^ and $ to match start/end
#
# Test: regex_strip("  Hello  ") -> "Hello"
# Test: regex_strip("xxxHelloxx", "x") -> "Hello"
# Test: regex_strip("abcHelloabc", "abc") -> "Hello"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 Strip spaces:", regex_strip("   Hello World   "))
# print("🔴 Strip x:", regex_strip("xxxHelloxxx", "x"))
# print("🔴 Strip abc:", regex_strip("abcHelloabc", "abc"))


# ----------------------------------------------------------------------
# 🔴 HARD 17: Phone Number & Email Extractor
# Given a block of text, find ALL phone numbers and email addresses
# Phone formats: XXX-XXX-XXXX, (XXX) XXX-XXXX, XXX.XXX.XXXX
# Email format: see HARD 14
#
# Test: Extract all contacts from the sample text below
# ----------------------------------------------------------------------

# sample_text = """
# Contact us at support@company.com or call 415-555-1234.
# You can also reach John at john.doe@email.org or (800) 123-4567.
# For sales: sales@bigcorp.co, phone: 555.999.8888
# Invalid: not-an-email, 123-45-6789 (not a phone)
# """

# Write your code below:


# Test your solution:
# print("🔴 Phone numbers found:")
# print("🔴 Emails found:")


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# Chapter 9 Concepts Covered:
#
# Basics:
# - import re, re.compile(), search(), group()
# - findall() for multiple matches
# - Grouping with parentheses and group(1), group(2)
#
# Character Classes:
# - Pipe | for alternatives
# - [abc] character classes, [^abc] negated classes
# - \d \w \s shorthand classes (and \D \W \S)
#
# Quantifiers:
# - ? (optional), * (zero+), + (one+)
# - {n}, {n,m} exact/range
# - Greedy vs lazy (add ? for lazy)
#
# Advanced:
# - ^ $ anchors, \b word boundaries
# - .* match everything, re.DOTALL for newlines
# - re.IGNORECASE for case-insensitive
# - sub() for substitution, back references \1
# - re.VERBOSE for readable regexes
# ======================================================================
