# ======================================================================
# 🎭 UNITTEST MOCK EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# ======================================================================

from unittest import mock
import unittest


# =====================================================================
#                    SECTION 1: CREATING MOCK OBJECTS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: YOUR FIRST MOCK
#
# Learn: mock.Mock(), called attribute
#
# Tasks:
# 1. Create a Mock object
# 2. Call the mock object
# 3. Verify the `called` attribute is True
# 4. Create another Mock but don't call it
# 5. Verify its `called` attribute is False
# ----------------------------------------------------------------------


class TestOne(unittest.TestCase):
    def test_create_and_call(self):
        m = mock.Mock()
        m()
        self.assertTrue(m.called)

    def test_create_but_not_call(self):
        m = mock.Mock()
        self.assertFalse(m.called)


# ----------------------------------------------------------------------
# 🟢 2: COUNTING CALLS
#
# Learn: call_count attribute
#
# Tasks:
# 1. Create a Mock object
# 2. Call it 5 times
# 3. Verify call_count equals 5
# 4. Call it 3 more times
# 5. Verify call_count equals 8
# ----------------------------------------------------------------------


class Test2(unittest.TestCase):
    def test_call_eight_times(self):
        m = mock.Mock()
        for _ in range(5):
            m()
        self.assertEqual(m.call_count, 5)

        for _ in range(3):
            m()
        self.assertEqual(m.call_count, 8)


# ----------------------------------------------------------------------
# 🟢 3: CHECKING CALL ARGUMENTS
#
# Learn: call_args attribute
#
# Tasks:
# 1. Create a Mock object
# 2. Call it with arguments: (1, 2, 3)
# 3. Check call_args to see the arguments
# 4. Call it again with different arguments: ("hello", key="value")
# 5. Check call_args again - notice it shows only the LAST call
# ----------------------------------------------------------------------


class Test3(unittest.TestCase):
    def test_args(self):
        m = mock.Mock()
        args = (1, 2, 3)
        m(args)
        self.assertEqual(m.call_args, mock.call(args))

        m("hello", key="value")
        self.assertEqual(m.call_args, mock.call("hello", key="value"))


# ----------------------------------------------------------------------
# 🟢 4: ALL CALLS HISTORY
#
# Learn: call_args_list attribute
#
# Tasks:
# 1. Create a Mock object
# 2. Call it with (1, 2)
# 3. Call it with ("a", "b")
# 4. Call it with (True, False)
# 5. Check call_args_list to see ALL calls in order
# ----------------------------------------------------------------------


class Test4(unittest.TestCase):
    def test_args_list(self):
        m = mock.Mock()

        args = [(1, 2), ("a", "b"), (True, False)]
        expected = list()
        for arg in args:
            # Unpack the tuple for more similar working
            m(*arg)
            expected.append(mock.call(*arg))

        self.assertEqual(m.call_args_list, expected)


# =====================================================================
#                    SECTION 2: MOCK RETURN VALUES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 5: SETTING RETURN VALUE
#
# Learn: return_value parameter
#
# Tasks:
# 1. Create a Mock with return_value=42
# 2. Call the mock and verify it returns 42
# 3. Create another Mock with return_value="hello"
# 4. Call it and verify the return value
# 5. Create a Mock that returns a list
# ----------------------------------------------------------------------


class Test5(unittest.TestCase):
    def test_return_value(self):
        m = mock.Mock()
        value = 42
        m.return_value = value
        self.assertEqual(m(), value)

        value2 = "hello"
        m2 = mock.Mock(return_value=value2)
        self.assertEqual(m2(), value2)

        m3 = mock.Mock(return_value=[])
        self.assertEqual(m3(), [])


# ----------------------------------------------------------------------
# 🟡 6: SIDE EFFECT - MULTIPLE RETURNS
#
# Learn: side_effect with a list
#
# Tasks:
# 1. Create a Mock with side_effect=[1, 2, 3]
# 2. Call it first time - should return 1
# 3. Call it second time - should return 2
# 4. Call it third time - should return 3
# 5. Call it fourth time - observe what happens
# ----------------------------------------------------------------------


