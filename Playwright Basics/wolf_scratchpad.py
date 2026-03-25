from playwright.sync_api import sync_playwright, expect
from pathlib import Path

# 🐺 WOLF SCRATCHPAD
# Use this file to test data extraction with Wolf live-evaluation!
# Because this is not a Pytest wrapper, Wolf will instantly run it top-to-bottom!

with sync_playwright() as p:
    # 1. Boot up a hidden browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

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

    print((last_names.sort()))

    print((filtered_last_names))

    for row in rows:
        print(row.inner_text())

    # assert last_names.sort() == filtered_last_names
