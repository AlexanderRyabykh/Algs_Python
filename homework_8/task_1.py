# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()
from hashlib import sha1
from collections import Counter


def calc_sublines(line):
    """
    Функция получения хешей всех подстрок из входной строки.
    :param line: строка
    :return: список всех хешей подстрок (с возможными подстроками)
    """
    result = []
    for i in range(1, len(line) + 1): # рамка
        for j in range(len(line) - i + 1): # стартовое положение положение среза
            result.append(sha1(line[j:j + i].encode('utf-8')).hexdigest())

    return result


line = input('Введите строку из маленьких латинских букв: ')

c = Counter(calc_sublines(line))

print(c)

print(f'В строке {line} всего подстрок - {sum(c.values())}')

print(f'В строке {line} различных подстрок - {len(list(c))}')
