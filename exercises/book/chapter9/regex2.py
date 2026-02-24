# ======================================================================
# 🐍 REGEX EXTRA PRACTICE - regex2.py
# ======================================================================
# Fresh exercises with new scenarios to reinforce regex skills
# Topics: character classes, quantifiers, anchors, groups, sub, findall
# ======================================================================

import re


# =====================================================================
#                    SECTION 1: CHARACTER CLASSES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Extract Prices
# Find all prices in a string (dollar sign followed by digits and optional cents)
# Format: $XX or $XX.XX
#
# Test: "Shirt $25.99, Hat $15, Shoes $89.50" -> ['$25.99', '$15', '$89.50']
# Test: "Free item, no price" -> []
# ----------------------------------------------------------------------

# text = "Shirt $25.99, Hat $15, Shoes $89.50 and socks for $4.00"

# # Write your code below:

# pattern = re.compile(r"\$\d+(?:\.\d{2})?")
# result = pattern.findall(text)

# Test your solution:
# print("🟢 Prices:", result)


# ----------------------------------------------------------------------
# 🟢 EASY 2: Extract Hashtags
# Find all hashtags in a tweet (# followed by word characters)
#
# Test: "Loving #Python and #Regex today! #100DaysOfCode"
#   -> ['#Python', '#Regex', '#100DaysOfCode']
# ----------------------------------------------------------------------

# tweet = "Loving #Python and #Regex today! #100DaysOfCode is fun #coding"

# # Write your code below:

# pattern = re.compile(r"#\w+")
# result = pattern.findall(tweet)

# # Test your solution:
# print("🟢 Hashtags:", result)


# ----------------------------------------------------------------------
# 🟢 EASY 3: Find Hex Colors
# Match hex color codes: # followed by exactly 6 hex digits (0-9, a-f, A-F)
#
# Test: "Colors: #FF5733, #00ff00, #123abc, #ZZZZZZ"
#   -> ['#FF5733', '#00ff00', '#123abc']
# Hint: hex digits are [0-9a-fA-F]
# ----------------------------------------------------------------------

# text = "Background: #FF5733, text: #00ff00, border: #123abc, invalid: #ZZZZZZ"

# # Write your code below:

# pattern = re.compile(r"(#[0-9a-fA-F]{6})")
# result = pattern.findall(text)

# # Test your solution:
# print("🟢 Hex colors:", result)


# ----------------------------------------------------------------------
# 🟢 EASY 4: Extract Capitalized Words
# Find all words that start with a capital letter
# (but not words that are ALL caps)
#
# Test: "Alice went to NEW York with Bob"
#   -> ['Alice', 'York', 'Bob']
# Hint: Capital letter followed by one or more lowercase letters
# ----------------------------------------------------------------------

# text = "Alice went to NEW York with Bob on MONDAY morning"

# # Write your code below:

# pattern = re.compile(r"[A-Z]{1}[a-z]+")
# result = pattern.findall(text)

# # Test your solution:
# print("🟢 Capitalized words:", result)


# =====================================================================
#                    SECTION 2: QUANTIFIERS & PATTERNS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 5: Match Time Format
# Find all times in HH:MM format (24-hour: 00:00 to 23:59)
#
# Test: "Wake up at 07:30, lunch at 12:00, sleep at 23:45"
#   -> ['07:30', '12:00', '23:45']
# Test: "Invalid: 25:00, 12:60" -> []
# ----------------------------------------------------------------------

# text = "Wake up at 07:30, lunch at 12:00, sleep at 23:45, not 25:00"

# # Write your code below:

# pattern = re.compile(r"(?:[01]\d|2[0-3]):[0-5]\d")
# result = pattern.findall(text)

# # Test your solution:
# print("🟢 Times:", result)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: License Plate Matcher
# Match US-style license plates: 3 letters followed by a space
# or dash, then 4 digits
# Format: ABC-1234 or ABC 1234
#
# Test: "Cars: ABC-1234, XYZ 5678, AB-123, ABCD-1234"
#   -> ['ABC-1234', 'XYZ 5678']
# ----------------------------------------------------------------------


