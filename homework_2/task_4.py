# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

num = int(input('Введите число элементов последовательности: '))

result = 0
step = -2

for i in range(num):
    step *= -0.5
    result += step

print(result)





