# ======================================================================
# 🪝 PYTEST HOOKS EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# All hooks go in conftest.py unless specified otherwise
# ======================================================================

import pytest
import json

# =====================================================================
#                    SECTION 1: pytest_addoption
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: BASIC COMMAND LINE OPTION
#
# Learn: pytest_addoption, parser.addoption
#
# Tasks:
# 1. Create conftest.py with pytest_addoption hook
# 2. Add option --env with choices: "dev", "staging", "prod"
# 3. Set default value to "dev"
# 4. Create a fixture that returns the option value
# 5. Create test that prints which environment is being used
# 6. Run: pytest --env=staging
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 2: BOOLEAN FLAG OPTION
#
# Learn: store_true action
#
# Tasks:
# 1. Add option --slow to enable slow tests
# 2. Use action="store_true" (flag, no value needed)
# 3. Create fixture to access the flag
# 4. Create tests that check the flag before running slow operations
# 5. Run: pytest --slow vs pytest (without flag)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 3: MULTIPLE VALUE OPTION
#
# Learn: action="append"
#
# Tasks:
# 1. Add option --browser that can be specified multiple times
# 2. Use action="append" to collect all values
# 3. Create tests that run for each browser specified
# 4. Run: pytest --browser=chrome --browser=firefox --browser=safari
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 4: REQUIRED OPTION
#
# Learn: required parameter, validation
#
# Tasks:
# 1. Add option --api-key that is required for certain tests
# 2. Create a fixture that retrieves the API key
# 3. Raise an error with helpful message if not provided
# 4. Create tests that use the API key
# 5. Test both with and without providing the option
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 2: pytest_generate_tests
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 5: DYNAMIC PARAMETRIZATION
#
# Learn: pytest_generate_tests, metafunc.parametrize
#
# Tasks:
# 1. Create pytest_generate_tests hook in conftest.py
# 2. Check if fixture name "dynamic_input" is in metafunc.fixturenames
# 3. Generate parameters dynamically (e.g., read from a list)
# 4. Use metafunc.parametrize() to add the parameters
# 5. Create a test using the dynamic_input fixture
# ----------------------------------------------------------------------


def test_dynamic(dynamic_input):
    print(f"Dynamic input: {dynamic_input}")
    assert isinstance(dynamic_input, int)


# ----------------------------------------------------------------------
# 🟡 6: PARAMETRIZE FROM COMMAND LINE
#
# Learn: Combining addoption with generate_tests
#
# Tasks:
# 1. Add --test-data option that accepts multiple values
# 2. In pytest_generate_tests, read the option values
# 3. Parametrize tests with the provided values
# 4. Run: pytest --test-data=1 --test-data=2 --test-data=3
# 5. Verify three test runs occur
# ----------------------------------------------------------------------


def test_parametrized_data(test_data):
    print("Key from CLI", test_data)
    assert isinstance(test_data, str)


# ----------------------------------------------------------------------
# 🔴 7: CONDITIONAL PARAMETRIZATION
#
# Learn: Complex parametrization logic
#
# Tasks:
# 1. Create pytest_generate_tests that checks fixture name
# 2. For "user_type" fixture, parametrize with ["admin", "user", "guest"]
# 3. For "permission" fixture, parametrize based on another condition
# 4. Create tests using these fixtures
# 5. Verify correct number of test combinations generated
# ----------------------------------------------------------------------


def test_user_type(user_type):
    print(user_type)
    assert user_type in ["admin", "user", "guest"]


def test_permission(permission):
    assert permission in ["read", "write", "read_and_write"]


# ----------------------------------------------------------------------
# 🔴 8: PARAMETRIZE FROM EXTERNAL FILE
#
# Learn: Reading test data from files
#
# Tasks:
# 1. Create a JSON or CSV file with test data
# 2. In pytest_generate_tests, read the file
# 3. Parametrize tests with data from the file
# 4. Handle file not found gracefully
# 5. Create tests that use the external data
# ----------------------------------------------------------------------


def test_json_params(json_data):
    if int(json_data) % 2 == 0:
        assert True
    else:
        assert False


