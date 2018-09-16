# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

# Задача 4, урок 3. Определить, какое число в массиве встречается чаще всего.

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


def get_key(dct, number):

    for key, value in dct.items():
        if number == value:
            return key


SIZE = 20

array = [random.randint(0, 20) for i in range(SIZE)]
print(array)
numbers = set(array)

cnt = dict.fromkeys(numbers, 0)
for item in array:
    cnt[item] += 1

frequency = max(cnt.values())
result = get_key(cnt, frequency)

print(f'Число {result} встречается {frequency} раз')
print(f'Переменные SIZE, array, numbers, cnt, frequency и result занимают '
      f'{sum(newer_show_size((SIZE, array, numbers, cnt, frequency, result)))} байт')

"""
Результат: Переменные SIZE, array, numbers, cnt, frequency и result занимают 1928 байт
Результат 2: Переменные SIZE, array, numbers, cnt, frequency и result занимают 1732 байт
Разлица в результате из-за размера множества numbers и словаря cnt, их размер определяется
количеством повторяющихся элементов в исходном массиве array: меньше повторов, больше numbers и cnt.
"""
