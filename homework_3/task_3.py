# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


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

maximum = array.index(find_max(array))
minimum = array.index(find_min(array))

array[maximum], array[minimum] = array[minimum], array[maximum]
print(array)

