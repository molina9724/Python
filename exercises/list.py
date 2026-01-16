# ----------------------------------------------------------------------
# Exercise 1: List Basics & Indexing
#
# 1. Create a list called `mixed_list` with at least 5 items of different types
#    (string, int, float, boolean)
# 2. Print the type of the list
# 3. Print the first item
# 4. Print the last item using negative indexing
# 5. Print the middle item
# 6. Change the second item to a new value
# 7. Print the updated list
#
# Write your code for Exercise 1 below:

# my_list = [1, 2.5, True, False, "No way"]
# print(type(my_list))
# print(my_list[0])
# print(my_list[-1])
# print(my_list[len(my_list)//2])
# my_list[1] = "I'm the new guy here"
# print(my_list)

# ----------------------------------------------------------------------
# Exercise 2: List Methods - Adding Items
#
# 1. Create an empty list called `fruits`
# 2. Use .append() to add "apple", "banana", "orange" one by one
# 3. Use .insert() to add "mango" at index 1
# 4. Use .extend() to add ["grape", "kiwi"] to the list
# 5. Print the final list
# 6. Print the length of the list
#
# Write your code for Exercise 2 below:

# fruits = []

# fruits.append("apple")
# fruits.append("banana")
# fruits.append("orange")

# fruits.insert(1, "mango")

# fruits.extend(["grape", "kiwi"])

# print(fruits)

# print(len(fruits))

# ----------------------------------------------------------------------
# Exercise 3: List Methods - Removing Items
#
# 1. Create a list: numbers = [10, 20, 30, 40, 50, 60, 70]
# 2. Remove the item 30 using .remove()
# 3. Remove the item at index 0 using .pop()
# 4. Remove the last item using .pop() without specifying index
# 5. Print the list after each removal
# 6. Clear the entire list using .clear()
# 7. Print the empty list
#
# Write your code for Exercise 3 below:

# numbers = [10, 20, 30, 40, 50, 60, 70]
# numbers.remove(30)
# print(numbers)
# numbers.pop(0)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.clear()
# print(numbers)

# ----------------------------------------------------------------------
# Exercise 4: List Slicing & Iteration
#
# 1. Create a list of numbers from 0 to 20: numbers = list(range(21))
# 2. Print every second number using slicing
# 3. Print numbers from index 5 to 15
# 4. Print the list in reverse using slicing
# 5. Use a for loop to print each number multiplied by 2
# 6. Use enumerate() to print each number with its index
#
# Write your code for Exercise 4 below:

# numbers = list(range(21))
# print(numbers[::2])
# print(numbers[5:15])
# print(numbers[::-1])

# for i in numbers:
#     print(i * 2)

# for index, number in enumerate(numbers):
#     print(f"{index} and {number}")


# ----------------------------------------------------------------------
# Exercise 5: List Searching & Sorting
#
# 1. Create a list: colors = ["red", "blue", "green", "yellow", "blue", "purple"]
# 2. Find the index of "green" using .index()
# 3. Count how many times "blue" appears using .count()
# 4. Check if "orange" is in the list using the `in` operator
# 5. Sort the list alphabetically using .sort()
# 6. Print the sorted list
# 7. Reverse the list using .reverse()
# 8. Print the reversed list
#
# Write your code for Exercise 5 below:

# colors = ["red", "blue", "green", "yellow", "blue", "purple"]
# print(colors.index("green"))
# print(colors.count("blue"))

# print("orange" in colors)  # Simple and clean!

# colors.sort()
# print(colors)

# colors.reverse()
# print(colors)

# ----------------------------------------------------------------------
# Exercise 6: Nested Lists (2D Lists)
#
# 1. Create a 2D list (list of lists) representing a 3x3 grid:
#    [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
# 2. Print the entire grid
# 3. Access and print the middle element (5)
# 4. Access and print the bottom-right element (9)
# 5. Change the top-left element to 0
# 6. Print the updated grid
# 7. Use nested loops to print each element
#
# Write your code for Exercise 6 below:

# grid = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
# print(grid)
# print(grid[len(grid)//2][len(grid)//2])
# print(grid[2][2])
# grid[0][0] = 0
# print(grid)

# for row in grid:
#     for element in row:
#         print(element)

# ----------------------------------------------------------------------
# Exercise 7: List Comprehension - Basics
#
# 1. Create a list of numbers from 1 to 10 using list comprehension
# 2. Create a list of squares (1, 4, 9, 16...) for numbers 1-10 using list comprehension
# 3. Create a list of even numbers from 1 to 20 using list comprehension
# 4. Create a list of odd numbers from 1 to 20 using list comprehension
# 5. Print all four lists
#
# Write your code for Exercise 7 below:


# ----------------------------------------------------------------------
# Exercise 8: List Comprehension - With Conditions
#
# 1. Create a list of words: words = ["hello", "world", "python", "list", "comprehension"]
# 2. Use list comprehension to create a new list with only words longer than 5 characters
# 3. Use list comprehension to create a new list with all words in uppercase
# 4. Use list comprehension to create a new list with the length of each word
# 5. Use list comprehension to create a new list with words that contain the letter 'o'
# 6. Print all the new lists
#
# Write your code for Exercise 8 below:


# ----------------------------------------------------------------------
# Exercise 9: List Operations & Built-in Functions
#
# 1. Create two lists: list1 = [1, 2, 3] and list2 = [4, 5, 6]
# 2. Concatenate them using + operator
# 3. Repeat list1 three times using * operator
# 4. Create a list of numbers: nums = [45, 12, 78, 34, 89, 23]
# 5. Find and print the maximum value using max()
# 6. Find and print the minimum value using min()
# 7. Find and print the sum using sum()
# 8. Find and print the average (sum divided by length)
#
# Write your code for Exercise 9 below:


# ----------------------------------------------------------------------
# Exercise 10: Shopping List Manager
#
# Create a shopping list program that:
# 1. Starts with an empty list
# 2. Asks the user to input 5 items (use a loop)
# 3. Prints the complete shopping list with numbers
# 4. Asks the user which item number to remove (convert to index)
# 5. Removes that item
# 6. Asks for a new item to add
# 7. Adds it to the list
# 8. Prints the final shopping list
# 9. Prints the total number of items
# 10. Sorts and prints the list alphabetically
#
# Write your code for Exercise 10 below:


# ----------------------------------------------------------------------
# Advanced Exercise 11: Number Analyzer
#
# Create a program that:
# 1. Asks the user to input numbers separated by spaces (e.g., "5 12 8 3 19 7")
# 2. Converts the input string into a list of integers
# 3. Calculates and prints:
#    - The sum of all numbers
#    - The average
#    - The maximum and minimum values
#    - How many even numbers there are
#    - How many odd numbers there are
# 4. Creates a new list with only numbers greater than 10
# 5. Creates a new list with each number doubled
# 6. Prints both new lists
#
# Write your code for Advanced Exercise 11 below:


# ----------------------------------------------------------------------
# Advanced Exercise 12: List Manipulation Challenge
#
# Given a list of mixed data types:
# data = [1, "hello", 3.14, True, "world", 42, False, "python", 2.71, 100]
#
# 1. Create separate lists for:
#    - Only integers
#    - Only strings
#    - Only floats
#    - Only booleans
# 2. Print each separated list
# 3. Print the count of each type
# 4. Create a new list with all strings converted to uppercase
# 5. Create a new list with all numbers (int and float) multiplied by 2
#
# Hint: Use type() to check the type of each item
#
# Write your code for Advanced Exercise 12 below:
