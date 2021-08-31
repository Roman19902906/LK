import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from datetime import datetime
from selenium.webdriver.support.ui import Select
import allure


class CalendarPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.calendar_wait = property(lambda: \
                                          self.browser.find_element(By.XPATH, '//*[@id="schedule-overlay"]/span'))
        # Поле календаря сотрудника
        self.calendar = lambda: self.browser.find_element(By.CSS_SELECTOR, "span.fc-title")
        # Кнопка календаря сотрудника
        self.button_calendar = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")
        # Дата на сайте
        self.date = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")
        # Проверка полей календаря
        self.check_cal = lambda: self.browser.find_elements_by_css_selector("span.fc-title")
        # Выбор сотрудника
        self.change_empl = lambda: Select(self.browser.find_element_by_tag_name("select"))
        # Ожидание активации кнопки календаря
        self.wait_button_calen = lambda: self.browser.find_element(By.CSS_SELECTOR,
                                            "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button")
        # Ожидание активации смены месяца
        self.wait_button_month = lambda: self.browser.find_element(By.XPATH,
                                            "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[4]/button")
        # Ожидание активации кнопки месяца
        self.wait_button_calenmonth = lambda: self.browser.find_element(By.CSS_SELECTOR,
                                            "#schedule-filters > form > div > div.text-right.col-lg-3.col-md-12 > button")

    @allure.step('Переход на страницу календаря')
    def calendar_button(self):
        self.browser.get("https://tt-develop.quality-lab.ru/calendar/")

    def check_days(self):
        for element in self.check_cal():
            pytest.assume(element.text == "09:00-18:00" or element.text == "")

    @property
    @allure.step('Ожидание загрузки календаря')
    def wait_calendar_button(self):
        self.wait_short.until(lambda browser: self.browser.find_element(By.CSS_SELECTOR, "span.fc-title"))
        return self


    @allure.step('Получение текущей даты')
    def check_date_time(self):
        current_datetime = datetime.now().date()
        currentdata = "%d.0%d.%d" % (current_datetime.day, current_datetime.month, current_datetime.year - 2000)
        pytest.assume(currentdata == self.date().text)


    @allure.step('Проверка смены месяца')
    def change_another_month(self):
        self.button_calendar().click()

    def button_another_month(self):
        self.wait_button_month().click()

    def check_another_month(self):
        self.wait_button_calenmonth().click()


    @allure.step('Смена сотрудника')
    def select_another_user(self):
        self.change_empl().select_by_value("503")

    def change_another_user(self):
        self.wait_button_calen().click()



