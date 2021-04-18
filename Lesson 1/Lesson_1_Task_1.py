# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Ссылка на блок-схемы:
# https://drive.google.com/file/d/1kh1gBrCEZGoMWFM9URr1Knbj4h1ZkpWw/view?usp=sharing

number = int(input('Введите трехзначное целое число: '))
a = number // 100
b = number % 100 // 10
c = number % 10
s = a + b + c
p = a * b* c
print(f'Сумма цифр числа: {s}\nПроизведение цифр числа: {p}')
