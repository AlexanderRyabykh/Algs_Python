# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.
import cProfile

n = int(input('До какого числа посчитать простые числа: '))

sieve = [i for i in range(n)]

sieve[1] = 0

for i in range(2, n):
    if sieve[i] != 0:
        j = i * 2   # j = i + i == i * 2
        while j < n:
            sieve[j] = 0
            j += i

res = [i for i in sieve if i != 0]
print(res)

# Анализ с помощью timeit генерации простых чисел (без номера)

# 100 loops, best of 3: 0.0128 usec per loop    n = 100
# 100 loops, best of 3: 0.0128 usec per loop    n = 200
# 100 loops, best of 3: 0.0128 usec per loop    n = 500
# 100 loops, best of 3: 0.0128 usec per loop    n = 1000
# 100 loops, best of 3: 0.00853 usec per loop   n = 5000 (why ???)

