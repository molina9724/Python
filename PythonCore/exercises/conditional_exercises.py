# Python Conditional Logic Exercises
#
# For each exercise, write your code directly below the commented instructions.
# Remember to save your work and run the file to test your solutions.
#

# ----------------------------------------------------------------------
# Exercise 1: Number Checker
#
# 1. Ask the user to input a number.
# 2. Convert the input to an integer.
# 3. Write an if/elif/else statement to determine if the number is
#    positive, negative, or zero.
# 4. Print a message to the user indicating the result.
#
# Write your code for Exercise 1 below:
number = int(input("Type in a number: "))
if number > 0:
    print("Your number is positive")
elif number < 0:
    print("Your number is negative")
else:
    print("Your number is zero")


# ----------------------------------------------------------------------
# Exercise 2: Driving Eligibility
#
# 1. Ask the user for their age.
# 2. Ask the user if they have a driver's license (yes/no).
# 3. Convert the age to an integer.
# 4. Use an `if` statement with the `and` operator to check if the user is
#    18 or older AND has a license (assume "yes" is the answer for having one).
# 5. Print "You are eligible to drive." or "You are not eligible to drive."
#
# Write your code for Exercise 2 below:
age = int(input("Type in your age: "))
license = input("Do you have a license (yes/no)").lower()
if age >= 18 and license == "yes":
    print("You're eligible to drive!")
else:
    print("You're not eligible to drive")

# ----------------------------------------------------------------------
# Exercise 3: Ternary Operator for Fruit
#
# 1. Create a variable `fruit` and assign it the value "apple".
# 2. You want to create a second variable `is_apple` which should be `True`
#    if `fruit` is "apple" and `False` otherwise.
# 3. First, solve this using a standard if/else statement.
# 4. Then, rewrite the same logic using a single-line ternary operator.
# 5. Print the `is_apple` variable to see the result.
#
# Write your code for Exercise 3 below:
fruit = "apple"
if fruit == "apple":
    is_fruit = True
else:
    is_fruit = False
print(is_fruit)

is_fruit = True if fruit == "apple" else False
print(is_fruit)

# ----------------------------------------------------------------------
# Exercise 4: Checking for "Truthiness"
#
# In Python, non-empty strings and non-zero numbers are considered "True".
#
# 1. Ask the user to enter their name.
# 2. Write an `if` statement that checks if the user entered *anything*.
#    Instead of `if name != ""`, just use `if name:`. This is more "Pythonic".
# 3. If the name was entered, print "Hello, [Name]!".
# 4. If the name was not entered (the user just pressed Enter),
#    print "You didn't enter a name!".
#
# Write your code for Exercise 4 below:
name = input("Type in your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name!")

# ----------------------------------------------------------------------
# Advanced Exercise 5: Simple Discount Calculator
#
# This exercise combines numeric calculations with conditional logic.
#
# 1. Ask the user for the total price of their shopping cart.
# 2. Convert the price to a float.
# 3. If the price is over 100.00, apply a 10% discount.
#    - Calculate the discount amount (price * 0.10).
#    - Calculate the new final price.
#    - Print a message showing the original price, the discount, and the new price.
# 4. If the price is 100.00 or less, inform the user that no discount is applied.
# 5. Print the final price to be paid.
#
# Write your code for Advanced Exercise 5 below:
total_price = float(input("Type in the total price of your shopping cart: "))

if total_price > 100:
    discount = total_price * 0.1
    final_price = total_price - discount
    print(f"Original price: ${total_price:.2f}")
    print(f"Discount (10%): ${discount:.2f}")
    print(f"Final price: ${final_price:.2f}")
else:
    print("No discount applied.")
    print(f"Final price: ${total_price:.2f}")
