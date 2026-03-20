from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=True, slow_mo=50)
page = browser.new_page()
page.goto("https://autbor.com/example3.html")
page.click("input[type=checkbox]")
page.click("input[type=checkbox]")
print(page.is_visible("#login_user"))
page.locator("#login_user").fill("A")
page.locator("#login_pass").fill("B")
page.click("input[type=submit]")
checkbox_elem = page.get_by_role("checkbox")
checkbox_elem.check()
checkbox_elem.uncheck()

browser.close()
playwright.stop()
