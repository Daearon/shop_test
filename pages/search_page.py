import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class SearchPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    hardcover_radio_button = "//div[@data-ga-label='Твердый переплет']"
    native_book_radio_button = "//div[@data-ga-label='Отечественная книга']"
    author_radio_button = "//div[@data-ga-label='Пехов А.Ю.']"
    product = "/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div[2]/a[2]"
    accept_button = "//*[@id='filterBox']/div/div[2]/div/div[16]/div/button[1]"
    cart = "/html/body/div[3]/header/div[2]/div[5]/div[4]/ul/li[5]/a/span[2]"

    # Getters

    def get_hardcover_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hardcover_radio_button)))

    def get_native_book_radio_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.native_book_radio_button)))

    def get_author_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.author_radio_button)))

    def get_accept_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_button)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_hardcover_radio_button(self):
        self.get_hardcover_radio_button().click()
        print("Click hardcover radio button")

    def click_native_book_radio_button(self):
        self.get_native_book_radio_button().click()
        print("Click native book radio button")

    def click_author_radio_button(self):
        self.get_author_radio_button().click()
        print("Click author radio button")

    def click_accept_button(self):
        self.get_accept_button().click()
        print("Click accept button")

    def click_product(self):
        self.get_product().click()
        print("Click product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def search_product(self):
        self.get_current_url()
        self.click_hardcover_radio_button()
        time.sleep(3)
        self.click_native_book_radio_button()
        time.sleep(3)
        self.click_author_radio_button()
        time.sleep(3)
        self.click_accept_button()
        time.sleep(10)
        self.click_product()
        time.sleep(5)
        self.click_cart()
