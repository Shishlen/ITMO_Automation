# 2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
def numbers(number_1, number_2):
    if number_1 > number_2:
        print(number_1)
    else:
        print(number_2)
numbers(8,11)




# 3. Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
def numbers(number_3, number_4):
    if number_3 != number_4 and number_3 + 135 > number_4:
        print("yes")
    else:
        print("no")
numbers(1,135 )




# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)
def month(number_5):
    if number_5 == 12 or number_5 in range(1,3):
        print("Зима")
    elif number_5 in range(3,6):
        print("Весна")
    elif number_5 in range(6,10):
        print("Лето")
    elif number_5 in range(9,12):
        print("Осень")
    else:
        print("Введите номер месяца")
month(6)




# 5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def numbers(number_6,number_7,number_8):
    if number_6 > 10 and number_7 > 10 and number_8 > 10:
        print("yes")
    else:
        print("no")
numbers(2,13,14)




# Доп *
# 6. Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
def number(list):
    summ = 0
    for number in list:
        if number > 0:
            summ += 1
    print(summ)
number([1, 0, 3, 4, -4])




# 7. Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def numbers(year, month) -> int:
    if year < 0 or month <= 0:
        print("Введите корректные значения")
    days_result = year * 12 * 29 + month * 29
    print(days_result)
numbers(1, 7)
