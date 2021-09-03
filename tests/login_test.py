import pytest
from LK.pages.login_page import LoginPage
import allure
from LK.tools.Json.ConfigTools import ConfigTools

@allure.epic('Негативные проверки входа')
class TestLogin():
    @allure.story('Проверка страницы авторизации с некорректным логином и паролем')
    def test_incorrectUserNameAndPassword(self, browser):
        login_page = LoginPage(browser)
        login_page\
            .user_name_input()\
            .password_input()\
            .invalidCredentials_isExist()\
            .submit_button()\
            .invalidCredentials_isNotExist()\
            .login_field_with_user()\
            .pass_field_without_password()

@allure.epic('Проверка с пустыми данными')
class TestLoginNegativ():
    @allure.story('Проверка URL страницы авторизации')
    def test_UserNameAndPassword(self, browser):
        login_page = LoginPage(browser)
        login_page\
            .submit_button()\
            .invalidCredentials_isNotExist()\
            .url_check_page()

@allure.epic('Логин: позитивные проверки')
class TestLoginPositive:
    logpass = [(ConfigTools.incorrect_login, ConfigTools.incorrect_password),
               (ConfigTools.correct_login, ConfigTools.correct_password)]

    @allure.story('Параметры: сначала неправильный логин/пароль, потом правильный')
    @pytest.mark.parametrize("login, password", logpass)
    def test_parametrized(self, browser, login, password):
        login_page = LoginPage(browser)
        login_page\
            .username_validate_input(login)\
            .password_validate_input(password)\
            .submit_button()\
            .avatar_button_click()\
            .username_check()\
            .email_check()

