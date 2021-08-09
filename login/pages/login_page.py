import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    Ic = (By.CSS_SELECTOR, ".m-login__signin > div:nth-child(1)")
    BUTTON = (By.NAME, "_submit")

    def test_input_username(self):
        input1 = self.browser.find_element(*LoginPage.USERNAME)
        input1.send_keys("TestUser")

    def test_input_password(self):
        input2 = self.browser.find_element(*LoginPage.PASSWORD)
        input2.send_keys("Password")

    def test_submit_button(self):
        button = self.browser.find_element(*LoginPage.BUTTON)
        button.click()

    def checking_the_message(self):
        TEXT1 = self.browser.find_element(*LoginPage.Ic)
        TEXT2 = TEXT1.text
        pytest.assume(TEXT2 == 'Invalid credentials.')

    def checking_invisible_message(self):
        TEXT = lambda: self.browser.find_element(*LoginPage.Ic)
        try:
            pytest.assume(TEXT != 'Invalid credentials.')
        except NoSuchElementException:
            return False
        return True
    def checking_user(self):
        element = self.browser.find_element_by_css_selector("#username")
        z = element.get_attribute("value")
        pytest.assume(z == 'TestUser')

    def checking_password(self):
        element1 = self.browser.find_element_by_css_selector("#password")
        r = element1.get_attribute("placeholder")
        pytest.assume(r == 'Пароль')


    def checking_URL(self):
        url = self.browser.current_url
        pytest.assume(url == 'https://tt-develop.quality-lab.ru/login')

    def test_input_username_positive(self):
        input1 = self.browser.find_element(*LoginPage.USERNAME)
        input1.send_keys("Авто Пользователь")

    def test_input_password_positive(self):
        input2 = self.browser.find_element(*LoginPage.PASSWORD)
        input2.send_keys("12345678")

    def test_avatar_button(self):
        button1 = self.browser.find_element_by_css_selector(".avatarCover")
        button1.click()

    def test_checking_name_avatar(self):
        name = self.browser.find_element_by_xpath(
            ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[1]")
        name1 = name.text
        pytest.assume(name1 == "Авто Пользователь")

    def test_checking_email_avatar(self):
        email = self.browser.find_element_by_xpath(
            ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[2]")
        email1 = email.text
        pytest.assume(email1 == "1241242@m.r")
