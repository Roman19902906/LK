import requests

class TestWeather:

    city_id = 0
    api_key = "d3a52bd2cee1c092415cc8a5dfad321c"

    # base_url переменная для хранения URL
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Дать название города
    city_name = input("Enter city name : ")

    # complete_url переменная для хранения
    # полный адрес URL
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # получить метод модуля запросов
    # вернуть объект ответа
    response = requests.get(complete_url)

    # json метод объекта ответа
    # преобразовать данные формата json в
    # данные формата питона
    x = response.json()

    # Теперь x содержит список вложенных словарей
    # Проверьте, что значение ключа "cod" равно
    # "404", значит город найден иначе,
    # город не найден

    if x["cod"] != "404":
        # сохранить значение "main"
        # введите переменную y
        y = x["main"]
        # сохранить значение, соответствующее
        # к "временному" ключу y
        current_temperature = y["temp"]
        # сохранить значение, соответствующее
        # к клавише "давления" у
        current_pressure = y["pressure"]
        # сохранить значение, соответствующее
        # к клавише «влажность» у
        current_humidiy = y["humidity"]
        # сохранить значение «погода»
        # введите переменную z
        z = x["weather"]
        # сохранить значение, соответствующее
        # к ключу "описание" в
        # 0 индекс z
        weather_description = z[0]["description"]

        # вывести следующие значения
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))
    else:
        print(" City Not Found ")