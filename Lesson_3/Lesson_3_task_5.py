# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint


SIZE = 10
START_VALUE = -50
FINAL_VALUE = 50
array = [randint(START_VALUE, FINAL_VALUE) for _ in range(SIZE)]
print(array)

max_negative = 0
max_negative_pos = None

for i in range(len(array)):
    if max_negative < array[i] < 0 or array[i] < 0 and max_negative == 0:
        max_negative = array[i]
        max_negative_pos = i

if max_negative < 0:
    print(f'Максимальное отрицательное число - {max_negative} на позиции {max_negative_pos}.')
else:
    print(f'Отрицательные элементы отсутствуют.')
