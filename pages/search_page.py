import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from base.base_class import XpathUtils as XU


class SearchPage(Base):
    """Click on 3 filters, choosing book and send into cart, transfer to cart"""

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    hardcover_radio_button = "//div[@data-ga-label='Твердый переплет']"
    native_book_radio_button = "//div[@data-ga-label='Отечественная книга']"
    author_radio_button = "//div[@data-ga-label='Пехов А.Ю.']"
    product = f"//div[{XU.contains_class('card')} and .//a[{XU.contains_text('Кровные братья')}]]//a[contains(@id, 'js-add-to-cart')]"
    accept_button = "//*[@id='filterBox']/div//button[1]"
    cart = "//a[starts-with(@href, '/cart/')]"

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

    def get_product_to_cart_button(self):
        WebDriverWait(self.driver, 30).until(EC.url_contains("filter"))
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

    def click_product_to_cart_button(self):
        self.get_product_to_cart_button().click()
        print("Click product to cart button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def search_product(self):
        self.get_current_url()
        self.click_hardcover_radio_button()
        self.click_native_book_radio_button()
        self.click_author_radio_button()
        self.click_accept_button()
        time.sleep(2) # need short sleep for correct work of filters and buying product
        self.click_product_to_cart_button()
        self.click_cart()
