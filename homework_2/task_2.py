# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')

digits = list(map(int, num))

evens = 0
odds = 0

for i in digits:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f'В числе {num} чётных цифр {evens}, нечётных - {odds}')