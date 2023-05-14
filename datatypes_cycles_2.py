#Домашнее задание к лекции "Введение в типы данных и циклы. Часть 2"

#Задание 1

ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

new = []

for valuess in ids.values():
    for i in valuess:
        new.append(i)
print(f'Результат: {set(new)}')
    
   
#Задание 2

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

count_gen = 0
sample = []
for query in queries:
    count_gen +=1
    words = query.split()
    count = len(words)
    sample.append(count)
 
count_dict = {}
for item in sample:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
        
for i, j in count_dict.items():
    print(f'Поисковых запросов, содержащих {i} слов(а): {round(j/count_gen*100,2)}%')


#Задание 3

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}


for keys, values in results.items():
    roi = round(((values['revenue'] / values['cost']) - 1) * 100, 2)
    values['ROI'] = roi

print(f'Результат:\n{results}')

#Задание 4

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_value = max(stats, key=stats.get)

print(f'Максимальный объем продаж на рекламном канале: {max_value}')












