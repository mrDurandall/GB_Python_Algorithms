# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint


SIZE = 10
START_VALUE = 0
FINAL_VALUE = 100
array = [randint(START_VALUE, FINAL_VALUE) for _ in range(SIZE)]
print(array)

min_ = array[0]
min_pos = 0
max_ = array[0]
max_pos = 0

for i in range(1, len(array)):
    if array[i] < min_:
        min_ = array[i]
        min_pos = i
    if array[i] > max_:
        max_ = array[i]
        max_pos = i

print(f'Максимальное число - {max_} на позиции {max_pos}. \nМинимальное число - {min_} на позиции {min_pos}. ')
array[min_pos], array[max_pos] = array[max_pos], array[min_pos]
print(array)
