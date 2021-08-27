from pages.calendar_page import CalendarPage
import allure


@allure.epic('Проверки графика')
class TestCalendar:
    @allure.story('Проверка даты')
    def test_data1(self, auth):
        login_page = CalendarPage(auth)
        login_page.test_cal_button()
        login_page.test_data_time()

    @allure.story('Проверка смены месяца')
    def test_month1(self, auth):
        login_page = CalendarPage(auth)
        login_page.test_cal_button()
        login_page.test_another_month()

    @allure.story('Проверка смены пользователя')
    def test_user1(self, auth):
        login_page = CalendarPage(auth)
        login_page.test_cal_button()
        login_page.test_another_user()