# =====================================================================
#                    SECTION 3: pytest_collection_finish
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 9: LIST COLLECTED TESTS
#
# Learn: pytest_collection_finish, session.items
#
# Tasks:
# 1. Create pytest_collection_finish hook
# 2. Iterate over session.items
# 3. Print each test's name and location
# 4. Print total count of collected tests
# 5. Run pytest and observe the output
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 10: FILTER BY MARKER
#
# Learn: item.get_closest_marker()
#
# Tasks:
# 1. Create tests with different markers (@pytest.mark.smoke, @pytest.mark.regression)
# 2. In pytest_collection_finish, find tests with specific marker
# 3. Print list of tests with "smoke" marker
# 4. Print list of tests with "regression" marker
# 5. Show count for each category
# ----------------------------------------------------------------------


class TestSmokeAndRegression:

    @pytest.mark.smoke
    def test_smoke_1(self):
        assert True

    @pytest.mark.smoke
    def test_smoke_2(self):
        assert True

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_smoke_3(self):
        assert True

    @pytest.mark.regression
    def test_regression_1(self):
        assert True

    @pytest.mark.regression
    def test_regression_2(self):
        assert True

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_regression_3(self):
        assert True

    def test_with_no_mark(self):
        assert True


# ----------------------------------------------------------------------
# 🔴 11: MODIFY COLLECTION
#
# Learn: Modifying session.items
#
# Tasks:
# 1. Create pytest_collection_modifyitems hook (similar to collection_finish)
# 2. Reorder tests based on a criteria (e.g., markers, names)
# 3. Put "smoke" tests first, then "regression", then others
# 4. Create tests with various markers
# 5. Verify execution order changed
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 12: DESELECT TESTS DYNAMICALLY
#
# Learn: Removing items from collection
#
# Tasks:
# 1. Create hook that checks a condition (e.g., environment variable)
# 2. Deselect (remove) certain tests based on condition
# 3. Report which tests were deselected and why
# 4. Test with different environment settings
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: pytest_sessionfinish
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 13: SESSION SUMMARY
#
# Learn: pytest_sessionfinish, session object
#
# Tasks:
# 1. Create pytest_sessionfinish hook
# 2. Access session information (testscollected, testsfailed)
# 3. Print a custom summary after all tests complete
# 4. Include pass/fail counts and duration
# 5. Run tests and observe the summary
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 14: EXIT STATUS HANDLING
#
# Learn: exitstatus parameter
#
# Tasks:
# 1. Create pytest_sessionfinish with exitstatus parameter
# 2. Print different messages based on exit status
# 3. Exit status 0 = all passed, 1 = some failed, etc.
# 4. Create mix of passing and failing tests
# 5. Observe different exit status messages
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 15: GENERATE TEST REPORT
#
# Learn: Writing results to file
#
# Tasks:
# 1. In pytest_sessionfinish, collect all test results
# 2. Generate a simple text or JSON report file
# 3. Include test names, status, and duration
# 4. Save to a file (e.g., test_report.txt)
# 5. Verify report file is created after test run
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 16: SEND NOTIFICATION
#
# Learn: Post-run actions
#
# Tasks:
# 1. In pytest_sessionfinish, prepare a summary message
# 2. Simulate sending notification (print to console)
# 3. Include: total tests, passed, failed, duration
# 4. Only "send" notification if there are failures
# 5. Format message appropriately
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: OTHER USEFUL HOOKS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 17: pytest_runtest_setup
#
# Learn: Hook that runs before each test
#
# Tasks:
# 1. Create pytest_runtest_setup(item) hook
# 2. Print the test name before it starts
# 3. Check for specific markers and perform setup actions
# 4. Skip test dynamically based on condition
# 5. Observe output for each test
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 18: pytest_runtest_teardown
#
# Learn: Hook that runs after each test
#
# Tasks:
# 1. Create pytest_runtest_teardown(item) hook
# 2. Print the test name after it completes
# 3. Perform cleanup actions
# 4. Log test completion time
# 5. Observe output after each test
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 19: pytest_runtest_makereport
#
# Learn: Customizing test reports
#
# Tasks:
# 1. Create pytest_runtest_makereport hook
# 2. Access the test outcome (passed, failed, skipped)
# 3. Add custom information to the report
# 4. Store results for later use (e.g., in a fixture)
# 5. Use stored results in pytest_sessionfinish
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 20: pytest_configure
#
# Learn: Hook for initial configuration
#
# Tasks:
# 1. Create pytest_configure(config) hook
# 2. Register custom markers programmatically
# 3. Set up global configuration
# 4. Initialize any resources needed for the test session
# 5. Verify configuration is applied before tests run
# ----------------------------------------------------------------------


