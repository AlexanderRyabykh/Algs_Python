# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_1 = 5
SIZE_2 = 4

matrix = [[random.randint(0, 100) for _ in range(SIZE_1)] for i in range(SIZE_2)]
for line in matrix:
    for elem in line:
        print(f'{elem:>3}', end='')
    print()

matrix = list(zip(*matrix))

mins_of_columns = []

for col in matrix:
    mins_of_columns.append(min(col))

print(f'Результат - {max(mins_of_columns)}')