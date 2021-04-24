# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли);
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры);
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# В качестве анализируемой задачи возьмем задание 4 к уроку 2:
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# Мое решение в тот раз:

# функция получения n-ного слагаемого
# def term(n):
#     if n == 1:
#         return 1
#     else:
#         return -0.5 * term(n-1)
#
#
# num = int(input('Введите колчиство слагаемых: '))
# s = 0
# for i in range(1, num+1):
#     s = s + term(i)
# print(s)

import timeit
import cProfile
import sys

sys.setrecursionlimit(1500)

# Немного доработаем его для удобства оценки скорости выполнения и исключения ввода с клавиатуры:


def term(n):
    '''Функция получения n-го слагаемого.'''
    if n == 1:
        return 1
    else:
        return -0.5 * term(n-1)


def total_sum(num):
    '''Функция получения полной суммы.'''
    s = 0
    for i in range(1, num+1):
        s = s + term(i)
    return s

# Визуально видно, что в функции total_sum выполняется цикл, количество проходов которого напрямую зависит
# от исходного числа (n). При каждом проходе цикла вызывается рекрсивная функция term, которая также вызывает
# сама себя столько же раз. Таким образом можно предположить, что порядок роста для данной функции
# будет O(n**2). Проверим это экспериментально с использованием timeit.


print(timeit.timeit('total_sum(1)', number=1000, globals=globals()))
print(timeit.timeit('total_sum(10)', number=1000, globals=globals()))
print(timeit.timeit('total_sum(100)', number=1000, globals=globals()))
print(timeit.timeit('total_sum(1000)', number=1000, globals=globals()))

# Получены следующие результаты:
# 1     - 0.0004259
# 10    - 0.0072008
# 100   - 0.6235501
# 1000  - 79.396431
# Таким образом при увеличении тестового числа на 1 порядок, время выполнения увеличивается на 2 порядка,
# что соответствует O(n**2)

# Проанализируем функцию с помощью cProfile

cProfile.run('total_sum(1000)')

# Результат:
#          500504 function calls (1004 primitive calls) in 0.201 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.201    0.201 <string>:1(<module>)
# 500500/1000    0.200    0.000    0.200    0.000 Lesson_4_Task_1.py:40(term)
#         1    0.000    0.000    0.201    0.201 Lesson_4_Task_1.py:48(total_sum)
#         1    0.000    0.000    0.201    0.201 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Мы видим, что "узким местом" в коде является рекурсивная фуекция, которая была вызвана 500500 раз
# и заняла почти все время выполнения программы. Следовательно необходимо избавиться от нее.

def term_2(n):
    '''Функция получения n-го слагаемого.'''
    term = 1
    c = 1
    while c < n:
        term *= -0.5
        c += 1
    return term


def total_sum_2(num):
    '''Функция получения полной суммы.'''
    s = 0
    for i in range(1, num+1):
        s = s + term_2(i)
    return s


# В данном варианте исключен рекурсивный вызов функции, однако все равно присутствует цикл в цикле,
# так что порядок роста тоже должен быть O(n**2). Проверим время выполнения функции:

print(timeit.timeit('total_sum_2(1)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_2(10)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_2(100)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_2(1000)', number=1000, globals=globals()))


# Получены следующие результаты:
# 1     - 0.0005061999999999983
# 10    - 0.005934200000000001
# 100   - 0.3733118
# 1000  - 41.5232953
# С ростом порядка тестового числа время также увеличивается на два порядка, однако время выполнения
# сократилось приблизительно в 2 раз по сравнению с вариантом с рекурсией.

# Проанализируем время выполнения элементов кода:

cProfile.run('total_sum_2(10000)')

#          10004 function calls in 4.965 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.965    4.965 <string>:1(<module>)
#         1    0.005    0.005    4.965    4.965 Lesson_4_Task_1.py:103(total_sum_2)
#     10000    4.960    0.000    4.960    0.000 Lesson_4_Task_1.py:93(term_2)
#         1    0.000    0.000    4.965    4.965 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Мы видим, что основные потери времени наблюдаются на функции term_2, которая была вызвана 10000 раз.
# Значит надо постараться избавитья от нее:


def total_sum_3(num):
    '''Функция получения полной суммы.'''
    s = 0
    term = 1
    for _ in range(num):
        s = s + term
        term *= -0.5
    return s

# В данной функции всего один цикл, количество выполнений которого линейно зависит от тестового числа.
# Таким образом порядок роста должен быть O(n). Проверим время выполнения.


print(timeit.timeit('total_sum_3(1)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_3(10)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_3(100)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_3(1000)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_3(10000)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_3(100000)', number=1000, globals=globals()))


# Получены следующие результаты:
# 1      - 0.0003967000000000137
# 10     - 0.0010001999999999928
# 100    - 0.006986300000000001
# 1000   - 0.0737097
# 10000  - 0.7256697999999999
# 100000 - 7.2819924

# Мы видим, что при увеличении тестового числа на 1 порядок, время выполнения также увеличивается на 1 порядок.
# Что соответствует O(n).

cProfile.run('total_sum_3(100000)')

#         4 function calls in 0.008 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.008    0.008    0.008    0.008 Lesson_4_Task_1.py:147(total_sum_3)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# В выводе отсутствуют явно выбивающиеся места, так что можно сделать вывод,
# что дальнейшая оптимизация средствами языка не требуется.

# P.S. Я конечно помню, что при n > 55 можно просто выводить 2/3,
# но тогда все проверки на больших числах потеряют смысл, а мы тут сегодня ради этого.
# Но в качестве бонуса ;)

def total_sum_cheat(num):
    '''Функция получения полной суммы.'''
    if num > 55:
        return 2/3
    s = 0
    term = 1
    for _ in range(num):
        s = s + term
        term *= -0.5
    return s

print(timeit.timeit('total_sum_cheat(1)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_cheat(10)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_cheat(55)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_cheat(56)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_cheat(10000)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_cheat(100000)', number=1000, globals=globals()))
print(timeit.timeit('total_sum_cheat(1000000000000)', number=1000, globals=globals()))

# Результаты:
# 0.00040969999999999895
# 0.001031199999999996
# 0.0040757999999999975
# 0.00011350000000000249
# 0.00011079999999999424
# 0.00011039999999999661
# 0.00010999999999999899
# В данном случае варианты с тестовым числом > 55 выполняются даже быстрее чем при меньшем.
# И это не случайная ошибка.
