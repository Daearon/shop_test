from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class DriverInstance:
    driver: [WebDriver, None] = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls.driver is None:
            cls.driver = cls.create_chrome_driver()
        return cls.driver

    @staticmethod
    def create_chrome_driver() -> WebDriver:
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable logging'])
        g = Service("C:\\Users\\alexa\\OneDrive\\Desktop\\Selenium\\resourse\\chromedriver.exe")
        d = webdriver.Chrome(options=options, service=g)
        d.maximize_window()
        return d

    @classmethod
    def close_driver(cls):
        if cls.driver is not None:
            cls.driver.close()
            cls.driver = None
