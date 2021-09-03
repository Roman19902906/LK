from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from datetime import datetime
import allure
from LK.tools.Json.ConfigTools import ConfigTools


class CalendarPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        # блок с текстом, сообщающим текущий месяц и год
        self.grafik_text = lambda: self.browser.find_element(By.ID, 'schedule-month-title')

        # поп-ап "Обновление календаря"
        self.calendar_wait = lambda: self.browser.find_element(By.XPATH, '//*[@id="schedule-overlay"]/span')

        # Календарь сотрудника
        self.calendar = lambda: self.browser.find_element(By.CSS_SELECTOR, "span.fc-title")

        # Кнопка выбора месяца сотрудника
        self.button_calendar = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")

        # Кнопка "Принять"
        self.button_calendar_submit = lambda: self.browser.find_element_by_xpath(
            '// *[ @ id = "schedule-filters"] / form / div / div[4] / button')

        # Дата на сайте
        self.date = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")

        # Проверка полей календаря
        self.calendar_check = lambda: self.browser.find_elements_by_css_selector("span.fc-title")

        # поле справа от "Сотрудник", по клику выпадающий список
        self.sotrudnik_dropdown = lambda: \
            self.browser.find_element(By.ID, 'select2--container')

        # поле для ввода ФИО сотрудника
        self.sotrudnik_input = lambda: \
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[''2]/span/span/span[1]/input')

        # кнопка "Применить"
        self.submit_button = lambda: \
            self.browser.find_element(By.XPATH, '//*[@id="schedule-filters"]/form/div/div[' '4]/button')

        # Кнопка смены месяца
        self.month_change = lambda: self.browser.find_element(By.XPATH,
                                                              "//html/body/div[9]/div[2]/table/tbody/tr/td/span[10]")

    @allure.step('Переход на страницу календаря')
    def calendar_button(self):
        self.browser.get("https://tt-develop.quality-lab.ru/calendar/")
        return self

    @allure.step('Ожидание поп-ап "Ожидание календаря"')
    def wait_calendar_button(self):
        self.wait_short.until(lambda browser: not self.calendar_wait().is_displayed())
        return self

    @allure.step('Проверяет соответствует ли месяц и год на странице с графиком работника')
    def check_month_and_year(self):
        expected = str(datetime.now().month) + str(datetime.now().year)
        try:
            self.grafik_text()
        except:
            self.is_exist(find=expected,
                          where=self.grafik_text().text,
                          pass_text='Месяц и год соответствуют ожидаемому',
                          fail_text='Месяц и год не соответствуют ожидаемым')
        return self

    @allure.step('кликаем кнопку выбора месяца')
    def change_another_month(self):
        self.button_calendar().click()
        return self

    @allure.step('Кликаем месяц')
    def button_another_month(self):
        self.month_change().click()
        return self

    @allure.step('Кликаем кнопку календаря "Применить"')
    def check_another_month(self):
        self.button_calendar_submit().click()
        return self

    @allure.step('Выбираю сотрудника')
    def choose_another_employee(self):
        self.sotrudnik_dropdown().click()
        self.sotrudnik_input().send_keys(ConfigTools.user, Keys.ENTER)
        self.submit_button().click()
        return self

    @allure.step('Проверка рабочих дней календаря')
    def check_exists_workdays_in_calendar(self):
        self.check_exists_workdays()
        return self

    @allure.step('Проверка выходных дней календаря')
    def check_exists_holidays_in_calendar(self):
        self.check_exists_holidays()
        return self
