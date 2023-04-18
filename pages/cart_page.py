import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):
    """Product in cart; methods in this class confirm product for order and delete product in end of test"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    continue_button = "//div[@class='cartBox__buttons']/a[@href = '/cart/order/']"
    cart_word = "//h1[@class ='main__title title title--48']"
    bin = "//div[@class='card__controls']//a[.//*[name()='svg' and @class='icon icon-remove']]"

    # Getters

    def get_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_bin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bin)))

    # Actions

    def click_continue_button(self):
        self.get_continue().click()
        print("Click continue button")

    def click_bin_button(self):
        self.get_bin().click()
        print("Click bin button")

    # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.assert_element_text(self.get_cart_word(), "Корзина")
        self.click_continue_button()
        time.sleep(6)  # next page is heavy, need sleep for correct work

    """Delete product from cart"""

    def product_delete(self):
        self.click_bin_button()
