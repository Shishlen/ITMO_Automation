# task_9_oop
class Button:

    type: str = "Кнопка"

    def __init__(self, text, link):  # Стандартный метод для объявления атрибута
        self.text = text  # self - внутренний объект класса "Этот атрибут возьми и что-то сделай"
        self.link = link


# Создаем экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

home_two = ButtonTwo('Домой', '/home', 'button#home') # Cоздаем класс экземпляра

print(home_two.click()) # Вызываем метод