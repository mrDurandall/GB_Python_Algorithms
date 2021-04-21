# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


ROWS = 5
COLUMNS = 4
matrix = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
print(matrix)

for r_num, row in enumerate(matrix):
    row_sum = 0
    for i in range(len(row)-1):
        row[i] = int(input(f'Введеите значение ячейки ({i},{r_num}): '))
        row_sum += row[i]
    row[-1] = row_sum

for row in matrix:
    print(row)
