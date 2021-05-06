# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint


def bubble_reversed(data):
    n = 1
    while n < len(data):
        # На каждом проходе цикла введем проверку массива на отсортированность.
        # Добавим переменную issorted, которой в начале прохода внешнего цикла присваивается значение True
        issorted = True
        # Во внутреннем цикле при выполненной перестановке присвоим ему значение False
        # После выхода из внутреннего цикла проверим состояние этой переменной.
        # Если перестановок не выполнялось,
        # значит массив уже отсортирован и можно досрочно прекратить выполнение внешнего цикла.

        # т.к. после каждого прохода цикла наименьший элемент массива оказывается на последнем месте,
        # то при следующем проходе его можно не трогать, так что можно при каждом проходе рассматривать
        # меньшее количество элементов.
        # for i in range(len(array) - 1):
        for i in range(len(data) - n):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                issorted = False
        # Вывод i для проверки того, сколько раз был выполнен внутренний цикл.
        # print(i)
        # В варианте с for i in range(len(array) - 1): цикл каждый раз выполняется 10 раз
        # В варианте for i in range(len(array) - n): цикл с каждым проходом выполняется на 1 раз меньше
        # Таким образом второй вариант позволяет сократить общее число проходов цикла и ускорить выполнение функции.

        # вывод номера прохода цикла и текущего состояния сортируемого массива для тестирования
        # print(f'{n}{array}')
        # Без проверки на сортированность цикл всегда выполняется 9 раз.
        # С проверкой на 10 случайных значениях: от 5 до 9 раз.
        # Таким образом среднее время выполнения функции уменььшается.
        if issorted:
            break
        n += 1
    return data


array = [randint(-100, 99) for i in range(10)]
print(array)
bubble_reversed(array)
print(array)
