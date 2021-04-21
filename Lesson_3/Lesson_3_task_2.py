# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint


SIZE = 10
START_VALUE = 0
FINAL_VALUE = 100
array_1 = [randint(START_VALUE, FINAL_VALUE) for _ in range(SIZE)]
print(array_1)

array_2 = []

for pos in range(len(array_1)):
    if array_1[pos] % 2 == 0:
        array_2.append(pos)

print(array_2)
