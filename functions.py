#Домашнее задание к лекции "Функции"

#Задание 1 
#Пункт 1. Пользователь по команде "p" может узнать владельца документа по его номеру
#Пункт 2. Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_name_by_number(number):
    for document in documents:
        if document['number'] == number:
            print(document['name'])
    return None

# Функция нахождения владельца
def func1():
    num = input("Введите номер документа: ")
    print("Результат:")
    found = False  # Variable to track if the document is found
    for keys, values in directories.items():
        if num in values:
            print("Владелец документа:")
            find_name_by_number(num)
            found = True
            break
    if not found:
        print("No such document")
    

#Функция нахожднния полки
def func2():
    num = input("Введите номер документа: ")
    for keys, values in directories.items():
        #if num in values:
            for i in values:
                if i == num:
                    print(keys)



# Пользовательский ввод
user_input = ''

while user_input != 'q':
    user_input = input("Enter a value (enter 'q' to quit): ")
    
    print("You entered:", user_input)
    if user_input == 'p': 
        func1 ()
    if user_input == 's': 
       func2 ()     

print("Loop ended. 'q' entered.")


