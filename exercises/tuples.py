# ----------------------------------------------------------------------
# Exercise 1: Tuple Basics & Creation
#
# 1. Create a tuple called `colors` with 5 color names
# 2. Print the type of the tuple
# 3. Print the first color
# 4. Print the last color using negative indexing
# 5. Print the middle color
# 6. Try to change the second color (this should cause an error - comment it out after trying)
# 7. Print the length of the tuple
#
# Write your code for Exercise 1 below:

# colors = "black", "white", "red", "blue", "green"
# print(type(colors))
# print(colors[0])
# print(colors[-1])
# print(colors[len(colors)//2])

# # tuples cannot change!
# # colors[2] = "yellow"

# print(len(colors))

# ----------------------------------------------------------------------
# Exercise 2: Different Ways to Create Tuples
#
# 1. Create an empty tuple called `empty`
# 2. Create a tuple with one element (remember the comma!) called `single`
# 3. Create a tuple without parentheses: `no_parens` with values 1, 2, 3
# 4. Create a nested tuple with at least 2 levels
# 5. Print all four tuples and their types
# 6. Try creating a single-element tuple WITHOUT the comma and see what type it is
#
# Write your code for Exercise 2 below:s

# empty = ()
# single = (True,)
# no_parens = 1, 2, 3
# nested_tuple = (1, (2, 3), (4, (5, 6)))

# print(f"{empty} {type(empty)}")
# print(f"{single} {type(single)}")
# print(f"{no_parens} {type(no_parens)}")
# print(f"{nested_tuple} {type(nested_tuple)}")

# no_comma = 9
# print(type(no_comma))

# ----------------------------------------------------------------------
# Exercise 3: Tuple Indexing & Slicing
#
# 1. Create a tuple: numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 2. Access and print the element at index 5
# 3. Print elements from index 2 to 7
# 4. Print every second element
# 5. Print the tuple in reverse
# 6. Print the last 3 elements
# 7. Try to use negative indices to access elements
#
# Write your code for Exercise 3 below:

# numbers = tuple(range(10))
# print(numbers[5])
# print(numbers[2:7])
# print(numbers[1::2])
# print(numbers[::-1])
# print(numbers[-1])

# ----------------------------------------------------------------------
# Exercise 4: Iterating Over Tuples
#
# 1. Create a tuple: mixed = (42, "hello", 3.14, True, [1, 2, 3])
# 2. Use a for loop to print each element
# 3. Use enumerate() to print each element with its index
# 4. Use a for loop to print only the string elements (use type checking)
# 5. Count how many numeric types (int, float) are in the tuple
#
# Write your code for Exercise 4 below:

# mixed = (42, "hello", 3.14, True, [1, 2, 3])
# for i in mixed:
#     print(i)

# for index, value in enumerate(mixed):
#     print(index, value)

# for i in mixed:
#     if type(i) == str:
#         print(i)

# int_float = 0
# for i in mixed:
#     if type(i) == int or type(i) == float:
#         int_float += 1
#     if type(i) == list or type(i) == tuple:
#         for j in i:
#             if type(j) == int or type(j) == float:
#                 int_float += 1

# print(int_float)

# ----------------------------------------------------------------------
# Exercise 5: Tuple Unpacking - Basics
#
# 1. Create a tuple: coordinates = (10, 20, 30)
# 2. Unpack it into three variables: x, y, z
# 3. Print x, y, z separately
# 4. Create a tuple with 5 elements and unpack it in one line
# 5. Try unpacking with wrong number of variables (comment out after seeing error)
# 6. Use the unpacking operator * to print tuple elements separated by spaces
#
# Write your code for Exercise 5 below:

# coordinates = (10, 20, 30)
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)

# my_tuple = a, b, c, d, e = (1, 2, 3, 4, 5)
# print(*my_tuple)

# ----------------------------------------------------------------------
# Exercise 6: Tuple Packing
#
# 1. Create variables: name = "Alice", age = 25, city = "NYC"
# 2. Pack them into a tuple called `person` without using parentheses
# 3. Print the tuple
# 4. Create a tuple by packing values directly: my_tuple = 1, 2, 3, 4, 5
# 5. Print both tuples
# 6. Verify they are actually tuples using type()
#
# Write your code for Exercise 6 below:

# name = "Alice"
# age = 25
# city = "NYC"

# person = name, age, city
# print(person)

# my_tuple = 1, 2, 3, 4, 5
# print(my_tuple)

# print(type(person))
# print(type(my_tuple))

# ----------------------------------------------------------------------
# Exercise 7: Swapping Values
#
# 1. Create two variables: a = 100, b = 200
# 2. Print them: "Before: a = ..., b = ..."
# 3. Swap their values using tuple unpacking (one line!)
# 4. Print them: "After: a = ..., b = ..."
# 5. Create three variables and swap them in a rotation (a->b, b->c, c->a)
# 6. Verify the swap worked correctly
#
# Write your code for Exercise 7 below:

# a = 100
# b = 200

# print(f"Before: a={a}, b={b}")
# a, b = b, a
# print(f"After: a={a}, b={b}")

# x, y, z = 1, 2, 3
# x, y, z = y, z, x
# print(x, y, z)

# ----------------------------------------------------------------------
# Exercise 8: Tuple Operations
#
# 1. Create two tuples: tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6)
# 2. Concatenate them using +
# 3. Repeat tuple1 three times using *
# 4. Check if 2 is in tuple1 using `in` operator
# 5. Find the index of element 5 in tuple2
# 6. Count how many times 1 appears in tuple1
# 7. Find min, max, and sum of tuple1
#
# Write your code for Exercise 8 below:

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# three_times = (tuple1*3)

