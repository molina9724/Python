# =============================================================================
# 🐍 PYTHON ASSERTIONS BOOTCAMP - Master the assert Statement
# =============================================================================
# Assertions are a debugging tool that lets you test if a condition is True.
# If the condition is False, Python raises an AssertionError.
#
# Syntax: assert condition, "optional error message"
#
# IMPORTANT: Assertions can be disabled with `python -O script.py`
# So NEVER use them for data validation in production code!
# Use them for catching programmer errors during development.
# =============================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Basic Assert
# 1. Create a variable `age` with the value 25
# 2. Write an assert statement that checks if age is positive
# 3. Write another assert that checks if age is less than 150
# 4. Run the code - it should pass silently (no output means success!)
#
# Hint: assert condition, "error message"

# Write your code below:


# Test: Run this - if no error, your asserts passed!
# print("🟢 EASY 1: All assertions passed!")


# ----------------------------------------------------------------------
# 🟢 EASY 2: Assert with Message
# 1. Create a variable `username` with a non-empty string
# 2. Assert that username is not empty (len > 0)
# 3. Include a helpful error message in the assert
# 4. Try changing username to "" and see what happens
#
# Test: username = "alice" → should pass
#       username = "" → should raise AssertionError with your message

# Write your code below:


# print("🟢 EASY 2: Username is valid!")


# ----------------------------------------------------------------------
# 🟢 EASY 3: Assert Type Check
# 1. Create a function `double(n)` that doubles a number
# 2. At the start of the function, assert that n is an int or float
# 3. Return n * 2
#
# Test: double(5) → 10
# Test: double(3.5) → 7.0
# Test: double("hello") → AssertionError
#
# Hint: Use isinstance(n, (int, float))

# Write your code below:


# Test your solution:
# print("🟢 double(5):", double(5))         # → 10
# print("🟢 double(3.5):", double(3.5))     # → 7.0
# print("🟢 double('hello'):", double("hello"))  # → AssertionError!


# ----------------------------------------------------------------------
# 🟢 EASY 4: Assert Return Value
# 1. Create a function `get_first(items)` that returns the first item
# 2. Assert that items is not empty BEFORE trying to access items[0]
# 3. Return items[0]
#
# Test: get_first([1, 2, 3]) → 1
# Test: get_first(["a", "b"]) → "a"
# Test: get_first([]) → AssertionError

# Write your code below:


# Test your solution:
# print("🟢 get_first([1, 2, 3]):", get_first([1, 2, 3]))  # → 1
# print("🟢 get_first(['a', 'b']):", get_first(["a", "b"]))  # → "a"
# print("🟢 get_first([]):", get_first([]))  # → AssertionError


# ----------------------------------------------------------------------
# 🟡 MEDIUM 1: Multiple Assertions
# 1. Create a function `create_user(name, age, email)`
# 2. Assert that:
#    - name is a non-empty string
#    - age is between 0 and 150
#    - email contains "@"
# 3. Return a dictionary with the user data
#
# Test: create_user("Alice", 25, "alice@email.com") → works
# Test: create_user("", 25, "alice@email.com") → AssertionError (empty name)
# Test: create_user("Bob", -5, "bob@email.com") → AssertionError (invalid age)
# Test: create_user("Carol", 30, "invalid") → AssertionError (no @)

# Write your code below:


# Test your solution:
# print("🟡 create_user valid:", create_user("Alice", 25, "alice@email.com"))
# print("🟡 create_user empty name:", create_user("", 25, "alice@email.com"))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 2: Assert Preconditions
# 1. Create a function `divide(a, b)` that divides a by b
# 2. Assert preconditions:
#    - Both a and b are numbers (int or float)
#    - b is not zero
# 3. Return a / b
#
# Think: Why use assert instead of try/except here?
# Answer: assert documents what the function expects (programmer errors)
#         try/except handles runtime errors (user input, file not found, etc.)

# Write your code below:


# Test your solution:
# print("🟡 divide(10, 2):", divide(10, 2))  # → 5.0
# print("🟡 divide(7, 0):", divide(7, 0))    # → AssertionError


# ----------------------------------------------------------------------
# 🟡 MEDIUM 3: Assert Postconditions
# 1. Create a function `calculate_discount(price, discount_percent)`
# 2. Preconditions (assert before calculation):
#    - price >= 0
#    - 0 <= discount_percent <= 100
# 3. Calculate: final_price = price * (1 - discount_percent / 100)
# 4. Postcondition (assert after calculation):
#    - final_price >= 0
#    - final_price <= price
# 5. Return final_price
#
# Test: calculate_discount(100, 20) → 80.0
# Test: calculate_discount(50, 0) → 50.0
# Test: calculate_discount(100, 150) → AssertionError (invalid discount)

