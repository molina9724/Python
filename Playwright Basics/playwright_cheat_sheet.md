
---

## 9. Unittest in Python: Naming, Discovery & CLI Usage

### Key Unittest Rules for Test Discovery  
To ensure your tests are auto-discoverable and runnable using built-in tools (`python -m unittest`):

**File naming:**
- Test files must be named `test*.py` (e.g., `test_math.py`, `test_login.py`)

**Class naming:**
- Classes must inherit from `unittest.TestCase`
- Class names can be anything, but convention is: `TestXxx` (e.g., `TestMath`)

**Method naming:**
- Test methods must start with `test_`

**Example Layout:**

```python
# test_example_unittest.py
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)
    def test_subtract(self):
        self.assertEqual(5 - 3, 2)
```

### How to Run Unittest Tests

From your project root, run:

- Run all discoverable test files:
  ```bash
  python -m unittest discover
  ```
- Run a specific file:
  ```bash
  python -m unittest Playwright\ Basics.test_example_unittest
  # Or (if in this dir):
  python -m unittest test_example_unittest
  ```
- Run a single test case in a file:
  ```bash
  python -m unittest Playwright\ Basics.test_example_unittest.TestMath
  ```
- Run a single test method:
  ```bash
  python -m unittest Playwright\ Basics.test_example_unittest.TestMath.test_add
  ```
*Note: Use dot notation - periods between package(dir), file (drop .py), class, and method.*

### Troubleshooting Discovery
- Test file isn’t found? Check for `test` prefix in filename AND it’s in the right folder.
- Class/method not found? Confirm you spelled `Test` and `test_` correctly and subclassed `unittest.TestCase`.
- Don’t use pytest-only features (like fixtures) in unittest files—they won’t work.

### Mixing Unittest and Pytest in One Repo
- Possible, safe, and sometimes useful! Pytest will automatically discover and run unittest-based test cases as well.
- Keep different frameworks in separate files for clarity (e.g., `test_xx_pytest.py` and `test_xx_unittest.py`).
- Use Pytest’s CLI for everything if you want features like plugins, but you can fall back on plain unittest CLI for legacy tests.

**Project Structure Example:**

```
Playwright Basics/
├─ test_pytest_feature.py         # Pytest-style
├─ test_example_unittest.py       # Unittest-style
├─ ...                           # Your other test files
```

> Quick rule: If `python -m unittest discover` finds and runs it, so will Pytest. But not vice versa.

### Unittest “Gotchas”
- Unittest doesn’t pick up tests in files not starting with `test` by default!
- No fixtures like pytest. Use `setUp`/`tearDown` methods for prep and cleanup.
- Output is less rich than pytest’s; consider running under pytest for better reports if mixing.

---
