# ======================================================================
# 🐍 PYTHON EXCEPTION HANDLING - COMPREHENSIVE EXERCISES
# ======================================================================
# Topics: try, except, else, finally, raise, custom exceptions
# Instructions: Complete each exercise, test your solutions
# ======================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Basic Try/Except
# Create a function safe_divide(a, b)
# - Return the result of a / b
# - If division by zero occurs, return None
#
# Test: safe_divide(10, 2) -> 5.0
# Test: safe_divide(10, 0) -> None
# Test: safe_divide(0, 5) -> 0.0
# Test: safe_divide(-10, 2) -> -5.0
# ----------------------------------------------------------------------

# Write your code below:

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

# Test your solution:
# print("🟢 safe_divide(10, 2):", safe_divide(10, 2))
# print("🟢 safe_divide(10, 0):", safe_divide(10, 0))
# print("🟢 safe_divide(0, 5):", safe_divide(0, 5))
# print("🟢 safe_divide(-10, 2):", safe_divide(-10, 2))


# ----------------------------------------------------------------------
# 🟢 EASY 2: Converting User Input
# Create a function convert_to_int(value)
# - Try to convert value to an integer
# - If successful, return the integer
# - If it fails, return 0
#
# Test: convert_to_int("42") -> 42
# Test: convert_to_int("3.14") -> 0
# Test: convert_to_int("hello") -> 0
# Test: convert_to_int("") -> 0
# Test: convert_to_int(100) -> 100
# ----------------------------------------------------------------------

# Write your code below:

# def convert_to_int(value):
#     try:
#         return int(value)
#     except ValueError:
#         return 0


# Test your solution:
# print("🟢 convert_to_int('42'):", convert_to_int("42"))
# print("🟢 convert_to_int('3.14'):", convert_to_int("3.14"))
# print("🟢 convert_to_int('hello'):", convert_to_int("hello"))
# print("🟢 convert_to_int(''):", convert_to_int(""))
# print("🟢 convert_to_int(100):", convert_to_int(100))


# ----------------------------------------------------------------------
# 🟢 EASY 3: Safe List Access
# Create a function safe_get(lst, index)
# - Return the element at the given index
# - If index is out of range, return None
#
# Test: safe_get([1, 2, 3], 0) -> 1
# Test: safe_get([1, 2, 3], 2) -> 3
# Test: safe_get([1, 2, 3], 10) -> None
# Test: safe_get([1, 2, 3], -1) -> 3
# Test: safe_get([], 0) -> None
# ----------------------------------------------------------------------

# Write your code below:

# def safe_get(lst, index):
#     try:
#         return lst[index]
#     except:
#         return

# # Test your solution:
# print("🟢 safe_get([1,2,3], 0):", safe_get([1, 2, 3], 0))
# print("🟢 safe_get([1,2,3], 2):", safe_get([1, 2, 3], 2))
# print("🟢 safe_get([1,2,3], 10):", safe_get([1, 2, 3], 10))
# print("🟢 safe_get([1,2,3], -1):", safe_get([1, 2, 3], -1))
# print("🟢 safe_get([], 0):", safe_get([], 0))


# ----------------------------------------------------------------------
# 🟢 EASY 4: Safe Dictionary Access
# Create a function safe_dict_get(dictionary, key)
# - Return the value for the given key
# - If key doesn't exist, return "Key not found"
#
# Test: safe_dict_get({"a": 1, "b": 2}, "a") -> 1
# Test: safe_dict_get({"a": 1, "b": 2}, "c") -> "Key not found"
# Test: safe_dict_get({}, "x") -> "Key not found"
# Test: safe_dict_get({"name": "Alice"}, "name") -> "Alice"
# ----------------------------------------------------------------------

# Write your code below:

# def safe_dict_get(dictionary, key):
#     try:
#         return dictionary[key]
#     except:
#         return "Key not found"

