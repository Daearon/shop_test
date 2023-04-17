from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    login = "//input[@name='phone_or_email']"
    password = "//input[@name='password']"
    login_button = "//button[@class ='btn btn--primary btn--height60 btn--fullWidth']"
    personal_account_word = "//h1[@class ='main__title title title--48']"

    # Getters

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_personal_account_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_account_word)))

    # Actions

    def input_login(self, user_name):
        self.get_login().send_keys(user_name)
        print("Input login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    #Methods

    def authorization(self):
        self.get_current_url()
        self.input_login("alexandr8769@mail.ru")
        self.input_password("invinoveritas")
        self.click_login_button()
        self.assert_word(self.get_personal_account_word(), "Личный кабинет")