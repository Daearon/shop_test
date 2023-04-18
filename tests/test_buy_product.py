from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.search_page import SearchPage


def test_buy_product_1():
    """Create driver for browser correct work"""
    clear_terminal = Options()
    clear_terminal.add_experimental_option('excludeSwitches', ['enable logging'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service("C:\\Users\\alexa\\OneDrive\\Desktop\\Selenium\\resourse\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g, chrome_options=clear_terminal)
    driver.maximize_window()
    print("Test 1 start")
    """Use methods from each page unit"""
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

    print("Test 1 finish")