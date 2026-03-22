# ======================================================================
# 🎭 PLAYWRIGHT EXERCISES - the-internet.herokuapp.com
# ======================================================================

from playwright.sync_api import Page, expect
from pathlib import Path
import re

BASE_URL = "https://the-internet.herokuapp.com"


# =====================================================================
#                    SECTION 1: CLICK ACTIONS
# =====================================================================


# 🟢 1: ADD/REMOVE ELEMENTS - /add_remove_elements/
# Click "Add Element" 5 times, verify 5 Delete buttons, remove 2, verify 3 remain, remove all.
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
def test_02_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="username").fill("tomsmith")
    page.get_by_role("textbox", name="password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page.locator("#flash")).to_contain_text("You logged into a secure area! ")
    page.locator("a.button[href='/logout']").click()
    expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")


# 🟢 3: CHECKBOXES - /checkboxes
# Verify initial states, check/uncheck both, verify states changed, toggle back to original.
def test_03_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # ⚠️ NOTE: We cannot use get_by_role("checkbox", name="checkbox 1") here!
    # The developer of this training site wrote terrible, inaccessible HTML.
    # The text "checkbox 1" is NOT wrapped in a <label> tag linked to the <input>,
    # so Playwright (and Screen Readers) see a raw checkbox with absolutely no name attached to it.
    # We are forced to use .first and .last to locate them instead!

    expect(page.get_by_role("checkbox").first).not_to_be_checked()
    expect(page.get_by_role("checkbox").last).to_be_checked()

    page.get_by_role("checkbox").first.check()
    expect(page.get_by_role("checkbox").first).to_be_checked()

    page.get_by_role("checkbox").last.uncheck()
    expect(page.get_by_role("checkbox").last).not_to_be_checked()


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
    pass


# =====================================================================
#                    SECTION 2: DROPDOWN & SELECT
# =====================================================================


# 🟢 6: DROPDOWN - /dropdown
# Select "Option 1" by label, verify, select "Option 2" by value, verify, get all options as list.
def test_06_dropdown(page: Page):
    pass


# =====================================================================
#                    SECTION 3: DYNAMIC CONTENT
# =====================================================================


# 🟡 7: DYNAMIC CONTROLS - /dynamic_controls
# Click Remove, wait for "It's gone!", verify checkbox gone. Click Add, wait for reappear.
# Click Enable, wait for input enabled, fill text. Click Disable, verify disabled.
def test_07_dynamic_controls(page: Page):
    pass


# 🟡 8: DYNAMIC LOADING (Hidden) - /dynamic_loading/1
# Click Start, wait for loading, verify "Hello World!" appears. Element exists but is hidden initially.
def test_08_dynamic_loading_1(page: Page):
    pass


# 🟡 9: DYNAMIC LOADING (Rendered) - /dynamic_loading/2
# Click Start, wait for loading, verify "Hello World!" appears. Element does NOT exist until loading completes.
def test_09_dynamic_loading_2(page: Page):
    pass


# 🟡 10: DYNAMIC CONTENT - /dynamic_content
# Capture text from 3 rows, refresh, verify content changed. Enable static content, refresh, verify it stays same.
def test_10_dynamic_content(page: Page):
    pass


# =====================================================================
#                    SECTION 4: FILE OPERATIONS
# =====================================================================


# 🟢 11: FILE UPLOAD - /upload
# Create a test file, use set_input_files(), click Upload, verify "File Uploaded!" and filename displayed.
def test_11_file_upload(page: Page):
    pass


# 🟡 12: FILE DOWNLOAD - /download
# Get list of downloadable files, click first file, wait for download, verify file was downloaded.
def test_12_file_download(page: Page):
    pass


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
    pass


# 🟡 15: MULTIPLE WINDOWS - /windows
# Click "Click Here", handle new tab, verify "New Window" text, close new tab, switch back.
def test_15_multiple_windows(page: Page):
    pass


# =====================================================================
#                    SECTION 6: HOVER & MOUSE ACTIONS
# =====================================================================


# 🟢 16: HOVERS - /hovers
# Hover over each user image, verify name appears, click "View profile", verify URL, go back. Repeat for all 3.
def test_16_hovers(page: Page):
    pass


# 🟡 17: DRAG AND DROP - /drag_and_drop
# Verify A is left B is right. Drag A to B, verify swap. Drag again to swap back.
def test_17_drag_drop(page: Page):
    pass


# 🟡 18: HORIZONTAL SLIDER - /horizontal_slider
# Get initial value, use ArrowRight/ArrowLeft to change, set to max (5), set to min (0).
def test_18_slider(page: Page):
    pass


# =====================================================================
#                    SECTION 7: KEYBOARD & INPUT
# =====================================================================


# 🟢 19: KEY PRESSES - /key_presses
# Click input, press keys (Enter, Escape, Tab, Backspace, Delete, Arrows, F1, Shift, Space) and verify result text.
def test_19_key_presses(page: Page):
    pass


# 🟡 20: INPUTS (Number Field) - /inputs
# Focus number input, fill a number, use ArrowUp/Down to increment/decrement, verify non-numeric ignored.
def test_20_inputs(page: Page):
    pass


# =====================================================================
#                    SECTION 8: JAVASCRIPT ALERTS
# =====================================================================


# 🟢 21: JS ALERTS - /javascript_alerts
# Handle JS Alert (accept), JS Confirm (accept then dismiss), JS Prompt (type text and accept). Verify results.
def test_21_alerts(page: Page):
    pass


# =====================================================================
#                    SECTION 9: TABLES
# =====================================================================


# 🟡 22: SORTABLE DATA TABLES - /tables
# Extract Table 1 data, sort by Last Name, verify sorted. Find row with "jsmith" email, click edit. Delete "Bach" row.
def test_22_tables(page: Page):
    pass


# =====================================================================
#                    SECTION 10: CHALLENGING SCENARIOS
# =====================================================================


# 🟡 23: CHALLENGING DOM - /challenging_dom
# Buttons have random IDs. Find blue/red/green buttons by class. Click each. Get table data, find cell at row 3 col 4.
def test_23_challenging_dom(page: Page):
    pass


# 🟡 24: NOTIFICATION MESSAGES - /notification_message_rendered
# Click "Click here" multiple times, capture notification messages, collect all unique messages.
def test_24_notifications(page: Page):
    pass


# 🔴 25: INFINITE SCROLL - /infinite_scroll
# Get initial paragraph count, scroll down, wait for new content, verify count increased, scroll until 20+ paragraphs.
def test_25_infinite_scroll(page: Page):
    pass


# 🔴 26: ENTRY AD (Popup Modal) - /entry_ad
# Modal auto-appears. Verify visible, get title/body, close it, re-enable it, refresh and verify it reappears.
def test_26_entry_ad(page: Page):
    pass


# 🔴 27: EXIT INTENT - /exit_intent
# Move mouse to top of viewport to trigger exit intent modal. Verify content, close, trigger again.
def test_27_exit_intent(page: Page):
    pass


# 🔴 28: FLOATING MENU - /floating_menu
# Verify menu visible, scroll down 1000px, verify menu still visible. Click Home, verify scrolled to top.
def test_28_floating_menu(page: Page):
    pass


# =====================================================================
#                    SECTION 11: AUTHENTICATION
# =====================================================================


# 🔴 29: BASIC AUTH - /basic_auth
# Access with credentials in URL (admin:admin@...). Also try browser context http_credentials. Verify success.
def test_29_basic_auth(page: Page):
    pass


# 🔴 30: FORM AUTHENTICATION (Full Suite) - /login
# Test: wrong creds, correct user wrong pass, empty fields, correct login, access /secure without login, login+logout.
def test_30_auth_test_suite(page: Page):
    pass