class Test6(unittest.TestCase):
    def test_side_effect(self):
        side_effect = [1, 2, 3]
        m = mock.Mock(side_effect=side_effect)

        self.assertEqual(m(), side_effect[0])
        self.assertEqual(m(), side_effect[1])
        self.assertEqual(m(), side_effect[2])

        # Exception raised if consumed
        with self.assertRaises(StopIteration):
            m()


# ----------------------------------------------------------------------
# 🟡 7: SIDE EFFECT - RAISING EXCEPTIONS
#
# Learn: side_effect with an exception
#
# Tasks:
# 1. Create a Mock with side_effect=ValueError("error message")
# 2. Call the mock inside a try/except block
# 3. Verify the exception is raised
# 4. Create a Mock with side_effect=ConnectionError
# 5. Test that it raises when called
# ----------------------------------------------------------------------


class Test7(unittest.TestCase):
    def test_side_effect_error(self):
        m = mock.Mock(side_effect=ValueError("error"))

        try:
            m()
        except ValueError as e:
            self.assertEqual(str(e), "error")
        else:
            self.fail("ValueError not raised")

    def test_connection_error(self):
        m = mock.Mock(side_effect=ConnectionError)
        with self.assertRaises(ConnectionError):
            m()


# ----------------------------------------------------------------------
# 🟡 8: SIDE EFFECT - CUSTOM FUNCTION
#
# Learn: side_effect with a function
#
# Tasks:
# 1. Create a function that doubles its input
# 2. Create a Mock with side_effect=your_function
# 3. Call mock(5) and verify it returns 10
# 4. Call mock(100) and verify it returns 200
# 5. Create a side_effect function that behaves differently based on input
# ----------------------------------------------------------------------


class Test8(unittest.TestCase):
    def double(self, x):
        return x * 2

    def side_effect_func(self, x):
        if x % 2 == 0:
            return x + 1
        else:
            return x + 2

    def test_double(self):
        m = mock.Mock(side_effect=self.double)
        self.assertEqual(m(5), 10)
        self.assertEqual(m(100), 200)

    def test_side_effect(self):
        m = mock.Mock(side_effect=self.side_effect_func)
        self.assertEqual(m(5), 7)
        self.assertEqual(m(6), 7)


# =====================================================================
#                    SECTION 3: MOCK ASSERT METHODS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 9: ASSERT CALLED
#
# Learn: assert_called()
#
# Tasks:
# 1. Create a Mock object
# 2. Call it
# 3. Use assert_called() - should pass
# 4. Create another Mock, don't call it
# 5. Use assert_called() on it - observe it fails
# ----------------------------------------------------------------------


class Test9(unittest.TestCase):
    def test_assert_called(self):
        m = mock.Mock()
        m()
        m.assert_called()

        n = mock.Mock()
        n.assert_called()


# ----------------------------------------------------------------------
# 🟢 10: ASSERT CALLED ONCE
#
# Learn: assert_called_once()
#
# Tasks:
# 1. Create a Mock, call it once
# 2. Use assert_called_once() - should pass
# 3. Call it again (second time)
# 4. Use assert_called_once() - observe it fails
# 5. Understand difference between assert_called and assert_called_once
# ----------------------------------------------------------------------


class Test10(unittest.TestCase):
    def test_call_once(self):
        m = mock.Mock()
        m()
        m.assert_called_once()

    @unittest.expectedFailure
    def test_call_twice(self):
        m = mock.Mock()
        m()
        m()
        m.assert_called_once()


# ----------------------------------------------------------------------
# 🟡 11: ASSERT CALLED WITH
#
# Learn: assert_called_with()
#
# Tasks:
# 1. Create a Mock
# 2. Call it with arguments: (1, 2, 3)
# 3. Use assert_called_with(1, 2, 3) - should pass
# 4. Use assert_called_with(1, 2) - observe it fails
# 5. Call mock with keyword arguments and verify with assert_called_with
# ----------------------------------------------------------------------