# # Test your solution:
# print("🟢 safe_dict_get({'a':1,'b':2}, 'a'):", safe_dict_get({"a": 1, "b": 2}, "a"))
# print("🟢 safe_dict_get({'a':1,'b':2}, 'c'):", safe_dict_get({"a": 1, "b": 2}, "c"))
# print("🟢 safe_dict_get({}, 'x'):", safe_dict_get({}, "x"))

# ----------------------------------------------------------------------
# 🟢 EASY 5: Catching Multiple Exceptions
# Create a function parse_and_access(data, index)
# - data is a string representation of a list like "[1, 2, 3]"
# - Parse the string using eval() and access element at index
# - Handle: SyntaxError, IndexError, TypeError
# - Return the element or "Error occurred"
#
# Test: parse_and_access("[1, 2, 3]", 0) -> 1
# Test: parse_and_access("[1, 2, 3]", 10) -> "Error occurred"
# Test: parse_and_access("invalid", 0) -> "Error occurred"
# Test: parse_and_access("[1, 2, 3]", "a") -> "Error occurred"
# ----------------------------------------------------------------------

# Write your code below:

# def parse_and_access(data, index):
#     try:
#         return eval(data)[index]
#     except (IndexError, SyntaxError, TypeError, NameError):
#         return "Error occurred"


# # Test your solution:
# print("🟢 parse_and_access('[1,2,3]', 0):", parse_and_access("[1, 2, 3]", 0))
# print("🟢 parse_and_access('[1,2,3]', 10):", parse_and_access("[1, 2, 3]", 10))
# print("🟢 parse_and_access('invalid', 0):", parse_and_access("invalid", 0))
# print("🟢 parse_and_access('[1,2,3]', 'a'):", parse_and_access("[1, 2, 3]", "a"))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 1: Exception with Error Message
# Create a function divide_with_message(a, b)
# - Return a tuple: (success: bool, result_or_message: float/str)
# - On success: (True, result)
# - On ZeroDivisionError: (False, "Cannot divide by zero")
# - On TypeError: (False, "Invalid types for division")
#
# Test: divide_with_message(10, 2) -> (True, 5.0)
# Test: divide_with_message(10, 0) -> (False, "Cannot divide by zero")
# Test: divide_with_message("10", 2) -> (False, "Invalid types for division")
# Test: divide_with_message(10, "2") -> (False, "Invalid types for division")
# ----------------------------------------------------------------------

# Write your code below:

# def divide_with_message(a, b):
#     try:
#         return (True, a/b)
#     except ZeroDivisionError:
#         return (False, "Cannot divide by zero")
#     except TypeError:
#         return (False, "Invalid types for division")


# # Test your solution:
# print("🟡 divide_with_message(10, 2):", divide_with_message(10, 2))
# print("🟡 divide_with_message(10, 0):", divide_with_message(10, 0))
# print("🟡 divide_with_message('10', 2):", divide_with_message("10", 2))
# print("🟡 divide_with_message(10, 0):", divide_with_message(0, 5))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 2: Try/Except/Else
# Create a function read_positive_number(value)
# - Convert value to float
# - If conversion succeeds AND number is positive, return the number
# - If conversion succeeds but number is negative/zero, return "Must be positive"
# - If conversion fails, return "Invalid number"
#
# Test: read_positive_number("3.14") -> 3.14
# Test: read_positive_number("-5") -> "Must be positive"
# Test: read_positive_number("0") -> "Must be positive"
# Test: read_positive_number("abc") -> "Invalid number"
# Test: read_positive_number("100") -> 100.0
# ----------------------------------------------------------------------

# Write your code below:

# def read_positive_number(value):
#     try:
#         num = float(value)
#         return num if num > 0 else "Must be positive"
#     except ValueError:
#         return "Invalid number"


