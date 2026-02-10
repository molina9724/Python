# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# def list_to_string(my_list):
#     if len(my_list) == 1:
#         return str(my_list[0])
#     string = ""
#     for index in range(len(my_list)-1):
#         string += str(my_list[index]) + ", "
#     string += "and " + str(my_list[len(my_list)-1])
#     return string


# print(list_to_string(['apples', 'bananas', 'tofu', 'cats']))
# print(list_to_string(["hello", 3, 4]))
# print(list_to_string(["hello"]))
# print(list_to_string(["hello", "you"]))
# print(list_to_string([None, "you"]))
# print(list_to_string(["", "you"]))
# print(list_to_string([True, False, "you"]))

# try:
#     test = []
#     if len(test) == 0:
#         raise Exception("Add a value into that shit, man")
#     list_to_string(test)
# except Exception as e:
#     print(str(e))

# import random
# head_or_tails = ["T", "H"]
# repetitions = 10000
# results = []

# for rep in range(repetitions):
#     coin_flip = list()
#     for cero_to_hundred in range(100):
#         coin_flip.append(random.choice(head_or_tails))
#     index = 0
#     while index in range(len(coin_flip)-5):
#         if all(x == coin_flip[index] for x in coin_flip[index:index+6]):
#             results.append(coin_flip[index:index+6])
#             index += 6
#         index += 1
# print(len(results))

# Pangram Detector

# Write a function named is_pangram(sentence) that accepts a string argument, then returns True if it’s a pangram and False if not. A pangram is a sentence that uses all 26 letters of the alphabet at least once. For example, “The quick brown fox jumps over the yellow lazy dog” is a pangram.

# There are several ways to accomplish this task. One way is to have a variable named EACH_LETTER that starts as an empty list. Then, you can loop over the characters in the string argument, convert each to uppercase with the upper() method, and append it to the EACH_LETTER list if it is a letter and doesn’t already exist there. You can tell that a letter in char isn’t already in the EACH_LETTER list because the expression char not in EACH_LETTER will evaluate to True. After looping over each character in the user’s string, you’ll know that the string is a pangram if len(EACH_LETTER) evaluates to 26.

# For example, the output of your program could look like this:

#     Enter a sentence:
# The quick brown fox jumps over the yellow lazy dog.
# That sentence is a pangram.

# Or this:

# Enter a sentence:
# Hello, world!
# That sentence is not a pangram.

import string


def is_pangram(sentence):
    clean_sentence = "".join(sentence.lower().split(" "))
    stripped_sentence = set(clean_sentence)
    for char in string.ascii_lowercase:
        if char not in stripped_sentence:
            return "That sentence is not a pangram."
    return "That sentence is a pangram."


print(is_pangram("Hello there"))
print(is_pangram("The quick brown fox jumps over the yellow lazy dog."))