class Test11(unittest.TestCase):
    def test_with_full_arguments(self):
        m = mock.Mock()
        m(1, 2, 3)
        m.assert_called_with(1, 2, 3)

    @unittest.expectedFailure
    def test_with_missing_arguments(self):
        full_arguments = 1, 2, 3
        missing_arguments = 1, 2

        m = mock.Mock()
        m(full_arguments)
        m.assert_called_with(missing_arguments)

    def test_with_keyword_arguments(self):
        keyword_arguments = {"a": 10, "b": 20, "c": 30}
        m = mock.Mock()
        m(**keyword_arguments)
        m.assert_called_with(**keyword_arguments)


# ----------------------------------------------------------------------
# 🟡 12: ASSERT CALLED ONCE WITH
#
# Learn: assert_called_once_with()
#
# Tasks:
# 1. Create a Mock
# 2. Call it once with ("test", 123)
# 3. Use assert_called_once_with("test", 123) - should pass
# 4. Call it again with same arguments
# 5. Use assert_called_once_with again - observe it fails (called twice)
# ----------------------------------------------------------------------


class Test12(unittest.TestCase):
    def test_called_once_with(self):
        m = mock.Mock()
        args = ("test", 123)
        m(*args)
        m.assert_called_once_with(*args)

    @unittest.expectedFailure
    def test_called_twice_with(self):
        m = mock.Mock()
        args = ("test", 123)
        m(*args)
        m(*args)
        m.assert_called_once_with(*args)


# ----------------------------------------------------------------------
# 🟡 13: ASSERT ANY CALL
#
# Learn: assert_any_call()
#
# Tasks:
# 1. Create a Mock
# 2. Call it with ("first")
# 3. Call it with ("second")
# 4. Call it with ("third")
# 5. Use assert_any_call("second") - should pass even though it wasn't last
# ----------------------------------------------------------------------


class Test13(unittest.TestCase):
    def test_any_call(self):
        m = mock.Mock()
        m(1)
        m(2)
        m(3)
        m.assert_any_call(2)


# ----------------------------------------------------------------------
# 🟡 14: ASSERT NOT CALLED
#
# Learn: assert_not_called()
#
# Tasks:
# 1. Create a Mock
# 2. Use assert_not_called() - should pass
# 3. Call the mock
# 4. Use assert_not_called() - observe it fails
# ----------------------------------------------------------------------


class Test14(unittest.TestCase):
    def test_not_called(self):
        m = mock.Mock()
        m.assert_not_called()

    @unittest.expectedFailure
    def test_not_called_but_called(self):
        m = mock.Mock()
        m()
        m.assert_not_called()


# =====================================================================
#                    SECTION 4: @mock.patch DECORATOR
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 15: PATCH A FUNCTION
#
# Learn: @mock.patch decorator basics
#
# Tasks:
# 1. Create a module-level function called get_data() that returns "real data"
# 2. Create another function process_data() that calls get_data()
# 3. Write a test using @mock.patch to mock get_data
# 4. Make the mock return "fake data"
# 5. Verify process_data() uses the mocked value
# ----------------------------------------------------------------------


def get_data():
    return "real data"


def process_data():
    return get_data()


class TestPatchFunction(unittest.TestCase):
    @mock.patch("test_unittest_mock_object.get_data")
    def test_process_data_uses_mocked_get_data(self, mock_get_data: mock.Mock):
        mock_get_data.return_value = "fake data"
        result = process_data()
        self.assertEqual(result, "fake data")
        mock_get_data.assert_called_once()


# ----------------------------------------------------------------------
# 🟡 16: PATCH A CLASS METHOD
#
# Learn: @mock.patch with class methods
#
# Tasks:
# 1. Create a class with a method you want to mock
# 2. Create another method that depends on the first
# 3. Write a test using @mock.patch to mock the first method
# 4. Verify the dependent method uses the mocked version
# ----------------------------------------------------------------------


class MyClass:
    def return_one(self):
        return 1

    def add_one(self):
        return self.return_one() + 1


