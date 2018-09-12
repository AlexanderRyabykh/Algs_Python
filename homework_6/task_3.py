# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

# Задача 6, урок 3. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Задача запущена под win10 64x, python 3.6.4.

import random
import sys


def newer_show_size(x):
    """
    Составляем массив из байтов, занимаемых созданными объектами,
    включая байты вложенных объектов.
    На вход функции подаётся кортеж из исследуемых переменных,
    память под данный кортеж в результате не учитывается.
    """
    _result = []

    for i in x:
        _result.append(sys.getsizeof(i))

        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for y in i.items():
                    _result.append(sys.getsizeof(y))

            elif not isinstance(i, str):
                for y in i:
                    _result.append(sys.getsizeof(y))

    return _result


def find_sum(line, first, last):
    result = 0
    for i in range(first + 1, last):
        result += line[i]

    return result


def find_min(line):
    minimum = line[0]
    for item in line:
        if item < minimum:
            minimum = item

    return minimum


def find_max(line):
    maximum = line[0]
    for item in line:
        if item > maximum:
            maximum = item

    return maximum


SIZE = 10

array = [random.randint(0, 100) for i in range(SIZE)]
print(array)

min_index = array.index(find_min(array))
max_index = array.index(find_max(array))
print(f'Индекс с мин-м значением - {min_index}, с макс-м - {max_index}')
if min_index <= max_index:
    print('Сумма элементов между ними: ', find_sum(array, min_index, max_index))
else:
    print('Сумма элементов между ними: ', find_sum(array, max_index, min_index))

print(f'Переменные SIZE, array, min_index, max_index занимают '
      f'{sum(newer_show_size((SIZE, array, min_index, max_index)))} байт')

# Результат: Переменные SIZE, array, min_index, max_index занимают 280 байт
