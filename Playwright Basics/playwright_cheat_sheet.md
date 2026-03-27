# Playwright & Pytest Cheat Sheet

> Keep this file open! Your go-to reference for UI automation with Playwright + pytest.

---

## Table of Contents

1. ["Get By" Locators](#-get-by-locators-accessibility-first)
2. [Execution & Debugging Commands](#-execution--debugging-commands)
3. [What is `yield`?](#-what-is-yield-in-python)
4. [HTML Test Reports](#-html-test-reports-pytest-html)
5. [Assertion Pro Tips](#-pro-tips-for-assertions)
6. [Visual Regression Testing](#-visual-regression-testing)

---

## 1. "Get By" Locators (Accessibility First)

These are the preferred, resilient ways to find elements on a page.

| Element Type       | HTML Example                          | Playwright Command                              |
| :----------------- | :------------------------------------ | :---------------------------------------------- |
| **Button**         | `<button>Login</button>`              | `page.get_by_role("button", name="Login")`      |
| **Link**           | `<a href="/home">Home</a>`           | `page.get_by_role("link", name="More Info")`    |
| **Heading**        | `<h1>Welcome</h1>`                   | `page.get_by_role("heading", name="Welcome")`   |
| **Input (Label)**  | `<label>User</label><input>`         | `page.get_by_label("Username")`                 |
| **Input (Placeholder)** | `<input placeholder="...">`     | `page.get_by_placeholder("Enter your name")`    |
| **Checkbox**       | `<input type="checkbox">`            | `page.get_by_role("checkbox")`                  |
| **Radio**          | `<input type="radio">`               | `page.get_by_role("radio")`                     |
| **Dropdown**       | `<select><option>...</option></select>` | `page.get_by_role("combobox")`               |
| **Image**          | `<img alt="Logo">`                   | `page.get_by_role("img", name="Logo")`          |
| **Raw Text**       | `<div>Account Created</div>`         | `page.get_by_text("Account Created")`           |

---

## 2. Execution & Debugging Commands

Run these directly in your VS Code terminal (Zsh).

| Goal                       | Command                                                        |
| :------------------------- | :------------------------------------------------------------- |
| **Run all tests**          | `pytest "Playwright Basics/test_practice_round6.py"`           |
| **Run multiple browsers**  | `pytest --browser chromium --browser firefox`                  |
| **Parallel execution**     | `pytest -n auto` (requires `pip install pytest-xdist`)         |
| **Slowdown mode**          | `pytest --slowmo 500`                                          |
| **Headed mode**            | `pytest --headed`                                              |
| **Trace viewer (record)**  | `pytest --tracing on` (produces `test-results/trace.zip`)      |
| **Trace viewer (open)**    | `playwright show-trace test-results/*/trace.zip`               |
| **Launch inspector**       | `playwright codegen https://the-internet.herokuapp.com`        |
| **Debug mode**             | `PWDEBUG=1 pytest -s -k "test_name"`                          |

---

## 3. What is `yield` in Python?

`yield` lets a function **pause**, return a value, and **resume** later. Two main uses:

### Generators

Functions that return values one at a time:

```python
def count_up():
    yield 1
    yield 2
    yield 3

for number in count_up():
    print(number)  # 1, 2, 3
```

### Pytest Fixtures (Setup / Teardown)

Code before `yield` runs as **setup**; code after runs as **teardown**:

```python
@pytest.fixture
def setup_teardown():
    print("Setup!")
    yield
    print("Cleanup!")
```

> **TL;DR** — `yield` = pause, pass out a value, resume later. Perfect for setup/cleanup patterns in testing.

---

## 4. HTML Test Reports (pytest-html)

Generate a shareable HTML report from your test runs.

**Install:**

```bash
pip install pytest-html
```

**Run:**

```bash
pytest --html=report.html
```

- Creates `report.html` in the current directory.
- Open in your browser to see pass/fail summary, failure logs, and test durations.
- Customize the file name/location or combine with other plugins as needed.

---

## 5. Pro Tips for Assertions

| Technique         | Example                                                  | Why                                       |
| :---------------- | :------------------------------------------------------- | :---------------------------------------- |
| **Auto-wait**     | `expect(locator).to_be_visible()`                        | Waits automatically; don't use `.is_visible()` |
| **Negative**      | `.not_to_be_checked()` / `.not_to_be_visible()`         | Assert something is NOT in a given state  |
| **Contains**      | `.to_contain_text("substring")`                          | Partial text match instead of exact       |
| **Attributes**    | `expect(locator).to_have_attribute("href", "...")`       | Check technical HTML attributes           |

---

## 6. Visual Regression Testing

Uses [pytest-playwright-visual](https://pypi.org/project/pytest-playwright-visual/) for image-diff testing.

### Example Test

```python
def test_visual_homepage_the_internet(page, assert_snapshot):
    page.goto("https://the-internet.herokuapp.com/")
    assert_snapshot(page.screenshot(), name="the-internet-home.png")
```

- Always use `page.screenshot()` (returns PNG bytes).
- The `name` should be descriptive and end with `.png`.

### Workflow

**Step 1 — Create or update the baseline (first run):**

```bash
pytest "Playwright Basics/test_practice_round6.py" \
  -k "test_visual_homepage_the_internet" -v --update-snapshots
```

> This will intentionally fail with: `Snapshots updated. Please review images`

**Step 2 — Run the regression check:**

```bash
pytest "Playwright Basics/test_practice_round6.py" \
  -k "test_visual_homepage_the_internet" -v
```

> Passes if the screenshot matches the baseline within default tolerance.

### Troubleshooting

- **Only use static pages** — dynamic content causes false failures every time.
- **Review diffs** — check `Playwright Basics/snapshot_tests_failures/` for actual, expected, and diff PNGs.
- **Raise threshold** for minor acceptable fuzziness:

  ```python
  assert_snapshot(page.screenshot(), name="the-internet-home.png", threshold=0.2)
  ```
