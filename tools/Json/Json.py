import json


class ConfigTools:
    """
    Класс позволяющий читать json файлы (путь: tools -> Json).
    При ошибке: убрать _delete и добавить пароли в ключ 'login'
    """

    with open(r'C:\Users\mr Robot\Desktop\tests\LK\tools\Json\data.json', encoding='utf-8-sig') as data:
        data = json.load(data)
