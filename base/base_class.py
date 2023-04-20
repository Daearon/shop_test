import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url - {get_url}")

    """Method assert word"""

    def assert_element_text(self, element, result):
        value_element = element.text
        assert value_element == result, "Wrong value element"
        print("Good value element")

    """Method screenshot"""

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(
            f".\\screen\\{name_screenshot}")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, "Wrong url"
        print("Good url")

"""class for shortening xpath"""
class XpathUtils:
    @classmethod
    def contains_class(cls, class_name):
        return f"contains(concat(' ', @class, ' '), ' {class_name} ')"

    @classmethod
    def contains_text(cls, text):
        return f"contains(text(), '{text}')"