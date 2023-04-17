import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    continue_button = "//a[@class ='btn btn--primary btn--fullWidth btn-next-loading cartBox__button-dekstop']"
    cart_word = "//h1[@class ='main__title title title--48']"
    bin = "/html/body/div[3]/div/div[2]/div/div/div[1]/form/div[2]/div/div/div[4]/a[2]"

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
        self.assert_word(self.get_cart_word(), "Корзина")
        self.click_continue_button()
        time.sleep(6)

    def product_delete(self):
        self.click_bin_button()