# ----------------------------------------------------------------------
# Exercise 1: Creating Dictionaries - Different Ways
#
# 1. Create a dictionary using curly braces:
#    person = {"name": "Alice", "age": 25, "city": "NYC"}
# 2. Create a dictionary using dict() function:
#    person2 = dict(name="Bob", age=30, city="LA")
# 3. Create an empty dictionary both ways
# 4. Print all dictionaries and their types
# 5. Create a dictionary with mixed value types:
#    mixed = {"string": "hello", "number": 42, "list": [1,2,3], "bool": True}
# 6. Print the mixed dictionary
#
# Write your code for Exercise 1 below:

# person = {"name": "Alice", "age": 25, "city": "NYC"}
# person2 = dict(name="Bob", age=30, city="LA")

# empty1 = {}
# print(empty1)
# print(type(empty1))

# empty2 = dict()
# print(empty2)
# print(type(empty2))

# mixed = {"string": "hello", "number": 42, "list": [1, 2, 3], "bool": True}
# print(mixed)

# ----------------------------------------------------------------------
# Exercise 2: Accessing Dictionary Values
#
# 1. Create a dictionary:
#    student = {"name": "Charlie", "age": 20, "grade": 85, "courses": ["Math", "Science"]}
# 2. Access and print the name
# 3. Access and print the grade
# 4. Access and print the courses list
# 5. Try to access a key that doesn't exist: student["email"] (error - comment out!)
# 6. Use .get() method instead: student.get("email") (returns None, no error!)
# 7. Use .get() with default: student.get("email", "No email provided")
#
# Write your code for Exercise 2 below:

# student = {"name": "Charlie", "age": 20,
#            "grade": 85, "courses": ["Math", "Science"]}

# print(student["name"])
# print(student["grade"])
# print(student["courses"])

# # You cannot access a key that doesn't exist
# # print(student["last_name"])

# print(student.get("email"))
# print(student.get("email", "No email provided"))

# ----------------------------------------------------------------------
# Exercise 3: Adding and Modifying Dictionary Items
#
# 1. Create a dictionary: inventory = {"apples": 10, "bananas": 5}
# 2. Print the original dictionary
# 3. Add a new item: inventory["oranges"] = 8
# 4. Modify existing item: inventory["apples"] = 15
# 5. Print the updated dictionary
# 6. Add multiple items at once using .update():
#    inventory.update({"grapes": 20, "pears": 12})
# 7. Print the final dictionary
#
# Write your code for Exercise 3 below:

# inventory = {"apples": 10, "bananas": 5}
# print(inventory)
# inventory["oranges"] = 8
# inventory["apples"] = 15
# print(inventory)
# inventory.update({"grapes": 20, "pears": 12})
# print(inventory)

# ----------------------------------------------------------------------
# Exercise 4: Removing Dictionary Items
#
# 1. Create a dictionary:
#    data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# 2. Remove item using del: del data["a"]
# 3. Remove item using .pop(): value = data.pop("b")
# 4. Print the removed value
# 5. Try .pop() with default: data.pop("z", "Not found")
# 6. Remove and return last item: data.popitem()
# 7. Print the final dictionary
#
# Write your code for Exercise 4 below:

# data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# del data["a"]
# value = data.pop("b")
# print(value)

# value2 = data.pop("z", "Not found")
# print(value2)

# last_item = data.popitem()
# print(last_item)

# print(data)


# ----------------------------------------------------------------------
# Exercise 5: Dictionary Methods - keys(), values(), items()
#
# 1. Create a dictionary:
#    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
# 2. Get all keys: keys = scores.keys()
# 3. Get all values: values = scores.values()
# 4. Get all items (key-value pairs): items = scores.items()
# 5. Print each (notice the types - dict_keys, dict_values, dict_items)
# 6. Convert keys to list: list(scores.keys())
# 7. Convert values to list: list(scores.values())
#
# Write your code for Exercise 5 below:

# scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
# keys = scores.keys()
# values = scores.values()
# items = scores.items()

# print(keys)
# print(values)
# print(items)

# keys_list = list(keys)
# print(keys_list)

# values_list = list(values)
# print(values_list)

# ----------------------------------------------------------------------
# Exercise 6: Iterating Over Dictionaries
#
# 1. Create a dictionary:
#    person = {"name": "Alice", "age": 25, "city": "NYC", "job": "Engineer"}
# 2. Iterate over keys only:
#    for key in person:
#        print(key)
# 3. Iterate over values only:
#    for value in person.values():
#        print(value)
# 4. Iterate over key-value pairs:
#    for key, value in person.items():
#        print(f"{key}: {value}")
# 5. Iterate with enumerate to get index too
#
# Write your code for Exercise 6 below:

# person = {"name": "Alice", "age": 25, "city": "NYC", "job": "Engineer"}
# for key in person:
#     print(key)

# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)

# for index, value in enumerate(person):
#     print(index, value)

