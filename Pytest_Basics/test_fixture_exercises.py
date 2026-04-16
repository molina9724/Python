# ======================================================================
# 🔧 PYTEST FIXTURES EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# ======================================================================

import pytest


# =====================================================================
#                    SECTION 1: BASIC FIXTURES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: YOUR FIRST FIXTURE
#
# Learn: @pytest.fixture decorator, using fixtures in tests
#
# Tasks:
# 1. Create a fixture called sample_data that returns a list [1, 2, 3]
# 2. Create a test that uses the fixture as a parameter
# 3. Assert the length of sample_data is 3
# 4. Assert 2 is in sample_data
# 5. Run the test and verify it passes
# ----------------------------------------------------------------------


@pytest.fixture()
def sample_data():
    return [1, 2, 3]


def test_sample_data(sample_data):
    assert len(sample_data) == 3
    assert 2 in sample_data


# ----------------------------------------------------------------------
# 🟢 2: FIXTURE RETURNING DICTIONARY
#
# Learn: Fixtures can return any data type
#
# Tasks:
# 1. Create a fixture called user_data that returns a dictionary
# 2. Include keys: "name", "email", "age"
# 3. Create a test that verifies each key exists
# 4. Create another test that checks the values
# 5. Both tests should use the same fixture
# ----------------------------------------------------------------------


@pytest.fixture()
def user_data():
    user = {
        "name": "test",
        "email": "test@test.com",
        "age": 20,
    }
    return user


def test_user_data_keys(user_data):
    results = user_data
    assert "name" in results.keys()
    assert "email" in results.keys()
    assert "age" in results.keys()


def test_user_data_values(user_data):
    results = user_data
    assert results["name"] == "test"
    assert results["email"] == "test@test.com"
    assert results["age"] == 20


# ----------------------------------------------------------------------
# 🟢 3: FIXTURE RETURNING OBJECT
#
# Learn: Fixtures returning class instances
#
# Tasks:
# 1. Create a simple class (e.g., Calculator, User, or Config)
# 2. Create a fixture that returns an instance of the class
# 3. Create tests that use methods/attributes of the object
# 4. Verify the fixture provides a fresh instance
# ----------------------------------------------------------------------


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Do you want to blow up the whole universe or what?"


@pytest.fixture(scope="class")
def calculator():
    my_calculator = Calculator()
    return my_calculator


class TestCalculator:

    def test_calculator_add(self, calculator):
        assert calculator.add(0, 0) == 0

    def test_calculator_subtract(self, calculator):
        assert calculator.subtract(0, 0) == 0

    def test_calculator_multiply(self, calculator):
        assert calculator.multiply(0, 0) == 0

    def test_calculator_divide_by_zero(self, calculator):
        assert (
            calculator.divide(0, 0)
            == "Do you want to blow up the whole universe or what?"
        )

    def test_calculator_divide_not_by_zero(self, calculator):
        assert calculator.divide(0, 1) == 0


# ----------------------------------------------------------------------
# 🟡 4: MULTIPLE FIXTURES IN ONE TEST
#
# Learn: Tests can use multiple fixtures
#
# Tasks:
# 1. Create a fixture called first_number that returns 10
# 2. Create a fixture called second_number that returns 5
# 3. Create a test that uses both fixtures
# 4. Test addition, subtraction, multiplication using both values
# ----------------------------------------------------------------------


@pytest.fixture()
def first_number():
    return 10


@pytest.fixture()
def second_number():
    return 5


def test_two_fixtures(first_number, second_number):
    assert first_number == 10
    assert second_number == 5


def test_addition(first_number, second_number):
    assert first_number + second_number == 15


def test_subtraction(first_number, second_number):
    assert first_number - second_number == 5


def test_multiply(first_number, second_number):
    assert first_number * second_number == 50


# ----------------------------------------------------------------------
# 🟡 5: FIXTURE USING ANOTHER FIXTURE
#
# Learn: Fixtures can depend on other fixtures
#
# Tasks:
# 1. Create a fixture called base_url that returns a URL string
# 2. Create a fixture called api_endpoint that uses base_url
# 3. The api_endpoint should combine base_url with a path
# 4. Create a test that uses api_endpoint
# 5. Verify the full URL is correct
# ----------------------------------------------------------------------


@pytest.fixture()
def custom_base_url():
    return "https://www.google.com/"


@pytest.fixture()
def custom_api_endpoint(custom_base_url):
    results = custom_base_url
    results += "test_api_endpoint/test/"
    return results


def test_custom_api_endpoint(custom_api_endpoint):
    assert custom_api_endpoint == "https://www.google.com/test_api_endpoint/test/"


