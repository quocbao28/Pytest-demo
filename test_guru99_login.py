import pytest
from faker import Faker
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pages.guru99_login_page import Guru99LoginPage

SCREENSHOT_DIR = "screenshots"

def take_screenshot(driver, test_name):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    path = os.path.join(SCREENSHOT_DIR, f"{test_name}.png")
    driver.save_screenshot(path)
    print(f"[INFO] Screenshot saved to: {path}")

def test_register_and_login(driver, request):
    fake = Faker()
    page = Guru99LoginPage(driver)

    try:
        page.go_to_register_page()
        email = fake.email()
        user_id, password = page.register_user(email)
        page.go_to_login_page()
        page.login(user_id, password)

        assert "GTPL Bank" in driver.page_source

    except Exception:
        take_screenshot(driver, request.node.name)
        raise