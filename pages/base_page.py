from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def wait_short(self):
        return WebDriverWait(self.browser, 15)

