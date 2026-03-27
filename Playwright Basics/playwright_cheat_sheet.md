# 🎭 Playwright & Pytest Cheat Sheet

Keep this file open! This contains the "Golden Commands" you'll need to master UI Automation.

## 🏆 The "Get By" Locators (Accessibility First)

| Element Type | HTML Example | Playwright Command |
| :--- | :--- | :--- |
| **Button** | `<button>Login</button>` | `page.get_by_role("button", name="Login")` |
| **Link** | `<a href="/home">Home</a>` | `page.get_by_role("link", name="More Info")` |
| **Heading** | `<h1>Welcome</h1>` | `page.get_by_role("heading", name="Welcome")` |
| **Input (Label)** | `<label>User</label><input>` | `page.get_by_label("Username")` |
| **Input (Placeholder)** | `<input placeholder="...">` | `page.get_by_placeholder("Enter your name")` |
| **Checkbox** | `<input type="checkbox">` | `page.get_by_role("checkbox")` |
| **Radio** | `<input type="radio">` | `page.get_by_role("radio")` |
| **Dropdown** | `<select><option>...</option></select>` | `page.get_by_role("combobox")` |
| **Image** | `<img alt="Logo">` | `page.get_by_role("img", name="Logo")` |
| **Raw Text** | `<div>Account Created</div>` | `page.get_by_text("Account Created")` |

---

## 🛠️ Execution & Debugging Commands

Run these directly in your VS Code terminal (Zsh).

| Goal | Command |
| :--- | :--- |
| **Run All Tests** | `pytest "Playwright Basics/test_practice_round6.py"` |
| **Run Multiple Browsers** | `pytest --browser chromium --browser firefox` |
| **Parallel Execution** | `pytest -n auto` (Requires `pip install pytest-xdist`) |
| **Slowdown Mode** | `pytest --slowmo 500` |
| **Headed Mode** | `pytest --headed` |
| **Trace Viewer (Record)**| `pytest --tracing on` (Produces `test-results/trace.zip`) |
| **Trace Viewer (Open)** | `playwright show-trace test-results/*/trace.zip` |
| **Launch Inspector** | `playwright codegen https://the-internet.herokuapp.com` |
| **Debug Mode** | `PWDEBUG=1 pytest -s -k "test_name"` |

---

## ⚡ Pro Tips for Mastering Assertions

- **Auto-Wait**: Always use `expect(locator).to_be_visible()` instead of `locator.is_visible()`.
- **Negative**: Use `.not_to_be_checked()` or `.not_to_be_visible()`.
- **Contains**: Use `.to_contain_text("substring")` if you don't want to match the whole string.
- **Attributes**: Use `expect(locator).to_have_attribute("href", "...")` for technical checks.
