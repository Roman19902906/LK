from pages.calendar_page import CalendarPage
import allure
import time

@allure.epic('Проверки графика')
class TestCalendar:
    @allure.story('Проверка даты')
    def test_date(self, auth):
        calendar_page = CalendarPage(auth)
        calendar_page.calendar_button()
        calendar_page.wait_calendar_button
        calendar_page.check_date_time()
        calendar_page.check_days()

    @allure.story('Проверка смены месяца')
    def test_month(self, auth):
        calendar_page = CalendarPage(auth)
        calendar_page.calendar_button()
        calendar_page.wait_calendar_button
        calendar_page.change_another_month()
        calendar_page.wait_calendar_button
        calendar_page.button_another_month()
        calendar_page.wait_calendar_button
        calendar_page.check_another_month()
        calendar_page.check_days()

    @allure.story('Проверка смены пользователя')
    def test_user(self, auth):
        calendar_page = CalendarPage(auth)
        calendar_page.calendar_button()
        calendar_page.wait_calendar_button
        calendar_page.select_another_user()
        calendar_page.wait_calendar_button
        calendar_page.change_another_user()
        calendar_page.check_days()
