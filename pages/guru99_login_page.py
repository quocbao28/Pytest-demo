# Page Object for Guru99 site
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTER_LOCATORS, LOGIN_LOCATORS

class Guru99LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def go_to_register_page(self):
        self.driver.get("https://demo.guru99.com")
        self.wait.until(EC.presence_of_element_located(REGISTER_LOCATORS["email_input"]))

    def register_user(self, email):
        self.wait.until(EC.presence_of_element_located(REGISTER_LOCATORS["email_input"])).send_keys(email)
        self.driver.find_element(*REGISTER_LOCATORS["submit_button"]).click()
        user_id = self.wait.until(EC.presence_of_element_located(REGISTER_LOCATORS["user_id_text"])).text
        password = self.driver.find_element(*REGISTER_LOCATORS["password_text"]).text
        return user_id, password

    def go_to_login_page(self):
        self.driver.get("https://demo.guru99.com/V1/index.php")

    def login(self, user_id, password):
        self.wait.until(EC.presence_of_element_located(LOGIN_LOCATORS["uid_input"])).send_keys(user_id)
        self.driver.find_element(*LOGIN_LOCATORS["password_input"]).send_keys(password)
        self.driver.find_element(*LOGIN_LOCATORS["login_button"]).click()