class TestMyClass(unittest.TestCase):
    @mock.patch("test_unittest_mock_object.MyClass.return_one")
    def test_mock_return_one(self, mock_return_one: mock.Mock):
        mock_return_one.return_value = 2
        test = MyClass()
        result = test.return_one()
        self.assertEqual(result, 2)
        mock_return_one.assert_called_once()


# ----------------------------------------------------------------------
# 🟡 17: PATCH AS CONTEXT MANAGER
#
# Learn: mock.patch() with 'with' statement
#
# Tasks:
# 1. Create a function to be mocked
# 2. Write a test without decorator
# 3. Use 'with mock.patch("path.to.function") as mocked:'
# 4. Configure the mock inside the with block
# 5. Verify the mock works only inside the block
# ----------------------------------------------------------------------


def return_one():
    return 1


class TestReturnOne(unittest.TestCase):
    def test_return_one(self):
        with mock.patch("test_unittest_mock_object.return_one") as mocked:
            mocked.return_value = 2
            result = return_one()
            self.assertEqual(result, 2)
            mocked.assert_called_once()
        # It'll only work within the with
        self.assertEqual(return_one(), 1)


# ----------------------------------------------------------------------
# 🔴 18: MULTIPLE PATCHES
#
# Learn: Stacking @mock.patch decorators
#
# Tasks:
# 1. Create a function that calls two other functions
# 2. Write a test with two @mock.patch decorators
# 3. Note the order of parameters (bottom decorator = first parameter)
# 4. Configure both mocks with different return values
# 5. Verify both are used correctly
# ----------------------------------------------------------------------


def return_a():
    return "a"


def return_b():
    return "b"


def return_a_and_b():
    return return_a(), return_b()


class TestAB(unittest.TestCase):
    @mock.patch("test_unittest_mock_object.return_a")
    @mock.patch("test_unittest_mock_object.return_b")
    def test_a_and_b(self, mock_b, mock_a):
        # mock_b replaces return_b
        # mock_a replaces return_a
        mock_a.return_value = "z"
        mock_b.return_value = "y"

        result1, result2 = return_a_and_b()

        self.assertEqual(result1, "z")  # return_a replaced
        self.assertEqual(result2, "y")  # return_b replaced

        mock_a.assert_called_once()
        mock_b.assert_called_once()


# =====================================================================
#                    SECTION 5: MOCKING ATTRIBUTES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 19: NESTED ATTRIBUTES
#
# Learn: Mock automatic attribute creation
#
# Tasks:
# 1. Create a Mock object
# 2. Access mock.foo - observe it creates a new Mock
# 3. Access mock.foo.bar.baz - observe the chain
# 4. Set mock.foo.bar.return_value = "deep value"
# 5. Call mock.foo.bar() and verify the return value
# ----------------------------------------------------------------------


class Test19(unittest.TestCase):
    # Each access to an undefined attribute creates a new Mock,
    # unless it's been explicitly assigned

    def test_mock_fake_attributes(self):
        # This doesn't create attributes, just another mock
        m = mock.Mock()
        m.foo
        self.assertIsNot(m, m.foo)
        m.foo.bar.baz
        self.assertIsNot(m.foo, m.foo.bar.baz)
        m.foo.bar.return_value = "deep value"
        self.assertEqual(m.foo.bar(), "deep value")

    def test_mock_real_attributes(self):
        # Right way to create an attribute for a mock
        m = mock.Mock()
        m.random_attribute = 1
        self.assertEqual(m.random_attribute, 1)


# ----------------------------------------------------------------------
# 🟡 20: CONFIGURE MOCK
#
# Learn: configure_mock() method
#
# Tasks:
# 1. Create a Mock object
# 2. Use configure_mock to set multiple attributes at once
# 3. Set return_value, name, and custom attributes
# 4. Verify all configurations applied correctly
# ----------------------------------------------------------------------


class Test20(unittest.TestCase):
    def test_mock_configured_vs_auto_attribute(self):
        m = mock.Mock()
        m.configure_mock(return_value=True, name="named", x=9)
        # These are "real" attributes

        self.assertIs(m.return_value, True)
        self.assertEqual(m.name, "named")
        self.assertEqual(m.x, 9)

        # These are not set—auto-created child mocks
        self.assertIsNot(m.not_configured, 9)
        self.assertIsInstance(m.not_configured, mock.Mock)


