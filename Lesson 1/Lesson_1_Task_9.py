# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).


a = float(input('Введите первое число: '))
b = float(input('Введите второе число. Оно должно быть не равно первому: '))
c = float(input('Введите третье число. Оно должно быть не равно первому и второму: '))
if a < b < c or a > b > c:
    print(f'{b} - среднее')
elif b < a < c or b > a > c:
    print(f'{a} - среднее')
else:
    print(f'{c} - среднее')
