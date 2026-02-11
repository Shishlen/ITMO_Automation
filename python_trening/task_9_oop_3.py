class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}') # использование f- строки
        else:
            print('Обычная газировка')

drink_1 = Soda()
drink_2 = Soda('Малина')
drink_1.show_my_drink()
drink_2.show_my_drink()
