# ======================================================================
# 🧪 UNITTEST EXERCISES - Python Testing Framework
# ======================================================================
# Practice exercises - Write everything from scratch!
# ======================================================================

import unittest
import sys
import os


# =====================================================================
#                    SECTION 1: BASIC TEST CASES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: YOUR FIRST TEST CASE
#
# Tasks:
# 1. Create a TestCase class called TestMathOperations
# 2. Write test_addition: verify 2 + 2 == 4
# 3. Write test_subtraction: verify 10 - 5 == 5
# 4. Write test_multiplication: verify 3 * 7 == 21
# 5. Write test_division: verify 20 / 4 == 5.0
# 6. Run tests with: python -m unittest <filename>
# ----------------------------------------------------------------------


class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(10 - 5, 5)

    def test_multiplication(self):
        self.assertEqual(3 * 7, 21)

    def test_division(self):
        self.assertEqual(20 / 4, 5.0)


# ----------------------------------------------------------------------
# 🟢 2: STRING TESTING
#
# Tasks:
# 1. Create TestCase class called TestStringMethods
# 2. test_upper: verify "hello".upper() == "HELLO"
# 3. test_lower: verify "WORLD".lower() == "world"
# 4. test_strip: verify "  spaced  ".strip() == "spaced"
# 5. test_split: verify "a,b,c".split(",") == ["a", "b", "c"]
# 6. test_join: verify "-".join(["x", "y", "z"]) == "x-y-z"
# 7. test_replace: verify "foo".replace("o", "a") == "faa"
# ----------------------------------------------------------------------


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_lower(self):
        self.assertEqual("HELLO".lower(), "hello")

    def test_strip(self):
        self.assertEqual("   no spaces   ".strip(), "no spaces")

    def test_split(self):
        self.assertEqual("a b c".split(), ["a", "b", "c"])

    def test_join(self):
        self.assertEqual("*".join(["a", "b", "c"]), "a*b*c")

    def test_replace(self):
        self.assertEqual("122333444455555".replace("2", "*"), "1**333444455555")


# ----------------------------------------------------------------------
# 🟢 3: LIST TESTING
#
# Tasks:
# 1. Create TestCase class called TestListOperations
# 2. test_append: create list, append item, verify item is in list
# 3. test_remove: create list with item, remove it, verify it's gone
# 4. test_length: verify len([1,2,3,4,5]) == 5
# 5. test_index: verify [10,20,30].index(20) == 1
# 6. test_sort: verify sorted([3,1,2]) == [1,2,3]
# 7. test_reverse: verify list(reversed([1,2,3])) == [3,2,1]
# ----------------------------------------------------------------------


class TestListOperations(unittest.TestCase):

    def test_append(self):
        a_list = list()
        value = 10
        a_list.append(value)
        self.assertIn(value, a_list)

    def test_remove(self):
        a_list = list([10, 20, 30])
        value = 10
        a_list.remove(value)
        self.assertNotIn(value, a_list)

    def test_length(self):
        a_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(a_list), 5)

    def test_index(self):
        a_list = [1, 2, 3, 4, 5]
        self.assertEqual(a_list.index(3), 2)

    def test_sort(self):
        a_list = [5, 4, 3, 2, 1]
        self.assertEqual(sorted(a_list), [1, 2, 3, 4, 5])

    def test_reverse(self):
        a_list = [1, 2, 3, 4, 5]
        self.assertEqual(list(reversed(a_list)), [5, 4, 3, 2, 1])


# =====================================================================
#                    SECTION 2: ASSERT METHODS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 4: EQUALITY ASSERTS
#
# Tasks:
# 1. Create TestCase class called TestEqualityAsserts
# 2. test_equal_numbers: use assertEqual for 5 + 5 and 10
# 3. test_equal_strings: use assertEqual for two identical strings
# 4. test_equal_lists: use assertEqual for [1,2,3] and [1,2,3]
# 5. test_not_equal: use assertNotEqual for "cat" and "dog"
# 6. test_equal_dicts: use assertEqual for two identical dictionaries
# ----------------------------------------------------------------------


