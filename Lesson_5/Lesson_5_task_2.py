# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque
from random import randint

def hex_sum(hn1, hn2):
    """
    Функция сложения двух шестнадцатиричных чисел.
    Принимает в качестве аргумента два шестнадцатиричных числа
    в виде строк, содержащих символы 0-9, A-F.
    """
    # Основание системы счисления
    BASE = 16
    # Словарь, содержащий соответствие между шестнадцатиричными цифрами и десятичными числами
    hex_digits = {'0': 0,
                  '1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  'A': 10,
                  'B': 11,
                  'C': 12,
                  'D': 13,
                  'E': 14,
                  'F': 15}
    # И обратный словарь
    rev_hex_digits = {value: key for key, value in hex_digits.items()}

    number_1, number_2 = deque(list(hn1)), deque(list(hn2))

    # Проверяем, какое из чисел длиннее. Назначаем первым то, которое длиннее.
    if len(number_2) > len(number_1):
        number_1, number_2 = number_2, number_1

    # Выравниваем длину чисел, добавляя к короткому слева нули
    number_2.extendleft('0'*(len(number_1)-len(number_2)))

    # Для хранения результата создаем очередь, в которую бедм последовательно скалыдвать результаты сложения цифр
    res = deque()
    # переменная addition - то что "в уме"
    addition = 0
    for _ in range(len(number_1)):
        dec1 = hex_digits[number_1.pop()]
        dec2 = hex_digits[number_2.pop()]
        s = dec1 + dec2 + addition
        addition = s // BASE
        res.appendleft(rev_hex_digits[s % BASE])
    if addition != 0:
        res.appendleft(rev_hex_digits[addition])
    return ''.join(res)


def hex_multiplication(hn1, hn2):
    """
    Функция умножения двух шестнадцатиричных чисел.
    Принимает в качестве аргумента два шестнадцатиричных числа
    в виде строк, содержащих символы 0-9, A-F.
    """
    # Основание системы счисления
    BASE = 16
    # Словарь, содержащий соответствие между шестнадцатиричными цифрами и десятичными числами
    hex_digits = {'0': 0,
                  '1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  'A': 10,
                  'B': 11,
                  'C': 12,
                  'D': 13,
                  'E': 14,
                  'F': 15}
    # И обратный словарь
    rev_hex_digits = {value: key for key, value in hex_digits.items()}

    number_1, number_2 = list(hn1), deque(list(hn2))

    # Очередь, в которую будем добавлять результаты умножения первого числа на отдельные числа второго
    multiplications_list = deque()
    for i in range(len(number_2)):
        # результат умножения первого числа на одну цифру второго
        multiplication = deque()
        # То что "В уме"
        addition = 0
        # Текущий множитель
        factor = hex_digits[number_2.pop()]
        for n in reversed(number_1):
            dec1 = hex_digits[n]
            m = dec1 * factor + addition
            addition = m // BASE
            multiplication.appendleft(rev_hex_digits[m % BASE])
        if addition != 0:
            multiplication.appendleft(rev_hex_digits[addition])
        # Приводим результат умножения к строке
        multiplication = ''.join(multiplication)
        # Добавляем результат умножения в список результатов, с учетом положения множителя в числе
        multiplications_list.appendleft(''.join([multiplication, '0' * i]))
    res = ''
    # Теперь с помощью функции суммирования последовательно складываем все результаты умножения.
    for _ in range(len(multiplications_list)):
        res = hex_sum(res, multiplications_list.pop())
    return res


print(hex_sum('A2', 'C4F'))
print(hex_multiplication('A2', 'C4F'))

# Дальше код для проверки на случайных данных

# Первый список со случайными числами от 0 до 1000
test_array_1 = [randint(0, 1000) for _ in range(100)]
# Его представление в виде строк с шестнадцатиричными числами
test_array_1_hex = [f'{test_array_1[i]:X}' for i in range(100)]
# Второй список со случайными числами от 0 до 1000
test_array_2 = [randint(0, 1000) for _ in range(100)]
# Его представление в виде строк с шестнадцатиричными числами
test_array_2_hex = [f'{test_array_2[i]:X}' for i in range(100)]
# Результаты сложения чисел первого и второго списков в шестнадцатиричном виде
test_array_sum = [f'{test_array_1[i] + test_array_2[i]:X}' for i in range(100)]
# Результаты сложения тех же чисел в формате строк с шестнадцатиричными числами
# с использованием функции hex_sum
test_array_sum_my = [hex_sum(test_array_1_hex[i], test_array_2_hex[i]) for i in range(100)]
# Результаты усножения чисел первого и второго списков в шестнадцатиричном виде
test_array_mul = [f'{test_array_1[i] * test_array_2[i]:X}' for i in range(100)]
# Результаты умножения тех же чисел в формате строк с шестнадцатиричными числами
# с использованием функции hex_multiplication
test_array_mul_my = [hex_multiplication(test_array_1_hex[i], test_array_2_hex[i]) for i in range(100)]

# Выводим содержимое массивов столбцами для удобства сравнения
for i in range(100):
    print(f'{test_array_1[i]:<10X}'
          f'{test_array_2[i]:<10X}'
          f'{test_array_sum[i]:<10}'
          f'{test_array_sum_my[i]:<10}'
          # + если результаты сложения чисел разными способами совпадают 
          f'{"+" if test_array_sum[i] == test_array_sum_my[i] else "-":<3}'
          f'{test_array_mul[i]:<10}'
          f'{test_array_mul_my[i]:<10}'
          # + если результаты умножения чисел разными способами совпадают 
          f'{"+" if test_array_mul[i] == test_array_mul_my[i] else "-":<3}')