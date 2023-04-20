from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.search_page import SearchPage
from utils.driver_instance import DriverInstance


def test_buy_product_1():
    """Create driver for browser correct work"""
    driver = DriverInstance.get_driver()
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
    DriverInstance.close_driver()

    print("Test 1 finish")