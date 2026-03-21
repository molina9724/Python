import re
from playwright.sync_api import Page, expect


def test_05_add_remove_elements(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/add_remove_elements/
    1. Click the "Add Element" button 3 times
    2. Click one of the "Delete" buttons that appeared
    """
    pass


def test_06_context_menu(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/context_menu
    1. Find the box in the center of the page (id="hot-spot")
    2. Right-click on it using .click(button="right")
    3. A browser alert will pop up. Accept it with: page.on("dialog", lambda d: d.accept())
       (Put the page.on line BEFORE you right-click!)
    """
    pass


def test_07_dynamic_controls(page: Page):
    """
    Goal: Navigate to https://the-internet.herokuapp.com/dynamic_controls
    1. Find the checkbox next to "A checkbox" and .check() it
    2. Click the "Remove" button
    3. Click the "Enable" button under the disabled input
    4. Find the text input and .fill() it with "Playwright is awesome"
    """
    pass


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
    pass


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
    pass