# ----------------------------------------------------------------------
# 🟡 21: SPEC & AUTOSPEC PARAMETER
#
# Learn: spec and autospec to restrict and enforce mocks
#
# Tasks:
# 1. Create a real class with specific methods
# 2. Create a Mock with spec=YourClass
#    - Allows only class's attributes/methods (AttributeError for fake ones)
#    - Does *not* enforce correct function signatures (wrong arg count/type allowed!)
# 3. Create a Mock or patch with autospec=True
#    - Restricts to real attributes/methods
#    - **Also enforces correct argument count/names!**
#    - Using the wrong args (missing/too many) raises TypeError just like real function
# 4. Compare:
#    - spec only (bad calls succeed, fail at runtime)
#    - autospec (bad calls fail IMMEDIATELY, safer for refactoring)
#
# Why use autospec? Prevents false positives and catches breaking API changes!
#
# Quick reference:
#   spec=Class      → Only real attributes allowed
#   autospec=Class  → Real attributes & correct signature enforced
# ----------------------------------------------------------------------
#
# Example:
#   class Foo:
#       def bar(self, x): pass
#   m = mock.Mock(spec=Foo)
#   m.bar()         # works (bad!)
#   n = mock.create_autospec(Foo)
#   n.bar()         # TypeError: missing argument 'x'
#   n.fake()        # AttributeError: ...
# ----------------------------------------------------------------------


class Operations:
    @staticmethod
    def add_2(a, b):
        return a + b

    @staticmethod
    def subtract_2(a, b):
        return a - b


class TestOperations(unittest.TestCase):

    @mock.patch(
        "test_unittest_mock_object.Operations",
        spec=Operations,
        side_effect=[Operations.add_2(1, 2), Operations.subtract_2(1, 2)],
        autospec=True,
    )
    def test_operations(self, mock_operations):
        self.assertEqual(mock_operations(), 3)
        self.assertEqual(mock_operations(), -1)


# =====================================================================
#                    SECTION 6: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 22: MOCK AN API CALL
#
# Scenario: Test code that fetches data from an external API
#
# Tasks:
# 1. Create a function fetch_user_data(user_id) that would call an API
# 2. Create a function display_user(user_id) that uses fetch_user_data
# 3. Write tests that mock fetch_user_data
# 4. Test successful response scenario
# 5. Test API error scenario (mock raises exception)
# ----------------------------------------------------------------------

import requests
import json


