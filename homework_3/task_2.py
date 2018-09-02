# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10

array = [random.randint(0, 100) for i in range(SIZE)]
indices = []

for i, item in enumerate(array):
    if item % 2 == 0:
        indices.append(i)

print(array)
print(indices)