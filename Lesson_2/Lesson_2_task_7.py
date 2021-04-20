# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

def summary(number):
    if number == 1:
        return 1
    else:
        return number + summary(number - 1)


number = int(input('Введите любое натруальное число: '))
s = summary(number)
if s == number * (number + 1) / 2:
    print(f'Для n={number} равеноство 1+2+...+n = n(n+1)/2 верно!')
else:
    print(f'Для n={number} равеноство 1+2+...+n = n(n+1)/2 не верно!')
