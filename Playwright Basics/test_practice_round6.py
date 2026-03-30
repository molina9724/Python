# ======================================================================
# 🎭 PLAYWRIGHT EXERCISES - the-internet.herokuapp.com
# ======================================================================

from playwright.sync_api import Page, expect, sync_playwright, Playwright
from pathlib import Path
import re
import pytest
import sys

BASE_URL = "https://the-internet.herokuapp.com"


# =====================================================================
#                    SECTION 1: CLICK ACTIONS
# =====================================================================


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # Before each instructions until yield
    print("Before the test runs")
    page.goto("https://the-internet.herokuapp.com")
    yield
    # After each instructions after yield
    print("After the test runs")


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def mobile_page(browser, playwright: Playwright):
    iphone13 = playwright.devices["iPhone 13"]
    context = browser.new_context(**iphone13)
    page = context.new_page()
    # 🎥 Manually start the "Flight Recorder"
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page
    # 💾 Save the trace to a file
    # context.tracing.stop(path="test-results/manual-trace.zip")
    page.close()
    context.close()


@pytest.fixture(scope="function")
def browser_context(browser):
    context = browser.new_context()
    # 🎥 Manually start the "Flight Recorder"
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    # 💾 Save the trace to a file
    # context.tracing.stop(path="test-results/manual-trace.zip")
    context.close()


# 🟣 VISUAL REGRESSION TEST (The Internet)
def test_visual_homepage_the_internet(page, assert_snapshot):
    page.goto("https://the-internet.herokuapp.com/")
    assert_snapshot(page.screenshot(), name="the-internet-home.png")


