import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


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
        page = LoginPage(browser)
        page.test_input_username()
        page.test_input_password()
        page.checking_invisible_message()
        page.test_submit_button()
        page.checking_the_message()
        page.checking_user()
        page.checking_password()

class TestLoginNegativ():
    def test_UserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.test_submit_button()
        page.checking_invisible_message()
        page.checking_URL()


class TestLoginPositive:
    def test_UserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.test_input_username_positive()
        page.test_input_password_positive()
        page.test_submit_button()
        page.test_avatar_button()
        page.test_checking_name_avatar()
        page.test_checking_email_avatar()



