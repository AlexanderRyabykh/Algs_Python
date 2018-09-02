# 6. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

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

