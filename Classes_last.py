'''
Задание 1
Напишите функцию, которая возвращает название валюты (поле ‘Name’)
с максимальным значением курса с помощью сервиса www.cbr-xml-daily.ru...ly_json.js
'''
import requests

def get_api():
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    return r.json()['Valute']

def max_result():
    data = get_api()
    list_ = {}
    for i, j in data.items():
        list_.setdefault(i, j['Name'])

    max_value = max(list_, key=list_.get)
    print(max_value)

max_result()

'''
Задание 2
Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True 
в методах курсов валют (eur, usd итд) будет возвращать не курс валюты, а изменение по сравнению в прошлым значением. 
Считайте, self.diff будет принимать значение True только при возврате значения курса. 
При отображении всей информации о валюте он не используется.
'''
import requests
class Rate:
    def __init__(self, format_='value'):
        self.format_ = format_
    def exchange_rates(self):

        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    def make_format(self, currency, diff):

        response = self.exchange_rates()

        if currency in response:
                if self.format_ == 'full':
                    return response[currency]
                elif self.format_ == 'value':
                    if diff == True:
                        return response[currency]['Previous']
                    elif diff == False:
                        return response[currency]['Value']
        else:
            return "Error"
    def eur(self, diff):
        return self.make_format('EUR', diff)
    def usd(self, diff):
        return self.make_format('USD', diff)

ex_ = Rate(format_='value')
print(ex_.usd(True))

'''
Задание 3
Напишите класс Designer, который учитывает количество международных премий. 
Подсказки в коде занятия (“Ноутбук к лекциям «Понятие класса» + презентация”, zip-файл 
“Используемый ноутбук к лекциям «Понятие класса»).

'''
