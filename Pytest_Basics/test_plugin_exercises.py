# ======================================================================
# 🔌 PYTEST PLUGINS EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# Install plugins with: pip install <plugin-name>
# ======================================================================

import pytest
from pathlib import Path


# =====================================================================
#                    SECTION 1: pytest-cov (Coverage)
# =====================================================================
# Install: pip install pytest-cov
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: BASIC COVERAGE REPORT
#
# Learn: pytest --cov
#
# Tasks:
# 1. Create a simple module with a few functions (e.g., math operations)
# 2. Create tests that cover SOME but not all functions
# 3. Run: pytest --cov=your_module tests/
# 4. Observe the coverage percentage
# 5. Note which lines are not covered
# ----------------------------------------------------------------------


class Calculator:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Division by 0 is not allowed"


@pytest.fixture(scope="class")
def my_calculator():
    return Calculator()


class TestCalculator:

    def test_addition(self, my_calculator):
        assert my_calculator.addition(0, 0) == 0

    def test_subtraction(self, my_calculator):
        assert my_calculator.subtraction(0, 0) == 0

    def test_multiply(self, my_calculator):
        assert my_calculator.multiply(0, 0) == 0

    # def test_divide_by_zero(self, my_calculator):
    #     assert my_calculator.divide(0, 0) == "Division by 0 is not allowed"


# ----------------------------------------------------------------------
# 🟢 2: HTML COVERAGE REPORT
#
# Learn: --cov-report=html
#
# Tasks:
# 1. Use your module and tests from exercise 1
# 2. Run: pytest --cov=your_module --cov-report=html
# 3. Open the generated htmlcov/index.html in a browser
# 4. Explore the interactive report
# 5. Click on files to see line-by-line coverage
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 3: COVERAGE THRESHOLD
#
# Learn: --cov-fail-under
#
# Tasks:
# 1. Run: pytest --cov=your_module --cov-fail-under=90
# 2. Observe the test fails if coverage is below 90%
# 3. Add more tests to increase coverage
# 4. Run again until coverage meets the threshold
# 5. Experiment with different threshold values
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 4: EXCLUDE FILES FROM COVERAGE
#
# Learn: Coverage configuration
#
# Tasks:
# 1. Create a .coveragerc file or add to pyproject.toml
# 2. Configure files/patterns to exclude from coverage
# 3. Exclude test files themselves from coverage
# 4. Exclude __init__.py files
# 5. Run coverage and verify exclusions work
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 2: pytest-timeout
# =====================================================================
# Install: pip install pytest-timeout
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 5: BASIC TIMEOUT
#
# Learn: @pytest.mark.timeout
#
# Tasks:
# 1. Create a test with @pytest.mark.timeout(2) (2 seconds)
# 2. Inside, use time.sleep(1) - should pass
# 3. Create another test with timeout(1) and sleep(3) - should fail
# 4. Observe the timeout error message
# 5. Understand when timeouts are useful
# ----------------------------------------------------------------------

import time


# @pytest.mark.timeout(2)
def test_timeout():
    time.sleep(2)


# @pytest.mark.timeout(1)
def test_timeout2():
    time.sleep(3)


# ----------------------------------------------------------------------
# 🟡 6: GLOBAL TIMEOUT
#
# Learn: --timeout command line option
#
# Tasks:
# 1. Create several tests with different durations
# 2. Run: pytest --timeout=2
# 3. Observe which tests pass/fail based on duration
# 4. Test without --timeout to see normal behavior
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 7: TIMEOUT IN CONFIGURATION
#
# Learn: pytest.ini or pyproject.toml configuration
#
# Tasks:
# 1. Add timeout setting to pytest.ini: timeout = 5
# 2. Create tests without explicit timeout markers
# 3. Verify global timeout applies to all tests
# 4. Override global timeout with marker on specific test
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 3: pytest-xdist (Parallel Execution)
# =====================================================================
# Install: pip install pytest-xdist
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 8: PARALLEL TEST EXECUTION
#
# Learn: pytest -n <num>
#
# Tasks:
# 1. Create 10+ simple tests
# 2. Run: pytest (normal, note the time)
# 3. Run: pytest -n 2 (2 workers)
# 4. Run: pytest -n auto (auto-detect CPUs)
# 5. Compare execution times
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 9: PARALLEL WITH OUTPUT
#
# Learn: Observing parallel execution
#
# Tasks:
# 1. Create tests that print their name and start time
# 2. Run: pytest -n 4 -v
# 3. Observe tests running out of order
# 4. Understand the implications for test independence
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 10: HANDLING SHARED RESOURCES
#
# Learn: Tests must be independent for parallel execution
#
# Tasks:
# 1. Create tests that use a shared file
# 2. Run in parallel - observe failures/race conditions
# 3. Fix by using unique file names per test
# 4. Use tmp_path fixture for isolation
# 5. Verify parallel execution now works
# ----------------------------------------------------------------------

