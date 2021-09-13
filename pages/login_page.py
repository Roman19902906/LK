from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from LK.tools.Json.ConfigTools import ConfigTools


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        # Поле ввода логина
        self.user_name = lambda: self.browser.find_element_by_css_selector(
            "[name=_username]")
        # Поле ввода пароля
        self.password = lambda: self.browser.find_element_by_css_selector("#password")
        # Кнопка войти
        self.button = lambda: self.browser.find_element(By.NAME, "_submit")
        # Сообщение Invalid credentials.
        self.invalid_text = lambda: self.browser.find_element(By.CSS_SELECTOR, ".m-login__signin > div:nth-child(1)")
        # Кнопка аватара
        self.avatar = lambda: self.browser.find_element_by_css_selector(".avatarCover")
        # Проверка логина в кнопке аватара
        self.avatar_login = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[1]")
        # Проверка email в кнопке аватара
        self.avatare_mail = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[2]")

    # Сообщение об ошибке
    error_message = ConfigTools.login_error()

    @allure.step('Ввод логина')
    def user_name_input(self):
        self.user_name().send_keys(ConfigTools.incorrect_login())
        return self

    @allure.step('Ввод пароля')
    def password_input(self):
        self.password().send_keys(ConfigTools.incorrect_password())
        return self

    @allure.step('Нажать кнопку авторизации')
    def submit_button(self):
        self.button().click()
        return self

    @allure.step('Проверка URL страницы авторизации')
    def url_check_page(self):
        self.validate_url()
        return self

    @allure.step('Считаю наличие текста "Invalid Credentials" на странице авторизации успехом')
    def invalidCredentials_isExist(self):
        self.is_element_present(self.invalid_text)
        return self

    @allure.step('Считаю отсутствие текста "Invalid Credentials" на странице авторизации успехом')
    def invalidCredentials_isNotExist(self):
        self.element_is_not_present(self.invalid_text)
        return self

    @allure.step('После неудачной авторизации в поле логина присутствует имя пользователя')
    def invalid_user_login_is_present_and_correct(self):
        assert self.user_name().get_attribute('value') == ConfigTools.incorrect_login()
        assert self.password().get_attribute("value") == ""
        return self

    @allure.step('Ввод логина сотрудника сотрудника')
    def username_validate_input(self, login):
        self.user_name().send_keys(f"{login}")
        return self

    @allure.step('Ввод пароля сотрудника сотрудника')
    def password_validate_input(self, password):
        self.password().send_keys(f"{password}")
        return self

    @allure.step('Клик по кнопке аватара сотрудника')
    def avatar_button_click(self):
        self.avatar().click()
        return self

    @allure.step("Проверка что авторизован верный пользователь")
    def validate_login_user(self):
        assert self.avatar_login().text == ConfigTools.correct_login()
        assert self.avatare_mail().text == ConfigTools.email()
        return self
