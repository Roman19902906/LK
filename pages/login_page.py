import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
import allure
from LK.tools.Json.Json import Json

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        # Поле ввода логина
        self.username = lambda: self.browser.find_element(By.CSS_SELECTOR, "#username")
        # Поле ввода пароля
        self.password = lambda: self.browser.find_element(By.CSS_SELECTOR, "#password")
        # Кнопка войти
        self.button = lambda: self.browser.find_element(By.NAME, "_submit")
        # Сообщение Invalid credentials.
        self.invalid = lambda: self.browser.find_element(By.CSS_SELECTOR, ".m-login__signin > div:nth-child(1)")
        # Кнопка аватара
        self.avatar = lambda: self.browser.find_element_by_css_selector(".avatarCover")
        # Проверка логина в кнопке аватара
        self.avatarlogin = lambda: self.browser.find_element_by_xpath(
                ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[1]")
        # Проверка email в кнопке аватара
        self.avataremail = lambda: self.browser.find_element_by_xpath(
                ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[2]")

    @allure.step('Ввод логина TestUser')
    def input_username(self):
        self.username().send_keys(Json.data['auth']['incorrect']['login'])

    @allure.step('Ввод пароля Password')
    def input_password(self):
        self.password().send_keys(Json.data['auth']['incorrect']['password'])

    @allure.step('Авторизация')
    def submit_button(self):
        self.button().click()

    @allure.step('Проверка сообщения Invalid credentials.')
    def checking_the_message(self):
        pytest.assume(self.invalid().text == 'Invalid credentials.')

    @allure.step('Проверка непоявившегося сообщения Invalid credentials.')
    def checking_invisible_message(self):
        try:
            pytest.assume(self.invalid() != 'Invalid credentials.')
        except NoSuchElementException:
            return False
        return True

    @allure.step('Проверка логина TestUser')
    def checking_user(self):
        attrloguser = self.username().get_attribute("value")
        pytest.assume(attrloguser == 'TestUser')

    @allure.step('Проверка пустой строчки пароля')
    def checking_password(self):
        attributemptypass = self.password().get_attribute("placeholder")
        pytest.assume(attributemptypass == 'Пароль')

    @allure.step('Проверка URL страницы логина')
    def checking_URL(self):
        url = self.browser.current_url
        pytest.assume(url == 'https://tt-develop.quality-lab.ru/login')

    @allure.step('Ввод логина сотрудника сотрудника: Авто Пользователь')
    def input_username_positive(self, log):
        self.username().send_keys(f"{log}")

    @allure.step('Ввод пароля сотрудника сотрудника: 12345678')
    def input_password_positive(self, password):
        self.password().send_keys(f"{password}")

    @allure.step('Проверка URL страницы логина')
    def checking_URL_positive(self, url1):
        url = self.browser.current_url
        pytest.assume(url == f"{url1}"), "Страница не совпадает"

    @allure.step('Клик по кнопке аватара сотрудника')
    def avatar_button(self):
        self.avatar().click()

    @allure.step('Проверка логина сотрудника')
    def checking_name_avatar(self):
        pytest.assume(self.avatarlogin().text == "Авто Пользователь"), "Логин не совпдает"

    @allure.step('Проверка Email сотрудника')
    def checking_email_avatar(self):
        pytest.assume(self.avataremail().text == "1241242@m.r"), "Пароль не совпдает"



