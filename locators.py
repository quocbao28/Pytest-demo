from selenium.webdriver.common.by import By

REGISTER_LOCATORS = {
"email_input": (By.CSS_SELECTOR, "input[name='emailid']"),
    "submit_button": (By.CSS_SELECTOR, "input[name=btnLogin]"),
    "user_id_text": (By.XPATH, "//td[text()='User ID :']/following-sibling::td"),
    "password_text": (By.XPATH, "//td[text()='Password :']/following-sibling::td"),
}

LOGIN_LOCATORS = {
    "uid_input": (By.CSS_SELECTOR, "input[name=uid]"),
    "password_input": (By.CSS_SELECTOR, "input[name=password]"),
    "login_button": (By.CSS_SELECTOR, "input[name=btnLogin]"),
}