class TestEqualityAsserts(unittest.TestCase):

    def test_equal_numbers(self):
        self.assertEqual(5 + 5, 10)

    def test_equal_strings(self):
        self.assertEqual("a", "a")

    def test_equal_lists(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])

    def test_not_equal(self):
        self.assertNotEqual(1, 2)

    def test_equal_dicts(self):
        dic1 = {1: "a", 2: "b", 3: "c"}
        dic2 = {1: "a", 2: "b", 3: "c"}
        self.assertEqual(dic1, dic2)


# ----------------------------------------------------------------------
# 🟢 5: BOOLEAN ASSERTS
#
# Tasks:
# 1. Create TestCase class called TestBooleanAsserts
# 2. test_true_expression: use assertTrue for 10 > 5
# 3. test_false_expression: use assertFalse for 3 > 7
# 4. test_true_string: use assertTrue to verify non-empty string is truthy
# 5. test_false_empty: use assertFalse to verify empty list is falsy
# 6. test_true_membership: use assertTrue for 'a' in 'apple'
# ----------------------------------------------------------------------


class TestBooleanAsserts(unittest.TestCase):
    def test_true_expression(self):
        self.assertTrue(10 > 5)

    def test_false_expression(self):
        self.assertFalse(10 < 5)

    def test_true_string(self):
        self.assertTrue("Hello")

    def test_false_string(self):
        self.assertFalse("")

    def test_true_membership(self):
        self.assertTrue("a" in "apple")


# ----------------------------------------------------------------------
# 🟡 6: IDENTITY AND NONE ASSERTS
#
# Tasks:
# 1. Create TestCase class called TestIdentityAsserts
# 2. test_is_same: create a = b = [1,2,3], use assertIs(a, b)
# 3. test_is_not_same: create a = [1,2,3], b = [1,2,3], use assertIsNot
# 4. test_is_none: create x = None, use assertIsNone(x)
# 5. test_is_not_none: create x = "value", use assertIsNotNone(x)
# 6. test_singleton: verify True is True using assertIs
# ----------------------------------------------------------------------


