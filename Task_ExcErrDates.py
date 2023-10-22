'''
Задание 1
Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка напишите формат указанной
даты для перевода в объект datetime:
The Moscow Times — Wednesday, October 2, 2002
The Guardian — Friday, 11.10.13
Daily News — Thursday, 18 August 1977
'''
from datetime import datetime

TheMoscowTimes = 'Wednesday, October 2, 2002'
TheGuardian = 'Friday, 11.10.13'
DailyNews = 'Thursday, 18 August 1977'

d1 = datetime.strptime(TheMoscowTimes, '%A, %B %d, %Y')
d2 = datetime.strptime(TheGuardian, '%A, %d.%m.%y')
d3 = datetime.strptime(DailyNews, '%A, %d %B %Y')

print(f'TheMoscowTime is {d1}')
print(f'TheGuardian is {d2}')
print(f'DailyNews is {d3}')
print()

'''
Задание 2
Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]

Напишите функцию, которая проверяет эти даты на корректность. То есть для каждой даты возвращает True — дата корректна 
или False — некорректная.
'''

def checkdates(stream):
    for i in stream:
        try:
            d = datetime.strptime(i, '%Y-%m-%d')
            print(i)
            print(True)

        except ValueError:
            print(i)
            print(False)

stream = ['2018-04-02', '2018-02-29', '2018-19-02']
checkdates(stream)
print()

'''
Задание 3
Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. 
Даты должны вводиться в формате YYYY-MM-DD. В случае неверного формата или при start_date > end_date должен 
возвращаться пустой список.

'''
from datetime import timedelta

def date_range(start_date: str, end_date: str):
    date_list = []

    try:
        sd = datetime.strptime(start_date, '%Y-%m-%d')
        ed = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print(date_list)

    if sd > ed:
        return date_list

    while sd <= ed:
        i = sd.strftime('%Y-%m-%d')
        date_list.append(i)
        sd += timedelta(days=1)

    print(date_list)


date_range('2023-10-23', '2023-10-26')

'''
Задание 4 (необязательное)
Ваш коллега прислал код функции:

DEFAULT_USER_COUNT = 3

def delete_and_return_last_user(region, default_list=[‘A100’, ‘A101’, ‘A102’]):
""“
Удаляет из списка default_list последнего пользователя
и возвращает ID нового последнего пользователя.
”""
element_to_delete = default_list[-1]
default_list.remove(element_to_delete)

1
return default_list[DEFAULT_USER_COUNT-2]
При однократном вызове этой функции всё работает корректно:
delete_and_return_last_user(1)
‘A101’

Однако при повторном вызове получается ошибка IndexError: list index out of range.

Задание:

Что значит ошибка list index out of range?
Почему при первом запуске функция работает корректно, а при втором — нет?


Ответ: При первом вызове данной функции удаляется сразу последний элемент [‘A100’, ‘A101’, ‘A102’] 
- А102 (-1), а индекс возвращенный получаем [3-2 = 1] т.е. А101
Так как remove модифицирует список, то при втором вызове список уже [‘A100’, ‘A101’] и удаляется последний элемент
‘A101’, следовательно остается [A100]. Поэтому при обращении к индексу [3-2 = 1] которого уже нет выходит ошибка:
 list index out of range,остался только индекс - 0.

'''
