import pytest
from pages.login_page import LoginPage
from pages.calendar_page import CalendarPage
import allure


@allure.epic('Негативные проверки входа')
class TestLogin():
    @allure.story('Проверка страницы авторизации с некорректным логином и паролем')
    def test_incorrectUserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.test_input_username()
        page.test_input_password()
        page.checking_invisible_message()
        page.test_submit_button()
        page.checking_the_message()
        page.checking_user()
        page.checking_password()

@allure.epic('Проверка с пустыми данными')
class TestLoginNegativ():
    @allure.story('Проверка URL страницы авторизации')
    def test_UserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.test_submit_button()
        page.checking_invisible_message()
        page.checking_URL()

@allure.epic('Логин: позитивные проверки')
class TestLoginPositive:
    @allure.story('Проверка авторизации с корректным логином и паролем')
    @pytest.mark.parametrize('log, password, url1',
                             [("Тест", "Тест", "https://tt-develop.quality-lab.ru/report/stats/project"), ("Авто Пользователь", "12345678", "https://tt-develop.quality-lab.ru/report/group/edit")])
    def test_UserNameAndPassword(self, browser, log, password, url1):
        page = LoginPage(browser)
        page.test_input_username_positive(log)
        page.test_input_password_positive(password)
        page.test_submit_button()
        page.checking_URL_positive(url1)
        page.test_avatar_button()
        page.test_checking_name_avatar()
        page.test_checking_email_avatar()

