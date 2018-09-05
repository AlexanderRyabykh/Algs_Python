# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

def find_min(line):
    minimum = line[0]
    for item in line:
        if item < minimum:
            minimum = item

    return minimum

SIZE = 10

array = [random.randint(-20, 20) for i in range(SIZE)]
print(array)

max_min = find_min(array)
index = 0

for i, item in enumerate(array):
    if max_min < item <0:
        max_min = item
        index = i

if max_min == 0:
    print('Нет отрицательных значений в массиве')
else:
    print(f'Число {max_min} - индекс {index}')