shared_file = Path(
    "/Users/daniel_molina/Downloads/Python/Python/Pytest_Basics/shared_file.txt"
)


# @pytest.fixture(autouse=True)
# def clean_shared_file():
#     # Clean up before each test run
#     shared_file.write_text("start\n")


# def test_read_shared_file():
#     lines_seen = []
#     with open(shared_file, "r") as f:
#         for i in range(10):
#             lines = f.readlines()
#             lines_seen.append([l.strip() for l in lines])
#             time.sleep(0.05)
#     # Fail if 'testing writing...' line appears unexpectedly (race condition)
#     for lines in lines_seen:
#         if any("testing writing" in line for line in lines):
#             pytest.fail("Concurrent writer detected modification during read!")


# def test_write_shared_file():
#     # Wait to ensure reader is started
#     time.sleep(0.1)
#     with open(shared_file, "a") as f:
#         f.write("testing writing on a shared file\n")
#         f.flush()
#         time.sleep(0.1)
#     assert True

import shutil


def test_verify_tmp_path(tmp_path):
    assert tmp_path.exists()


def test_remove_tmp_path(tmp_path):
    shutil.rmtree(tmp_path)


# ----------------------------------------------------------------------
# 🔴 11: LOOPONFAIL
#
# Learn: --looponfail flag
#
# Tasks:
# 1. Create a failing test
# 2. Run: pytest --looponfail (or -f)
# 3. Observe it waits for file changes
# 4. Fix the test and save the file
# 5. Observe automatic re-run
# ----------------------------------------------------------------------


def test_fail_test():
    assert True


# =====================================================================
#                    SECTION 4: pytest-mock
# =====================================================================
# Install: pip install pytest-mock
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 12: BASIC MOCKER FIXTURE
#
# Learn: mocker fixture from pytest-mock
#
# Tasks:
# 1. Create a function that calls another function
# 2. Write a test that uses the mocker fixture
# 3. Use mocker.patch() to mock the inner function
# 4. Set return_value on the mock
# 5. Verify the mock was called
# ----------------------------------------------------------------------


def func_1():
    return True


def func_2():
    return func_1()


def test_mock(mocker):
    mock = mocker.patch(__name__ + ".func_1", return_value="patched")
    result = func_2()
    assert result == "patched"
    mock.assert_called_once()


# ----------------------------------------------------------------------
# 🟡 13: MOCKER.SPY
#
# Learn: Spying on real functions
#
# Tasks:
# 1. Create a function to spy on
# 2. Use mocker.spy() to wrap it
# 3. Call the function normally
# 4. Verify both: real behavior occurred AND call was tracked
# 5. Check call arguments using spy.assert_called_with()
# ----------------------------------------------------------------------

import sys
from pytest_mock import MockerFixture


def test_spy_method(mocker: MockerFixture):
    spy = mocker.spy(sys.modules[__name__], "func_1")
    result = func_1()
    assert result is True
    spy.assert_called_once_with()


