import re
from playwright.sync_api import Page, expect


def test_05_add_remove_elements(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/add_remove_elements/
    1. Click the "Add Element" button 3 times
    2. Click one of the "Delete" buttons that appeared
    """
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    for _ in range(3):
        page.locator("button[onclick='addElement()']").click()
    for _ in range(3):
        page.locator(".added-manually").first.click()


def test_06_context_menu(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/context_menu
    1. Find the box in the center of the page (id="hot-spot")
    2. Right-click on it using .click(button="right")
    3. A browser alert will pop up. Accept it with: page.on("dialog", lambda d: d.accept())
       (Put the page.on line BEFORE you right-click!)
    """
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page.on("dialog", lambda d: d.accept())
    page.locator("#hot-spot").click(button="right")

    # Weird logic


def test_07_dynamic_controls(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/dynamic_controls
    1. Find the checkbox next to "A checkbox" and .check() it
    2. Click the "Remove" button
    3. Click the "Enable" button under the disabled input
    4. Find the text input and .fill() it with "Playwright is awesome"
    """
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    page.locator("input[type='checkbox']").check()
    page.locator("button[onclick='swapCheckbox()']").click()
    page.locator("button[onclick='swapInput()']").click()
    page.locator("input[type='text']").fill("Playwright is awesome")


def test_08_basic_auth(page: Page):
    """
    Goal: Bypass HTTP Basic Authentication (username/password popup)
    Navigate to: https://admin:admin@the-internet.herokuapp.com/basic_auth
    (The trick: embed the credentials directly into the URL!)
    """
    pass


def test_09_multiple_windows(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/windows
    1. Click "Click Here" to open a new tab
    2. Playwright needs special handling for new tabs. Use this pattern:
       with page.expect_popup() as popup_info:
           page.locator("a[href='/windows/new']").click()
       new_page = popup_info.value
    3. Now use new_page (not page!) to read the new tab's content
    """
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()
    new_page = popup_info.value
    new_page.goto("https://the-internet.herokuapp.com/windows")
    page.bring_to_front()
    page.goto("https://playwright.dev/python/docs/api/class-locator#locator-press")


def test_10_javascript_alerts(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/javascript_alerts
    1. Set up a dialog handler BEFORE clicking: page.on("dialog", lambda d: d.accept())
    2. Click the "Click for JS Alert" button
    3. Click the "Click for JS Confirm" button
    4. For the JS Prompt, you need to TYPE text into the popup:
       page.on("dialog", lambda d: d.accept("Hello from Playwright!"))
       (Set this handler, then click the "Click for JS Prompt" button)
    """
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda d: d.accept())
    page.locator("button[onclick='jsAlert()']").click()
    page.once("dialog", lambda d: d.accept())
    page.locator("button[onclick='jsConfirm()']").click()

    page.once("dialog", lambda d: d.accept("Hello from Playwright!"))
    page.locator("button[onclick='jsPrompt()']").click()
