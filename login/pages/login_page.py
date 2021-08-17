import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure



class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    Ic = (By.CSS_SELECTOR, ".m-login__signin > div:nth-child(1)")
    BUTTON = (By.NAME, "_submit")

    def test_input_username(self):
        with allure.step("Ввод логина TestUser"):
            input1 = self.browser.find_element(*LoginPage.USERNAME)
            input1.send_keys("TestUser")

    def test_input_password(self):
        with allure.step("Ввод пароля Password"):
            input2 = self.browser.find_element(*LoginPage.PASSWORD)
            input2.send_keys("Password")

    def test_submit_button(self):
        with allure.step("Авторизация"):
            button = self.browser.find_element(*LoginPage.BUTTON)
            button.click()

    def checking_the_message(self):
        with allure.step("Проверка сообщения Invalid credentials."):
            TEXT1 = self.browser.find_element(*LoginPage.Ic)
            TEXT2 = TEXT1.text
            pytest.assume(TEXT2 == 'Invalid credentials.')

    def checking_invisible_message(self):
        with allure.step("Проверка непоявившегося сообщения Invalid credentials."):
            TEXT = lambda: self.browser.find_element(*LoginPage.Ic)
            try:
                pytest.assume(TEXT != 'Invalid credentials.')
            except NoSuchElementException:
                return False
            return True

    def checking_user(self):
        with allure.step("Проверка логина TestUser"):
            element = self.browser.find_element_by_css_selector("#username")
            z = element.get_attribute("value")
            pytest.assume(z == 'TestUser')

    def checking_password(self):
        with allure.step("Проверка пустой строчки пароля"):
            element1 = self.browser.find_element_by_css_selector("#password")
            r = element1.get_attribute("placeholder")
            pytest.assume(r == 'Пароль')

    def checking_URL(self):
        with allure.step("Проверка URL страницы логина"):
            url = self.browser.current_url
            pytest.assume(url == 'https://tt-develop.quality-lab.ru/login')

    def test_input_username_positive(self):
        with allure.step("Ввод логина сотрудника сотрудника: Авто Пользователь"):
            input1 = self.browser.find_element(*LoginPage.USERNAME)
            input1.send_keys("Авто Пользователь")

    def test_input_password_positive(self):
        with allure.step("Ввод пароля сотрудника сотрудника: 12345678"):
            input2 = self.browser.find_element(*LoginPage.PASSWORD)
            input2.send_keys("12345678")

    def test_avatar_button(self):
        with allure.step("Клик по кнопке аватара сотрудника"):
            button1 = self.browser.find_element_by_css_selector(".avatarCover")
            button1.click()

    def test_checking_name_avatar(self):
        with allure.step("Проверка логина сотрудника"):
            name = self.browser.find_element_by_xpath(
                ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[1]")
            name1 = name.text
            pytest.assume(name1 == "Авто Пользователь")

    def test_checking_email_avatar(self):
        with allure.step("Проверка Email сотрудника"):
            email = self.browser.find_element_by_xpath(
                ".//html/body/div[1]/header/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div[2]/span[2]")
            email1 = email.text
            pytest.assume(email1 == "1241242@m.r")

    def test_cal_button(self):
        with allure.step("Переход на страницу календаря"):
            self.browser.get("https://tt-develop.quality-lab.ru/calendar/")
        with allure.step("Проверка загрузки календаря"):
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title"))
            )

    def test_data_time(self):
        with allure.step("Получение текущей даты"):
            current_datetime = datetime.now().date()
        with allure.step("Получение текущей даты из календаря сотрудника"):
            data = self.browser.find_element_by_xpath(
                ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")
            data1 = data.text
            currentdata = "%d.0%d.%d" % (current_datetime.day, current_datetime.month, current_datetime.year - 2000)
        with allure.step("Сравнение текущей даты и даты из календаря сотрудника"):
            pytest.assume(currentdata == data1)
        with allure.step("Проверка графика сотрудника"):
            elements = self.browser.find_elements_by_css_selector("span.fc-title")
            for element in elements:
                pytest.assume(element.text == "09:00-18:00" or element.text == "")

    def test_another_month(self):
        with allure.step("Открыте календаря"):
            wait = WebDriverWait(self.browser, 20)
            buttonCalendar = self.browser.find_element_by_xpath(
                ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")
            buttonCalendar.click()
        with allure.step("Выбор рабочего месяца сентябрь"):
            wait.until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//html/body/div[9]/div[2]/table/tbody/tr/td/span[9]"))).click()
        with allure.step("Выбор графика работы в сентябре сотрудника"):
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button"))).click()
            element1 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title"))
            )
            elements = self.browser.find_elements_by_css_selector("span.fc-title")
        with allure.step("Проверка графика сотрудника"):
            for element in elements:
                pytest.assume(element.text == "09:00-18:00" or element.text == "")

    def test_another_user(self):
        with allure.step("Смена сотрудника"):
            select = Select(self.browser.find_element_by_tag_name("select"))
            select.select_by_value("503")
        with allure.step("Открыте графика работы сотрудника"):
            wait = WebDriverWait(self.browser, 20)
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button"))).click()
            element1 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title"))
            )
        with allure.step("Проверка графика работы сотрудника"):
            elements = self.browser.find_elements_by_css_selector("span.fc-title")
            for element in elements:
                pytest.assume(element.text == "")