# 🟢 1: ADD/REMOVE ELEMENTS - /add_remove_elements/
# Click "Add Element" 5 times, verify 5 Delete buttons, remove 2, verify 3 remain, remove all.
@pytest.mark.skip(reason="Just want to skip one")
def test_01_add_remove(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    for _ in range(5):
        page.get_by_role("button", name="Add Element").click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(5)

    for _ in range(2):
        page.get_by_role("button", name="Delete").first.click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(3)

    for _ in range(3):
        page.get_by_role("button", name="Delete").first.click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(0)


# 🟢 2: BASIC LOGIN FLOW - /login
# Fill username "tomsmith", password "SuperSecretPassword!", login, verify success, logout, verify back on login.
@pytest.mark.skipif(sys.version_info < (3, 12), reason="Requires Python 3.12 or higher")
def test_02_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="username").fill("tomsmith")
    page.get_by_role("textbox", name="password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    page.locator("a.button[href='/logout']").click()
    expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")


# 🟢 3: CHECKBOXES - /checkboxes
# Verify initial states, check/uncheck both, verify states changed, toggle back to original.
def test_03_checkboxes(mobile_page):
    mobile_page.goto("https://the-internet.herokuapp.com/checkboxes")

    # ⚠️ NOTE: We cannot use get_by_role("checkbox", name="checkbox 1") here!
    # The developer of this training site wrote terrible, inaccessible HTML.
    # The text "checkbox 1" is NOT wrapped in a <label> tag linked to the <input>,
    # so Playwright (and Screen Readers) see a raw checkbox with absolutely no name attached to it.
    # We are forced to use .first and .last to locate them instead!

    expect(mobile_page.get_by_role("checkbox").first).not_to_be_checked()
    expect(mobile_page.get_by_role("checkbox").last).to_be_checked()

    mobile_page.get_by_role("checkbox").first.check()
    expect(mobile_page.get_by_role("checkbox").first).to_be_checked()

    mobile_page.get_by_role("checkbox").last.uncheck()
    expect(mobile_page.get_by_role("checkbox").last).not_to_be_checked()


# 🟡 4: CONTEXT MENU (Right-click) - /context_menu
# Right-click the box, handle the JS alert, verify alert text is "You selected a context menu".
def test_04_context_menu(page: Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")

    def handle_alert(dialog):
        assert dialog.message == "You selected a context menu"
        dialog.accept()

    page.once("dialog", handle_alert)
    page.locator("#hot-spot").click(button="right")


# 🟡 5: DISAPPEARING ELEMENTS - /disappearing_elements
# Count menu items, refresh multiple times, detect when "Gallery" appears/disappears, click it when present.
def test_05_disappearing(page: Page):
    page.goto("https://the-internet.herokuapp.com/disappearing_elements")
    while True:
        gallery = page.locator("a[href='/gallery/']")
        gallery_count = gallery.count()

        if gallery_count > 0:
            gallery.click()
            expect(page).to_have_url(
                re.compile(r"https://the-internet.herokuapp.com/gallery/")
            )
            break
        else:
            print("Gallery didn't show up this time!")
        page.reload()


# =====================================================================
#                    SECTION 2: DROPDOWN & SELECT
# =====================================================================


# 🟢 6: DROPDOWN - /dropdown
# Select "Option 1" by label, verify, select "Option 2" by value, verify, get all options as list.
def test_06_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.get_by_role("combobox").select_option(label="Option 1")
    expect(page.get_by_role("combobox")).to_have_value("1")
    page.get_by_role("combobox").select_option(value="2")
    expect(page.get_by_role("combobox")).to_have_value("2")

    # Use value, it's more intuitive


# =====================================================================
#                    SECTION 3: DYNAMIC CONTENT
# =====================================================================


# 🟡 7: DYNAMIC CONTROLS - /dynamic_controls
# Click Remove, wait for "It's gone!", verify checkbox gone. Click Add, wait for reappear.
# Click Enable, wait for input enabled, fill text. Click Disable, verify disabled.
def test_07_dynamic_controls(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    page.get_by_role("button", name="Remove").click()
    expect(page.get_by_role("checkbox")).not_to_be_visible()

    page.get_by_role("button", name="Add").click()
    expect(page.get_by_role("checkbox")).to_be_visible()

    page.get_by_role("button", name="Enable").click()
    expect(page.get_by_role("textbox")).to_be_enabled()
    page.get_by_role("textbox").fill("1234567890")
    page.get_by_role("button", name="Disable").click()
    expect(page.get_by_role("textbox")).to_be_disabled()


# 🟡 8: DYNAMIC LOADING (Hidden) - /dynamic_loading/1
# Click Start, wait for loading, verify "Hello World!" appears. Element exists but is hidden initially.
def test_08_dynamic_loading_1(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    page.get_by_role("link", name="Example 1: Element on page that is hidden").click()
    page.get_by_role("button", name="Start").click()
    expect(page.locator("#finish")).to_be_visible()


# 🟡 9: DYNAMIC LOADING (Rendered) - /dynamic_loading/2
# Click Start, wait for loading, verify "Hello World!" appears. Element does NOT exist until loading completes.
def test_09_dynamic_loading_2(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    page.get_by_role("link", name="Example 2: Element rendered after the fact").click()
    page.get_by_role("button", name="Start").click()
    expect(page.locator("#finish")).to_be_visible()


# 🟡 10: DYNAMIC CONTENT - /dynamic_content
# Capture text from 3 rows, refresh, verify content changed. Enable static content, refresh, verify it stays same.
def test_10_dynamic_content(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_content")
    text = page.locator(".large-10.columns").all_inner_texts()
    page.reload()
    text_after_refresh = page.locator(".large-10.columns").all_inner_texts()
    assert text != text_after_refresh


# =====================================================================
#                    SECTION 4: FILE OPERATIONS
# =====================================================================


# 🟢 11: FILE UPLOAD - /upload
# Create a test file, use set_input_files(), click Upload, verify "File Uploaded!" and filename displayed.
def test_11_file_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    file = Path(
        "/Users/daniel_molina/Downloads/Python/Python/Playwright Basics/wolf_scratchpad.py"
    )
    page.set_input_files(
        "#file-upload",
        f"{str(file)}",
    )
    page.get_by_role("button", name="Upload").click()
    expect(page.get_by_role("heading", name="File Uploaded!")).to_be_visible()
    expect(page.get_by_text(file.name)).to_be_visible()


# 🟡 12: FILE DOWNLOAD - /download
# Get list of downloadable files, click first file, wait for download, verify file was downloaded.
def test_12_file_download(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")
    download_link = page.locator(".example a").get_by_text("some-file.txt")
    with page.expect_download() as download_info:
        download_link.click()
    download = download_info.value
    download.save_as("/Users/daniel_molina/Downloads/" + download.suggested_filename)


# =====================================================================
#                    SECTION 5: FRAMES & WINDOWS
# =====================================================================


# 🟡 13: FRAMES - iFrame - /iframe
# Switch to the TinyMCE editor iframe, clear content, type new text, verify text was entered.
def test_13_iframe(page: Page):
    pass


# 🟡 14: NESTED FRAMES - /nested_frames
# Navigate into nested frames. Get text from LEFT, MIDDLE, RIGHT (inside top frame) and BOTTOM frame.
def test_14_nested_frames(page: Page):
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    top = page.frame_locator("frame[name='frame-top']")
    left = top.frame_locator("frame[name='frame-left']")
    middle = top.frame_locator("frame[name='frame-middle']")
    right = top.frame_locator("frame[name='frame-right']")
    bottom = page.frame_locator("frame[name='frame-bottom']")

    left_text = left.get_by_text("LEFT").inner_text()
    middle_text = middle.get_by_text("MIDDLE").inner_text()
    right_text = right.get_by_text("RIGHT").inner_text()
    bottom_text = bottom.get_by_text("BOTTOM").inner_text()

    assert left_text.strip() == "LEFT"
    assert right_text.strip() == "RIGHT"
    assert middle_text.strip() == "MIDDLE"
    assert bottom_text.strip() == "BOTTOM"


# 🟡 15: MULTIPLE WINDOWS - /windows
# Click "Click Here", handle new tab, verify "New Window" text, close new tab, switch back.
def test_15_multiple_windows(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()
    new_page = popup_info.value
    expect(new_page.get_by_text("New Window")).to_be_visible()


# =====================================================================
#                    SECTION 6: HOVER & MOUSE ACTIONS
# =====================================================================


# 🟢 16: HOVERS - /hovers
# Hover over each user image, verify name appears, click "View profile", verify URL, go back. Repeat for all 3.
def test_16_hovers(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")

    avatars = page.locator(".figure")

    for index, avatar in enumerate(avatars.all(), 1):
        avatar.hover()
        expect(avatar.get_by_text(f"name: user{index}")).to_be_visible()
        expect(avatar.get_by_role("link", name="View profile")).to_be_visible()


# 🟡 17: DRAG AND DROP - /drag_and_drop
# Verify A is left B is right. Drag A to B, verify swap. Drag again to swap back.
def test_17_drag_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    expect(page.locator("#column-a")).to_have_text("A")
    expect(page.locator("#column-b")).to_have_text("B")

    page.locator("#column-a").drag_to(page.locator("#column-b"))

    expect(page.locator("#column-a")).to_have_text("B")
    expect(page.locator("#column-b")).to_have_text("A")


# 🟡 18: HORIZONTAL SLIDER - /horizontal_slider
# Get initial value, use ArrowRight/ArrowLeft to change, set to max (5), set to min (0).
def test_18_slider(page: Page):
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    initial_value = page.get_by_role("slider").input_value()
    page.get_by_role("slider").click()
    while page.get_by_role("slider").input_value() != "5":
        page.keyboard.press("ArrowRight")


# =====================================================================
#                    SECTION 7: KEYBOARD & INPUT
# =====================================================================


# 🟢 19: KEY PRESSES - /key_presses
# Click input, press keys (Enter, Escape, Tab, Backspace, Delete, Arrows, F1, Shift, Space) and verify result text.
def test_19_key_presses(page: Page):
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.locator("#target").click()
    results = {
        # "Enter": "ENTER",
        "Escape": "ESCAPE",
        "Tab": "TAB",
        "Backspace": "BACK_SPACE",
        "Delete": "DELETE",
        "ArrowUp": "UP",
        "ArrowDown": "DOWN",
        "ArrowLeft": "LEFT",
        "ArrowRight": "RIGHT",
        "F1": "F1",
        "Shift": "SHIFT",
        "Space": "SPACE",
    }
    for key in results.keys():
        page.keyboard.press(key)
        expect(page.locator("#result")).to_have_text(f"You entered: {results[key]}")


# 🟡 20: INPUTS (Number Field) - /inputs
# Focus number input, fill a number, use ArrowUp/Down to increment/decrement, verify non-numeric ignored.
def test_20_inputs(page: Page):
    page.goto("https://the-internet.herokuapp.com//inputs")
    number = 10
    page.get_by_role("spinbutton").fill(str(number))
    expect(page.get_by_role("spinbutton")).to_have_value(str(number))

    page.keyboard.press("ArrowUp")
    expect(page.get_by_role("spinbutton")).to_have_value(str(number + 1))
    page.keyboard.press("ArrowDown")
    expect(page.get_by_role("spinbutton")).to_have_value(str(number))

    page.get_by_role("spinbutton").clear()
    page.get_by_role("spinbutton").type("abc")
    expect(page.get_by_role("spinbutton")).to_have_value("")


# =====================================================================
#                    SECTION 8: JAVASCRIPT ALERTS
# =====================================================================


# 🟢 21: JS ALERTS - /javascript_alerts
# Handle JS Alert (accept), JS Confirm (accept then dismiss), JS Prompt (type text and accept). Verify results.
def test_21_alerts(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_contain_text("You successfully clicked an alert")

    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_contain_text("You clicked: Ok")

    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_contain_text("You clicked: Cancel")

    text = "hello"
    page.once("dialog", lambda dialog: dialog.accept(text))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_contain_text(f"You entered: {text}")


# =====================================================================
#                    SECTION 9: TABLES
# =====================================================================


# 🟡 22: SORTABLE DATA TABLES - /tables
# Extract Table 1 data, sort by Last Name, verify sorted. Find row with "jsmith" email, click edit. Delete "Bach" row.
def test_22_tables(page: Page):
    page.goto("https://the-internet.herokuapp.com/tables")

    table = page.locator("#table1")
    expect(table.get_by_role("columnheader", name="Last Name")).not_to_contain_class(
        "headerSortUp"
    )
    expect(table.get_by_role("columnheader", name="Last Name")).not_to_contain_class(
        "headerSortDown"
    )

    rows = table.locator("tbody tr").all()
    last_names = [row.locator("td").first.inner_text() for row in rows]

    table.get_by_role("columnheader", name="Last Name").click()
    filtered_last_names = [row.locator("td").first.inner_text() for row in rows]

    assert sorted(last_names) == filtered_last_names

    # for row in rows:
    #     if "jsmith@gmail.com" in row.inner_text():
    #         row.get_by_role("link", name="edit").click()
    #     if "Bach" in row.inner_text():
    #         row.get_by_role("link", name="delete").click()

    # No loop needed!
    table.locator("tr").filter(has_text="jsmith@gmail.com").get_by_role(
        "link", name="edit"
    ).click()
    table.locator("tr").filter(has_text="Bach").get_by_role(
        "link", name="delete"
    ).click()


# =====================================================================
#                    SECTION 10: CHALLENGING SCENARIOS
# =====================================================================


# 🟡 23: CHALLENGING DOM - /challenging_dom
# Buttons have random IDs. Find blue/red/green buttons by class. Click each. Get table data, find cell at row 3 col 4.
def test_23_challenging_dom(page: Page):
    page.goto("https://the-internet.herokuapp.com/challenging_dom")
    all_buttons = page.locator(".large-2.columns .button").all()
    for button in all_buttons:
        button.click()

    table_data = page.locator(".large-10.columns table")
    cell = page.locator("tbody tr").nth(2).locator("td").nth(3)

    expect(cell).to_have_text(re.compile(r"Definiebas\d+"))


# 🟡 24: NOTIFICATION MESSAGES - /notification_message_rendered
# Click "Click here" multiple times, capture notification messages, collect all unique messages.
def test_24_notifications(page: Page):
    page.goto("https://the-internet.herokuapp.com/notification_message_rendered")

    messages = []
    for _ in range(10):
        page.get_by_role("link", name="Click here").click()
        message = page.locator("#flash").inner_text()
        if message not in messages:
            messages.append(message)
    assert len(messages) >= 2


# 🔴 25: INFINITE SCROLL - /infinite_scroll
# Get initial paragraph count, scroll down, wait for new content, verify count increased, scroll until 20+ paragraphs.
def test_25_infinite_scroll(page: Page):
    page.goto("https://the-internet.herokuapp.com/infinite_scroll")

    while page.locator(".jscroll-added").count() < 20:
        old_count = page.locator(".jscroll-added").count()
        page.keyboard.press("End")
        expect(page.locator(".jscroll-added")).to_have_count(old_count + 1)


# 🔴 26: ENTRY AD (Popup Modal) - /entry_ad
# Modal auto-appears. Verify visible, get title/body, close it, re-enable it, refresh and verify it reappears.
def test_26_entry_ad(page: Page):
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    expect(page.locator(".modal-title")).to_be_visible()
    title = page.locator(".modal-title").inner_text()
    body = page.locator(".modal-footer").inner_text()
    page.locator("#modal").get_by_text("Close").click()
    page.get_by_role("link", name="click here").click()
    page.reload()
    expect(page.locator(".modal-title")).to_be_visible()


# 🔴 27: EXIT INTENT - /exit_intent
# Move mouse to top of viewport to trigger exit intent modal. Verify content, close, trigger again.
def test_27_exit_intent(page: Page):
    page.goto("https://the-internet.herokuapp.com/exit_intent")
    page.locator("html").dispatch_event("mouseleave")
    expect(page.locator(".modal")).to_be_visible()

    title = page.locator(".modal-title").inner_text()
    assert title.lower() == "This is a modal window".lower()

    body = page.locator(".modal-body").inner_text()
    assert (
        body.lower()
        == "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something).".lower()
    )

    page.locator(".modal-footer").click()
    expect(page.locator(".modal")).not_to_be_visible()
    page.reload()
    page.locator("html").dispatch_event("mouseleave")
    expect(page.locator(".modal")).to_be_visible()


# 🔴 28: FLOATING MENU - /floating_menu
# Verify menu visible, scroll down 1000px, verify menu still visible. Click Home, verify scrolled to top.
def test_28_floating_menu(page: Page):
    page.goto("https://the-internet.herokuapp.com/floating_menu")
    expect(page.get_by_role("heading", name="Floating Menu")).to_be_visible()
    page.mouse.wheel(0, 1000)
    expect(page.get_by_role("heading", name="Floating Menu")).to_be_visible()
    page.get_by_role("link", name="Home").click()
    page.evaluate("window.scrollTo(0, 0)")
    assert page.evaluate("window.scrollY") == 0


# =====================================================================
#                    SECTION 11: AUTHENTICATION
# =====================================================================


# 🔴 29: BASIC AUTH - /basic_auth
# Access with credentials in URL (admin:admin@...). Also try browser context http_credentials. Verify success.
def test_29_basic_auth(page: Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    expect(page.get_by_role("heading", name="Basic Auth")).to_be_visible()
    expect(
        page.get_by_text("Congratulations! You must have the proper credentials.")
    ).to_be_visible()


# 🔴 30: FORM AUTHENTICATION (Full Suite) - /login
# Test: wrong creds, correct user wrong pass, empty fields, correct login, access /secure without login, login+logout.
@pytest.mark.parametrize(
    "user, password, expected",
    [
        ("tomsmith", "WrongPassword", "Your password is invalid"),
        ("", "", "Your username is invalid"),
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area"),
    ],
)
def test_30a_login_scenarios(page: Page, user, password, expected):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="Username").fill(user)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_have_text(re.compile(expected))


def test_30b_secure_without_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login/secure")
    expect(page.get_by_role("heading")).to_have_text(re.compile("Not Found"))


def test_30c_login_logout(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_have_text(
        re.compile("You logged into a secure area!")
    )
    page.locator(".button.secondary.radius").click()
    expect(page.locator("#flash")).to_have_text(
        re.compile("You logged out of the secure area!")
    )
