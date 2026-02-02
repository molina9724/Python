# =============================================================================
# 🐍 PYTHON LOGIC BOOTCAMP - Progressive Exercises
# =============================================================================

# ----------------------------------------------------------------------
# 🟢 EASY 1: Count Vowels
# 1. Create a function count_vowels(text)
# 2. Convert text to lowercase to handle uppercase vowels
# 3. Loop through each character
# 4. If the character is a vowel (a, e, i, o, u), add 1 to a counter
# 5. Return the counter
#
# Test: count_vowels("hello world") -> 3
# Test: count_vowels("Python") -> 1
# Test: count_vowels("aeiou") -> 5
# Edge: count_vowels("") -> 0 (empty string)
# Edge: count_vowels("xyz") -> 0 (no vowels)
# Edge: count_vowels("AEIOU") -> 5 (uppercase)

# Write your code below:
from collections import Counter


# def count_vowels(text):
#     lower_text = text.lower()
#     vowels = {"a", "e", "i", "o", "u"}
#     vowel_count = 0
#     for char in lower_text:
#         if char in vowels:
#             vowel_count += 1
#     return vowel_count


# Test your solution:
# print("🟢 count_vowels('hello world'):", count_vowels("hello world"))  # -> 3
# print("🟢 count_vowels('Python'):", count_vowels("Python"))            # -> 1
# print("🟢 count_vowels('aeiou'):", count_vowels("aeiou"))              # -> 5
# print("🟢 count_vowels('') [empty]:", count_vowels(""))                # -> 0
# print("🟢 count_vowels('xyz') [no vowels]:", count_vowels("xyz"))      # -> 0
# print("🟢 count_vowels('AEIOU') [uppercase]:", count_vowels("AEIOU"))  # -> 5


# ----------------------------------------------------------------------
# 🟢 EASY 2: Count Words
# 1. Create a function count_words(text)
# 2. Words are separated by spaces
# 3. Count how many words are in the text
# 4. Return the count
#
# Test: count_words("hello world") -> 2
# Test: count_words("I love Python") -> 3
# Test: count_words("one") -> 1
# Edge: count_words("") -> ? (empty string - what should happen?)
# Edge: count_words("   ") -> ? (only spaces)
# Edge: count_words("hello  world") -> ? (double space)

# Write your code below:
# def count_words(text):
#     if not text.strip():
#         return 0
#     clean_text = " ".join(text.split())
#     separate_words = clean_text.split(" ")
#     return len(separate_words)


# Test your solution:
# print("🟢 count_words('hello world'):", count_words("hello world"))    # -> 2
# print("🟢 count_words('I love Python'):", count_words("I love Python"))  # -> 3
# print("🟢 count_words('one'):", count_words("one"))                    # -> 1
# print("🟢 count_words('') [empty]:", count_words(
#     ""))                  # -> ? Think about this!
# print("🟢 count_words('   ') [spaces only]:",
#       count_words("   "))      # -> ? Think about this!
# print("🟢 count_words('hello  world') [double space]:", count_words(
#     "hello  world"))  # -> ? Think about this!


# ----------------------------------------------------------------------
# 🟢 EASY 3: Find Longest Word
# 1. Create a function find_longest_word(text)
# 2. Split the text into words
# 3. Keep track of the longest word you've seen
# 4. Return the longest word
#
# Test: find_longest_word("I love Python") -> "Python"
# Test: find_longest_word("cat dog elephant") -> "elephant"
# Test: find_longest_word("a bb ccc") -> "ccc"
# Edge: find_longest_word("hi") -> "hi" (single word)
# Edge: find_longest_word("ab cd ef") -> ? (tie - which one to return?)
# Edge: find_longest_word("") -> ? (empty string)

# Write your code below:

# def find_longest_word(text):
#     words = text.split(" ")
#     longest_word = words[0]
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word

# Test your solution:
# print("🟢 find_longest_word('I love Python'):", find_longest_word("I love Python"))  # -> Python
# print("🟢 find_longest_word('cat dog elephant'):", find_longest_word("cat dog elephant"))  # -> elephant
# print("🟢 find_longest_word('a bb ccc'):", find_longest_word("a bb ccc"))  # -> ccc
# print("🟢 find_longest_word('hi') [single word]:", find_longest_word("hi"))  # -> hi
# print("🟢 find_longest_word('ab cd ef') [tie]:", find_longest_word("ab cd ef"))  # -> first one? ab


