import re
from playwright.sync_api import Page, expect


def test_11_text_and_visibility(page: Page):
    """
    Goal: Learn to assert that text appears and elements become visible.
    Navigate to: https://the-internet.herokuapp.com/dynamic_loading/1

    1. Click the "Start" button.
    2. Assert that the loading spinner is visible.
    3. Assert that the finish text appears and contains "Hello World!".
    """
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("div[id='start'] button").click()
    expect(page.locator("img[src='/img/ajax-loader.gif']")).to_be_visible()
    expect(page.locator("#finish")).to_contain_text("Hello World!")


def test_12_checkbox_states(page: Page):
    """
    Goal: Assert the state of checkboxes (checked vs unchecked).
    Navigate to: https://the-internet.herokuapp.com/checkboxes

    1. Assert that the first checkbox is NOT checked.
    2. Assert that the second checkbox IS checked.
    3. Check the first checkbox.
    4. Assert that the first checkbox is now checked!
    """
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    expect(page.locator("input[type='checkbox']").first).not_to_be_checked()
    expect(page.locator("input[type='checkbox']").last).to_be_checked()
    page.locator("input[type='checkbox']").first.check()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()


def test_13_input_values(page: Page):
    """
    Goal: Assert the value currently typed inside a text box.
    Navigate to: https://the-internet.herokuapp.com/login

    1. Find the username input and fill it with "SuperQAEngine".
    2. Assert that the text box physically holds that exact value.
    """
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("SuperQAEngine")
    expect(page.locator("#username")).to_have_value("SuperQAEngine")


def test_14_page_title_and_url(page: Page):
    """
    Goal: Assert the metadata of the page itself (Title and URL).
    Navigate to: https://playwright.dev/

    1. Assert that the URL contains the word "playwright".
    2. Assert that the title of the tab contains "Playwright".
    """
    page.goto("https://playwright.dev/")
    expect(page).to_have_url(re.compile("playwright"))
    expect(page).to_have_title(re.compile("Playwright"))


def test_15_disabled_elements(page: Page):
    """
    Goal: Assert that a user physically CANNOT interact with an element.
    Navigate to: https://the-internet.herokuapp.com/dynamic_controls

    1. Assert that the text input field is disabled.
    2. Click the "Enable" button.
    3. Wait for it to become enabled by asserting the opposite.
    """
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    page.locator("button[onclick='swapInput()']").click()
    expect(page.locator("input[type='text']")).to_be_enabled()
