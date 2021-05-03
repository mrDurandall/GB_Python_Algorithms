# Вариант 2 - Вариант с разбора ДЗ. Без рекурсии.

# Сразу импортируем sys для подсчета использованной памяти и randint для использования при тестировании
import sys
from random import randint


def printtotalsize(*objects):
    """
    Функция для подсчета памяти, используемой объектами, переданными в качестве аргументов.
    Получает список объектов, выводит содержимое каждого, его тип и занимаемый объем памяти.
    Если объект - список или кортеж, ркурсивно вызывает сама себя для содержимого данного объекта.
    """
    total_size = 0
    for obj in objects:
        spam = sys.getsizeof(obj)
        total_size += spam
        print(f'{obj} : {type(obj)} : {spam:>10}')
        if type(obj) == list or type(obj) == tuple:
            printtotalsize(*obj)
        if type(obj) == dict:
            printtotalsize(*(list(obj.keys()) + list(obj.values())))
    print(f'Суммарный объем использованной памяти: {total_size}')

BASE = 10

# Для тестирования жестко зададим колчиество чисел и искомое число
# num = int(input("Введите количество чисел: "))
# digit = int(input("Какую цифру подсчитать: "))
num = 100
digit = 5
count = 0
for i in range(1, num + 1):
    # ans = int(input(f'Введите число {i}: '))
    ans = randint(1, 500)
    while ans > 0:
        if ans % BASE == digit:
            count += 1
        ans //= BASE  # ans = ans // 10

print(f'Было введено {count} цифр {digit}')


# Для получения списка используемых объектов применим print(locals())
# {... 'BASE': 10, 'num': 100, 'digit': 5, 'count': 13, 'i': 100, 'ans': 0}

# Измерим память, используемую данными переменными:
# printtotalsize(BASE, num, digit, count, i, ans)
# Результат подсчетов:

# 10 : <class 'int'> :         28
# 100 : <class 'int'> :         28
# 5 : <class 'int'> :         28
# 25 : <class 'int'> :         28
# 100 : <class 'int'> :         28
# 0 : <class 'int'> :         24
# Суммарный объем использованной памяти: 164

# Таким образом полный расход памяти при данном решении задачи будет 164