class TestIdentityAsserts(unittest.TestCase):
    def test_is_same(self):
        a = b = [1, 2, 3]
        self.assertIs(a, b)

    def test_is_not_same(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertIsNot(a, b)

    def test_is_none(self):
        none_variable = None
        self.assertIsNone(none_variable)

    def test_is_not_none(self):
        no_none = 0
        self.assertIsNotNone(no_none)

    def test_is_singleton(self):
        self.assertIs(True, True)


# ----------------------------------------------------------------------
# 🟡 7: MEMBERSHIP ASSERTS
#
# Tasks:
# 1. Create TestCase class called TestMembershipAsserts
# 2. test_in_list: use assertIn to verify 3 is in [1,2,3,4,5]
# 3. test_not_in_list: use assertNotIn to verify 10 is not in [1,2,3]
# 4. test_in_string: use assertIn to verify "py" is in "python"
# 5. test_in_dict: use assertIn to verify key exists in dictionary
# 6. test_not_in_string: use assertNotIn to verify "xyz" not in "hello"
# ----------------------------------------------------------------------


class TestMembershipAsserts(unittest.TestCase):
    def test_in_list(self):
        self.assertIn(3, [1, 2, 3])

    def test_not_in_list(self):
        self.assertNotIn(1, [2, 3, 4])

    def test_in_string(self):
        self.assertIn("py", "python")

    def test_in_dict(self):
        a_dict = {1: "a", 2: "b", 3: "c"}
        self.assertIn(1, a_dict)

    def test_not_in_string(self):
        self.assertNotIn("x", "python")


# ----------------------------------------------------------------------
# 🟡 8: INSTANCE ASSERTS
#
# Tasks:
# 1. Create TestCase class called TestInstanceAsserts
# 2. test_is_string: use assertIsInstance to verify "hello" is str
# 3. test_is_int: use assertIsInstance to verify 42 is int
# 4. test_is_list: use assertIsInstance to verify [] is list
# 5. test_not_instance: use assertNotIsInstance to verify "5" is not int
# 6. test_custom_class: create a class, instantiate, verify instance
# ----------------------------------------------------------------------


class ThisIsMyClass:
    pass


class TestInstanceAsserts(unittest.TestCase):
    def test_is_string(self):
        self.assertIsInstance("Hello", str)

    def test_is_int(self):
        self.assertIsInstance(10, int)

    def test_is_list(self):
        self.assertIsInstance([1, 2, 3], list)

    def test_not_instance(self):
        self.assertNotIsInstance(50, frozenset)

    def test_custom_class(self):
        an_object = ThisIsMyClass()
        self.assertIsInstance(an_object, ThisIsMyClass)


# =====================================================================
#                    SECTION 3: TEST FIXTURES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 9: setUp AND tearDown
#
# Tasks:
# 1. Create TestCase class called TestWithSetUp
# 2. In setUp: create self.test_list = [1, 2, 3]
# 3. In tearDown: print "Test completed"
# 4. test_list_exists: verify self.test_list is not None
# 5. test_list_length: verify len(self.test_list) == 3
# 6. test_modify_list: append to self.test_list, verify length is 4
# 7. test_original_list: verify self.test_list still has 3 items
#    (setUp creates fresh list for each test!)
# ----------------------------------------------------------------------


# class TestWithSetUp(unittest.TestCase):
#     def setUp(self):
#         self.test_list = [1, 2, 3]

#     def tearDown(self):
#         print("Test completed")

#     def test_list_exists(self):
#         self.assertIsNotNone(self.test_list)

#     def test_list_length(self):
#         self.assertEqual(len(self.test_list), 3)

#     def test_modify_list(self):
#         self.test_list.append(4)
#         self.assertEqual(len(self.test_list), 4)

#     def test_original_list(self):
#         self.assertEqual(len(self.test_list), 3)


# ----------------------------------------------------------------------
# 🟡 10: setUpClass AND tearDownClass
#
# Tasks:
# 1. Create TestCase class called TestWithClassSetUp
# 2. In setUpClass: print "Starting TestCase", set cls.shared_data = []
# 3. In tearDownClass: print "Finished TestCase"
# 4. test_first: append "first" to cls.shared_data
# 5. test_second: append "second" to cls.shared_data
# 6. test_third: verify shared_data contains items from previous tests
#
# Note: setUpClass and tearDownClass need @classmethod decorator
# ----------------------------------------------------------------------


class TestWithSetUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print("Starting TestCase")
        cls.shared_data = []

    @classmethod
    def tearDownClass(cls):
        pass
        # print("Finished Test case")

    def test_first(self):
        self.shared_data.append("First")
        self.assertEqual(len(self.shared_data), 1)

    def test_second(self):
        self.shared_data.append("Second")
        self.assertEqual(len(self.shared_data), 2)

    def test_third(self):
        self.shared_data.append("Third")
        self.assertEqual(len(self.shared_data), 3)


# ----------------------------------------------------------------------
# 🟡 11: COMBINED FIXTURES
#
# Tasks:
# 1. Create TestCase class called TestAllFixtures
# 2. setUpClass: print "=== TestCase Started ===" and set cls.counter = 0
# 3. tearDownClass: print "=== TestCase Finished ===" and final counter
# 4. setUp: increment cls.counter, print "Test #{counter} starting"
# 5. tearDown: print "Test #{counter} finished"
# 6. Create 3 test methods with simple assertions
# 7. Run and observe execution order
# ----------------------------------------------------------------------


class TestAllFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("=== TestCase Started ===")
        cls.counter = 0

    @classmethod
    def tearDownClass(cls):
        print("=== TestCase Finished ===")

    def setUp(self):
        TestAllFixtures.counter += 1
        print(f"Test #{self.counter} starting")

    def tearDown(self):
        print(f"Test #{self.counter} finished")

    def test_first(self):
        self.assertEqual(1, 1)

    def test_second(self):
        self.assertEqual(1, 1)

    def test_third(self):
        self.assertEqual(1, 1)


# =====================================================================
#                    SECTION 4: TEST SUITES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 12: CREATE A TEST SUITE
#
# Tasks:
# 1. Create two TestCase classes:
#    - TestAddition with test_add_positive, test_add_negative
#    - TestSubtraction with test_sub_positive, test_sub_negative
# 2. Create a TestSuite called math_suite
# 3. Add TestAddition to the suite using makeSuite()
# 4. Add TestSubtraction to the suite using makeSuite()
# 5. Create a runner and run the suite
#
# Hint: unittest.TextTestRunner().run(suite)
# ----------------------------------------------------------------------


class TestAddition(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(1 + 2, 3)

    def test_add_negative(self):
        self.assertEqual(1 + (-1), 0)


class TestSubtraction(unittest.TestCase):
    def test_sub_positive(self):
        self.assertEqual(1 - 1, 0)

    def test_sub_negative(self):
        self.assertEqual(1 - (-1), 2)


# def suite():
#     math_suite = unittest.TestSuite()
#     math_suite.addTest(unittest.makeSuite(TestAddition))
#     math_suite.addTest(unittest.makeSuite(TestSubtraction))
#     return math_suite


# ----------------------------------------------------------------------
# 🟡 13: NESTED TEST SUITES
#
# Tasks:
# 1. Create TestCase class TestMultiplication
# 2. Create TestCase class TestDivision
# 3. Create suite_1 containing TestAddition and TestSubtraction
# 4. Create suite_2 containing TestMultiplication and TestDivision
# 5. Create master_suite containing suite_1 and suite_2
# 6. Run the master_suite
#
# Hint: Use addTests([suite_1, suite_2]) for adding multiple suites
# ----------------------------------------------------------------------


class TestMultiplication(unittest.TestCase):
    def test_mul_positive(self):
        self.assertEqual(2 * 2, 4)


class TestDivision(unittest.TestCase):
    def test_div_positive(self):
        self.assertEqual(2 / 2, 1)


# ----------------------------------------------------------------------
# Commentary on suite construction and best practices (added by reviewer):
#
# ⚠️ Note: This code uses unittest.defaultTestLoader.loadTestsFromTestCase, which is the modern and future-proof method to aggregate all test methods from a TestCase class into a suite.
# Older courses and materials sometimes use unittest.makeSuite(), but that method is deprecated in Python 3.11+ and should be avoided for new code.
#
# Example alternate construction:
#   suite_1 = unittest.TestSuite([
#       unittest.defaultTestLoader.loadTestsFromTestCase(TestAddition),
#       unittest.defaultTestLoader.loadTestsFromTestCase(TestSubtraction),
#   ])
#
# Both methods (the code here, and the commented alternate above) are valid up to Python 3.10. Always prefer the loader idiom for future compatibility!
# For more, see: https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase
# ----------------------------------------------------------------------

suite_1 = unittest.TestSuite()
suite_1.addTests(
    [
        unittest.defaultTestLoader.loadTestsFromTestCase(TestAddition),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestSubtraction),
    ]
)

suite_2 = unittest.TestSuite()
suite_2.addTests(
    [
        unittest.defaultTestLoader.loadTestsFromTestCase(TestMultiplication),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestDivision),
    ]
)

