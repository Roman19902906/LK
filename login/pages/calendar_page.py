import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalendarPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        # Поле календаря сотрудника
        self.calendar = lambda: self.browser.find_element(By.CSS_SELECTOR, "span.fc-title")
        # Кнопка календаря сотрудника
        self.buttoncalendar = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")
        # Дата на сайте
        self.data = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")
        # Проверка полей календаря
        self.checkcal = lambda: self.browser.find_elements_by_css_selector("span.fc-title")
        # Выбор сотрудника
        self.changeempl = lambda: Select(self.browser.find_element_by_tag_name("select"))
        # Ожидание полей календаря при входе
        self.wait1 = lambda: WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.fc-title")))
        # Ожидание активации кнопки календаря
        self.waitbuttoncalen = lambda: WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button")))
        # Ожидание активации смены месяца
        self.waitbuttonmonth = lambda: WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//html/body/div[9]/div[2]/table/tbody/tr/td/span[9]")))
        # Ожидание активации кнопки месяца
        self.waitbuttoncalenmonth = lambda: WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button")))

    @allure.step('Переход на страницу календаря')
    def test_cal_button(self):
        self.browser.get("https://tt-develop.quality-lab.ru/calendar/")
        self.wait1()

    @allure.step('Получение текущей даты')
    def test_data_time(self):
        current_datetime = datetime.now().date()
        currentdata = "%d.0%d.%d" % (current_datetime.day, current_datetime.month, current_datetime.year - 2000)
        pytest.assume(currentdata == self.data().text)
        dayscal = self.checkcal()
        for element in dayscal:
            pytest.assume(element.text == "09:00-18:00" or element.text == "")

    @allure.step('Проверка смены месяца')
    def test_another_month(self):
        self.buttoncalendar().click()
        self.waitbuttonmonth().click()
        self.waitbuttoncalenmonth().click()
        dayscal = self.checkcal()
        for element in dayscal:
            pytest.assume(element.text == "09:00-18:00" or element.text == "")

    @allure.step('Смена сотрудника')
    def test_another_user(self):
        self.changeempl().select_by_value("503")
        self.waitbuttoncalen().click()
        dayscal = self.checkcal()
        for element in dayscal:
            pytest.assume(element.text == "09:00-18:00" or element.text == "")
