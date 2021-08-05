import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


class TestFirst():
    def test_1(start_fun):
        print('Тест №1')
        pytest.assume(2 + 2 == 4)

    def test_2(start_fun):
        print('Тест №2')
        pytest.assume(2 + 2 == 5)

    def test_3(start_fun):
        print('Тест №3')
        pytest.assume(2 + 2 == 4)

    def test_4(start_fun):
        print('Тест №3')
        pytest.assume(1 / 0 == 1)

    def test_5(start_fun):
        print('Тест №5')

class TestLogin:
    def test_initWebDriver(self):
        browser = webdriver.Chrome()
        browser.get("https://tt-develop.quality-lab.ru")
        options = Options()
        options.add_argument("--window-size=500x500")
        browser.set_window_size(200, 100)
        browser.maximize_window()
        browser.quit()

    def test_incorrectUserNameAndPassword(self, browser):
        input1 = browser.find_element_by_css_selector("#username")
        input1.send_keys("TestUser")
        input2 = browser.find_element_by_css_selector("#password")
        input2.send_keys("Password")
        TEXT = lambda: browser.find_element_by_xpath(".//div[text() = 'Invalid credentials.']")
        try:
            pytest.assume(TEXT != 'Invalid credentials.')
        except NoSuchElementException:
            return False
        return True

        button = browser.find_element_by_name("_submit")
        button.click()
        pytest.assume(TEXT == 'Invalid credentials.')

