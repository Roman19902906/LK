import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import allure


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

    @allure.story('Проверка с негативными данными')
    @allure.step('Проверка страницы авторизации с некорректным логином и паролем')
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
    @allure.story('Проверка авторизации без пароля')
    @allure.step('Проверка URL страницы авторизации')
    def test_UserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.test_submit_button()
        page.checking_invisible_message()
        page.checking_URL()


class TestLoginPositive:
    @allure.story('Позитивная проверка корректности авторизации')
    @allure.step('Проверка авторизации с корректным логином и паролем')
    def test_UserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.test_input_username_positive()
        page.test_input_password_positive()
        page.test_submit_button()
        page.test_avatar_button()
        page.test_checking_name_avatar()
        page.test_checking_email_avatar()


class TestCalendar:
    @allure.story('Проверки графиков работы пользователей')
    @allure.step('Проверка даты')
    def test_data1(self, auth):
        page = LoginPage(auth)
        page.test_cal_button()
        page.test_data_time()

    @allure.story('Проверки графиков работы пользователей')
    @allure.step('Проверка смены месяца')
    def test_month1(self, auth):
        page = LoginPage(auth)
        page.test_cal_button()
        page.test_another_month()

    @allure.story('Проверки графиков работы пользователей')
    @allure.step('Проверка смены пользователя')
    def test_user1(self, auth):
        page = LoginPage(auth)
        page.test_cal_button()
        page.test_another_user()