# ----------------------------------------------------------------------
# 🟢 EASY 4: Reverse String
# 1. Create a function reverse_string(text)
# 2. Do NOT use [::-1] or reversed()
# 3. Build a new string character by character
# 4. Return the reversed string
#
# Test: reverse_string("hello") -> "olleh"
# Test: reverse_string("Python") -> "nohtyP"
# Test: reverse_string("a") -> "a"
# Edge: reverse_string("") -> "" (empty string)
# Edge: reverse_string("aa") -> "aa" (palindrome)
# Edge: reverse_string("ab cd") -> "dc ba" (with space)

# Write your code below:

# def reverse_string(text):
#     reversed_list = list()
#     for char in text:
#         reversed_list.insert(0, char)
#     reversed_word = "".join(reversed_list)
#     return reversed_word


# # Test your solution:
# print("🟢 reverse_string('hello'):", reverse_string("hello"))  # -> olleh
# print("🟢 reverse_string('Python'):", reverse_string("Python"))  # -> nohtyP
# print("🟢 reverse_string('a'):", reverse_string("a"))  # -> a
# print("🟢 reverse_string('') [empty]:", reverse_string(""))  # -> ""
# print("🟢 reverse_string('aa') [palindrome]:", reverse_string("aa"))  # -> aa
# print("🟢 reverse_string('ab cd') [with space]:", reverse_string("ab cd"))  # -> dc ba


# ----------------------------------------------------------------------
# 🟡 MEDIUM 1: Is Palindrome
# 1. Create a function is_palindrome(text)
# 2. A palindrome reads the same forwards and backwards
# 3. Ignore spaces and case
# 4. Return True if palindrome, False otherwise
#
# Test: is_palindrome("racecar") -> True
# Test: is_palindrome("hello") -> False
# Test: is_palindrome("A man a plan a canal Panama") -> True
# Edge: is_palindrome("") -> True (empty is palindrome?)
# Edge: is_palindrome("a") -> True (single char)
# Edge: is_palindrome("Aa") -> True (case insensitive)

# Write your code below:

# def is_palindrome(text):
#     clean = "".join(text.lower().split(" "))
#     return clean == clean[::-1]


# # Test your solution:
# print("🟡 is_palindrome('racecar'):", is_palindrome("racecar"))  # -> True
# print("🟡 is_palindrome('hello'):", is_palindrome("hello"))  # -> False
# print("🟡 is_palindrome('A man a plan a canal Panama'):",
#       is_palindrome("A man a plan a canal Panama"))  # -> True
# print("🟡 is_palindrome('') [empty]:", is_palindrome(""))  # -> True?
# print("🟡 is_palindrome('a') [single]:", is_palindrome("a"))  # -> True
# print("🟡 is_palindrome('Aa') [case]:", is_palindrome("Aa"))  # -> True


# ----------------------------------------------------------------------
# 🟡 MEDIUM 2: Find Duplicates
# 1. Create a function find_duplicates(items)
# 2. Find all items that appear more than once
# 3. Return a list of the duplicates
#
# Test: find_duplicates([1, 2, 3, 2, 4, 3]) -> [2, 3]
# Test: find_duplicates(["a", "b", "a", "c"]) -> ["a"]
# Test: find_duplicates([1, 2, 3]) -> []
# Edge: find_duplicates([]) -> [] (empty list)
# Edge: find_duplicates([1, 1, 1, 1]) -> [1] (same item many times)
# Edge: find_duplicates([1]) -> [] (single item)

# Write your code below:


# def find_duplicates(items):
#     counter = Counter(items)
#     return [key for key, value in counter.items() if value > 1]


# # Test your solution:
# print("🟡 find_duplicates([1, 2, 3, 2, 4, 3]):",
#       find_duplicates([1, 2, 3, 2, 4, 3]))  # -> [2, 3]
# print("🟡 find_duplicates(['a', 'b', 'a', 'c']):",
#       find_duplicates(["a", "b", "a", "c"]))  # -> ['a']
# print("🟡 find_duplicates([1, 2, 3]):", find_duplicates([1, 2, 3]))  # -> []
# print("🟡 find_duplicates([]) [empty]:", find_duplicates([]))  # -> []
# print("🟡 find_duplicates([1, 1, 1, 1]) [all same]:",
#       find_duplicates([1, 1, 1, 1]))  # -> [1]
# print("🟡 find_duplicates([1]) [single]:", find_duplicates([1]))  # -> []


