# Word Match Game

# The word game Jotto was created in 1955, and the 1980s game show Lingo later repurposed its concept (which you might recognize as another, more recent, game). You can make your own version of this game in Python.

# Create a program that has the user guess a five-letter word. Your code should include a function named get_word_hint(secret_word, guess_word) that returns a five-character string of hints. The hints are an uppercase O for a correct letter in the same place in the secret word, a lowercase o for a correct letter in a different place in the secret word, and x for letters that are not in the secret word. If the guessed word is the same as the secret word, the function should return OOOOO.

# For example, if the secret word is CRANE and the guess word is CANDY, get_word_hint('CRANE', 'CANDY') should return Oooxx because the first letter in CANDY matches the first letter in the secret word, CRANE. The next two hint characters are oo because the A and N characters in CANDY exist in CRANE but at different indexes. The last two hint characters are xx because the D and Y in CANDY don’t appear in CRANE at all.

# The rest of the program should randomly choose a secret word from a list of five-character words and then give the user six tries to guess it. You can use this list of words:


import random


def get_word_hint(secret_word, guess_word):
    hint = ""
    for index in range(len(secret_word)):
        if secret_word[index] == guess_word[index]:
            hint += "O"
        elif guess_word[index] in secret_word:
            hint += "o"
        else:
            hint += "x"
    return hint


words = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
secret_word = random.choice(words)
print(secret_word)
print("BRICK")
print(get_word_hint(secret_word, "BRICK"))
