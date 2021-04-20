# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# Ссылка на блок-схемы: https://drive.google.com/file/d/1OT1525rZlQp-xVruIp0182YjiJBnRriE/view?usp=sharing

while True:
    print('Введите 2 целых числа и знак операции.')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    operation = input('Введите знак операции (+, -, * или /). '
                      'Для завершения программы введите символ 0: ')
    if operation == '0':
        print('Выполнение программы завершено!')
        break
    elif operation == '+':
        print(f'{a} + {b} = {a + b}')
    elif operation == '-':
        print(f'{a} - {b} = {a - b}')
    elif operation == '*':
        print(f'{a} * {b} = {a * b}')
    elif operation == '/':
        print(f'{a} / {b} = {a / b}')
    else:
        print('Введен некорректный знак операции!')
