# Функция сравнения кортежей
def test_passing():
    assert (1,2,3) == (1,2,3)

# Функция сравнения ( файлд )
# def test_fail():
#     assert 'test' == 'testing'


# Функция для проверки на несоответствие
def test_not():
    a = 'test'
    b = 'testing'
    assert not a == b


# Функция для проверки несоответствия списков х,у
def test_list():
    x = ['a', 'b', 'c']
    y = [1, 2, 3]
    assert not x == y # вариант 1
    assert x != y # вариант 2
