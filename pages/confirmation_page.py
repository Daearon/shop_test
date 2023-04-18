import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ConfirmationPage(Base):
    """On this page need click on 3 button, choosing delivery form, destination point and payment form,
    next is creating screenshot, return to cart for delete product. Click on confirmation button goes to immediately create order"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    pickup_delivery_radio_button = "//input[..//span[contains(text(), 'Самовывоз')]]"
    destination_point_button = "//a[../..//div[contains(text(), 'Дзержинского')]]"
    payment_form_button = "//input[@value='cash']"
    order_confirmation_button = "//div[@class='info-group']/button[@type = 'submit' and @form='form-cart-order']"
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
        self.click_destination_point_button()
        self.click_payment_form_button()
        self.screenshot()
        self.click_cart()