# Write your code below:


# Test your solution:
# print("🟡 calculate_discount(100, 20):", calculate_discount(100, 20))  # → 80.0
# print("🟡 calculate_discount(50, 0):", calculate_discount(50, 0))      # → 50.0
# print("🟡 calculate_discount(100, 150):", calculate_discount(100, 150))  # → Error


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: Assert with Collections
# 1. Create a function `average(numbers)`
# 2. Assert preconditions:
#    - numbers is a list
#    - numbers is not empty
#    - all items in numbers are int or float
# 3. Calculate and return the average
#
# Hint: Use all() with a generator expression for the type check
#       all(isinstance(n, (int, float)) for n in numbers)

# Write your code below:


# Test your solution:
# print("🟡 average([1, 2, 3, 4]):", average([1, 2, 3, 4]))  # → 2.5
# print("🟡 average([10]):", average([10]))                  # → 10.0
# print("🟡 average([]):", average([]))                      # → AssertionError
# print("🟡 average([1, 'two', 3]):", average([1, 'two', 3]))  # → AssertionError


# ----------------------------------------------------------------------
# 🟡 MEDIUM 5: Assert Invariants in a Class
# 1. Create a class `BankAccount` with:
#    - __init__(self, initial_balance) - assert balance >= 0
#    - deposit(self, amount) - assert amount > 0, then add to balance
#    - withdraw(self, amount) - assert amount > 0, assert enough balance
#    - After each operation, assert balance >= 0 (invariant)
# 2. The balance should NEVER go negative (that's the invariant!)
#
# Test: account = BankAccount(100)
#       account.deposit(50) → balance = 150
#       account.withdraw(30) → balance = 120
#       account.withdraw(200) → AssertionError (insufficient funds)

# Write your code below:


# Test your solution:
# account = BankAccount(100)
# print("🟡 Initial balance:", account.balance)  # → 100
# account.deposit(50)
# print("🟡 After deposit 50:", account.balance)  # → 150
# account.withdraw(30)
# print("🟡 After withdraw 30:", account.balance)  # → 120
# account.withdraw(200)  # → AssertionError!


# ----------------------------------------------------------------------
# 🔴 HARD 1: Assert in Recursive Function
# 1. Create a function `factorial(n)` that calculates n!
# 2. Assert preconditions:
#    - n is an integer
#    - n >= 0
# 3. Assert postcondition:
#    - result >= 1 (factorial is always at least 1)
# 4. Implement recursively: n! = n * (n-1)! with base case 0! = 1
#
# Test: factorial(5) → 120
# Test: factorial(0) → 1
# Test: factorial(-3) → AssertionError
# Test: factorial(3.5) → AssertionError

# Write your code below:


# Test your solution:
# print("🔴 factorial(5):", factorial(5))    # → 120
# print("🔴 factorial(0):", factorial(0))    # → 1
# print("🔴 factorial(1):", factorial(1))    # → 1
# print("🔴 factorial(-3):", factorial(-3))  # → AssertionError


# ----------------------------------------------------------------------
# 🔴 HARD 2: Assert with Data Validation
# 1. Create a function `parse_coordinate(coord_string)`
# 2. Input is a string like "12.5,45.3" (latitude,longitude)
# 3. Assert preconditions:
#    - coord_string is a string
#    - coord_string contains exactly one comma
# 4. Parse the string into lat and lon (floats)
# 5. Assert postconditions:
#    - -90 <= lat <= 90
#    - -180 <= lon <= 180
# 6. Return (lat, lon) as a tuple
#
# Test: parse_coordinate("40.7,-74.0") → (40.7, -74.0)
# Test: parse_coordinate("0,0") → (0.0, 0.0)
# Test: parse_coordinate("91,0") → AssertionError (lat out of range)
# Test: parse_coordinate("40.7;-74.0") → AssertionError (no comma)

# Write your code below:


# Test your solution:
# print("🔴 parse_coordinate('40.7,-74.0'):", parse_coordinate("40.7,-74.0"))
# print("🔴 parse_coordinate('0,0'):", parse_coordinate("0,0"))
# print("🔴 parse_coordinate('91,0'):", parse_coordinate("91,0"))  # → Error


