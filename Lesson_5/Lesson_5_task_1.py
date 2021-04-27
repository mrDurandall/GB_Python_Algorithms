# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

# Данные константы позволяют быстро изменить расчетные периоды с кварталов на месяцы, полугодия и т.д.
PERIODS = 4
PERIOD_NAME = 'квартал'

companies = defaultdict(list)
number_of_companies = int(input('Введите количество компаний: '))
sum_income = 0
for _ in range(number_of_companies):
    while True:
        name = input('Введите название компании: ')
        if name not in companies:
            break
        print('Выручка для данной компании уже известна. Введите название повторно.')
    for qr in range(PERIODS):
        income = int(input(f'Введите прибыль компании {name} за {qr+1}-й {PERIOD_NAME}: '))
        companies[name].append(income)
    companies[name].append(sum(companies[name]))
    sum_income += companies[name][PERIODS]

avg_income = sum_income / len(companies)
print(f'Средняя выручка всех компаний составила {avg_income:.2f}.')

# Вариант без создания дополнительных массивов и использования лишней памяти, но с дополнительным циклом:
print('Прибыл следующих компаний выше или равна средней:')
print('\n'.join([f'{comp} со средней выручкой '
                 f'{companies[comp][PERIODS]}' for comp in companies if companies[comp][PERIODS] >= avg_income]))
print('Прибыл следующих компаний ниже средней:')
print('\n'.join([f'{comp} со средней выручкой '
                 f'{companies[comp][PERIODS]}' for comp in companies if companies[comp][PERIODS] < avg_income]))

# Вариант с использованием доп. памяти:
# winners = []
# losers = []
# for comp in companies:
#     if companies[comp][PERIODS] >= avg_income:
#         winners.append(comp)
#     else:
#         losers.append(comp)
# print('Прибыл следующих компаний выше или равна средней:')
# print('\n'.join(winners))
# print('Прибыл следующих компаний ниже средней:')
# print('\n'.join(losers))
#
