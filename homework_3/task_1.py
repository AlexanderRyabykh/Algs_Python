# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

array = [i for i in range(2, 100)]

counts = [0 for _ in range(8)]

for num in range(8):
    for item in array:
        if item % (num + 2) == 0:
            counts[num] += 1
    print(f'В интервале от [2; 99] {counts[num]} чисел кратно {num + 2}')


