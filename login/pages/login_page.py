import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        input3 = self.browser.find_element(*LoginPage.USERNAME)
        input3.send_keys("Авто Пользователь")

    def test_input_password_positive(self):
        input4 = self.browser.find_element(*LoginPage.PASSWORD)
        input4.send_keys("12345678")

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

    def test_cal_button(self):
        self.browser.get("https://tt-develop.quality-lab.ru/calendar/")
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title"))
        )

    def test_data_time(self):
        current_datetime = datetime.now().date()
        data = self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")
        data1 = data.text
        currentdata = "%d.0%d.%d" % (current_datetime.day, current_datetime.month, current_datetime.year - 2000)
        pytest.assume(currentdata == data1)
        elements = self.browser.find_elements_by_css_selector("span.fc-title")
        for element in elements:
            pytest.assume(element.text == "09:00-18:00" or element.text == "")

    def test_another_month(self):
        wait = WebDriverWait(self.browser, 20)
        input5 = self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")
        input5.click()
        wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//html/body/div[9]/div[2]/table/tbody/tr/td/span[9]"))).click()
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button"))).click()
        element1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title"))
        )
        elements = self.browser.find_elements_by_css_selector("span.fc-title")
        for element in elements:
            pytest.assume(element.text == "09:00-18:00" or element.text == "")

    def test_another_user(self):
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_value("503")
        wait = WebDriverWait(self.browser, 20)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button"))).click()
        element1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title"))
        )
        elements = self.browser.find_elements_by_css_selector("span.fc-title")
        for element in elements:
            pytest.assume(element.text == "")