# ----------------------------------------------------------------------
# 🟡 MEDIUM 3: Remove Duplicates
# 1. Create a function remove_duplicates(items)
# 2. Remove duplicates while keeping original order
# 3. Do NOT use set() directly (that loses order)
# 4. Return the list without duplicates
#
# Test: remove_duplicates([1, 2, 3, 2, 4, 3]) -> [1, 2, 3, 4]
# Test: remove_duplicates(["a", "b", "a", "c"]) -> ["a", "b", "c"]
# Test: remove_duplicates([1, 1, 1]) -> [1]
# Edge: remove_duplicates([]) -> [] (empty list)
# Edge: remove_duplicates([1]) -> [1] (single item)
# Edge: remove_duplicates([1, 2, 3]) -> [1, 2, 3] (no duplicates)

# Write your code below:

# def remove_duplicates(items):
#     seen = set()
#     result = []
#     for element in items:
#         if element not in seen:
#             seen.add(element)
#             result.append(element)
#     return result

# # Test your solution:
# print("🟡 remove_duplicates([1, 2, 3, 2, 4, 3]):", remove_duplicates([1, 2, 3, 2, 4, 3]))  # -> [1, 2, 3, 4]
# print("🟡 remove_duplicates(['a', 'b', 'a', 'c']):", remove_duplicates(["a", "b", "a", "c"]))  # -> ['a', 'b', 'c']
# print("🟡 remove_duplicates([1, 1, 1]):", remove_duplicates([1, 1, 1]))  # -> [1]
# print("🟡 remove_duplicates([]) [empty]:", remove_duplicates([]))  # -> []
# print("🟡 remove_duplicates([1]) [single]:", remove_duplicates([1]))  # -> [1]
# print("🟡 remove_duplicates([1, 2, 3]) [no dups]:", remove_duplicates([1, 2, 3]))  # -> [1, 2, 3]


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: Count Character Frequency
# 1. Create a function count_character_frequency(text)
# 2. Count how many times each character appears
# 3. Ignore spaces
# 4. Return a dictionary with characters as keys and counts as values
#
# Test: count_character_frequency("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# Test: count_character_frequency("aaa") -> {'a': 3}
# Test: count_character_frequency("ab ab") -> {'a': 2, 'b': 2}
# Edge: count_character_frequency("") -> {} (empty string)
# Edge: count_character_frequency("   ") -> {} (only spaces)
# Edge: count_character_frequency("a") -> {'a': 1} (single char)
# Write your code below:

# def count_character_frequency(text):
#     letter_count = dict()
#     for char in text:
#         if char != " ":
#             letter_count[char] = letter_count.setdefault(char, 0) + 1
#     return letter_count
#     return Counter(char for char in text if char != " ") -> One liner


# Test your solution:
# print("🟡 count_character_frequency('hello'):", count_character_frequency(
#     "hello"))  # -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# print("🟡 count_character_frequency('aaa'):",
#       count_character_frequency("aaa"))  # -> {'a': 3}
# print("🟡 count_character_frequency('ab ab'):",
#       count_character_frequency("ab ab"))  # -> {'a': 2, 'b': 2}
# print("🟡 count_character_frequency('') [empty]:",
#       count_character_frequency(""))  # -> {}
# print("🟡 count_character_frequency('   ') [spaces]:", count_character_frequency(
#     "   "))  # -> {}
# print("🟡 count_character_frequency('a') [single]:",
#       count_character_frequency("a"))  # -> {'a': 1}


# ----------------------------------------------------------------------
# 🔴 HARD 1: Manual Split
# 1. Create a function my_split(text, separator=" ")
# 2. Implement str.split() manually
# 3. Do NOT use .split()
# 4. Build words character by character
# 5. Return a list of the parts
#
# Test: my_split("hello world") -> ["hello", "world"]
# Test: my_split("a,b,c", ",") -> ["a", "b", "c"]
# Test: my_split("one") -> ["one"]
# Edge: my_split("") -> [""] or [] ? (empty string)
# Edge: my_split("   ") -> ["", "", "", ""] ? (only separators)
# Edge: my_split("hello  world") -> ["hello", "", "world"] (double separator)

# Write your code below:

# def my_split(text, separator=" "):
#     partial_word = ""
#     words = list()

#     for char in text:
#         if char != separator:
#             partial_word += char
#         else:
#             words.append(partial_word)
#             partial_word = ""
#     words.append(partial_word)
#     return words


# # Test your solution:
# print("🔴 my_split('hello world'):", my_split(
#     "hello world"))  # -> ['hello', 'world']
# print("🔴 my_split('a,b,c', ','):", my_split("a,b,c", ","))  # -> ['a', 'b', 'c']
# print("🔴 my_split('one'):", my_split("one"))  # -> ['one']
# print("🔴 my_split('') [empty]:", my_split(""))  # -> [''] or []
# print("🔴 my_split('   ') [spaces only]:", my_split("   "))  # -> ['', '', '', '']
# print("🔴 my_split('hello  world') [double sep]:", my_split("hello  world"))  # -> ['hello', '', 'world']


