from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from LK.tools.Json.ConfigTools import ConfigTools


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        # Поле ввода логина
        self.user_name = lambda: self.browser.find_element(By.CSS_SELECTOR, "#username")
        # Поле ввода пароля
        self.password = lambda: self.browser.find_element(By.CSS_SELECTOR, "#password")
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

    error_message = (ConfigTools.data['login_error'])

    @allure.step('Ввод логина TestUser')
    def user_name_input(self):
        self.user_name().send_keys(ConfigTools.data['incorrect_login'])
        return self

    @allure.step('Ввод пароля Password')
    def password_input(self):
        self.password().send_keys(ConfigTools.data['incorrect_password'])
        return self

    @allure.step('Нажать кнопку авторизации')
    def submit_button(self):
        self.button().click()
        return self

    def url_check(self):
            self.is_exist(find=self.login_url,
                          where=self.browser.current_url,
                          pass_text='Мы находимся на странице авторизации',
                          fail_text='Мы находимся не на странице авторизации')

    @allure.step('Считаю наличие текста "Invalid Credentials" на странице авторизации успехом')
    def invalidCredentials_isExist(self):
        try:
            self.invalid_text()
        except:
            self.is_exist(find=self.error_message,
                      where=self.invalid_text().text,
                      pass_text=self.error_message + ' есть на странице',
                      fail_text=self.error_message + ' нет на странице')
        return self

    @allure.step('Считаю отсутствие текста "Invalid Credentials" на странице авторизации успехом')
    def invalidCredentials_isNotExist(self):
        try:
            self.invalid_text()
        except:
            self.is_not_exist(find=self.error_message,
                          where=self.invalid_text().text)
        return self

    @allure.step('После неудачной авторизации в поле логина присутствует имя пользователя')
    def login_field_with_user(self):
        try:
            self.user_name()
        except:
            self.is_exist(find='TestUser',
                      where=self.user_name().get_attribute('value'))
        return self

    @allure.step('После неудачной авторизации в поле пароля отсутствует пароль')
    def pass_field_without_password(self):
        try:
            self.password()
        except:
            self.is_exist(find='',
                      where=self.password().get_attribute('value'),
                      pass_text='После неудачной авторизации пароль в поле не сохранился',
                      fail_text='После неудачной авторизации пароль в поле сохранился')

        return self


    @allure.step('Ввод логина сотрудника сотрудника')
    def username_validate_input(self, login):
        self.user_name().send_keys(f"{login}")
        return self

    @allure.step('Ввод пароля сотрудника сотрудника')
    def password_validate_input(self, password):
        self.password().send_keys(f"{password}")
        return self

    @allure.step('Проверяю, действительно ли мы на странице c репортом')
    def check_url(self):
        BasePage.is_exist(self,
                              find=BasePage.otchet_url,
                              where=self.browser.current_url,
                              pass_text='Мы находимся на странице с репортом',
                              fail_text='Мы находимся не на странице с репортом')
        return self

    @allure.step('Клик по кнопке аватара сотрудника')
    def avatar_button_click(self):
        self.avatar().click()
        return self


    @allure.step('Проверяю соответствует ли имя пользователя ожидаемому')
    def username_check(self):
        expected = (ConfigTools.data['name'])
        actual = self.avatar_login().text
        BasePage.is_exist(self,
                              find=expected,
                              where=str(actual),
                              pass_text='Имя пользователя соответствует ожидаемому',
                              fail_text='Имя пользователя не соответствует ожидаемому')
        return self

    @allure.step('Проверяю соответствует ли электоронная почта ожидаемой')
    def email_check(self):
        expected = (ConfigTools.data['email'])
        actual = self.avatare_mail().text

        BasePage.is_exist(self,
                              find=expected,
                              where=str(actual),
                              pass_text='Почта пользователя соостветствует ожидаемой',
                              fail_text='Почта пользователя не соостветствует ожидаемой')
        return self