# ----------------------------------------------------------------------
# 🟡 14: MOCKER.STUB
#
# Learn: Creating stub objects
#
# Tasks:
# 1. Use mocker.stub() to create a stub with a name
# 2. Use the stub as a callback or dependency
# 3. Verify the stub was called
# 4. Compare stub vs mock behavior
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 15: PATCH OBJECT ATTRIBUTE
#
# Learn: mocker.patch.object()
#
# Tasks:
# 1. Create a class with methods
# 2. Create an instance of the class
# 3. Use mocker.patch.object() to mock a specific method
# 4. Verify the patched method returns mock value
# 5. Other methods should still work normally
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: pytest-html
# =====================================================================
# Install: pip install pytest-html
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 16: GENERATE HTML REPORT
#
# Learn: --html option
#
# Tasks:
# 1. Create several tests (mix of pass, fail, skip)
# 2. Run: pytest --html=report.html
# 3. Open report.html in a browser
# 4. Explore the report structure
# 5. Note the pass/fail/skip counts and details
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 17: SELF-CONTAINED REPORT
#
# Learn: --self-contained-html
#
# Tasks:
# 1. Run: pytest --html=report.html --self-contained-html
# 2. Compare file size to non-self-contained
# 3. Self-contained includes CSS/JS inline
# 4. Useful for sharing report as single file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 18: CUSTOM HTML REPORT
#
# Learn: Extending pytest-html with hooks
#
# Tasks:
# 1. Create conftest.py with pytest_html_report_title hook
# 2. Set a custom title for the report
# 3. Use pytest_html_results_table_header to add columns
# 4. Use pytest_html_results_table_row to add data
# 5. Generate report and verify customizations
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: pytest-asyncio
# =====================================================================
# Install: pip install pytest-asyncio
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 19: BASIC ASYNC TEST
#
# Learn: @pytest.mark.asyncio
#
# Tasks:
# 1. Create an async function to test (async def ...)
# 2. Create a test with @pytest.mark.asyncio decorator
# 3. Use await inside the test
# 4. Run the test and verify it works
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: ASYNC FIXTURE
#
# Learn: Async fixtures with pytest-asyncio
#
# Tasks:
# 1. Create an async fixture (async def with @pytest.fixture)
# 2. Use await in the fixture setup
# 3. Create an async test that uses the fixture
# 4. Verify async fixture and test work together
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 21: TESTING ASYNC FUNCTIONS
#
# Learn: Testing real async code
#
# Tasks:
# 1. Create an async function that fetches/processes data
# 2. Create async tests to verify behavior
# 3. Test both successful and error scenarios
# 4. Use asyncio.sleep to simulate delays
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 22: ASYNC WITH TIMEOUT
#
# Learn: Combining asyncio with timeout
#
# Tasks:
# 1. Create an async test with @pytest.mark.timeout
# 2. Create async operation that may hang
# 3. Verify timeout works with async code
# 4. Use asyncio.wait_for for internal timeouts
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: COMBINING PLUGINS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 23: COVERAGE WITH PARALLEL
#
# Learn: pytest-cov + pytest-xdist
#
# Tasks:
# 1. Run: pytest -n 4 --cov=your_module
# 2. Verify coverage is collected across all workers
# 3. Note any compatibility issues
# 4. Generate combined coverage report
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 24: FULL REPORTING SUITE
#
# Learn: Multiple plugins together
#
# Tasks:
# 1. Create comprehensive test suite
# 2. Run with: pytest --cov=module --html=report.html --timeout=10
# 3. Generate both coverage and HTML reports
# 4. Open HTML report and verify coverage data included
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 25: PLUGIN COMPATIBILITY CHECK
#
# Learn: Testing plugin combinations
#
# Tasks:
# 1. Install multiple plugins: cov, html, xdist, mock, timeout
# 2. Create tests using features from each plugin
# 3. Run with various plugin combinations
# 4. Document any conflicts or issues
# 5. Find working configuration for all plugins
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Plugin Installation
# ======================================================================
#
# pip install pytest-cov        # Coverage reporting
# pip install pytest-timeout    # Test timeouts
# pip install pytest-xdist      # Parallel execution
# pip install pytest-mock       # Mocking fixture
# pip install pytest-html       # HTML reports
# pip install pytest-asyncio    # Async test support
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Common Commands
# ======================================================================
#
# Coverage:
#   pytest --cov=module_name
#   pytest --cov=module --cov-report=html
#   pytest --cov=module --cov-fail-under=80
#
# Timeout:
#   pytest --timeout=5
#   @pytest.mark.timeout(10)
#
# Parallel:
#   pytest -n 4          # 4 workers
#   pytest -n auto       # auto-detect CPUs
#   pytest --looponfail  # re-run on file change
#
# HTML:
#   pytest --html=report.html
#   pytest --html=report.html --self-contained-html
#
# Async:
#   @pytest.mark.asyncio
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - pytest-mock
# ======================================================================
#
# mocker.patch("path.to.function")     # Patch a function
# mocker.patch.object(obj, "method")   # Patch object method
# mocker.spy(obj, "method")            # Spy on real method
# mocker.stub(name="my_stub")          # Create a stub
#
# ======================================================================


# ======================================================================
# ⚠️  PLUGIN COMPATIBILITY NOTES
# ======================================================================
#
# - Some plugins may conflict with each other
# - Always test plugin combinations before use
# - xdist may have issues with some other plugins
# - Check plugin documentation for known issues
# - Keep plugins updated to latest versions
#
# ======================================================================


# ======================================================================
# 🚀 HOW TO RUN
# ======================================================================
#
# Basic:              pytest
# With coverage:      pytest --cov=mymodule
# Parallel:           pytest -n auto
# With timeout:       pytest --timeout=30
# HTML report:        pytest --html=report.html
# Combined:           pytest -n 4 --cov=mod --html=report.html
#
# ======================================================================