# =====================================================================
#                    SECTION 2: YIELD FIXTURES (SETUP/TEARDOWN)
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 6: BASIC YIELD FIXTURE
#
# Learn: yield keyword for setup/teardown
#
# Tasks:
# 1. Create a fixture that prints "SETUP" before yield
# 2. Yield a value (e.g., a string or number)
# 3. Print "TEARDOWN" after yield
# 4. Create a test using this fixture
# 5. Run with pytest -s to see the output order
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 7: FILE HANDLING FIXTURE
#
# Learn: Using yield for resource cleanup
#
# Tasks:
# 1. Create a fixture that opens a file for writing
# 2. Yield the file handle
# 3. After yield, close the file and optionally delete it
# 4. Create a test that writes to the file
# 5. Verify the file is properly closed after test
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 8: DATABASE CONNECTION SIMULATION
#
# Learn: Connection setup/teardown pattern
#
# Tasks:
# 1. Create a mock database connection class
# 2. Create a fixture that "connects" (prints/sets flag)
# 3. Yield the connection object
# 4. "Disconnect" after yield
# 5. Create tests that use the connection
# 6. Verify connection is closed even if test fails
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 9: NESTED YIELD FIXTURES
#
# Learn: Multiple yield fixtures working together
#
# Tasks:
# 1. Create fixture A with setup/teardown (prints messages)
# 2. Create fixture B that depends on A, also with setup/teardown
# 3. Create a test using fixture B
# 4. Observe the order: A setup → B setup → test → B teardown → A teardown
# 5. Run with pytest -s to verify order
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 3: FIXTURE SCOPE
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 10: FUNCTION SCOPE (DEFAULT)
#
# Learn: scope="function" - runs for each test
#
# Tasks:
# 1. Create a fixture with scope="function" (or no scope - default)
# 2. Add print statements in setup and teardown
# 3. Create 3 tests using this fixture
# 4. Run with pytest -s
# 5. Observe: fixture runs 3 times (once per test)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 11: MODULE SCOPE
#
# Learn: scope="module" - runs once per module
#
# Tasks:
# 1. Create a fixture with scope="module"
# 2. Add print statements to see when it runs
# 3. Create 3 tests in the same file using this fixture
# 4. Run with pytest -s
# 5. Observe: fixture runs only once for all tests in module
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 12: CLASS SCOPE
#
# Learn: scope="class" - runs once per test class
#
# Tasks:
# 1. Create a fixture with scope="class"
# 2. Create a test class with 3 test methods using the fixture
# 3. Create another test class with 2 test methods using same fixture
# 4. Run with pytest -s
# 5. Observe: fixture runs once per class (2 times total)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 13: SESSION SCOPE
#
# Learn: scope="session" - runs once for entire test session
#
# Tasks:
# 1. Create a fixture with scope="session" in conftest.py
# 2. Create multiple test files, each with tests using the fixture
# 3. Run pytest on the entire directory
# 4. Observe: fixture runs only once for all files
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 14: MIXED SCOPES
#
# Learn: Using fixtures with different scopes together
#
# Tasks:
# 1. Create a session-scoped fixture (e.g., app configuration)
# 2. Create a module-scoped fixture that uses the session fixture
# 3. Create a function-scoped fixture that uses the module fixture
# 4. Create tests using various combinations
# 5. Observe the initialization order and frequency
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: CONFTEST.PY (SHARING FIXTURES)
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 15: BASIC CONFTEST
#
# Learn: Sharing fixtures via conftest.py
#
# Tasks:
# 1. Create a conftest.py file in your test directory
# 2. Define a fixture in conftest.py
# 3. Create multiple test files that use this fixture
# 4. Do NOT import conftest - Pytest finds it automatically
# 5. Verify all test files can access the fixture
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 16: HIERARCHICAL CONFTEST
#
# Learn: conftest.py at different directory levels
#
# Tasks:
# 1. Create a directory structure:
#    tests/
#    ├── conftest.py (root fixture)
#    ├── test_root.py
#    └── subdir/
#        ├── conftest.py (subdir fixture)
#        └── test_sub.py
# 2. Define different fixtures at each level
# 3. Test which fixtures are available where
# 4. Verify subdir can access both its own and parent fixtures
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 17: OVERRIDE FIXTURES
#
# Learn: Overriding fixtures in subdirectories
#
# Tasks:
# 1. Define a fixture "config" in root conftest.py
# 2. Define a fixture with same name "config" in subdir conftest.py
# 3. Create tests in both locations using the config fixture
# 4. Verify root tests get root fixture
# 5. Verify subdir tests get subdir fixture (override)
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: AUTOUSE FIXTURES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 18: BASIC AUTOUSE
#
# Learn: autouse=True - fixture runs automatically
#
# Tasks:
# 1. Create a fixture with autouse=True
# 2. Print a message when it runs
# 3. Create tests that do NOT list the fixture as parameter
# 4. Run tests and observe fixture still runs
# 5. Understand when autouse is useful
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: AUTOUSE WITH SCOPE
#
# Learn: Combining autouse with different scopes
#
# Tasks:
# 1. Create autouse fixture with scope="module"
# 2. Create another autouse fixture with scope="function"
# 3. Create multiple tests
# 4. Observe which runs when and how often
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 20: AUTOUSE FOR LOGGING
#
# Learn: Practical autouse example
#
# Tasks:
# 1. Create autouse fixture that logs test start time
# 2. Use yield to log test end time after test completes
# 3. Calculate and print test duration
# 4. Apply to multiple tests automatically
# 5. No test should need to explicitly request the fixture
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: PARAMETRIZED FIXTURES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 21: FIXTURE WITH PARAMS
#
# Learn: @pytest.fixture(params=[...])
#
# Tasks:
# 1. Create a fixture with params=[1, 2, 3]
# 2. Use request.param to access current parameter
# 3. Create a test using this fixture
# 4. Run and observe: test runs 3 times (once per param)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: FIXTURE PARAMS WITH IDS
#
# Learn: Naming parametrized fixture instances
#
# Tasks:
# 1. Create a fixture with params and ids
# 2. ids should be descriptive names for each param
# 3. Run pytest -v to see the test names
# 4. Verify custom ids appear in output
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 23: COMPLEX FIXTURE PARAMS
#
# Learn: Fixtures with dictionary/object params
#
# Tasks:
# 1. Create a fixture with params as list of dictionaries
# 2. Each dict represents a test scenario
# 3. Access different keys from request.param
# 4. Create tests using the complex fixture
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 24: WEB DRIVER FIXTURE
#
# Learn: Browser automation setup/teardown
#
# Tasks:
# 1. Create a fixture that simulates browser setup
# 2. Use yield to provide the "driver"
# 3. Teardown should "close" the browser
# 4. Use scope="class" or scope="module" for efficiency
# 5. Create tests that use the driver
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 25: TEST DATABASE FIXTURE
#
# Learn: Database setup with test data
#
# Tasks:
# 1. Create session-scoped fixture that "creates" test database
# 2. Create function-scoped fixture that adds test data
# 3. Teardown should "rollback" or clean data
# 4. Create tests that verify data operations
# 5. Ensure each test starts with clean state
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 26: API CLIENT FIXTURE
#
# Learn: HTTP client setup
#
# Tasks:
# 1. Create a fixture that creates an "API client" object
# 2. Configure base URL, headers, authentication
# 3. Use yield to provide the client
# 4. Teardown should cleanup (close session, etc.)
# 5. Create tests that use the client for "requests"
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 27: TEMPORARY DIRECTORY FIXTURE
#
# Learn: File system test isolation
#
# Tasks:
# 1. Create a fixture that creates a temporary directory
# 2. Yield the directory path
# 3. Teardown should delete the directory and contents
# 4. Create tests that create files in the temp directory
# 5. Verify cleanup happens after each test
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 28: COMPLETE TEST SUITE
#
# Scenario: Build a realistic test suite with multiple fixtures
#
# Tasks:
# 1. Create conftest.py with:
#    - Session-scoped configuration fixture
#    - Module-scoped "service" fixture
#    - Function-scoped "data" fixture with params
#    - Autouse logging fixture
# 2. Create multiple test files using these fixtures
# 3. Demonstrate proper setup/teardown order
# 4. Use mix of scopes appropriately
# 5. Run full suite and verify behavior
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Fixture Decorator
# ======================================================================
#
# @pytest.fixture(
#     scope="function",    # function, class, module, session
#     autouse=False,       # True = runs without explicit request
#     params=None,         # List of values to parametrize
#     ids=None,            # Names for parametrized instances
#     name=None            # Rename the fixture
# )
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Fixture Scopes
# ======================================================================
#
# Scope      | Runs
# -----------|--------------------------------------------------
# function   | Once per test function (default)
# class      | Once per test class
# module     | Once per module (.py file)
# session    | Once per test session (all files)
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Yield Fixture Pattern
# ======================================================================
#
# @pytest.fixture
# def resource():
#     # SETUP code here
#     obj = create_resource()
#     yield obj  # This is what the test receives
#     # TEARDOWN code here (runs after test)
#     obj.cleanup()
#
# ======================================================================


# ======================================================================
# 📁 FILE STRUCTURE
# ======================================================================
#
# project/
# ├── conftest.py         <- Shared fixtures (auto-discovered)
# ├── test_module1.py     <- Tests (can use conftest fixtures)
# ├── test_module2.py     <- Tests (can use conftest fixtures)
# └── subdir/
#     ├── conftest.py     <- Fixtures for subdir only
#     └── test_sub.py     <- Can use both conftest files
#
# ======================================================================


# ======================================================================
# 🚀 HOW TO RUN
# ======================================================================
#
# Basic:              pytest
# Show prints:        pytest -s
# Verbose:            pytest -v
# Both:               pytest -vs
# Specific file:      pytest test_file.py
# Specific test:      pytest test_file.py::test_name
#
# ======================================================================
