# Guru99 Login Test Suite (Pytest + POM)

## Structure
```
.
├── pages/
│   ├── locators.py          # All selectors in one place
│   ├── guru99_login_page.py   # Page Object for login flow
├── test_guru99_login.py        # Main test case using the POM
├── screenshots/               # Auto-created folder for failure screenshots
└── README.md
```

## How to Run
Install dependencies:
```bash
pip install selenium faker pytest
```

Run tests:
```bash
pytest test_guru99_login.py
```

Run tests with browser:

```bash
pytest test_guru99_login.py --browser=chrome
```

Run tests with headless mode:

```bash
pytest test_guru99_login.py --browser=chrome --headless
```


## Features
- Uses Page Object Model
- Stores all locators in a central place
- Uses `WebDriverWait` instead of sleep
- Captures screenshots if the test fails
- Ready to plug into GitHub Actions for CI

---