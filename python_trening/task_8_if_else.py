# Проверяется значение num
num = 3
if num >= 0:
    print("Число больше либо равно 0")
else:
    print("Число отрицательное")

# str_2 содержит в себе str_1 ?
str_1 = 'test'
str_2 = 'test1'
if str_1 in str_2:
    print("Содержит")
else:
    print ("Не содержит")

# if elif else
num_float = 3.4

# Проверка условий
if num_float > 0:
    print("Положительное число")
elif num_float == 0:
    print("Ноль")
else:
    print("Отрицательное число") #если ни одно из условий не подошло

# if - or and
permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

# Написать программу, которая отвечает, какое Ваше текущее звание исходя из курса
# варианты званий:
# 1. Бакалавр 1-4 курс (включительно)
# 2. Магистр 5-6 курс (включительно)
# 3. Аспирант 7-9 курс (включительно)

def study_rank(a):
    if a == 1 or a == 2 or a == 3 or a == 4:
        print("Бакалавр")
    elif a in range(5,6):
        print("Магистр")
    elif a in range(7,9):
        print("Аспирант")
    else:
        print("Введите корректный год обучения")

study_rank(11)

# Дано число. Если оно > 100 или < -100, тот вывести на экран "-", иначе вывести "+"

def chislo(b):
    if b > 100 or b < -100:
        print("-")
    else:
        print("+")
chislo(19)