# # Test your solution:
# print("🟡 read_positive_number('3.14'):", read_positive_number("3.14"))
# print("🟡 read_positive_number('-5'):", read_positive_number("-5"))
# print("🟡 read_positive_number('0'):", read_positive_number("0"))
# print("🟡 read_positive_number('abc'):", read_positive_number("abc"))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 3: Try/Except/Finally
# Create a function process_file_simulation(filename)
# - Simulate file operations (no actual file needed)
# - If filename is "valid.txt", return "File processed"
# - If filename is "error.txt", raise an exception during "processing"
# - If filename is anything else, return "File not found"
# - Always print "Cleanup complete" at the end (use finally)
# - Return the appropriate result
#
# Test: process_file_simulation("valid.txt") -> "File processed" (prints "Cleanup complete")
# Test: process_file_simulation("error.txt") -> "Processing error" (prints "Cleanup complete")
# Test: process_file_simulation("other.txt") -> "File not found" (prints "Cleanup complete")
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🟡 Result:", process_file_simulation("valid.txt"))
# print("🟡 Result:", process_file_simulation("error.txt"))
# print("🟡 Result:", process_file_simulation("other.txt"))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: Raising Exceptions
# Create a function validate_age(age)
# - Raise ValueError if age is not an integer
# - Raise ValueError if age is negative
# - Raise ValueError if age is greater than 150
# - Return "Valid age" if all checks pass
#
# Test: validate_age(25) -> "Valid age"
# Test: validate_age(-5) -> raises ValueError
# Test: validate_age(200) -> raises ValueError
# Test: validate_age("25") -> raises ValueError
# Test: validate_age(0) -> "Valid age"
# Test: validate_age(150) -> "Valid age"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🟡 validate_age(25):", validate_age(25))
# print("🟡 validate_age(0):", validate_age(0))
# try:
#     print("🟡 validate_age(-5):", validate_age(-5))
# except ValueError as e:
#     print("🟡 validate_age(-5): ValueError -", e)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 5: Nested Try/Except
# Create a function complex_operation(data)
# - data is a dictionary that should have keys: "values" (list) and "index" (int)
# - Get the list from data["values"]
# - Get the index from data["index"]
# - Return the element at that index divided by 10
# - Handle all possible errors with specific messages:
#   - KeyError: "Missing required key"
#   - IndexError: "Index out of range"
#   - TypeError: "Invalid data type"
#   - ZeroDivisionError: "Division error"
#
# Test: complex_operation({"values": [100, 200, 300], "index": 1}) -> 20.0
# Test: complex_operation({"values": [100], "index": 5}) -> "Index out of range"
# Test: complex_operation({"index": 0}) -> "Missing required key"
# Test: complex_operation({"values": "not a list", "index": 0}) -> "Invalid data type"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🟡 complex_operation({'values': [100,200,300], 'index': 1}):",
#       complex_operation({"values": [100, 200, 300], "index": 1}))
# print("🟡 complex_operation({'values': [100], 'index': 5}):",
#       complex_operation({"values": [100], "index": 5}))
# print("🟡 complex_operation({'index': 0}):",
#       complex_operation({"index": 0}))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: Exception Information
# Create a function detailed_error_info(func, *args)
# - Try to call func with the given args
# - If successful, return {"success": True, "result": result}
# - If exception occurs, return:
#   {
#     "success": False,
#     "error_type": type name as string,
#     "error_message": the exception message
#   }
#
# Test: detailed_error_info(int, "42") -> {"success": True, "result": 42}
# Test: detailed_error_info(int, "abc") -> {"success": False, "error_type": "ValueError", ...}
# Test: detailed_error_info(lambda x: 1/x, 0) -> {"success": False, "error_type": "ZeroDivisionError", ...}
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🟡 detailed_error_info(int, '42'):", detailed_error_info(int, "42"))
# print("🟡 detailed_error_info(int, 'abc'):", detailed_error_info(int, "abc"))
# print("🟡 detailed_error_info(lambda x: 1/x, 0):", detailed_error_info(lambda x: 1/x, 0))


