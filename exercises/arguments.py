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

# ----------------------------------------------------------------------
# Exercise AR7: The "Kitchen Sink" (Mixing All Types)
# 1. Create a function called `super_printer` that takes:
#    - `title` (positional)
#    - `*args` (arbitrary positional)
#    - `**kwargs` (arbitrary keyword)
# 2. Print the title.
# 3. Print "Items:" followed by the args tuple.
# 4. Print "Settings:" followed by the kwargs dictionary.
# 5. Test it with: super_printer("My Data", 1, 2, 3, color="blue", debug=True)

# Write your code for Exercise AR7 below:

# def super_printer(title, *args, **kwargs):
#     print(f"{title}")
#     for item in args:
#         print(f"Items: {item}")
#     for key, value in kwargs.items():
#         print(f"Settings: {key} - {value}")


# super_printer("My Data", 1, 2, 3, color="blue", debug=True)

# ----------------------------------------------------------------------
# Exercise AR8: The String Joiner (*args)
# 1. Create a function called `join_words` that takes:
#    - `separator` (positional)
#    - `*words` (arbitrary arguments)
# 2. Use the string .join() method to join all words using the separator.
#    Hint: separator.join(words)
# 3. Return the result.
# 4. Test: print(join_words("-", "Python", "is", "cool")) -> "Python-is-cool"
# 5. Test: print(join_words(" ", "Hello", "World")) -> "Hello World"

# Write your code for Exercise AR8 below:

# def join_words(separator, *words):
#     joined_words = separator.join(words)
#     return joined_words


# print(join_words(" - ", "Python", "is", "cool"))
# print(join_words(" ", "Hello", "World"))

# ----------------------------------------------------------------------
# Exercise AR9: Dictionary Merging (Unpacking Trick)
# 1. You have two dictionaries:
#    default_settings = {"theme": "light", "notifications": True}
#    user_overrides = {"theme": "dark"}
# 2. Create a new dictionary called `final_config`.
# 3. Use the unpacking operator `**` inside the curly braces `{}` to merge them.
#    Syntax hint: {**dict1, **dict2}
#    (Note: dict2 wins if there are duplicate keys!)
# 4. Print `final_config`.

# Write your code for Exercise AR9 below:

# default_settings = {"theme": "light", "notifications": True}
# user_overrides = {"theme": "dark"}

# final_config = {**default_settings, **user_overrides}
# print(final_config)

# ----------------------------------------------------------------------
# Exercise AR10: The Wrapper (Passing Args Through)
# 1. Create a function `math_op(a, b)` that returns a + b.
# 2. Create a function `logger(func, *args)` that:
#    - Prints "Running function..."
#    - Calls `func` passing `*args` into it.
#    - Returns the result.
# 3. Test: print(logger(math_op, 10, 20))
#    (This teaches you how to pass arguments *through* a middleman function)

# Write your code for Exercise AR10 below:

# def math_op(a, b):
#     return a + b


# def logger(func, *args):
#     print("Running function... ")
#     return (func(*args))


# print(logger(math_op, 10, 20))

# ----------------------------------------------------------------------
# Exercise AR11: Kwargs Filtering
# 1. Create a function `create_user(**kwargs)`
# 2. Inside, check if the key "admin" is in kwargs.
#    - If yes, and it's True, print "Creating Admin Account"
#    - Otherwise, print "Creating Standard Account"
# 3. Print the full user data (kwargs) at the end.
# 4. Test: create_user(username="bob", admin=True)
# 5. Test: create_user(username="alice", admin=False)
# 6. Test: create_user(username="charlie")

# Write your code for Exercise AR11 below:

# def create_user(**kwargs):
#     if kwargs.get("admin") == True:
#         print("Creating Admin Account")
#     else:
#         print("Creating Standard Account")
#     for key, value in kwargs.items():
#         print(f"{key} - {value}")


# create_user(username="bob", admin=True)
# create_user(username="alice", admin=False)
# create_user(username="charlie")

# ----------------------------------------------------------------------
# Exercise AR12: Unpacking in Loops
# 1. Create a list of tuples, where each tuple is (name, age):
#    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# 2. Write a for loop that unpacks these directly in the loop statement.
#    Syntax: for name, age in people:
# 3. Inside the loop, print "{name} is {age} years old."
# (This is a very common form of unpacking!)

# Write your code for Exercise AR12 below:

# people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# for name, age in people:
#     print(f"{name} is {age} years old.")
