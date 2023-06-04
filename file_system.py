#Переведите содержимое файла purchase_log.txt* в словарь purchases вида:
#{‘1840e0b9d4’: ‘Продукты’, …}

import json

purchase_data = {}

with open("purchase_log.txt", "r", encoding = 'utf-8') as file:
    header = file.readline()


    for line in file:
        purchase = json.loads(line)

        user_id = purchase["user_id"]
        category = purchase["category"]

        purchase_data[user_id] = category


print(purchase_data)