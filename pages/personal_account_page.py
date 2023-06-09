from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PersonalAccountPage(Base):
    """On this page creating search request with author's name in search field"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    search_field = "//input[@name='q']"
    search_button = "//button[@class='btn btn--search']"

    # Getters

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    # Actions

    def input_search(self, search_text):
        self.get_search_field().send_keys(search_text)
        print("Input text in search field")

    def click_search_button(self):
        self.get_search_button().click()
        print("Click search button")

    #Methods

    def input_search_text(self):
        self.get_current_url()
        self.input_search("Пехов")
        self.click_search_button()
        self.assert_url("https://fkniga.ru/search/?q=%D0%9F%D0%B5%D1%85%D0%BE%D0%B2")