import re
from playwright.sync_api import Page, expect


def test_16_get_by_role_basics(page: Page):
    # URL: https://the-internet.herokuapp.com/add_remove_elements/
    # Goal: Click "Add Element" and assert "Delete" button appears using exclusively get_by_role.
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.get_by_role("button", name="Add Element").click()
    delete_button = page.get_by_role("button", name="Delete")
    expect(delete_button).to_be_visible()


def test_17_get_by_placeholder_and_label(page: Page):
    # URL: https://the-internet.herokuapp.com/login
    # Goal: Login using get_by_label for text boxes, and get_by_role for the button.
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")


def test_18_custom_error_messages(page: Page):
    # URL: https://the-internet.herokuapp.com/checkboxes
    # Goal: Assert checkbox 1 is checked, but force a custom failure string (e.g. "ERROR: Box unchecked!").
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = page.get_by_role("checkbox").first
    expect(checkbox1, "ERROR: Box unchecked!").to_be_checked()


def test_19_get_by_text(page: Page):
    # URL: https://the-internet.herokuapp.com/hovers
    # Goal: Hover over the first image, then locate the phrase "name: user1" using get_by_text. Assert it's visible.
    page.goto("https://the-internet.herokuapp.com/hovers")
    first_image = page.locator(".figure").first
    first_image.hover()
    user1_text = page.get_by_text(re.compile(r"name:\s*user1", re.IGNORECASE))
    expect(user1_text).to_be_visible()
