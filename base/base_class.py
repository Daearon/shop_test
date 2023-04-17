import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url - {get_url}")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, "Wrong value word"
        print("Good value word")

    """Method screenshot"""

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(
            'C:\\Users\\alexa\\OneDrive\\Desktop\\Selenium_final_project\\shop_test\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, "Wrong url"
        print("Good url")