# Write your code below:


# text = "Plates spotted: ABC-1234, XYZ 5678, AB-123, ABCD-1234, MNO-9999"

# pattern = re.compile(r"\b[a-zA-Z]{3}(?: |-)\d{4}")
# result = pattern.findall(text)

# # Test your solution:
# print("🟡 License plates:", result)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 7: Repeated Words Detector
# Find words that appear twice in a row (like "the the" or "is is")
# Use groups and back references!
#
#
# Test: "This is is a test test of the the system"
#   -> ['is', 'test', 'the']
# ----------------------------------------------------------------------

# text = "This is is a test test of the the system system"

# Write your code below:

# pattern = re.compile(r"(\w+)\s+\1")
# result = pattern.findall(text)

# # Test your solution:
# print("🟡 Repeated words:", result)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 8: Data Scraper
# Extract all key:value pairs from a config-style string
# Format: key=value separated by semicolons
# Keys are letters/underscores only, values can be anything except ;
#
# Test: "name=Alice;age=30;city=Miami"
#   -> [('name', 'Alice'), ('age', '30'), ('city', 'Miami')]
# Test: "host=localhost;port=5432;db=myapp"
#   -> [('host', 'localhost'), ('port', '5432'), ('db', 'myapp')]
# ----------------------------------------------------------------------

# config = "name=Alice;age=30;city=Miami;role=Engineer"

# # Write your code below:

# pattern = re.compile(r"(\w+)=(.\w)")
# result = pattern.findall(config)

# # Test your solution:
# print("🟡 Config values:", result)


# =====================================================================
#                    SECTION 3: ANCHORS & VALIDATION
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 MEDIUM 9: Username Validator
# Validate usernames with these rules:
# - 3 to 16 characters long
# - Only letters, digits, underscores, hyphens
# - Must start with a letter
# - Cannot end with underscore or hyphen
#
# Test: "john_doe" -> valid
# Test: "ab" -> invalid (too short)
# Test: "3invalid" -> invalid (starts with digit)
# Test: "bad_" -> invalid (ends with underscore)
# Test: "this_is_way_too_long_username" -> invalid (too long)
# ----------------------------------------------------------------------

# usernames = [
#     "john_doe",
#     "ab",
#     "3invalid",
#     "bad_",
#     "ok-name",
#     "this_is_way_too_long_username",
#     "A1",
#     "valid123",
#     "also-valid",
# ]

# # Write your code below:

# pattern1 = re.compile(r".{3,16}")
# pattern2 = re.compile(r"(?:\w+|\-+|\_+)+")
# pattern3 = re.compile(r"^[a-zA-Z]")
# pattern4 = re.compile(r"[a-zA-Z]$")

# results = ""
# for name in usernames:
#     if (
#         pattern1.fullmatch(name)
#         and pattern2.search(name)
#         and pattern3.search(name)
#         and pattern4.search(name)
#     ):
#         print(name)
#         print("You did it, you son of a bitch")

# Test your solution:
# for u in usernames:
#     print(f"🟡 '{u}': {'✅' if is_valid else '❌'}")


# ----------------------------------------------------------------------
# 🟡 MEDIUM 10: Credit Card Masker
# Given a credit card number (with or without dashes),
# mask all but the last 4 digits with X
#
# Use sub() with groups to keep only the last 4
#
# Test: "4111-1111-1111-1111" -> "XXXX-XXXX-XXXX-1111"
# Test: "5500000000005555" -> "XXXXXXXXXXXX5555"
# Hint: capture the last 4 digits as a group
# ----------------------------------------------------------------------

cards = [
    "4111-1111-1111-1111",
    "5500000000005555",
    "3782-822463-10005",
]

# Write your code below:
pattern = re.compile(r"(.+)(-?\d{4}$)")

