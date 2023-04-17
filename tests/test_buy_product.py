import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.search_page import SearchPage


def test_buy_product_1():
    clear_terminal = Options()
    clear_terminal.add_experimental_option('excludeSwitches', ['enable logging'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service("C:\\Users\\alexa\\OneDrive\\Desktop\\Selenium\\resourse\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g, chrome_options=clear_terminal)
    print("Test 1 start")

    mp = MainPage(driver)
    mp.transfer_to_auth()
    lp = LoginPage(driver)
    lp.authorization()
    pap = PersonalAccountPage(driver)
    pap.input_search_text()
    sp = SearchPage(driver)
    sp.search_product()
    cp = CartPage(driver)
    cp.product_confirmation()
    confp = ConfirmationPage(driver)
    confp.confirmation_order()
    cp.product_delete()




    # login = LoginPage(driver)
    # login.authorization()
    # mp = MainPage(driver)
    # mp.selecting_product()
    # cp = CartPage(driver)
    # cp.product_confirmation()
    # up = UserPage(driver)
    # up.user_information_confirmation()
    # pp = PaymentPage(driver)
    # pp.finish_buy_product()
    # fp = FinishPage(driver)
    # fp.finish()
    # print("Test finish")