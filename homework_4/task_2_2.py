# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.

# код подсмотрен на habr'е mail.ru :)

import math
import cProfile


def is_prime(num):

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_prime_numbers(count):

    prime_numbers = [2]
    next_number = 3

    while len(prime_numbers) < count:
        if is_prime(next_number):
            prime_numbers.append(next_number)
        next_number += 1

    return prime_numbers


print()
cProfile.run("get_prime_numbers(100000)")

""" Алгоритм нелинейный по времени.
Самая "трудоёмкая" функция - is_prime()"""

# Анализ с помощью cProfile

# Число № 10 - 0 s - максимально вызовов функции 28
# Число № 20 - 0 s - максимально вызовов функции 70
# Число № 100 - 0.001 s - максимально вызовов функции 540
# Число № 1000 - 0.02 s - максимально вызовов функции 7918
# Число № 10000 - 0.584 s - максимально вызовов функции 104728
# Число № 100000 - 16.176 s - максимально вызовов функции 1299708


# get_prime_numbers(10)

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        27    0.000    0.000    0.000    0.000 task_2_2.py:13(is_prime)
#         1    0.000    0.000    0.000    0.000 task_2_2.py:21(get_prime_numbers)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        27    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# get_prime_numbers(20)

#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        69    0.000    0.000    0.000    0.000 task_2_2.py:13(is_prime)
#         1    0.000    0.000    0.000    0.000 task_2_2.py:21(get_prime_numbers)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        70    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        69    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#        19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# get_prime_numbers(100)

#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       539    0.001    0.000    0.001    0.000 task_2_2.py:13(is_prime)
#         1    0.000    0.000    0.001    0.001 task_2_2.py:21(get_prime_numbers)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       539    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# get_prime_numbers(1000)

#         1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#      7917    0.013    0.000    0.015    0.000 task_2_2.py:13(is_prime)
#         1    0.004    0.004    0.020    0.020 task_2_2.py:21(get_prime_numbers)
#         1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#      7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      7917    0.002    0.000    0.002    0.000 {built-in method math.sqrt}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# get_prime_numbers(10000)

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.586    0.586 <string>:1(<module>)
#    104727    0.481    0.000    0.511    0.000 task_2_2.py:13(is_prime)
#         1    0.059    0.059    0.586    0.586 task_2_2.py:21(get_prime_numbers)
#         1    0.000    0.000    0.586    0.586 {built-in method builtins.exec}
#    104728    0.013    0.000    0.013    0.000 {built-in method builtins.len}
#    104727    0.030    0.000    0.030    0.000 {built-in method math.sqrt}
#      9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# get_prime_numbers(100000)

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002   16.177   16.177 <string>:1(<module>)
#   1299707   14.932    0.000   15.320    0.000 task_2_2.py:13(is_prime)
#         1    0.686    0.686   16.175   16.175 task_2_2.py:21(get_prime_numbers)
#         1    0.000    0.000   16.177   16.177 {built-in method builtins.exec}
#   1299708    0.154    0.000    0.154    0.000 {built-in method builtins.len}
#   1299707    0.388    0.000    0.388    0.000 {built-in method math.sqrt}
#     99999    0.014    0.000    0.014    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}