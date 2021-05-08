# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# В сумму не включаем пустую строку и строку целиком.


def substrings_counter(s):
    """Функция для подсчета уникальных подстрок в строке
    Реализована через сохранение хэшей подстрок в множество.
    Использование именно хэша, а не самих подстрок, позволяет сэкономить память.
    Также по этой причине использована встроенная функция hash а не hashlib.
    встроенная функция возвращает объект int, а функции из hashlib - str.
    Таким образом при длинной исходной строке и без использования хэш-функции
    мы бы получили множество с большим количеством объектов str большого размера
    (строка даже с 1 символом - 50 байт).
    При использовании функций из hashlib получается множество с большим колчиеством объектов str,
    но они имеют одинаковый размер (89 байтов для sha1).
    При использовании встроенной функции hash - множество с объектами int размером по 36 байт."""
    # Для хранения хешей подстрок создадим множество, т.к. оно автоматически удаляет дублирующиеся значения.
    substrings_hash = set()
    # Первым циклом задаем количество символов в подстроке substr_len от 1 до N-1 (т.к. строка целиком нам не нужна)
    for substr_len in range(1, len(s)):
        # Вложенным циклом берем срезы строки длиной substr_len начиная с 0 символа по N-substr_len.
        for start_symb in range(len(s) - substr_len + 1):
            # Хеши данных срезов сохраняем в множество. Хэши дублирующихся подстрок автоматически удаляются.
            substrings_hash.add(hash(s[start_symb:start_symb + substr_len]))
    # В качестве результата выполнения функции возвращаем просто длину полученного множества,
    # что и будет количеством уникальных подстрок.
    return len(substrings_hash)


def substrings_counter_test(s):
    """Функция для проверки функции substrings_counter
    Также берет все подстроки, но собирает их в список.
    Затем выводит на экран список всех подстрок и его длину.
    После этого применяет к той же строке функцию substrings_counter и выводит ее результат."""
    print(s)
    all_substrings = []

    for substr_len in range(1, len(s)):
        for start_symb in range(len(s) - substr_len + 1):
            substring = s[start_symb:start_symb + substr_len]
            all_substrings.append(substring)
    print(all_substrings)
    print(f'Всего подстрок в строке: {len(all_substrings)}')
    print(f'Уникальных подстрок: {substrings_counter(s)}')
    print('*' * 20 + '\n')


substrings_counter_test('123456')
substrings_counter_test('112345')
substrings_counter_test('111156')
substrings_counter_test('123411')
substrings_counter_test('111111')

substrings_counter_test('papa')
substrings_counter_test('sova')
