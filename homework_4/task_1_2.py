# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать. (дз 3.6)

import random
import cProfile


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


NUMBER = 100
SIZE = 1000000

array = [random.randint(0, NUMBER) for i in range(SIZE)]
# print(array)

min_index = array.index(find_min(array))
max_index = array.index(find_max(array))
print(f'Индекс с мин-м значением - {min_index}, с макс-м - {max_index}')
if min_index <= max_index:
    print('Сумма элементов между ними: ', find_sum(array, min_index, max_index))
else:
    print('Сумма элементов между ними: ', find_sum(array, max_index, min_index))

# cProfile.run('find_sum(array, min_index, max_index)')

"""Вывод: В выбранном диапазоне параметров NUMBER и SIZE время выполнения 
алгоритма от величины параметров не зависит"""

# Анализ с помощью timeit

# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 100 SIZE = 10
# 100 loops, best of 3: 0.00853 usec per loop   NUMBER = 100 SIZE = 50
# 100 loops, best of 3: 0.00853 usec per loop   NUMBER = 100 SIZE = 100
# 100 loops, best of 3: 0.00853 usec per loop   NUMBER = 100 SIZE = 1000
# 100 loops, best of 3: 0.0128 usec per loop    NUMBER = 100 SIZE = 100000
# 100 loops, best of 3: 0.0128 usec per loop    NUMBER = 100 SIZE = 1000000

# Анализ с помощью cProfile

# NUMBER = 100 SIZE = 1000000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1_2.py:12(find_sum)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}






