import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

UNLOCKED_USERS = (
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
)
TESTDATA = [(user, PASSWORD, INVENTORY_URL) for user in UNLOCKED_USERS]

LOCKED_USERS = ("locked_out_user",)
"""place the locked user after the first unlocked user to match the
order shown on the demo page (was previously inserted at index 1
when using a mutable list)"""
ALL_USERS = (UNLOCKED_USERS[0],) + LOCKED_USERS + UNLOCKED_USERS[1:]

# explicit expected order for the login credentials block on the page
EXPECTED_LOGIN_USERNAMES = list(ALL_USERS)


@pytest.fixture(scope="function", autouse=True)
def go_home(page: Page):
    page.goto(BASE_URL)
    return page


def test_01_document_title(page: Page):
    expect(page).to_have_title("Swag Labs")


def test_02_page_title(page: Page):
    heading = page.locator(".login_logo")
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Swag Labs")


def test_03_username_textbox_is_displayed(page: Page):
    login_input = page.get_by_role("textbox", name="Username")
    expect(login_input).to_be_visible()


def test_04_password_textbox_is_displayed(page: Page):
    password_input = page.get_by_role("textbox", name="Password")
    expect(password_input).to_be_visible()


def test_05_login_button_is_displayed(page: Page):
    login_button = page.get_by_role("button", name="Login")
    expect(login_button).to_be_visible()


def test_06_usernames_heading_is_displayed(page: Page):
    users_heading = page.get_by_role("heading", name="Accepted usernames are:")
    expect(users_heading).to_be_visible()
    expect(users_heading).to_have_text("Accepted usernames are:")


def test_07_usernames(page: Page):
    container = page.locator("#login_credentials")
    text = container.inner_text()  # <- inner_text keeps visible newlines
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines and lines[0].lower().startswith("accepted usernames"):
        usernames = lines[1:]
    else:
        usernames = lines

    assert usernames == EXPECTED_LOGIN_USERNAMES


def test_08_password_heading(page: Page):
    heading = page.get_by_role("heading", name="Password for all users:")
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Password for all users:")


def test_09_password(page: Page):
    container = page.locator(".login_password")
    text = container.inner_text()
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines and lines[0].lower().startswith("password"):
        password = lines[1:]
    else:
        password = lines

    assert password == ["secret_sauce"]


@pytest.mark.parametrize(
    "user, password, expected", argvalues=TESTDATA, ids=UNLOCKED_USERS
)
def test_10_successful_login_and_logout(page: Page, user, password, expected):
    page.get_by_role("textbox", name="Username").fill(user)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(expected)

    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url(BASE_URL)
    expect(page).to_have_url(BASE_URL)
