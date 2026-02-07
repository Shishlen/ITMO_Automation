# Программа для измерения величины строки через пробелы до символа

a: int = 5
b: str = "строка"
c: list = [1,2,3,4]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('|', 15))