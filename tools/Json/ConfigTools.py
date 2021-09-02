import json


class ConfigTools:
    """
    Класс позволяющий читать json файлы (путь: tools -> Json).
    """

    with open(r'C:\Users\mr Robot\Desktop\tests\LK\tools\Json\data.json', encoding='utf-8-sig') as data:
        data = json.load(data)
