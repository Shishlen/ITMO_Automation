from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search = Input('input#search', 'Строка ввода')




class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

button = Button('Button#button', 'Нажать на кнопку')




class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


title_1 = Title('Title#title_1', 'Ввести заголовок')


class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

link_url = Link('Link#linkurl', 'Ввести ссылку')

print(button.check_test())
print(search.check_test())
print(title_1.check_test())
print(link_url.check_test())