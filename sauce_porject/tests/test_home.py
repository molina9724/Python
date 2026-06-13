import re

import pytest
from playwright.sync_api import Page, Playwright, expect

BASE_URL = "https://www.saucedemo.com/"


def test_01_document_title(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title(re.compile("Swag Labs"))


def test_02_page_title(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("heading", name="Swag Labs")).to_have_text("Swag Labs")


def test_03_username_textbox_is_displayed(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()


def test_04_password_textbox_is_displayed(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()


def test_05_login_button_is_displayed(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("button", name="Login")).to_be_visible()


def test_06_usernames_heading_is_displayed(page: Page):
    page.goto(BASE_URL)
    expect(page.locator(".login_credentials")).to_be_visible()


def test_07_usernames_heading(page: Page):
    page.goto(BASE_URL)
    heading = page.get_by_role("heading", name="Accepted usernames are:").text_content()
    assert heading == "Accepted usernames are:"


def test_08_usernames(page: Page):
    page.goto(BASE_URL)
    container = page.locator("#login_credentials")
    text = container.inner_text()  # <- inner_text keeps visible newlines
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines and lines[0].lower().startswith("accepted usernames"):
        usernames = lines[1:]
    else:
        usernames = lines

    assert usernames == [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
    ]


def test_09_password_heading(page: Page):
    page.goto(BASE_URL)
    expect(page.get_by_role("heading", name="Password for all users:")).to_have_text(
        "Password for all users:"
    )


def test_10_password(page: Page):
    page.goto(BASE_URL)
    container = page.locator(".login_password")
    text = container.inner_text()
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines and lines[0].lower().startswith("password"):
        password = lines[1:]
    else:
        password = lines

    assert password == ["secret_sauce"]
