#Домашнее задание к лекции "Функции"

#Задание 1 
#Пункт 1. Пользователь по команде "p" может узнать владельца документа по его номеру
#Пункт 2. Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится
#Пункт 3. Пользователь по команде "l" может увидеть полную информацию по всем документам
#Пункт 4. Пользователь по команде "ads" может добавить новую полку
#Пункт 5. Пользователь по команде "ds" может удалить существующую полку из данных

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

#Вспомогательные функции
def find_name_by_number(number):
    for document in documents:
        if document['number'] == number:
            print(document['name'])
    return None

def find_shelf(num):
    for keys, values in directories.items():
        if num in values:
            return keys

# Функция нахождения владельца
def func1():
    num = input("Введите номер документа: ")
    print("Результат:")
    found = False  
    for keys, values in directories.items():
        if num in values:
            print("Владелец документа:")
            find_name_by_number(num)
            found = True
            break
    if not found:    # Выполнится если False
        print("Документ не найден в базе")
    

#Функция нахожднния полки
def func2():
    num = input("Введите номер документа: ")
    for keys, values in directories.items():
        if num in values:
            print(f'Документ хранится на полке: {keys}')
            break
    else:                    
        print ("Документ не найдент в базе")    
        
#Функция может увидеть полную информацию по всем документам       
def func3(): 
    for document in documents:
        print(f"№ {document['number']}, тип: {document['type']}, владелец: {document['name']}, полка хранения: {find_shelf(document['number'])} ")       
      

# Функция может добавить новую полку
def func4 ():
    print("Результат:\n")
    num = input("Введите номер полки: ")
    
    if num in directories:
        print("Такая полка уже существует.Текущий перечень полок:")
    else:
        directories[num] = []
        print('Полка добавлена. Текущий перечень полок:')
   
    
    keys_line = ', '.join([key for key in directories.keys()])
    print(keys_line)
    
# Функция может удалить полку
def func5 ():
    print("Результат:\n")
    num = input("Введите номер полки: ")
    
    if num not in directories:
        print("Такой полки не существует.Текущий перечень полок:")
        
    elif directories[num] != []:
        print('На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:')
        
    else:
        del directories[num]
        print('Полка удалена.Текущий перечень полок:')
   
    keys_line = ', '.join([key for key in directories.keys()])
    print(keys_line)    
    
    
    
    

# Пользовательский ввод
user_input = ''

while user_input != 'q':
    user_input = input("Введите команду (введите 'q' для выхода): ")
    
    print("Вы ввели:", user_input)
    if user_input == 'p': 
       func1 ()
    if user_input == 's': 
       func2 () 
    if user_input == 'l':
       func3 ()
    if user_input == 'ads':
       func4 ()
    if user_input == 'ds':
       func5 ()

print("Конец программы. Вы ввели 'q'")