# ----------------------------------------------------------------------
# 🔴 HARD 1: Custom Exception Classes
# Create the following:
# 1. A custom exception class ValidationError that inherits from Exception
# 2. A custom exception class AgeValidationError that inherits from ValidationError
# 3. A custom exception class EmailValidationError that inherits from ValidationError
#
# Then create function validate_user(name, age, email):
# - Raise AgeValidationError if age < 0 or age > 150
# - Raise EmailValidationError if "@" not in email
# - Raise ValidationError if name is empty
# - Return "User valid" if all pass
#
# Test: validate_user("Alice", 25, "alice@email.com") -> "User valid"
# Test: validate_user("", 25, "alice@email.com") -> raises ValidationError
# Test: validate_user("Bob", -5, "bob@email.com") -> raises AgeValidationError
# Test: validate_user("Charlie", 30, "invalid-email") -> raises EmailValidationError
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 validate_user('Alice', 25, 'alice@email.com'):",
#       validate_user("Alice", 25, "alice@email.com"))
# try:
#     validate_user("", 25, "alice@email.com")
# except ValidationError as e:
#     print("🔴 Empty name caught:", type(e).__name__)


# ----------------------------------------------------------------------
# 🔴 HARD 2: Exception Handler Decorator
# Create a decorator called exception_handler that:
# - Wraps any function
# - Catches any exception that occurs
# - Returns a dictionary: {"error": True, "type": "ExceptionType", "message": "..."}
# - If no exception, returns: {"error": False, "result": actual_result}
#
# Test with:
# @exception_handler
# def risky_divide(a, b):
#     return a / b
#
# Test: risky_divide(10, 2) -> {"error": False, "result": 5.0}
# Test: risky_divide(10, 0) -> {"error": True, "type": "ZeroDivisionError", ...}
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# @exception_handler
# def risky_divide(a, b):
#     return a / b
#
# print("🔴 risky_divide(10, 2):", risky_divide(10, 2))
# print("🔴 risky_divide(10, 0):", risky_divide(10, 0))


# ----------------------------------------------------------------------
# 🔴 HARD 3: Retry Mechanism
# Create a function retry(func, max_attempts, *args, **kwargs)
# - Try to execute func with given args and kwargs
# - If it fails, retry up to max_attempts times
# - Return {"success": True, "result": ..., "attempts": n} on success
# - Return {"success": False, "error": ..., "attempts": max_attempts} if all fail
#
# Test with a function that randomly fails
#
# Example usage:
# def unstable_function():
#     import random
#     if random.random() < 0.7:  # 70% chance to fail
#         raise ValueError("Random failure")
#     return "Success!"
#
# retry(unstable_function, 5) -> might succeed after a few attempts
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# import random
# def unstable():
#     if random.random() < 0.5:
#         raise ValueError("Failed")
#     return "OK"
#
# print("🔴 retry(unstable, 5):", retry(unstable, 5))


# ----------------------------------------------------------------------
# 🔴 HARD 4: Context Manager with Exception Handling
# Create a class called SafeOperation that:
# - Works as a context manager (implement __enter__ and __exit__)
# - Logs when operation starts (print "Operation started")
# - Catches any exception that occurs inside the with block
# - Logs the exception type if one occurs
# - Always logs "Operation ended" when exiting
# - Stores the exception in self.exception (None if no exception)
# - Suppresses the exception (doesn't re-raise it)
#
# Usage:
# with SafeOperation() as op:
#     result = 10 / 0
# print(op.exception)  # Should show ZeroDivisionError
#
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# with SafeOperation() as op:
#     x = 10 / 2
# print("🔴 Exception after safe operation:", op.exception)
#
# with SafeOperation() as op:
#     x = 10 / 0
# print("🔴 Exception after error:", type(op.exception).__name__)


