# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def counter(number, n, c):
    if number // 10 == 0:
        if number == n:
            return c + 1
        else:
            return c
    else:
        if number % 10 == n:
            return counter(number // 10, n, c + 1)
        else:
            return counter(number // 10, n, c)


total = int(input('Ведите количество чисел: '))
n = int(input('Ведите искомую цифру: '))
c = 0
for i in range(total):
    number = int(input(f'Ведите {i+1}-е число: '))
    c = counter(number, n, c)
print(f'В введенной последовательности чисел цифра {n} встречается {c} раз.')