master_suite = unittest.TestSuite()
master_suite.addTests([(suite_1), suite_2])


# =====================================================================
#                    SECTION 5: SKIPPING TESTS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 14: UNCONDITIONAL SKIP
#
# Tasks:
# 1. Create TestCase class called TestSkipping
# 2. test_normal: a regular test that passes
# 3. test_skipped: use @unittest.skip("reason") to skip this test
# 4. test_another_normal: another regular test
# 5. Run tests and observe skipped test in output
# ----------------------------------------------------------------------


class TestSkipping(unittest.TestCase):
    def test_normal(self):
        pass

    @unittest.skip("Just skipping this one!")
    def test_skipped(self):
        pass

    def test_normal_2(self):
        pass


# ----------------------------------------------------------------------
# 🟡 15: CONDITIONAL SKIP
#
# Tasks:
# 1. Create TestCase class called TestConditionalSkip
# 2. test_skip_on_windows: use @unittest.skipIf to skip on Windows
#    Hint: sys.platform.startswith("win")
# 3. test_skip_on_linux: use @unittest.skipIf to skip on Linux
#    Hint: sys.platform.startswith("linux")
# 4. test_skip_unless_env: use @unittest.skipUnless to skip unless
#    environment variable "RUN_SLOW_TESTS" is set
# 5. test_always_runs: a test that runs on all platforms
# ----------------------------------------------------------------------