# ----------------------------------------------------------------------
# Exercise 7: Dictionary Membership Testing
#
# 1. Create a dictionary:
#    config = {"debug": True, "timeout": 30, "retries": 3}
# 2. Check if "debug" is a key: "debug" in config
# 3. Check if "verbose" is a key: "verbose" in config
# 4. Check if a VALUE exists (need to check in .values()):
#    30 in config.values()
# 5. Safe access pattern:
#    if "timeout" in config:
#        print(config["timeout"])
# 6. Use .get() as alternative: config.get("timeout", 60)
#
# Write your code for Exercise 7 below:

# config = {"debug": True, "timeout": 30, "retries": 3}
# if "debug" in config:
#     print(True)

# if "verbose" in config:
#     print(True)
# else:
#     print(False)

# if 50 in config.values():
#     print(True)
# else:
#     print(False)

# if "timeout" in config:
#     print(config["timeout"])

# ----------------------------------------------------------------------
# Exercise 8: Nested Dictionaries
#
# 1. Create a nested dictionary:
#    students = {
#        "student1": {"name": "Alice", "grade": 85, "courses": ["Math", "Science"]},
#        "student2": {"name": "Bob", "grade": 92, "courses": ["English", "History"]},
#        "student3": {"name": "Charlie", "grade": 78, "courses": ["Math", "Art"]}
#    }
# 2. Access Alice's grade: students["student1"]["grade"]
# 3. Access Bob's courses: students["student2"]["courses"]
# 4. Add a new student
# 5. Modify Charlie's grade
# 6. Iterate through all students and print their names and grades
#
# Write your code for Exercise 8 below:

# students = {
#     "student1": {"name": "Alice", "grade": 85, "courses": ["Math", "Science"]},
#     "student2": {"name": "Bob", "grade": 85, "courses": ["English", "History"]},
#     "student3": {"name": "Charlie", "grade": 78, "courses": ["Math", "Art"]}
# }

# print(students["student1"]["grade"])
# print(students["student2"]["courses"])

# students["student4"] = {"name": "Daniel",
#                         "grade": 100, "courses": ["Art", "Python"]}
# print(students)

# for value in students.values():
#     print(value["name"], value["grade"])

# ----------------------------------------------------------------------
# Exercise 9: Dictionary Comprehension
#
# 1. Create a dictionary of squares:
#    squares = {x: x**2 for x in range(1, 6)}
# 2. Create a dictionary from two lists:
#    keys = ["a", "b", "c"]
#    values = [1, 2, 3]
#    combined = {k: v for k, v in zip(keys, values)}
# 3. Filter dictionary with condition:
#    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
#    high_scores = {k: v for k, v in scores.items() if v >= 90}
# 4. Transform values:
#    doubled = {k: v*2 for k, v in scores.items()}
#
# Write your code for Exercise 9 below:


# ----------------------------------------------------------------------
# Exercise 10: Dictionary from Lists using zip()
#
# 1. Create two lists:
#    names = ["Alice", "Bob", "Charlie"]
#    ages = [25, 30, 35]
# 2. Combine using zip() and dict():
#    people = dict(zip(names, ages))
# 3. Print the dictionary
# 4. Try with three lists (keys, values1, values2) - how to handle?
# 5. Create nested dictionary from multiple lists
#
# Write your code for Exercise 10 below:


# ----------------------------------------------------------------------
# Exercise 11: Dictionary .get() vs Direct Access
#
# 1. Create a dictionary: data = {"a": 1, "b": 2, "c": 3}
# 2. Access existing key directly: data["a"]
# 3. Access existing key with .get(): data.get("a")
# 4. Try to access non-existing key directly (error - comment out!):
#    # data["z"]
# 5. Access non-existing key with .get(): data.get("z")
# 6. Access non-existing key with default: data.get("z", 0)
# 7. Understand when to use each approach
#
# Write your code for Exercise 11 below:


# ----------------------------------------------------------------------
# Exercise 12: Dictionary .setdefault()
#
# 1. Create a dictionary: counts = {"a": 1, "b": 2}
# 2. Use .setdefault() on existing key: counts.setdefault("a", 0)
# 3. Use .setdefault() on new key: counts.setdefault("c", 0)
# 4. Print the dictionary (notice "c" was added!)
# 5. Compare to .get() - .get() doesn't modify the dictionary
# 6. Use case: counting occurrences in a list
#    letters = ["a", "b", "a", "c", "b", "a"]
#    for letter in letters:
#        counts.setdefault(letter, 0)
#        counts[letter] += 1
#
# Write your code for Exercise 12 below:


