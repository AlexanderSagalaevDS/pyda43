"""
Создаем словарь purchases из файла purchase_log.
Из файла визиты visit_log читаем id и сравниваем нахождение данного id с ключом в словаре.
"""
import json

purchases = {}
purchases_logged = {}
with open("visit_log.csv", "r", encoding='utf-8') as file_log:
    with open("purchase_log.txt", "r", encoding='utf-8') as file_purchase:
        with open("funnel.csv", "w" ) as file_write:

            lines = file_purchase.readlines()
            for line in lines:
                purchase = json.loads(line)
                user_id = purchase["user_id"]
                category = purchase["category"]
                purchases[user_id] = category

            for i in file_log:
                i = i.strip().split(',')
                if i[0] in purchases.keys():
                    purchases_logged[i[0]] = purchases.get(i[0])

            json.dump(purchases_logged, file_write, ensure_ascii=False, indent=4)









