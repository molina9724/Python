from playwright.sync_api import sync_playwright, expect
from pathlib import Path

# 🐺 WOLF SCRATCHPAD
# Use this file to test data extraction with Wolf live-evaluation!
# Because this is not a Pytest wrapper, Wolf will instantly run it top-to-bottom!

with sync_playwright() as p:
    # 1. Boot up a hidden browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/notification_message_rendered")

    messages = []
    for _ in range(10):
        page.get_by_role("link", name="Click here").click()
        message = page.locator("#flash").inner_text().strip()
        if message not in messages:
            messages.append(message)
    print(messages)