# Test your solution:
# for card in cards:
# print(f"🟡 {card} -> {pattern.sub('XXXX', cards[0])}")


# =====================================================================
#                    SECTION 4: REAL-WORLD EXTRACTION
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 11: Markdown Link Extractor
# Extract all markdown links from text
# Format: [link text](url)
#
# Capture both the text AND the URL as separate groups
#
# Test: "Visit [Google](https://google.com) or [GitHub](https://github.com)"
#   -> [('Google', 'https://google.com'), ('GitHub', 'https://github.com')]
# ----------------------------------------------------------------------

# text = """Check out [Google](https://google.com) for search,
# [GitHub](https://github.com) for code, and
# [Stack Overflow](https://stackoverflow.com) for answers."""

# Write your code below:


# Test your solution:
# for text, url in result:
#     print(f"🔴 Text: '{text}' -> URL: {url}")


# ----------------------------------------------------------------------
# 🔴 HARD 12: Variable Name Converter
# Convert camelCase to snake_case using regex
# Insert an underscore before each uppercase letter, then lowercase all
#
# Test: "getElementById" -> "get_element_by_id"
# Test: "firstName" -> "first_name"
# Test: "HTMLParser" -> "h_t_m_l_parser"
#
# Hint: Find uppercase letters and replace with _lowercase
# Use sub() with a function or back reference
# ----------------------------------------------------------------------

# camel_names = [
#     "getElementById",
#     "firstName",
#     "lastName",
#     "maxRetryCount",
#     "isValid",
#     "toString",
# ]

# Write your code below:


# Test your solution:
# for name in camel_names:
#     print(f"🔴 {name} -> {snake}")


# ----------------------------------------------------------------------
# 🔴 HARD 13: Multi-Format Phone Normalizer
# Take phone numbers in ANY of these formats and convert to (XXX) XXX-XXXX:
#   "4155551234", "415-555-1234", "415.555.1234",
#   "(415) 555-1234", "1-415-555-1234"
#
# Step 1: Extract the 10 digits regardless of format
# Step 2: Reformat them
#
# Test: "4155551234" -> "(415) 555-1234"
# Test: "1-415-555-1234" -> "(415) 555-1234"
# Test: "415.555.1234" -> "(415) 555-1234"
# ----------------------------------------------------------------------

# phones = [
#     "4155551234",
#     "415-555-1234",
#     "415.555.1234",
#     "(415) 555-1234",
#     "1-415-555-1234",
#     "+1 415 555 1234",
# ]

# Write your code below:


# Test your solution:
# for phone in phones:
#     print(f"🔴 {phone} -> {normalized}")


# ----------------------------------------------------------------------
# 🔴 HARD 14: Text Censoring System
# Create a function that censors "bad words" in text by replacing
# the middle characters with asterisks, keeping first and last letter
#
# Bad words list: ["damn", "hell", "crap"]
#
# Test: "What the hell is this crap" -> "What the h**l is this c**p"
# Test: "Go to hell, damn it" -> "Go to h**l, d**n it"
#
# Hint: Use re.sub() with a function as replacement
# The function receives a match object and returns the replacement
# ----------------------------------------------------------------------

# text = "What the hell is this damn crap, go to hell"
# bad_words = ["damn", "hell", "crap"]

# Write your code below:


# Test your solution:
# print(f"🔴 Censored: {censored}")


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# 🟢 EASY (5):    Prices, hashtags, hex colors, capitalized words, time
# 🟡 MEDIUM (5):  License plates, repeated words, CSV, usernames, cards
# 🔴 HARD (4):    Markdown links, camelCase, phone normalizer, censoring
#
# Key Concepts Practiced:
# - \d \w \s and custom [character classes]
# - + * ? {n} {n,m} quantifiers
# - Greedy vs Lazy matching
# - ^ $ \b anchors and boundaries
# - () groups and \1 back references
# - re.sub() with strings AND functions
# - re.search() vs re.findall() vs re.fullmatch()
# ======================================================================
