# ----------------------------------------------------------------------
# Exercise AR1: Positional vs Keyword Arguments
# 1. Create a function called `calculate_bill` that takes two parameters:
#    - `amount` (cost of the meal)
#    - `tip_percent` (percentage to tip)
# 2. Inside, calculate total = amount + (amount * tip_percent / 100)
# 3. Print the total formatted to 2 decimal places.
# 4. Call the function using ONLY positional arguments (e.g., 50, 20).
# 5. Call the function using ONLY keyword arguments (swapped order).
# 6. Call the function using mixed arguments (positional for amount, keyword for tip).

# Write your code for Exercise AR1 below:

# def calculate_bill(amount, tip_percent):
#     total = amount + (amount * tip_percent / 100)
#     print(f"{total:.2f}")


# calculate_bill(50, 50)
# calculate_bill(tip_percent=20, amount=10)
# calculate_bill(40, tip_percent=40)

# ----------------------------------------------------------------------
# Exercise AR2: Default Arguments
# 1. Create a function called `greet_user` that takes:
#    - `name` (required)
#    - `greeting` (optional, default value should be "Hello")
#    - `punctuation` (optional, default value should be "!")
# 2. Return a string combining them (e.g., "Hello, Alice!")
# 3. Print the result of calling it with just "Bob".
# 4. Print the result of calling it with "Charlie" and greeting="Good morning".
# 5. Print the result of calling it with "Dave", greeting="Hey", punctuation="."

# Write your code for Exercise AR2 below:

# def greet_user(name, greeting="Hello", punctuation="!"):
#     return f"{greeting}, {name}{punctuation}"


# print(greet_user("Bob"))
# print(greet_user("Charlie", "Good morning"))
# print(greet_user("Dave", greeting="Hey", punctuation="."))

# ----------------------------------------------------------------------
# Exercise AR3: Arbitrary Positional Arguments (*args)
# 1. Create a function called `multiply_all` that accepts any number of numeric arguments.
# 2. Inside, multiply all the numbers together (start with a total of 1).
# 3. Return the final product.
# 4. Test with: multiply_all(1, 2, 3, 4) -> Expected: 24
# 5. Test with: multiply_all(5, 5) -> Expected: 25

# Write your code for Exercise AR3 below:

# def multiply_all(*args):
#     total = 1
#     for value in args:
#         total *= value
#     return total


# print((multiply_all(1, 2, 3, 4)))
# print((multiply_all(5, 5)))

# ----------------------------------------------------------------------
# Exercise AR4: Arbitrary Keyword Arguments (**kwargs)
# 1. Create a function called `build_profile` that accepts any number of keyword arguments.
# 2. Inside, print "User Profile:"
# 3. Loop through the dictionary of arguments and print each key and value
#    (Format: "- Key: Value")
# 4. Test with: build_profile(name="Alice", age=30, job="Engineer")
# 5. Test with: build_profile(username="gamer123", level=99)

# Write your code for Exercise AR4 below:

# def build_profile(**kwargs):
#     print("User Profile")
#     for key, value in kwargs.items():
#         print(f"- {key}: {value}")


# build_profile(name="Alice", age=30, job="Engineer")
# build_profile(username="gamer123", level=99)

# ----------------------------------------------------------------------
# Exercise AR5: Unpacking Arguments
# 1. Create a simple function `xyz_coordinates(x, y, z)` that prints:
#    "X: {x}, Y: {y}, Z: {z}"
# 2. Create a list: point_list = [10, 20, 30]
# 3. Create a dictionary: point_dict = {'x': 5, 'y': 15, 'z': 25}
# 4. Call the function by unpacking `point_list` into it.
# 5. Call the function by unpacking `point_dict` into it.

# Write your code for Exercise AR5 below:

# def xyz_coordinates(x, y, z):
#     print(f"X: {x}, Y: {y}, Z: {z}")


# point_list = [10, 20, 30]
# point_dict = {'x': 5, 'y': 15, 'z': 25}

# xyz_coordinates(*point_list)
# xyz_coordinates(**point_dict)

# ----------------------------------------------------------------------
# Exercise AR6: The Mutable Default Trap
# 1. Create a function called `add_item` that takes:
#    - `item`
#    - `item_list` (optional)
# 2. IMPORTANT: Implement the "Safe" pattern for mutable defaults.
#    - Do NOT set `item_list=[]` in the definition.
#    - Set it to None, and check inside the function.
# 3. Append the item to the list and return the list.
# 4. Test 1: print(add_item("Apple"))
# 5. Test 2: print(add_item("Banana"))
#    (If done correctly, Test 2 should NOT contain "Apple")

# Write your code for Exercise AR6 below:

# def add_item(item, item_list=None):
#     if item_list is None:
#         item_list = []
#     item_list.append(item)
#     return item_list


# print(add_item("Apple"))
# print(add_item("Banana"))
