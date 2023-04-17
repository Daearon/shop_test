import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ConfirmationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    pickup_delivery_radio_button = "//*[@id='form-cart-order']/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/label[1]/input"
    destination_point_button = "//*[@id='form-cart-order']/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]/a"
    payment_form_button = "//input[@value='cash']"
    order_confirmation_button = "//*[@id='form-cart-order']/div[1]/div[4]/div/div/div/div[4]/div[2]/div/button/span"
    cart = "//a[starts-with(@href, '/cart/')]"

    # Getters

    def get_pickup_delivery_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_delivery_radio_button)))

    def get_destination_point_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.destination_point_button)))

    def get_payment_form_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_form_button)))

    def get_order_confirmation_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_confirmation_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_pickup_delivery_radio_button(self):
        self.get_pickup_delivery_radio_button().click()
        print("Click pickup delivery radio button")

    def click_destination_point_button(self):
        self.get_destination_point_button().click()
        print("Click destination point button")

    def click_payment_form_button(self):
        self.get_payment_form_button().click()
        print("Click payment form button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")
    # Methods

    def confirmation_order(self):
        self.get_current_url()
        self.click_pickup_delivery_radio_button()
        time.sleep(3)
        self.click_destination_point_button()
        time.sleep(3)
        self.click_payment_form_button()
        time.sleep(3)
        self.screenshot()
        time.sleep(3)
        self.click_cart()
