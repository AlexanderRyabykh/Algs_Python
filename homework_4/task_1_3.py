# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# Найти максимальный элемент среди минимальных элементов столбцов матрицы. (дз 3.9)

import random
import cProfile

SIZE_1 = 2000
SIZE_2 = 2000

matrix = [[random.randint(0, 100) for _ in range(SIZE_1)] for i in range(SIZE_2)]
# for line in matrix:
#     for elem in line:
#         print(f'{elem:>3}', end='')
#     print()

matrix = list(zip(*matrix))

mins_of_columns = []

for col in matrix:
    mins_of_columns.append(min(col))

print(f'Результат - {max(mins_of_columns)}')

# cProfile.run('max(mins_of_columns)')

"""Вывод: Почему время не увеличивается при изменении параметров? """

# Анализ с помощью cProfile

# SIZE_1 = 5000 SIZE_2 = 5000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# SIZE_1 = 100 SIZE_2 = 100

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# SIZE_1 = 1000 SIZE_2 = 1000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# SIZE_1 = 2000 SIZE_2 = 2000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Анализ с помощью timeit
# Запуск через консоль с помощью python -m timeit -n 100 -s "import task_1_3"

# 100 loops, best of 3: 0.0128 usec per loop    SIZE_1 = 2000 SIZE_2 = 2000
# 100 loops, best of 3: 0.00853 usec per loop   SIZE_1 = 5000 SIZE_2 = 5000
