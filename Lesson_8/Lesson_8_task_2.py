# Закодируйте любую строку по алгоритму Хаффмана.
"""Получилось как-то местами очень неуклюже, но оно работает. Кодирует и раскодирует.
В качестве дерева по-особому использовал тип counter.
Вероятно, затраты памяти и ресурсов на этот код получились конские."""


import collections


def hoffman_encode(string):
    """
    Функция кодирования строки по алгоритму Хоффмана.
    :param string: На вход получает строку
    :return: Возвращает строку из нулей и единиц и словарь к ней.
    """
    # Сперва на основе строки создаем объект counter модуля collection,
    # который содержит информацию о том, какой символ сколько раз встречается
    symbols = collections.Counter()
    for symb in string:
        symbols[symb] += 1

    # Получаем бинарное дерево на основании этого словаря. Для этого применим к нему функцию hoffman_dict_to_tree
    # Из-за своих особенностей она возвращает словарь из 1 элемента, от которого нам нужен только ключ.
    # Поэтому такой неуклюжий код.
    tree = list(hoffman_dict_to_tree(symbols).keys())[0]

    # С помощью функции hoffman_tree_to_binary на основании этого дерева получаем словарь соответствия символов
    # бинарным кодам
    binary_dict = hoffman_tree_to_binary(tree)

    # На основании этого словаря переводим исходную строку в бинарную:
    binary_string = ''
    for symb in string:
        binary_string = f'{binary_string}{binary_dict.get(symb)}'

    # Возвращаем полученный словарь и бинарную строку
    return binary_dict, binary_string


def hoffman_dict_to_tree(counter):
    """
    Функция превращающая counter в вариант бинарного дерева.
    Раюотает рекурсивно.
    :param collect: На вход получает объект типа counter
    :return: Возвращает тоже counter, но "изуродованный" до вида бинарного дерева ;)
    """
    # Если получен объект из одной пары ключ/значение, то возвращается он сам.
    if len(counter) == 1:
        return counter

    # Иначе берутся два элемента с наименьшими значениями, удаляются из исходного объекта
    # И вместо них добавляется объект с ключем из этих двух элементов и значением равным сумме их значений.
    last1 = counter.most_common()[-1]
    last2 = counter.most_common()[-2]
    counter.pop(last1[0])
    counter.pop(last2[0])
    counter.update({(last2, last1): last1[1] + last2[1]})

    # Полученный объект рекурсивно обрабатывается этой же функций, пока не останется ТОЛЬКО ОДИН элемент
    # Здесь должно заиграть https://youtu.be/VEJ8lpCQbyw
    return hoffman_dict_to_tree(counter)


def hoffman_tree_to_binary(tree, string=''):
    """
    Функция из бинарного дерева, полученного функцией hoffman_dict_to_tree строит словарь соответствия
    символов бинарным кодам. Работает рекурсивно
    :param tree: то самое дерево
    :param string: бинарная строка "накопленная" на данный момент.
    :return: возвращается словарь типа {'a': '110'}
    """
    # словарь в который будут складываться результаты
    result_dict = {}

    # если в первом элементе полученного дерева объект типа str, значит это "лист" и мы можем вернуть в словарь
    # пару из значения его первого элемента и "накопленной" строки
    if isinstance(tree[0], str):
        return {tree[0]: string}

    # Иначе делим его на два отдельных элемента и вызываем для них рекурсивно эту же функцию.
    # Для левого добавляем к строке единицу, для правого ноль.
    left = hoffman_tree_to_binary(tree[0][0], f'{string}1')
    right = hoffman_tree_to_binary(tree[1][0], f'{string}0')

    # полученные результаты добавляем к итоговому словарю и возвращаем его
    result_dict.update(left)
    result_dict.update(right)
    return result_dict


def hoffman_decode(bin_string, bin_dict):
    """
    Обратная функция. На основаниия бинарного словаря и бинарной строки расшифровывает строку в обычный вид.
    :param bin_string:
    :param bin_dict:
    :return:
    """
    # Сперва "развернем словарь", чтобы бинарные коды были ключами, а обычные символы - значениями
    # Кстати, вероятно, стоит сразу строить словарь в таком виде.
    rev_bin_dict = {value: key for key, value in bin_dict.items()}
    # print(rev_bin_dict) это просто проверка

    # Строка, куда будем складывать полученные символы
    string = ''

    # счетчики текущей позиции и длины
    pos = 0
    length = 1


    while True:
        # срез строки с текущей позиции, текущей длины
        spam = bin_string[pos:pos + length]

        # если этот срез присутствует в ключах словаря:
        # - добавляем к строке соответветствующий символ
        # - увеличиваем позицию на текущую длину
        # - сбрасываем длину до 0
        if spam in rev_bin_dict.keys():
            string = f'{string}{rev_bin_dict.get(spam)}'
            pos += length
            length = 0

        # если длина становится равной длине бинарной строки, то выходим из цикла
        if pos == len(bin_string):
            break

        # в конце прохода цикла увеличиваем длину до единицы
        length += 1
    return string


string = 'Hello World!'
# string = 'aaabbbbbb'
bin_dict, bin_string = hoffman_encode(string)
print(bin_dict)
print(bin_string)

print(hoffman_decode(bin_string, bin_dict))