def fetch_user_data(user_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json()
    return response


def display_user(user_id):
    response = fetch_user_data(user_id)
    id = response["id"]
    name = response["name"]
    username = response["id"]
    email = response["email"]

    return f"User #{id}, {name}, {username}, {email}"


class TestAPICall(unittest.TestCase):

    @mock.patch("test_unittest_mock_object.fetch_user_data", autospec=True)
    def test_fetch_user_successful_call(self, mock_fetch_user_data):
        json_file = {"id": 1, "name": "test", "username": "test_test"}
        mock_fetch_user_data.return_value = json_file
        self.assertEqual(fetch_user_data(1), json_file)

        self.assertIn("id", json_file)
        self.assertIn("name", json_file)
        self.assertIn("username", json_file)

        mock_fetch_user_data.assert_called_once()

    @mock.patch("test_unittest_mock_object.fetch_user_data", autospec=True)
    def test_fetch_user_unsuccessful_call(self, mock_fetch_user_data):
        empty_json_file = dict()
        mock_fetch_user_data.return_value = empty_json_file
        self.assertEqual(fetch_user_data(1), empty_json_file)
        self.assertFalse(empty_json_file)
        mock_fetch_user_data.assert_called_once()


# ----------------------------------------------------------------------
# 🔴 23: MOCK FILE OPERATIONS
#
# Scenario: Test code that reads from a file without actual file
#
# Tasks:
# 1. Create a function that reads a config file
# 2. Create a function that uses the config
# 3. Mock the file reading using mock.patch and mock_open
# 4. Test with different mock file contents
# 5. Test file not found scenario
# ----------------------------------------------------------------------

from pathlib import Path
from unittest.mock import patch, mock_open

test_file = Path(
    "/Users/daniel_molina/Downloads/Python/Python/Unittest_Basics/test_file.txt"
)
with open(test_file, "a") as file:
    file.write("hello\n")


def read_config_file(file_name: Path):
    with open(file_name, "r") as file:
        for line in file.readlines():
            if "hello" in line.lower():
                return True

    return False


def simple_function(file_name: Path):
    results = read_config_file(file_name)
    return (
        "Your file says hello!" if results else "Too bad, no one says hello nowadays :X"
    )


class TestReadConfig(unittest.TestCase):
    @patch("builtins.open", mock_open(read_data="hello"))
    def test_mock_read_config_true(self):
        result = read_config_file(Path("mock_file.txt"))
        self.assertTrue(result)

    @patch("builtins.open", mock_open(read_data="random_string_that_will_return_false"))
    def test_mock_read_config_false(self):
        result = read_config_file(Path("mock_file.txt"))
        self.assertFalse(result)


# ----------------------------------------------------------------------
# 🔴 24: MOCK DATABASE
#
# Scenario: Test code that queries a database
#
# Tasks:
# 1. Create a class that represents database connection
# 2. Create functions that query the "database"
# 3. Mock the database class in tests
# 4. Test query returns expected results
# 5. Test database connection error handling
# ----------------------------------------------------------------------


class Database:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.users = list()

    def select_all(self):
        return self.users


class TestDatabase(unittest.TestCase):
    @mock.patch("test_unittest_mock_object.Database", autospec=Database)
    def test_mock_database(self, database_mock):
        database_mock.configure_mock(
            host="localhost", port=8080, name="mock_database", users=list()
        )
        database_mock.users.append(1)
        database_mock.users.append(2)
        database_mock.users.append(3)

        def select_all(self):
            return self.users

        self.assertEqual(select_all(database_mock), [1, 2, 3])


test = Database("localhost", 8080, "database")
test.users.append(1)
test.users.append(2)
print(test.select_all())

# ----------------------------------------------------------------------
# 🔴 25: MOCK DATETIME
#
# Scenario: Test code that depends on current time
#
# Tasks:
# 1. Create a function that behaves differently based on time of day
# 2. Mock datetime.now() to return a controlled time
# 3. Test morning behavior
# 4. Test evening behavior
# 5. Test edge cases (midnight, noon)
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Mock Attributes
# ======================================================================
#
# Attribute          | Description
# -------------------|------------------------------------------
# called             | True if mock was called
# call_count         | Number of times called
# call_args          | Arguments of last call (or None)
# call_args_list     | List of all calls with arguments
# return_value       | Value returned when mock is called
# side_effect        | Exception, function, or iterable
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Mock Assert Methods
# ======================================================================
#
# Method                              | Verifies
# ------------------------------------|--------------------------------
# assert_called()                     | Called at least once
# assert_called_once()                | Called exactly once
# assert_called_with(*args, **kw)     | Last call had these args
# assert_called_once_with(*args, **kw)| One call with these args
# assert_any_call(*args, **kw)        | These args used in any call
# assert_not_called()                 | Never called
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Creating Mocks
# ======================================================================
#
# Method                        | Usage
# ------------------------------|------------------------------------
# mock.Mock()                   | Create standalone mock object
# mock.MagicMock()              | Mock with magic methods pre-configured
# @mock.patch("path.to.obj")    | Decorator to replace object
# with mock.patch("path"):      | Context manager approach
# mock.patch.object(obj, "attr")| Patch attribute of specific object
#
# ======================================================================


# ======================================================================
# 🚀 HOW TO RUN
# ======================================================================
#
# python -m unittest filename.py
# python -m unittest -v filename.py
#
# ======================================================================


if __name__ == "__main__":
    unittest.main()
