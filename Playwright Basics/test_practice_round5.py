import pytest
from playwright.sync_api import Page, expect
import re

# HOOKS (Fixtures) IN PYTEST
# In Playwright Python, "Hooks" (like BeforeEach or AfterAll) are handled by Pytest "Fixtures".
# A fixture runs code BEFORE your test starts. If you use the "yield" keyword,
# you can also run code AFTER your test finishes!


@pytest.fixture(autouse=True)
def setup_and_teardown(page: Page):
    """
    Goal: Run this code automatically before AND after every single test in this file.
    1. Print "--> Test Starting: Navigating to Practice Site"
    2. Go to "https://the-internet.herokuapp.com/"
    3. Use the Python `yield` keyword to pause the hook here and let the test run!
    4. Print "--> Test Finished: Closing down."
    """
    print("Test Starting: Navigating to Practice Site")
    page.goto("https://the-internet.herokuapp.com/")
    yield
    print("Test Finished: Closing down")


def test_20_hooks_in_action(page: Page):
    """
    Goal: Because the 'setup_and_teardown' hook has autouse=True, we don't
          have to write page.goto("https://the-internet.herokuapp.com/") here!

    1. Assert that the page URL is already "https://the-internet.herokuapp.com/"
       (because the hook did it for us!)
    """
    expect(page).to_have_url(re.compile(r"https://the-internet.herokuapp.com/"))


def test_21_retry_mechanism(page: Page):
    """
    Goal: Learn how to force a test to retry if it explodes.
    (Actually, we do this via CLI arguments or pytest.ini, not inside the test itself!)

    1. Just try to click a button that doesn't exist to force a failure.
       Example: page.locator("#completely_fake_button").click(timeout=1000)
    """
    page.locator("#completely_fake_button").click(timeout=1000)
