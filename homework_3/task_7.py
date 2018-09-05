# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import random

SIZE = 10

array = [random.randint(0, 100) for i in range(SIZE)]
print(array)

min_1 = min(array)
array.remove(min_1)
if min_1 in array:
    print(f'Минимальное число - {min_1}, два в списке')
else:
    min_2 = min(array)
    print(f'Минимальное число - {min_1}, за ним - {min_2}')