# ----------------------------------------------------------------------
# Exercise 13: Merging Dictionaries
#
# 1. Create two dictionaries:
#    dict1 = {"a": 1, "b": 2}
#    dict2 = {"c": 3, "d": 4}
# 2. Merge using .update(): dict1.update(dict2)
# 3. Merge using unpacking (Python 3.5+): merged = {**dict1, **dict2}
# 4. Merge using | operator (Python 3.9+): merged = dict1 | dict2
# 5. Handle conflicts (same keys):
#    dict1 = {"a": 1, "b": 2}
#    dict2 = {"b": 3, "c": 4}
#    merged = dict1 | dict2  # dict2 values win
# 6. Print all results
#
# Write your code for Exercise 13 below:


# ----------------------------------------------------------------------
# Exercise 14: Counting with Dictionaries
#
# 1. Create a list of items:
#    fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
# 2. Count occurrences manually using a dictionary:
#    counts = {}
#    for fruit in fruits:
#        if fruit in counts:
#            counts[fruit] += 1
#        else:
#            counts[fruit] = 1
# 3. Print the counts
# 4. Alternative using .get():
#    counts = {}
#    for fruit in fruits:
#        counts[fruit] = counts.get(fruit, 0) + 1
# 5. Compare both methods
#
# Write your code for Exercise 14 below:


# ----------------------------------------------------------------------
# Exercise 15: Dictionary Keys Must Be Hashable
#
# 1. Create dictionary with valid keys:
#    valid = {
#        1: "int key",
#        "hello": "string key",
#        (1, 2): "tuple key",
#        frozenset([1, 2]): "frozenset key"
#    }
# 2. Try invalid keys (comment out after seeing errors):
#    # invalid = {[1, 2]: "list key"}  # Error!
#    # invalid = {{1, 2}: "set key"}   # Error!
# 3. Understand: keys must be immutable (hashable)
# 4. Values can be anything:
#    flexible = {"key1": [1, 2, 3], "key2": {1, 2, 3}, "key3": {"nested": "dict"}}
#
# Write your code for Exercise 15 below:


# ----------------------------------------------------------------------
# Exercise 16: Practical Use Case - Student Records
#
# 1. Create a student database:
#    students = {}
# 2. Add students with IDs as keys:
#    students[101] = {"name": "Alice", "grade": 85, "courses": ["Math", "Science"]}
#    students[102] = {"name": "Bob", "grade": 92, "courses": ["English", "History"]}
# 3. Look up a student by ID
# 4. Update a student's grade
# 5. Add a new course to a student
# 6. Print all students with grades above 90
# 7. Calculate average grade
#
# Write your code for Exercise 16 below:


# ----------------------------------------------------------------------
# Exercise 17: Dictionary vs List Performance (Conceptual)
#
# 1. Create a large dictionary: big_dict = {i: i*2 for i in range(100000)}
# 2. Create a large list: big_list = list(range(100000))
# 3. Understand conceptually:
#    - Dictionary lookup by key: O(1) - constant time
#    - List search for value: O(n) - linear time
# 4. Dictionary access: big_dict[50000] - instant!
# 5. List search: 50000 in big_list - has to check each element
# 6. Write comments explaining when to use each
#
# Write your code for Exercise 17 below:


# ----------------------------------------------------------------------
# Advanced Exercise 18: Inverting a Dictionary
#
# 1. Create a dictionary: original = {"a": 1, "b": 2, "c": 3}
# 2. Invert it (swap keys and values):
#    inverted = {v: k for k, v in original.items()}
# 3. Print both
# 4. Handle duplicate values (what happens?):
#    original = {"a": 1, "b": 2, "c": 1}
#    inverted = {v: k for k, v in original.items()}
#    # Only one "a" or "c" will survive!
# 5. Solution: make values lists:
#    inverted = {}
#    for k, v in original.items():
#        inverted.setdefault(v, []).append(k)
#
# Write your code for Advanced Exercise 18 below:


# ----------------------------------------------------------------------
# Advanced Exercise 19: Default Dictionary Behavior
#
# 1. Simulate defaultdict behavior manually:
#    counts = {}
#    items = ["a", "b", "a", "c", "b", "a"]
# 2. Count using .setdefault():
#    for item in items:
#        counts.setdefault(item, 0)
#        counts[item] += 1
# 3. Count using .get():
#    counts = {}
#    for item in items:
#        counts[item] = counts.get(item, 0) + 1
# 4. Compare both approaches
# 5. Understand when each is clearer
#
# Write your code for Advanced Exercise 19 below:


# ----------------------------------------------------------------------
# Advanced Exercise 20: Dictionary as a Cache/Lookup Table
#
# 1. Create a function that's expensive to compute:
#    def fibonacci(n):
#        if n <= 1:
#            return n
#        return fibonacci(n-1) + fibonacci(n-2)
# 2. Add caching with a dictionary:
#    cache = {}
#    def fibonacci_cached(n):
#        if n in cache:
#            return cache[n]
#        if n <= 1:
#            return n
#        result = fibonacci_cached(n-1) + fibonacci_cached(n-2)
#        cache[n] = result
#        return result
# 3. Compare performance conceptually
# 4. Understand memoization pattern
#
# Write your code for Advanced Exercise 20 below:
