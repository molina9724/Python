# Word Match Game

# The word game Jotto was created in 1955, and the 1980s game show Lingo later repurposed its concept (which you might recognize as another, more recent, game). You can make your own version of this game in Python.

# Create a program that has the user guess a five-letter word. Your code should include a function named get_word_hint(secret_word, guess_word) that returns a five-character string of hints. The hints are an uppercase O for a correct letter in the same place in the secret word, a lowercase o for a correct letter in a different place in the secret word, and x for letters that are not in the secret word. If the guessed word is the same as the secret word, the function should return OOOOO.

# For example, if the secret word is CRANE and the guess word is CANDY, get_word_hint('CRANE', 'CANDY') should return Oooxx because the first letter in CANDY matches the first letter in the secret word, CRANE. The next two hint characters are oo because the A and N characters in CANDY exist in CRANE but at different indexes. The last two hint characters are xx because the D and Y in CANDY don’t appear in CRANE at all.

# The rest of the program should randomly choose a secret word from a list of five-character words and then give the user six tries to guess it. You can use this list of words:


# import random


# def get_word_hint(secret_word, guess_word):
#     hint = ""
#     for index in range(len(guess_word)):
#         if secret_word[index] == guess_word[index]:
#             hint += "O"
#         elif guess_word[index] in secret_word:
#             hint += "o"
#         else:
#             hint += "x"
#     if len(hint) < 5:
#         empty_spaces = 5 - len(hint)
#         hint += empty_spaces * "_"
#     return hint


# def play():
#     max_attempts = 6
#     guess_word = ""
#     attempt = 1
#     words = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
#     secret_word = random.choice(words)

#     while attempt <= max_attempts:
#         guess_word = input("Guess the word: ").upper()
#         if secret_word == guess_word:
#             return "You won"
#         print(get_word_hint(secret_word, guess_word))
#         attempt += 1
#     return "You lost"


# print(play())

# mOcKiNg SpOnGeBoB mEmE

# You may have seen the “Mocking Spongebob” meme format, which renders a statement in alternating uppercase and lowercase letters. Write a function named spongecase(text) that takes a string argument and returns the string in this format. Apply the following rules:

#     Leave non-letters unmodified.
#     Make the first letter lowercase.
#     For every letter, set the next letter to the opposite case. (Non-letter characters don’t change the case used for the next letter.)

# The program should ask the user for a sentence and then display that sentence with “Mocking Spongebob” casing:

# Enter a sentence:
# Hello. It is nice to meet you.
# hElLo. It Is NiCe To MeEt YoU.

# def spongecase(text):
#     mocking = ""
#     index = 1
#     last_was_lower = True
#     mocking = text[0].lower()
#     while index <= len(text)-1:
#         if text[index].isalpha():
#             if last_was_lower:
#                 mocking += text[index].upper()
#                 last_was_lower = False
#             else:
#                 mocking += text[index].lower()
#                 last_was_lower = True
#         else:
#             mocking += text[index]
#         index += 1
#     return mocking


# print(spongecase("Hello. It is nice to meet you."),
#       "→ Expected: hElLo. It Is NiCe To MeEt YoU.")
# print(spongecase("SPONGEBOB"), "→ Expected: sPoNgEbOb")
# print(spongecase("I love Python!"), "→ Expected: i LoVe PyThOn!")
# print(spongecase("abc"), "→ Expected: aBc")
# print(spongecase("a b c"), "→ Expected: a B c")
# print(spongecase("Hello!!!"), "→ Expected: hElLo!!!")
