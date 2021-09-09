from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from LK.tools.Json.ConfigTools import ConfigTools
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def wait_short(self):
        return WebDriverWait(self.browser, 15)

    def is_element_present(self, element):
        """Проверка наличия элемента"""
        try:
            element
        except NoSuchElementException:
            return False
        return True

    def element_is_not_present(self, element):
        """Проверка отсутсвия элемента"""
        try:
            element
        except NoSuchElementException:
            return True
        return False

    def validate_url(self):
        """Проверка url"""
        assert ConfigTools.login_url() == self.browser.current_url, "URL адрес не совпадает"
