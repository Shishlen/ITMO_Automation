# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# Выведите в консоль значение аргумента Loc, объекта search

# class Input:
#
#     def __init__(self, loc):
#         self.loc = loc
#
# search = Input('input#search')
#
# print(search.loc)

# Добавьте к классу Input атрибут объекта text
# Создать классы: Button, Tittle, Link
# Для каждого класса атрибуты text и loc
# Каждому из 4 классов создать объекты с любыми данными
# Вывести в консоль text и loc

class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('input#search', 'Строка ввода')

print(search.loc)
print(search.text)

print('\n')


class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

button = Button('Button#button', 'Нажать на кнопку')
print(button.loc)
print(button.text)

print('\n')


class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


title_1 = Title('Title#title_1', 'Ввести заголовок')
print(title_1.loc)
print(title_1.text)

print('\n')


class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

link_url = Link('Link#linkurl', 'Ввести ссылку')
print(link_url.loc)
print(link_url.text)