# @pytest.mark.custom_marker
# def test_true():
#     assert True


# =====================================================================
#                    SECTION 6: COMBINING HOOKS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 21: ENVIRONMENT-BASED TEST SUITE
#
# Scenario: Different tests for different environments
#
# Tasks:
# 1. Use pytest_addoption to add --env option
# 2. Use pytest_collection_modifyitems to filter tests by environment
# 3. Use pytest_sessionfinish to report environment-specific results
# 4. Create tests marked for specific environments
# 5. Run with different --env values and observe behavior
# ----------------------------------------------------------------------


def test_stg():
    assert False


def test_stg_2():
    assert True


def test_prod_1():
    assert True


def test_dev_1():
    assert True


# ----------------------------------------------------------------------
# 🔴 22: CUSTOM TEST RETRY
#
# Scenario: Retry failed tests automatically
#
# Tasks:
# 1. Use pytest_addoption to add --retries option
# 2. Track failed tests during the session
# 3. Use appropriate hooks to implement retry logic
# 4. Report which tests needed retries
# 5. Create flaky tests to verify retry behavior
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 23: TEST TIMING REPORT
#
# Scenario: Track and report test execution times
#
# Tasks:
# 1. Use pytest_runtest_setup to record start time
# 2. Use pytest_runtest_teardown to calculate duration
# 3. Store timing data for all tests
# 4. Use pytest_sessionfinish to generate timing report
# 5. Show slowest tests and average duration
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 24: DYNAMIC FIXTURE INJECTION
#
# Scenario: Add fixtures based on markers
#
# Tasks:
# 1. Use pytest_generate_tests to check for markers
# 2. Inject different fixtures based on marker presence
# 3. Create tests with various markers
# 4. Verify correct fixtures are injected
# 5. Handle missing markers gracefully
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 25: FULL CUSTOM TEST FRAMEWORK
#
# Scenario: Build a mini test framework using multiple hooks
#
# Tasks:
# 1. pytest_addoption: Add --report-format (json, html, text)
# 2. pytest_configure: Set up logging, register markers
# 3. pytest_collection_finish: Print test plan
# 4. pytest_runtest_setup/teardown: Log test lifecycle
# 5. pytest_sessionfinish: Generate report in specified format
# 6. Create comprehensive tests to verify all hooks work together
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Common Hooks
# ======================================================================
#
# Hook                              | When It Runs
# ----------------------------------|------------------------------------
# pytest_addoption                  | Before command line parsing
# pytest_configure                  | After command line parsing
# pytest_collection_modifyitems     | After test collection
# pytest_collection_finish          | After collection is complete
# pytest_generate_tests             | During test collection
# pytest_runtest_setup              | Before each test
# pytest_runtest_call               | During test execution
# pytest_runtest_teardown           | After each test
# pytest_runtest_makereport         | After each test phase
# pytest_sessionfinish              | After all tests complete
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Hook Parameters
# ======================================================================
#
# Hook                    | Key Parameters
# ------------------------|----------------------------------------------
# pytest_addoption        | parser (add options), pluginmanager
# pytest_configure        | config (pytest configuration)
# pytest_generate_tests   | metafunc (parametrize, fixturenames)
# pytest_collection_*     | session (items list)
# pytest_runtest_*        | item (single test item)
# pytest_sessionfinish    | session, exitstatus (0=pass, 1=fail)
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - parser.addoption
# ======================================================================
#
# Parameter    | Description
# -------------|--------------------------------------------------
# action       | "store", "store_true", "append"
# default      | Default value if not provided
# help         | Help text for --help
# choices      | List of allowed values
# required     | Whether option is required
# type         | Type conversion (int, str, etc.)
#
# ======================================================================


# ======================================================================
# 📁 FILE STRUCTURE
# ======================================================================
#
# project/
# ├── conftest.py      <- All hooks go here
# ├── test_sample.py   <- Your tests
# ├── test_another.py  <- More tests
# └── pytest.ini       <- Pytest configuration (optional)
#
# ======================================================================


# ======================================================================
# 🚀 HOW TO RUN
# ======================================================================
#
# Basic:           pytest
# With option:     pytest --env=staging
# Verbose:         pytest -v
# Show prints:     pytest -s
# Specific file:   pytest test_sample.py
#
# ======================================================================