# ----------------------------------------------------------------------
# 🔴 HARD 2: Manual Replace
# 1. Create a function my_replace(text, old, new)
# 2. Implement str.replace() manually
# 3. Do NOT use .replace()
# 4. Replace all occurrences of 'old' with 'new'
# 5. Return the new string
#
# Test: my_replace("hello world", "world", "Python") -> "hello Python"
# Test: my_replace("aaa", "a", "b") -> "bbb"
# Test: my_replace("hello", "x", "y") -> "hello"
# Edge: my_replace("", "a", "b") -> "" (empty string)
# Edge: my_replace("hello", "ll", "LL") -> "heLLo" (multi-char replace)
# Edge: my_replace("hello", "", "x") -> ? (empty old - tricky!)

# Write your code below:

# def my_replace(text, old, new):
#     replaced = ""
#     while True:
#         index = text.find(old)
#         if index != -1:
#             replaced += text[0:index] + new
#             text = text[index+len(old):]
#         else:
#             replaced += text
#             break
#     return replaced


# # Test your solution:
# print("🔴 my_replace('hello world', 'world', 'Python'):", my_replace(
#     "hello world", "world", "Python"))  # -> hello Python
# print("🔴 my_replace('aaa', 'a', 'b'):", my_replace("aaa", "a", "b"))  # -> bbb
# print("🔴 my_replace('hello', 'x', 'y'):",
#       my_replace("hello", "x", "y"))  # -> hello
# print("🔴 my_replace('', 'a', 'b') [empty]:", my_replace("", "a", "b"))  # -> ""
# print("🔴 my_replace('hello', 'll', 'LL'):",
#       my_replace("hello", "ll", "LL"))  # -> heLLo


# ----------------------------------------------------------------------
# 🔴 HARD 3: Manual Count
# 1. Create a function my_count(text, substring)
# 2. Implement str.count() manually
# 3. Do NOT use .count()
# 4. Count non-overlapping occurrences
# 5. Return the count
#
# Test: my_count("hello", "l") -> 2
# Test: my_count("banana", "ana") -> 1
# Test: my_count("hello", "x") -> 0
# Edge: my_count("", "a") -> 0 (empty string)
# Edge: my_count("hello", "") -> ? (empty substring - tricky!)
# Edge: my_count("aaaa", "aa") -> 2 (non-overlapping)

# Write your code below:


# Test your solution:
# print("🔴 my_count('hello', 'l'):", my_count("hello", "l"))  # -> 2
# print("🔴 my_count('banana', 'ana'):", my_count("banana", "ana"))  # -> 1
# print("🔴 my_count('hello', 'x'):", my_count("hello", "x"))  # -> 0
# print("🔴 my_count('', 'a') [empty text]:", my_count("", "a"))  # -> 0
# print("🔴 my_count('aaaa', 'aa') [non-overlap]:", my_count("aaaa", "aa"))  # -> 2


# ----------------------------------------------------------------------
# 🔴 HARD 4: Reverse List In Place
# 1. Create a function my_reverse_list(items)
# 2. Reverse the list IN PLACE (modify the original)
# 3. Do NOT use [::-1], reversed(), or .reverse()
# 4. Swap elements manually
#
# Test:
#   lst = [1, 2, 3, 4]
#   my_reverse_list(lst)
#   print(lst) -> [4, 3, 2, 1]
# Edge: [] -> [] (empty list)
# Edge: [1] -> [1] (single item)
# Edge: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1] (odd length)

# Write your code below:


# Test your solution:
# lst1 = [1, 2, 3, 4]
# my_reverse_list(lst1)
# print("🔴 my_reverse_list([1, 2, 3, 4]):", lst1)  # -> [4, 3, 2, 1]
# lst2 = ["a", "b", "c"]
# my_reverse_list(lst2)
# print("🔴 my_reverse_list(['a', 'b', 'c']):", lst2)  # -> ['c', 'b', 'a']
# lst3 = []
# my_reverse_list(lst3)
# print("🔴 my_reverse_list([]) [empty]:", lst3)  # -> []
# lst4 = [1]
# my_reverse_list(lst4)
# print("🔴 my_reverse_list([1]) [single]:", lst4)  # -> [1]
# lst5 = [1, 2, 3, 4, 5]
# my_reverse_list(lst5)
# print("🔴 my_reverse_list([1,2,3,4,5]) [odd]:", lst5)  # -> [5, 4, 3, 2, 1]
