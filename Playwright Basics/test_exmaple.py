import re
from playwright.sync_api import expect, Page
from playwright.sync_api import sync_playwright


def test_has_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title(re.compile("The Internet", re.IGNORECASE))
    test = page.get_by_role("link", name="Checkboxes")
    print(test)


playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=True, slow_mo=50)
page = browser.new_page()
page.goto("https://the-internet.herokuapp.com/")
expect(page).to_have_title(re.compile("The Internet", re.IGNORECASE))
test = page.get_by_role("link", name="Checkboxes")
print(test.is_visible())
