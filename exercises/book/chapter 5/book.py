# 1.Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
# spam = 5
# assert isinstance(spam, int), "spam must be an integer"
# assert spam >= 10, "spam must be <=9"

# 2.Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)

# eggs = "Hello"
# bacon = "hello"

# assert eggs.lower() != bacon.lower(), "eggs and bacon should have different values"

# 3.Write an assert statement that always triggers an AssertionError.

# assert False, "always triggering"

# 4.What two lines must your program have to be able to call logging.debug()?

# 5.What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?

# 6.What are the five logging levels?

# 7.What line of code can you add to disable all logging messages in your program?

# 8.Why is using logging messages better than using print() to display the same message?

# 9.What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

# 10.After you click Continue, when will the debugger stop?

# 11.What is a breakpoint?

# 12.How do you set a breakpoint on a line of code in Mu?

# Practice Program: Debugging Coin Toss
# The following program is meant to be a simple coin toss guessing game. The player gets two guesses. (It’s an easy game.) However, the program has multiple bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.

# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()

# toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# if toss == 0:
#     toss = "tails"
# else:
#     toss = "heads"

# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')
