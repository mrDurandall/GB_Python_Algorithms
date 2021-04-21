# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9

START_VALUE_1 = 2
FINAL_VALUE_1 = 100
START_VALUE_2 = 2
FINAL_VALUE_2 = 10
array = [number for number in range(START_VALUE_1, FINAL_VALUE_1)]

for i in range(START_VALUE_2, FINAL_VALUE_2):
    c = 0
    for n in array:
        if n % i == 0:
            c += 1
    print(f'Числу {i} кратно {c} чисел')
