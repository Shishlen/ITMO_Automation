# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого.
# Результаты выводить в консоль.

class Rectangle:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def area(self):
        return self.weight * self.height

    def perimeter(self):
        return (self.weight * 2) + (self.height * 2)


side_1 = Rectangle(3, 9)
side_2 = Rectangle(5, 8)
side_3 = Rectangle(12, 39)

print("Площадь прямоугольников:")
print("Прямоугольник А: ", side_1.area())
print("Прямоугольник В: ", side_2.area())
print("Прямоугольник С: ", side_3.area())

print("\n")

print("Периметр прямоугольников:")
print("Прямоугольник А: ", side_1.perimeter())
print("Прямоугольник В: ", side_2.perimeter())
print("Прямоугольник С: ", side_3.perimeter())


# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия
# и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a % self.b

    def subtraction(self):
        return self.a - self.b


value_math = Math(13, 7)

print("Сложение: ", value_math.division())
print("Умножение: ", value_math.multiplication())
print("Деление: ", value_math.division())
print("Вычитание: ", value_math.subtraction())

print("\n")

# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:
    def __init__(self, text, loc = " ", type_button = "Кнопка",):
        self.text = text
        self.type_button = type_button
        self.loc = loc
    def click(self):
        return f"Клик по кнопке {self.text}"

# Кнопки раздела Elements

elements_button_1 = Button("Text Box")
elements_button_2 = Button("Check Box")
elements_button_3 = Button("Radio Button")
elements_button_4 = Button("Web Tables")
elements_button_5 = Button("Buttons")
elements_button_6 = Button("Links")
elements_button_7 = Button("Broken Links - Images")
elements_button_8 = Button("Upload and Download")
elements_button_9 = Button("Dynamic Properties")

# Кнопки раздела Forms

forms_button_1 = Button("Practice Form")

# Кнопки раздела Alerts, Frame & Windows (AFW)

afw_button_1 = Button("Browser Windows")
afw_button_2 = Button("Alerts")
afw_button_3 = Button("Frames")
afw_button_4 = Button("Nested Frames")
afw_button_5 = Button("Modal Dialogs")

# Кнопки раздела Widgets

widgets_button_1 = Button("Accordian")
widgets_button_2 = Button("Auto Complete")
widgets_button_3 = Button("Date Picker")
widgets_button_4 = Button("Slider")
widgets_button_5 = Button("Progress Bar")
widgets_button_6 = Button("Tabs")
widgets_button_7 = Button("Tool Tips")
widgets_button_8 = Button("Menu")
widgets_button_9 = Button("Select Menu")

# Кнопки раздела Interactions

interactions_button_1 = Button("Sortable")
interactions_button_2 = Button("Selectable")
interactions_button_3 = Button("Resizable")
interactions_button_4 = Button("Droppable")
interactions_button_5 = Button("Dragabble")

# Кнопки раздела Book Store Application (BSApp)

bsapp_button_1 = Button("Login")
bsapp_button_2 = Button("Book Store")
bsapp_button_3 = Button("Profile")
bsapp_button_4 = Button("Book Store API")


print("РАЗДЕЛ ELEMENTS:")
print(elements_button_1.text)
print(elements_button_2.text)
print(elements_button_3.text)
print(elements_button_4.text)
print(elements_button_5.text)
print(elements_button_6.text)
print(elements_button_7.text)
print(elements_button_8.text)
print(elements_button_9.text)

print("\n")

print(elements_button_1.click())
print(elements_button_2.click())
print(elements_button_3.click())
print(elements_button_4.click())
print(elements_button_5.click())
print(elements_button_6.click())
print(elements_button_7.click())
print(elements_button_8.click())
print(elements_button_9.click())

print("\n")

print("РАЗДЕЛ FORMS:")
print(forms_button_1.text)

print("\n")

print(forms_button_1.click())

print("\n")

print("РАЗДЕЛ ALERTS, FRAME & WINDOWS:")
print(afw_button_1.text)
print(afw_button_2.text)
print(afw_button_3.text)
print(afw_button_4.text)
print(afw_button_5.text)

print("\n")

print(afw_button_1.click())
print(afw_button_2.click())
print(afw_button_3.click())
print(afw_button_4.click())
print(afw_button_5.click())

print("\n")

print("РАЗДЕЛ WIDGETS:")
print(widgets_button_1.text)
print(widgets_button_2.text)
print(widgets_button_3.text)
print(widgets_button_4.text)
print(widgets_button_5.text)
print(widgets_button_6.text)
print(widgets_button_7.text)
print(widgets_button_8.text)
print(widgets_button_9.text)

print("\n")

print(widgets_button_1.click())
print(widgets_button_2.click())
print(widgets_button_3.click())
print(widgets_button_4.click())
print(widgets_button_5.click())
print(widgets_button_6.click())
print(widgets_button_7.click())
print(widgets_button_8.click())
print(widgets_button_9.click())

print("\n")

print("РАЗДЕЛ INTERACTIONS:")
print(interactions_button_1.text)
print(interactions_button_2.text)
print(interactions_button_3.text)
print(interactions_button_4.text)
print(interactions_button_5.text)

print("\n")

print(interactions_button_1.click())
print(interactions_button_2.click())
print(interactions_button_3.click())
print(interactions_button_4.click())
print(interactions_button_5.click())

print("\n")

print("РАЗДЕЛ BOOK STORE APPLICATION:")
print(bsapp_button_1.text)
print(bsapp_button_2.text)
print(bsapp_button_3.text)
print(bsapp_button_4.text)

print("\n")

print(bsapp_button_1.click())
print(bsapp_button_2.click())
print(bsapp_button_3.click())
print(bsapp_button_4.click())

print("\n")


# 4. В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        self.ignition = False

    def start_ignition(self):
        self.ignition = True
        print("Автомобиль заведен")

    def stop_ignition(self):
        self.ignition = False
        print("Автомобиль заглушен")


Current_car = Car("Black", "Sedan", "2016")
Current_car.start_ignition()
Current_car.stop_ignition()

print("\n")

print("Тип: ", Current_car.type)
print("Год: ", Current_car.year)
print("Цвет: ", Current_car.color)


# 5. папка python_trening
# Создайте файл task_9_checks.py
# a. создайте класс Checks, принимающий 1 аргумент при инициализации (loc)
# b. создайте для него метод check_text, метод возвращает self.loc
# в файле task_9_oop_1.py
# c. наследуйте все классы от класса Checks
# i. чтобы использовать класс из другого файла его нужно импортировать
# from название файла(без расширения) import название класса
# d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
# e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py

class Checks:
    def __init__(self, loc):
        self.loc = loc

    def check_test(self):
        return self.loc

