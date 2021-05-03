# Вариант 3 - Вариант с сохранением подсчета каждой цифры в словарь.

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
alldigits = {}
for i in range(1, num + 1):
    # ans = int(input(f'Введите число {i}: '))
    ans = randint(1, 500)
    while ans > 0:
        if spam not in alldigits.keys():
            alldigits.update({ans % BASE: 1})
        else:
            alldigits[ans % BASE] += 1
        ans //= BASE  # ans = ans // 10

print(alldigits)

# Для получения списка используемых объектов применим print(locals())
# {... 'BASE': 10, 'num': 100, 'alldigits': {2: 44, 4: 39, 3: 33, 1: 48, 6: 16, 8: 17, 9: 21, 0: 16, 7: 23, 5: 19},
# 'i': 100, 'ans': 0, 'spam': 1}

# Измерим память, используемую данными переменными:
printtotalsize(BASE, num, alldigits, i, ans)
# Результат подсчетов:

# 10 : <class 'int'> :         28
# 100 : <class 'int'> :         28
# {7: 30, 2: 36, 8: 19, 4: 40, 5: 26, 1: 41, 3: 36, 0: 23, 9: 15, 6: 15} : <class 'dict'> :        360
# 7 : <class 'int'> :         28
# 2 : <class 'int'> :         28
# 8 : <class 'int'> :         28
# 4 : <class 'int'> :         28
# 5 : <class 'int'> :         28
# 1 : <class 'int'> :         28
# 3 : <class 'int'> :         28
# 0 : <class 'int'> :         24
# 9 : <class 'int'> :         28
# 6 : <class 'int'> :         28
# 30 : <class 'int'> :         28
# 36 : <class 'int'> :         28
# 19 : <class 'int'> :         28
# 40 : <class 'int'> :         28
# 26 : <class 'int'> :         28
# 41 : <class 'int'> :         28
# 36 : <class 'int'> :         28
# 23 : <class 'int'> :         28
# 15 : <class 'int'> :         28
# 15 : <class 'int'> :         28
# Суммарный объем использованной памяти: 556
# 100 : <class 'int'> :         28
# 0 : <class 'int'> :         24
# Суммарный объем использованной памяти: 468

# С учетом особенностей вывода функции printtotalsize суммарный объем памяти будет 556 + 468 = 1024 байта
# Объект словарь сам по себе занимает целых 360 байт, каждый его ключ и значение также занимает по 28 байт.
# Плюс общие переменные программы.
# Однако при увеличении количества вводимых чисел со 100 до, например, 1000 используемая память не увеличивается.

