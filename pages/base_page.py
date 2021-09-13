from datetime import datetime as dt
from selenium.webdriver.support.wait import WebDriverWait
from LK.tools.Json.ConfigTools import ConfigTools
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def wait_short(self):
        return WebDriverWait(self.browser, 15)

    def validate_url(self):
        """Проверка url"""
        assert self.browser.current_url == '/'.join(ConfigTools.project_url(), "login"), "URL адрес не совпадает"

    @staticmethod
    def normalize(offset_month:int = 0, offset_year:int = 0):
        """Нормализует месяцы и года с учётом смещения"""
        current_year = dt.now().year + offset_year
        current_month = dt.now().month + offset_month
        while current_month > 12:
            current_month -= 12
            current_year += 1
        while current_month < 0:
            current_month += 12
            current_year -= 1
        return current_month, current_year