<<<<<<< Updated upstream
#Домашнее задание к лекции "Введение в типы данных и циклы. Часть 1"
#Задание 1

variable = 'Test'

if len(variable)%2 == 0:
    print('четное, результат:')
    print(f'{variable[len(variable)//2-1]}{variable[len(variable)//2]}')
    
else:
    print('Нечетное, результат:')
    print(variable[len(variable)//2])
    
    
#Задание 2


sum = 0
while True:
    word = input("Введите число:")    

    if int(word) == 0:
        break
    else:
        sum = sum + int(word)

print(f'Результат {sum}')
    

#Задание 3

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']    
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print(boys)
print(girls)

boys.sort()
girls.sort()

if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
    print(boys)
    print(girls)
else:
    couple=zip(boys,girls)
    print('Идеальные пары: ')
    for people in list(couple):
        print(f'{people[0]} и {people[1]}')



#Задание 4

countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах:')

for country in countries_temperature:
    print(f'{country[0]} - {round( ((sum(country[1])/len(country[1]))-32)*5/9 ,2)} C ')






























   

=======
#Домашнее задание к лекции "Введение в типы данных и циклы. Часть 1"
#Задание 1

variable = 'Test'

if len(variable)%2 == 0:
    print('четное, результат:')
    print(f'{variable[len(variable)//2-1]}{variable[len(variable)//2]}')
    
else:
    print('Нечетное, результат:')
    print(variable[len(variable)//2])
    
    
#Задание 2


sum = 0
while True:
    word = input("Введите число:")    

    if int(word) == 0:
        break
    else:
        sum = sum + int(word)

print(f'Результат {sum}')
    

#Задание 3

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']    
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print(boys)
print(girls)

boys.sort()
girls.sort()

if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
    print(boys)
    print(girls)
else:
    couple=zip(boys,girls)
    print('Идеальные пары: ')
    for people in list(couple):
        print(f'{people[0]} и {people[1]}')



#Задание 4

countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах:')

for country in countries_temperature:
    print(f'{country[0]} - {round( ((sum(country[1])/len(country[1]))-32)*5/9 ,2)} C ')






























   

>>>>>>> Stashed changes
