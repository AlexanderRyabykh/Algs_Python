# 4. Определить, какое число в массиве встречается чаще всего.
import random

def get_key(dct, number):

    for key, value in dct.items():
        if number == value:
            return key


SIZE = 20

array = [random.randint(0, 20) for i in range(SIZE)]
print(array)
numbers = set(array)

cnt = dict.fromkeys(numbers, 0)
for item in array:
    cnt[item] += 1

frequency = max(cnt.values())
result = get_key(cnt, frequency)

print(f'Число {result} встречается {frequency} раз')