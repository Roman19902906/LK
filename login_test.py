import pytest
from pages.login_page import LoginPage
import allure


@allure.epic('Негативные проверки входа')
class TestLogin():
    @allure.story('Проверка страницы авторизации с некорректным логином и паролем')
    def test_incorrectUserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.input_username()
        page.input_password()
        page.checking_invisible_message()
        page.submit_button()
        page.checking_the_message()
        page.checking_user()
        page.checking_password()

@allure.epic('Проверка с пустыми данными')
class TestLoginNegativ():
    @allure.story('Проверка URL страницы авторизации')
    def test_UserNameAndPassword(self, browser):
        page = LoginPage(browser)
        page.submit_button()
        page.checking_invisible_message()
        page.checking_URL()

@allure.epic('Логин: позитивные проверки')
class TestLoginPositive:
    @allure.story('Проверка авторизации с корректным логином и паролем')
    @pytest.mark.parametrize('log, password, url1',
                             [("Тест", "Тест", "https://tt-develop.quality-lab.ru/report/stats/project"), ("Авто Пользователь", "12345678", "https://tt-develop.quality-lab.ru/report/group/edit")])
    def test_UserNameAndPassword(self, browser, log, password, url1):
        page = LoginPage(browser)
        page.input_username_positive(log)
        page.input_password_positive(password)
        page.submit_button()
        page.checking_URL_positive(url1)
        page.avatar_button()
        page.checking_name_avatar()
        page.checking_email_avatar()