# if 2 in tuple1:
#     print("It is")
# else:
#     print("It's not")

# print(tuple2.index(5))

# print(tuple1.count(1))

# print(min(tuple1))
# print(max(tuple1))
# print(sum(tuple1))

# ----------------------------------------------------------------------
# Exercise 9: == vs is Operators
#
# 1. Create two tuples with same values: t1 = (1, 2, 3) and t2 = (1, 2, 3)
# 2. Check if t1 == t2 (values equal)
# 3. Check if t1 is t2 (same object in memory)
# 4. Print their id() values
# 5. Create two lists with same values: l1 = [1, 2, 3] and l2 = [1, 2, 3]
# 6. Check if l1 == l2
# 7. Check if l1 is l2
# 8. Print their id() values
# 9. Compare the results - why are tuples the same object but lists aren't?
#
# Write your code for Exercise 9 below:


# t1 = (1, 2, 3)
# t2 = (1, 2, 3)

# if t1 == t2:
#     print("They are equal")
# else:
#     print("They are not equal")

# if id(t1) == id(t2):
#     print("{t1} is {t2}")
# else:
#     print("{t1} is not {t2}")
#     print(id(t1))
#     print(id(t2))


# print(id(t1))
# print(id(t2))

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]

# if l1 == l2:
#     print("They are equal")
# else:
#     print("They are not equal")

# if id(l1) == id(l2):
#     print("{l1} is {l2}")
# else:
#     print("{l1} is not {l2}")
#     print(id(l1))
#     print(id(l2))

# ----------------------------------------------------------------------
# Exercise 10: Tuple Immutability
#
# 1. Create a tuple: my_tuple = (1, 2, 3, 4, 5)
# 2. Try to change the first element (should error - comment it out)
# 3. Try to append an element (should error - comment it out)
# 4. Try to remove an element (should error - comment it out)
# 5. Create a NEW tuple by concatenating: new_tuple = my_tuple + (6, 7)
# 6. Create a NEW tuple by slicing: sliced = my_tuple[1:4]
# 7. Print both new tuples
# 8. Verify the original tuple is unchanged
#
# Write your code for Exercise 10 below:


# ----------------------------------------------------------------------
# Exercise 11: Nested Tuples
#
# 1. Create a nested tuple representing a tic-tac-toe board:
#    board = (
#        ('X', 'O', 'X'),
#        ('O', 'X', 'O'),
#        ('O', 'X', 'X')
#    )
# 2. Access and print the center element (should be 'X')
# 3. Access and print the top-right corner
# 4. Print the entire first row
# 5. Use nested loops to print the entire board nicely
# 6. Count how many 'X' are in the entire board
#
# Write your code for Exercise 11 below:


# ----------------------------------------------------------------------
# Exercise 12: Tuple with Mutable Elements
#
# 1. Create a tuple containing a list: my_tuple = (1, 2, [3, 4, 5])
# 2. Print the tuple
# 3. Try to change the first element (should error - comment out)
# 4. Access the list inside the tuple and modify it (this WILL work!)
# 5. Print the tuple again - notice the list changed!
# 6. Explain in a comment why this works even though tuples are immutable
#
# Write your code for Exercise 12 below:


# ----------------------------------------------------------------------
# Advanced Exercise 13: Multiple Assignment & Unpacking
#
# 1. Create a function that returns multiple values as a tuple:
#    def get_stats(numbers):
#        return (min(numbers), max(numbers), sum(numbers))
# 2. Call it with a list of numbers and unpack the result into three variables
# 3. Print each statistic
# 4. Use the * operator to unpack remaining values:
#    first, *middle, last = (1, 2, 3, 4, 5, 6)
# 5. Print first, middle, and last
# 6. Create a tuple of tuples and unpack in a loop:
#    people = (("Alice", 25), ("Bob", 30), ("Charlie", 35))
#    for name, age in people:
#        print(f"{name} is {age} years old")
#
# Write your code for Advanced Exercise 13 below:


# ----------------------------------------------------------------------
# Advanced Exercise 14: Tuple Comparison
#
# 1. Create tuples: t1 = (1, 2, 3) and t2 = (1, 2, 4)
# 2. Compare them using <, >, <=, >= operators
# 3. Understand that tuples are compared element by element (lexicographically)
# 4. Create tuples: t3 = (1, 2) and t4 = (1, 2, 0)
# 5. Compare t3 and t4 - which is "greater"?
# 6. Sort a list of tuples: students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# 7. Print the sorted list (sorts by first element, then second if tied)
#
# Write your code for Advanced Exercise 14 below:


# ----------------------------------------------------------------------
# Advanced Exercise 15: When to Use Tuples vs Lists
#
# Create examples demonstrating when to use tuples:
#
# 1. Coordinates that shouldn't change: position = (x, y, z)
# 2. RGB color values: color = (255, 128, 0)
# 3. Database record: student = (id, name, grade)
# 4. Function returning multiple values
# 5. Dictionary keys (tuples can be keys, lists cannot!)
#
# Create examples demonstrating when to use lists:
#
# 1. Shopping list that changes: shopping = ["milk", "eggs"]
# 2. Collection of scores that grows: scores = [85, 90, 78]
# 3. Queue of tasks: tasks = ["task1", "task2"]
#
# Write code examples and comments explaining the choice
#
# Write your code for Advanced Exercise 15 below:
