# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# Определить, какое число в массиве встречается чаще всего. (дз 3.4)

# python -m timeit -n 100 -s "import task_1_1"

import random
import cProfile


def get_key(dct, number):

    for key, value in dct.items():
        if number == value:
            return key


NUMBER = 20
SIZE = 100000

array = [random.randint(0, NUMBER) for i in range(SIZE)]
print(array)
numbers = set(array)

cnt = dict.fromkeys(numbers, 0)
for item in array:
    cnt[item] += 1

frequency = max(cnt.values())
result = get_key(cnt, frequency)

print(f'Число {result} встречается {frequency} раз')
# cProfile.run("get_key(cnt, frequency)")

"""Вывод: В выбранном диапазоне параметров NUMBER и SIZE время выполнения 
алгоритма от величины параметров не зависит"""

# анализ с помощью timeit

# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 20  SIZE = 20
# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 50  SIZE = 20
# 100 loops, best of 3: 0.0213 usec per loop    NUMBER = 100 SIZE = 20
# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 200 SIZE = 20
# 100 loops, best of 3: 0.0128 usec per loop    NUMBER = 500 SIZE = 20

# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 20  SIZE = 50
# 100 loops, best of 3: 0.00853 usec per loop   NUMBER = 20  SIZE = 100
# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 20  SIZE = 200
# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 20  SIZE = 500
# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 20  SIZE = 1000

# "crash-test" :)
# 100 loops, best of 3: 0.0171 usec per loop    NUMBER = 1000  SIZE = 1000
# 100 loops, best of 3: 0.0128 usec per loop    NUMBER = 1000  SIZE = 10000
# 100 loops, best of 3: 0.0128 usec per loop    NUMBER = 1000  SIZE = 100000

# анализ с помощью cprofile

# NUMBER = 20 SIZE = 100000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1_1.py:12(get_key)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# NUMBER = 1000 SIZE = 100000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1_1.py:12(get_key)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}