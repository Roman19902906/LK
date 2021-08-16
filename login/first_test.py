import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import time


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
        time.sleep(5)


class TestCalendar:
    def test_data1(self, auth):
        page = LoginPage(auth)
        page.test_cal_button()
        page.test_data_time()

    def test_month1(self, auth):
        page = LoginPage(auth)
        page.test_cal_button()
        page.test_another_month()

    def test_user1(self, auth):
        page = LoginPage(auth)
        page.test_cal_button()
        page.test_another_user()