# ----------------------------------------------------------------------
# 🔴 HARD 5: Multi-Level Exception Handling
# Create a function process_transaction(transaction):
# - transaction is a dict with keys: "type", "amount", "account"
#
# Processing rules:
# - If type is "withdraw":
#   - amount must be positive (raise ValueError if not)
#   - amount must be <= 10000 (raise custom LimitExceededError if not)
# - If type is "deposit":
#   - amount must be positive (raise ValueError if not)
# - If type is anything else:
#   - raise custom InvalidTransactionError
#
# - account must be a string of exactly 10 digits (raise custom InvalidAccountError if not)
#
# Return "Transaction successful" if all validations pass
#
# Create all necessary custom exception classes
#
# Test: process_transaction({"type": "withdraw", "amount": 500, "account": "1234567890"})
#       -> "Transaction successful"
# Test: process_transaction({"type": "withdraw", "amount": 50000, "account": "1234567890"})
#       -> raises LimitExceededError
# Test: process_transaction({"type": "invalid", "amount": 100, "account": "1234567890"})
#       -> raises InvalidTransactionError
# Test: process_transaction({"type": "deposit", "amount": 100, "account": "123"})
#       -> raises InvalidAccountError
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 Valid withdraw:", process_transaction({"type": "withdraw", "amount": 500, "account": "1234567890"}))
# try:
#     process_transaction({"type": "withdraw", "amount": 50000, "account": "1234567890"})
# except LimitExceededError as e:
#     print("🔴 Limit exceeded caught:", e)


# ----------------------------------------------------------------------
# 🔴 HARD 6: Exception Chaining
# Create a function load_config(filename):
# - If filename doesn't end with ".json", raise ValueError
# - Simulate loading by:
#   - If filename == "missing.json", raise FileNotFoundError
#   - If filename == "corrupt.json", raise a new ConfigError with
#     the original exception chained (use "from")
#   - If filename == "valid.json", return {"setting": "value"}
#
# Create ConfigError custom exception
# Use exception chaining with "raise ... from ..."
#
# Test: load_config("valid.json") -> {"setting": "value"}
# Test: load_config("invalid.txt") -> raises ValueError
# Test: load_config("missing.json") -> raises FileNotFoundError
# Test: load_config("corrupt.json") -> raises ConfigError (with chained exception)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 load_config('valid.json'):", load_config("valid.json"))
# try:
#     load_config("corrupt.json")
# except ConfigError as e:
#     print("🔴 ConfigError caught:", e)
#     print("🔴 Original cause:", e.__cause__)


# ----------------------------------------------------------------------
# 🔴 HARD 7: Complete Error Handling System
# Create a class ErrorTracker that:
# - Keeps a log of all errors that occur
# - Has method execute(func, *args, **kwargs) that:
#   - Runs the function and catches any exception
#   - Logs the error with timestamp, function name, error type, message
#   - Returns the result or None if error occurred
# - Has method get_error_count() -> total number of errors
# - Has method get_errors_by_type(error_type) -> list of errors of that type
# - Has method get_all_errors() -> list of all error logs
# - Has method clear_errors() -> clears the error log
#
# Error log format: {"timestamp": ..., "function": ..., "type": ..., "message": ...}
#
# Test:
# tracker = ErrorTracker()
# tracker.execute(int, "42")  # success
# tracker.execute(int, "abc") # error
# tracker.execute(lambda: 1/0) # error
# print(tracker.get_error_count())  # 2
# print(tracker.get_errors_by_type("ValueError"))  # 1 error
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# tracker = ErrorTracker()
# print("🔴 execute(int, '42'):", tracker.execute(int, "42"))
# print("🔴 execute(int, 'abc'):", tracker.execute(int, "abc"))
# print("🔴 execute(lambda: 1/0):", tracker.execute(lambda: 1/0))
# print("🔴 Error count:", tracker.get_error_count())
# print("🔴 ValueError errors:", tracker.get_errors_by_type("ValueError"))
# print("🔴 All errors:", tracker.get_all_errors())


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# 🟢 EASY (5):     Basic try/except, specific exceptions, multiple catches
# 🟡 MEDIUM (6):   else/finally, raising exceptions, nested handling
# 🔴 HARD (7):     Custom exceptions, decorators, retry, context managers
#
# Exception Types Covered:
# - ZeroDivisionError    - ValueError         - TypeError
# - KeyError             - IndexError         - FileNotFoundError
# - SyntaxError          - AttributeError     - Custom Exceptions
#
# Concepts Tested:
# - try / except / else / finally
# - Catching specific vs general exceptions
# - Raising exceptions with raise
# - Custom exception classes
# - Exception chaining (raise from)
# - Getting exception information
# - Exception handling in decorators
# - Context managers with exceptions
# ======================================================================
