from LK.pages.calendar_page import CalendarPage
import allure


@allure.epic('Проверки графика')
class TestCalendar:
    @allure.story('Проверка даты')
    def test_date(self, auth):
        calendar_page = CalendarPage(auth)
        calendar_page\
            .calendar_button()\
            .wait_calendar_button()\
            .check_month_and_year()\
            .check_workdays()\
            .check_day_off()

    @allure.story('Проверка смены месяца')
    def test_month(self, auth):
        calendar_page = CalendarPage(auth)
        calendar_page\
            .calendar_button()\
            .wait_calendar_button()\
            .change_another_month()\
            .wait_calendar_button()\
            .button_another_month()\
            .wait_calendar_button()\
            .check_another_month()\
            .check_workdays()\
            .check_day_off()

    @allure.story('Проверка смены пользователя')
    def test_user(self, auth):
        calendar_page = CalendarPage(auth)
        calendar_page\
            .calendar_button()\
            .wait_calendar_button()\
            .choose_another_employee()\
            .wait_calendar_button()\
            .check_workdays()\
            .check_day_off()
