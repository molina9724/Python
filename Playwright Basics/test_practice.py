import re
from playwright.sync_api import Page, expect


def test_01_login(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/login
    1. Fill username with: tomsmith
    2. Fill password with: SuperSecretPassword!
    3. Click the Login button
    4. Assert that you logged in successfully (hint: look for the green flash message)
    """
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button").click()
    expect(page.locator("#flash")).to_be_visible()


def test_02_checkboxes_and_dropdowns(page: Page):
    """
    Goal: Navigate to checkboxes and dropdown pages
    1. Check checkbox 1
    2. Uncheck checkbox 2
    3. Select option 2 from the dropdown
    """
    page.goto("https://the-internet.herokuapp.com")
    page.locator("a[href='/checkboxes']").click()
    page.locator("input:nth-child(1)").check()
    page.locator("//input[2]").uncheck()
    page.goto("https://the-internet.herokuapp.com")
    page.locator("a[href='/dropdown']").click()
    page.locator("#dropdown").select_option("2")


def test_03_mouse_hover(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/hovers
    1. Hover over the first profile picture to reveal the hidden text
    """
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.locator(".figure").first.hover()


def test_04_keyboard_and_files(page: Page):
    """
    Goal: Master Keyboard events and native File Uploads

    --- PART A: Keyboard presses ---
    1. Navigate to: https://the-internet.herokuapp.com/key_presses
    2. Find the input box (it has id="target")
    3. Use .focus() on it to put your blinking cursor inside.
    4. Use .press("Space") on it to simulate a human hitting the Spacebar!

    --- PART B: File Uploads ---
    5. Navigate to: https://the-internet.herokuapp.com/upload
    6. Find the 'Choose File' button (it has id="file-upload")
    7. Use .set_input_files("pytest.ini") on it to attach your local pytest config file!
    8. Find the 'Upload' button (it has id="file-submit") and click() it to submit the form.
    """
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.focus("#target")
    page.press("#target", "Space")

    page.goto("https://the-internet.herokuapp.com/upload")
    # page.locator("#file-upload").click()
    page.set_input_files(
        "#file-upload", "/Users/daniel_molina/Downloads/Python/Python/pytest.ini"
    )
    page.locator("#file-submit").click()
