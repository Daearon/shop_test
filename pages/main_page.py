from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    url = 'https://fkniga.ru/'

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    auth_button = "//a[@class ='btn btn--controlMain btn-auth']"

    # Getters

    def get_auth_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.auth_button)))

    # Actions

    def click_auth_button(self):
        self.get_auth_button().click()
        print("Click auth button")

    # Methods

    def transfer_to_auth(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_auth_button()
        self.assert_url("https://fkniga.ru/auth/")