from playwright.sync_api import sync_playwright
from pathlib import Path

# 🐺 WOLF SCRATCHPAD
# Use this file to test data extraction with Wolf live-evaluation!
# Because this is not a Pytest wrapper, Wolf will instantly run it top-to-bottom!

with sync_playwright() as p:
    # 1. Boot up a hidden browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 2. Go to the URL
    page.goto("https://the-internet.herokuapp.com/upload")

    file = Path(
        "/Users/daniel_molina/Downloads/Python/Python/Playwright Basics/wolf_scratchpad.py"
    )
    print(file.name)
    print(type(file.name))
    text = page.locator("#uploaded-files").all_inner_texts()
    print(text)

    browser.close()