class TestConditionalSkip(unittest.TestCase):
    @unittest.skipIf(sys.platform.startswith("win"), "Skipping on Windows")
    def test_skip_on_windows(self):
        pass

    @unittest.skipIf(sys.platform.startswith("linux"), "We're skipping Linux, man")
    def test_skip_on_linux(self):
        pass

    @unittest.skipIf(sys.platform.startswith("darwin"), "We're skipping Mac, man")
    def test_skip_on_mac(self):
        pass

    @unittest.skipUnless(
        os.getenv("RUN_SLOW_TESTS"), "Skipped since you haven't setup RUN_SLOW_TESTS"
    )
    def test_skip_unless_env(self):
        pass

    def test_always_run(self):
        pass


print(sys.platform)

# ----------------------------------------------------------------------
# 🟡 16: SKIP ENTIRE TEST CASE
#
# Tasks:
# 1. Create TestCase class called TestSkippedClass
# 2. Apply @unittest.skip("reason") decorator to entire class
# 3. Add 3 test methods inside
# 4. Run and verify ALL tests in the class are skipped
# 5. Create another normal TestCase to compare
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: EXPECTED FAILURES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 17: EXPECTED FAILURE DECORATOR
#
# Tasks:
# 1. Create TestCase class called TestExpectedFailures
# 2. test_expected_fail: use @unittest.expectedFailure
#    - Write assertion that WILL fail (e.g., assertEqual(1, 2))
#    - Should be marked as "expected failure" (xfail)
# 3. test_unexpected_success: use @unittest.expectedFailure
#    - Write assertion that PASSES
#    - Will be marked as "unexpected success"
# 4. test_normal_pass: a regular passing test
# 5. test_normal_fail: a regular failing test (to compare)
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 18: TEST A CALCULATOR CLASS
#
# Tasks:
# 1. Create Calculator class with: add, subtract, multiply, divide
#    - divide should raise ValueError for division by zero
# 2. Create TestCalculator with:
#    - setUp: create self.calc = Calculator()
#    - test_add, test_subtract, test_multiply, test_divide
#    - test_divide_by_zero: verify ValueError is raised
#
# Hint: Use self.assertRaises(ValueError) for exception testing
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: TEST A USER CLASS
#
# Tasks:
# 1. Create User class with:
#    - __init__(self, username, email)
#    - is_valid_email() - returns True if email contains "@"
#    - get_domain() - returns part after "@" in email
# 2. Create TestUser with:
#    - test_user_creation
#    - test_valid_email
#    - test_invalid_email
#    - test_get_domain
#    - test_empty_email
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 20: TEST A SHOPPING CART
#
# Tasks:
# 1. Create ShoppingCart class with:
#    - add_item(name, price, quantity=1)
#    - remove_item(name)
#    - get_total()
#    - get_item_count()
#    - clear()
# 2. Create TestShoppingCart with full test coverage
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 21: TEST A FILE HANDLER
#
# Tasks:
# 1. Create FileHandler class with:
#    - write_file(filename, content)
#    - read_file(filename)
#    - file_exists(filename)
#    - delete_file(filename)
# 2. Create TestFileHandler with:
#    - setUpClass: create test directory
#    - tearDownClass: remove test directory
#    - tearDown: cleanup test files
#    - Full test coverage for all methods
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 22: TEST A BANK ACCOUNT
#
# Tasks:
# 1. Create BankAccount class with:
#    - __init__(self, owner, balance=0)
#    - deposit(amount) - raise ValueError if amount <= 0
#    - withdraw(amount) - raise ValueError if insufficient funds
#    - get_balance()
#    - transfer(amount, other_account)
# 2. Create TestBankAccount with full test coverage
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: ADVANCED SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 23: TEST A USER DATABASE
#
# Tasks:
# 1. Create UserDatabase class with:
#    - add_user(user_id, name, email)
#    - get_user(user_id)
#    - delete_user(user_id)
#    - get_all_users()
#    - search_by_name(name) - partial match, case insensitive
# 2. Create TestUserDatabase with full CRUD test coverage
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 24: TEST A PASSWORD VALIDATOR
#
# Tasks:
# 1. Create PasswordValidator class with:
#    - validate(password) - returns (bool, list of errors)
#    Rules: min 8 chars, uppercase, lowercase, digit, special char
# 2. Create tests for every validation rule and edge case
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 25: COMPLETE TEST SUITE PROJECT
#
# Tasks:
# 1. Create TodoList class with:
#    - add_task(title, priority="medium")
#    - complete_task(task_id)
#    - delete_task(task_id)
#    - get_pending_tasks()
#    - get_completed_tasks()
#    - get_tasks_by_priority(priority)
#
# 2. Create THREE separate TestCase classes:
#    - TestTodoCreation
#    - TestTodoCompletion
#    - TestTodoFiltering
#
# 3. Create comprehensive test suite grouping all TestCases
#
# 4. Include tests with:
#    - @unittest.skip for "not yet implemented" feature
#    - @unittest.expectedFailure for known bug
#    - @unittest.skipIf for platform-specific test
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Assert Methods
# ======================================================================
#
# assertEqual(a, b)           | a == b
# assertNotEqual(a, b)        | a != b
# assertTrue(x)               | bool(x) is True
# assertFalse(x)              | bool(x) is False
# assertIs(a, b)              | a is b
# assertIsNot(a, b)           | a is not b
# assertIsNone(x)             | x is None
# assertIsNotNone(x)          | x is not None
# assertIn(a, b)              | a in b
# assertNotIn(a, b)           | a not in b
# assertIsInstance(a, b)      | isinstance(a, b)
# assertNotIsInstance(a, b)   | not isinstance(a, b)
# assertRaises(exc)           | function raises exc
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Fixtures
# ======================================================================
#
# setUpClass      | Once before all tests (needs @classmethod)
# setUp           | Before EACH test method
# tearDown        | After EACH test method
# tearDownClass   | Once after all tests (needs @classmethod)
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Decorators
# ======================================================================
#
# @unittest.skip("reason")            | Always skip
# @unittest.skipIf(cond, "reason")    | Skip if condition True
# @unittest.skipUnless(cond, "reason")| Skip unless condition True
# @unittest.expectedFailure           | Test expected to fail
#
# ======================================================================


# ======================================================================
# 🚀 HOW TO RUN
# ======================================================================
#
# All tests:        python -m unittest test_filename.py
# Specific class:   python -m unittest test_filename.TestCaseName
# Specific test:    python -m unittest test_filename.TestCaseName.test_method
# Verbose:          python -m unittest -v test_filename.py
# Discover all:     python -m unittest discover
#
# ======================================================================


if __name__ == "__main__":
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(master_suite)
    # Uncomment for only the test suite and comment unittest.main()

    unittest.main()