# ----------------------------------------------------------------------
# 🔴 HARD 3: Assert in Sorting Algorithm
# 1. Create a function `is_sorted(items)` that returns True if list is sorted
# 2. Create a function `my_sort(items)` that:
#    - Assert precondition: items is a list
#    - Sort the list (you can use any method)
#    - Assert postcondition: result is_sorted (use your is_sorted function!)
#    - Return the sorted list
# 3. This demonstrates using assertions for testing algorithm correctness!
#
# Test: my_sort([3, 1, 4, 1, 5]) → [1, 1, 3, 4, 5]
# Test: my_sort([]) → []
# Test: my_sort([5, 4, 3, 2, 1]) → [1, 2, 3, 4, 5]

# Write your code below:


# Test your solution:
# print("🔴 my_sort([3, 1, 4, 1, 5]):", my_sort([3, 1, 4, 1, 5]))
# print("🔴 my_sort([]):", my_sort([]))
# print("🔴 my_sort([5, 4, 3, 2, 1]):", my_sort([5, 4, 3, 2, 1]))


# ----------------------------------------------------------------------
# 🔴 HARD 4: Design by Contract
# 1. Create a class `Stack` that implements a basic stack
# 2. Implement:
#    - __init__(self, max_size) - assert max_size > 0
#    - push(self, item) - assert not full, add item
#    - pop(self) - assert not empty, remove and return top item
#    - peek(self) - assert not empty, return top without removing
#    - is_empty(self) - return True if empty
#    - is_full(self) - return True if size == max_size
# 3. Each method should assert its preconditions!
#
# This is called "Design by Contract" - a powerful programming technique!

# Write your code below:


# Test your solution:
# stack = Stack(3)  # Max 3 items
# print("🔴 is_empty:", stack.is_empty())  # → True
# stack.push("a")
# stack.push("b")
# stack.push("c")
# print("🔴 is_full:", stack.is_full())    # → True
# # stack.push("d")  # → AssertionError (full!)
# print("🔴 peek:", stack.peek())          # → "c"
# print("🔴 pop:", stack.pop())            # → "c"
# print("🔴 pop:", stack.pop())            # → "b"


# ----------------------------------------------------------------------
# 🔴 HARD 5: Assert vs Exceptions - When to Use Which
# 1. Create TWO versions of a function `safe_divide`:
#
#    Version A: `safe_divide_assert(a, b)` - use assertions
#    Version B: `safe_divide_exception(a, b)` - use try/except
#
# 2. Both should handle division by zero, but:
#    - Assertions are for PROGRAMMER errors (bugs in code)
#    - Exceptions are for RUNTIME errors (bad user input, etc.)
#
# 3. Think about: When would you use each version?
#
# Answer in comments:
# - Use assert when: ???
# - Use exception when: ???

# Write your code below:


# Test your solution:
# print("🔴 safe_divide_assert(10, 2):", safe_divide_assert(10, 2))
# print("🔴 safe_divide_exception(10, 2):", safe_divide_exception(10, 2))
# print("🔴 safe_divide_assert(10, 0):", safe_divide_assert(10, 0))  # For internal use
# print("🔴 safe_divide_exception(10, 0):", safe_divide_exception(10, 0))  # For user input


# =============================================================================
# 📚 BONUS: Key Takeaways About Assertions
# =============================================================================
#
# ✅ USE ASSERTIONS FOR:
#    - Catching programmer errors during development
#    - Documenting what your code expects (preconditions)
#    - Verifying internal logic (postconditions, invariants)
#    - Testing during development
#
# ❌ DON'T USE ASSERTIONS FOR:
#    - Validating user input (use exceptions instead)
#    - Checking conditions that could legitimately fail at runtime
#    - Security checks (assertions can be disabled!)
#    - Anything in production that MUST be checked
#
# 💡 REMEMBER:
#    - python script.py → assertions are ENABLED
#    - python -O script.py → assertions are DISABLED (optimized mode)
#
# =============================================================================


# ----------------------------------------------------------------------
# 🏆 CHALLENGE: Write Your Own!
# Now that you understand assertions, create your own function that uses:
# 1. At least 2 precondition assertions
# 2. At least 1 postcondition assertion
# 3. A helpful error message for each assert
#
# Ideas:
# - A function that calculates percentage
# - A function that formats a phone number
# - A function that validates a password
# - A function that calculates BMI
#
# Be creative!

# Write your code below:
