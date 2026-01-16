# ----------------------------------------------------------------------
# Exercise 1: String Basics & Type Checking
#
# 1. Create three string variables:
#    - first_name with your first name
#    - last_name with your last name
#    - favorite_quote with any quote (use both single and double quotes in different variables)
# 2. Print the type of each variable using type()
# 3. Print the length of each string using len()
# 4. Print all three strings
#
# Write your code for Exercise 1 below:

# first_name = "Carlos"
# last_name = "Valderrama"
# favorite_quote = "To live is to die"

# print(type(first_name))
# print(type(last_name))
# print(type(favorite_quote))

# print(len(first_name))
# print(len(last_name))
# print(len(favorite_quote))

# print(first_name)
# print(last_name)
# print(favorite_quote)

# ----------------------------------------------------------------------
# Exercise 2: String Indexing & Iteration
#
# 1. Ask the user to input a word (at least 5 characters)
# 2. Print:
#    - The first character
#    - The last character
#    - The middle character (use len() to find it)
# 3. Use a for loop to print each character on a separate line
# 4. Use a for loop with enumerate() to print each character with its index
#
# Write your code for Exercise 2 below:

# word = input("input a word (at least 5 characters)")
# print(word[0])
# print(word[-1])

# middle = len(word) // 2
# print(word[middle])

# for i in word:
#     print(f"{i} \n")

# for index, char in enumerate(word):
#     print(f"{char} : {index}")

# ----------------------------------------------------------------------
# Exercise 3: String Slicing Practice
#
# Given the string: my_string = "Python Programming"
#
# 1. Extract and print "Python" (first word)
# 2. Extract and print "Programming" (second word)
# 3. Extract every second character from the entire string
# 4. Reverse the entire string using slicing
# 5. Get the last 5 characters
# 6. Get characters from index 7 to 14
#
# Write your code for Exercise 3 below:

# my_string = "Python Programming"
# first_word = my_string[slice(0, 6)]
# print(first_word)

# second_word = my_string[slice(7, len(my_string))]
# print(second_word)

# for i in my_string.split(" "):
#     second_letter = i[slice(1, 2)]
#     print(second_letter)

# reversed_word = my_string[::-1]
# print(reversed_word)

# last_five = my_string[slice(len(my_string)-5, len(my_string))]
# last_fives = my_string[-5:]
# print(last_five)
# print(last_fives)

# seven_to_fourteen = my_string[7:14]
# print(seven_to_fourteen)

# seven_to_fourteen = my_string[::2]
# print(seven_to_fourteen)

# ----------------------------------------------------------------------
# Exercise 4: String Methods Exploration
#
# 1. Ask the user to input a sentence
# 2. Print the sentence in:
#    - All uppercase
#    - All lowercase
#    - Title case (first letter of each word capitalized)
# 3. Count how many times the letter 'e' appears (use .count())
# 4. Replace all spaces with hyphens (use .replace())
# 5. Check if the sentence starts with "Hello" (use .startswith())
#
# Write your code for Exercise 4 below:

# sentence = "Hello there!. How are you today? - Doing well, my man!"
# print(sentence.upper())
# print(sentence.lower())
# for i in sentence:
#     if i[0].isupper():
#         print(i[0])

# e_amount = sentence.count("e")
# print(e_amount)

# hyphen_replace = sentence.replace(" ", "/")
# print(hyphen_replace)

# starts_with = sentence.startswith("Hello")
# print(starts_with)


# ----------------------------------------------------------------------
# Exercise 5: String Splitting & Joining
#
# 1. Ask the user to input a sentence with at least 4 words
# 2. Split the sentence into a list of words
# 3. Print each word on a separate line with its length
# 4. Join the words back together with " - " as separator
# 5. Print the result
#
# Write your code for Exercise 5 below:

# sentence = "Here are your four words"
# split_sentence = sentence.split(" ")
# print(split_sentence)
# for i in split_sentence:
#     print(f"{i} - {len(i)}")
# hyphen_sentence = "-".join(split_sentence)
# print(hyphen_sentence)

# ----------------------------------------------------------------------
# Exercise 6: String Formatting - Three Ways
#
# Create a program that asks for:
# - Name
# - Age
# - City
#
# Then print the same message using THREE different methods:
# 1. Using concatenation with str()
# 2. Using .format()
# 3. Using f-strings
#
# Write your code for Exercise 6 below:

# name = input("Name: ")
# age = input("Age: ")
# city = input("City: ")

# print("My name is " + name + ", my age is " + age + " and I'm from " + city)
# print("My name is {}, my age is {} and I'm from {}".format(name, age, city))
# print(f"My name is {name}, my age is {age} and I'm from {city}")

# ----------------------------------------------------------------------
# Exercise 7: String Search & Validation
#
# 1. Create a variable with a long text (at least 2 sentences)
# 2. Ask the user to input a word to search for
# 3. Check if the word exists in the text using in
# 4. If it exists:
#    - Find its position using .find()
#    - Count how many times it appears using .count()
#    - Print all this information
# 5. If it doesn't exist, print "Word not found"
#
# Write your code for Exercise 7 below:

# text = "If anyone tells you that a certain person speaks ill of you, do not make excuses about what is said of you but answer, He was ignorant of my other faults, else he would not have mentioned these alone."
# word_to_search = input("What word do you want to look for? ")
# if word_to_search in text:
#     position = text.find(word_to_search)
#     times = text.count(word_to_search)

#     print(f"{word_to_search} was found in {position} and is repeated {times} times")
# else:
#     print("Word not found")


# ----------------------------------------------------------------------
# Exercise 8: Password Validator
#
# Create a password validator that checks if a password is strong:
#
# 1. Ask user to input a password
# 2. Check and print whether:
#    - Length is at least 8 characters
#    - Contains at least one uppercase letter (use .isupper() with a loop)
#    - Contains at least one lowercase letter (use .islower() with a loop)
#    - Contains at least one digit (use .isdigit() with a loop)
# 3. If all conditions are met, print "Strong password!"
# 4. Otherwise, print which requirements are missing
#
# Write your code for Exercise 8 below:

# password = input("Type in a password: ")
# uppercase = 0
# lowercase = 0
# digit = 0
# flag = True
# if len(password) >= 8:
#     for i in password:
#         if i.isupper():
#             uppercase += 1
#         if i.islower():
#             lowercase += 1
#         if i.isdigit():
#             digit += 1
#     if uppercase < 1:
#         print("At least 1 uppercase")
#         flag = False
#     if lowercase < 1:
#         print("At least 1 lowercase")
#         flag = False
#     if digit < 1:
#         print("At least 1 digit")
#         flag = False
#     if flag:
#         print("Strong password!")
# else:
#     print("At least 8 chars")

# ----------------------------------------------------------------------
# Exercise 9: Text Analyzer
#
# Create a text analysis tool:
#
# 1. Ask user to input a paragraph (multiple sentences)
# 2. Calculate and print:
#    - Total number of characters (including spaces)
#    - Total number of characters (excluding spaces) - use .replace()
#    - Number of words - use .split()
#    - Number of sentences (count periods, question marks, exclamation marks)
#    - Most common word (hint: use .split() and count each word)
# 3. Format the output nicely using f-strings
#
# Write your code for Exercise 9 below:

# paragraph = "Epictetus was a Greek Stoic philosopher. He was born into slavery at Hierapolis, Phrygia and lived in Rome until his banishment, after which he spent the rest of his life in Nicopolis in northwestern Greece."

# total_char = len(paragraph)
# total_char_no_spaces = len(paragraph.replace(" ", ""))

# total_words = len(paragraph.split(" "))

# sentence_number = 0
# for i in paragraph:
#     if i in ".?!":
#         sentence_number += 1

# clean_text = paragraph.lower()
# for char in ".,!?;:":
#     clean_text = clean_text.replace(char, "")
# words = clean_text.split(" ")

# most_common_word = words[0]
# times = 1

# for i in words:
#     if words.count(i) > times:
#         most_common_word = i
#         times = words.count(i)
# print(most_common_word)
# print(times)


# ----------------------------------------------------------------------
# Advanced Exercise 10: String Reverser with Options
#
# Create a program that:
#
# 1. Asks user to input a sentence
# 2. Asks what they want to do:
#    - Type 'r' to reverse the entire sentence
#    - Type 'w' to reverse each word individually (but keep word order)
#    - Type 'c' to reverse only the characters (keep spaces in place)
#    - Type 'v' to remove all vowels
#    - Type 'p' to create a palindrome check
# 3. Use if/elif/else to handle each option
# 4. Use slicing, loops, and string methods as needed
# 5. Print the result with nice formatting
#
# Write your code for Advanced Exercise 10 below:

# sentence = "Epictetus was a Greek Stoic philosopher"

# action = input("What do you want to do, ah? ")
# reverse_each_word = []
# reverse_only_char = []
# no_vowel = sentence
# if action == "r":
#     reverse_sentence = sentence[::-1]
#     print(reverse_sentence)
# elif action == "w":
#     split = sentence.split(" ")
#     for i in split:
#         reverse_each_word.append(i[::-1])
#     reverse_each_word = " ".join(reverse_each_word)
#     print(reverse_each_word)
# elif action == "c":
#     split = sentence.split(" ")
#     for i in split:
#         reverse_only_char.append(i[::-1])
#     reverse_only_char.reverse()
#     reverse_only_char = " ".join(reverse_only_char)
#     print(reverse_only_char)
# elif action == "v":
#     for i in "aeiou":
#         no_vowel = no_vowel.replace(i, "")
#     print(no_vowel)
# elif action == "p":

#     x = sentence.replace(" ", "")
#     y = list(x)
#     y.reverse()
#     z = "".join(y)
#     if x == z:
#         print("Palindrome")
#     else:
#         print("No palindrome")
