# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

# Первый вариант:

# def merge_sort(data):
#     print(data)
#     if len(data) == 1:
#         return data
#     first = merge_sort(data[:len(data) // 2])
#     second = merge_sort(data[len(data) // 2:])
#     first_idx = second_idx = 0
#     result = []
#     while first_idx < len(first) and second_idx < len(second):
#         if first[first_idx] < second[second_idx]:
#             result.append(first[first_idx])
#             first_idx += 1
#         else:
#             result.append(second[second_idx])
#             second_idx += 1
#     if first_idx < len(first):
#         for i in range(first_idx, len(first)):
#             result.append(first[i])
#     else:
#         for i in range(second_idx, len(second)):
#             result.append(second[i])
#     return result


# Вариант второй, немного доработанный.
# Здесь для результата заране создается пустой список необходимой длины.
# Это позволяет исключить затраты ресурсов на его изменение при увеличении.
# Исчезает необходимость постоянно вызывать изменение размера памяти, выделенной под список.
# Может быть существенно При большом объеме сортируемых данных.


def merge_sort(data):
    # Печатаем полученные данные, для проверки.
    # print(data)

    # Список единичной длины считаем отсортированным и возвращаем его же.
    if len(data) == 1:
        return data

    # Делим список на две половины и к каждой рекурсивно применяем функцию сортировки.
    first = merge_sort(data[:len(data) // 2])
    second = merge_sort(data[len(data) // 2:])

    # Счетчики элементов половин, которые будем проверять и счетчик элементов результирующего массива,
    # который будем присваивать
    first_idx = 0
    second_idx = 0
    result_idx = 0

    # Заранее создаем пустой массив для результата. Длина будет совпадать с длиной исходного.
    result = [None] * len(data)

    #  По порядку сравниваем элементы первого и второго массивов.
    #  Очередному элементу результирующего массива присваиваем значение меньшего.
    #  Увеличиваем соответствующий счетчик. Повторяем до тех пор, пока не дойдем до конца одного из списков.
    while first_idx < len(first) and second_idx < len(second):
        if first[first_idx] < second[second_idx]:
            result[result_idx] = first[first_idx]
            result_idx += 1
            first_idx += 1
        else:
            result[result_idx] = second[second_idx]
            result_idx += 1
            second_idx += 1

    # Проверяем, в каком из списков остались элементы и присваиваем их последним элементам результирующего списка.
    if first_idx < len(first):
        for i in range(first_idx, len(first)):
            result[result_idx] = first[i]
            result_idx += 1
    else:
        for i in range(second_idx, len(second)):
            result[result_idx] = second[i]
            result_idx += 1

    # Печатаем отсортированные данные, для проверки
    # print(result)
    return result

# P.S. Кстати, практически такой вариант приведен в википедии. Заглянул уже после того как написал его.
# Просто из любопытства. Честно, честно ;)
# Поэтому даже страшно, а точно ли я правильно написал. Но, вроде, все по описанию алгоритма.
# Так что, надеюсь, это уже статью в вики кто-то поправил. :)
# P.P.S. А вот в викиучебнике действительно что-то странное написано.


array = [round(random.random() * 50, 4) for i in range(10)]

print(array)
array = merge_sort(array)
print(array)
