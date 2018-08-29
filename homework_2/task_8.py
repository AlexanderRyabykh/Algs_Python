# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def find_digit(number, dgt):
    amount = 0
    while number != 0:
        if number % 10 == dgt:
            amount += 1
        number /= 10
        number = int(number)

    return amount

print('Введите последовательность натуральных чисел, разделяя пробелом: ')
nums = list(map(int, input().split(' ')))

dgt = int(input('Какую цифру ищем? '))
result = 0

for item in nums:
    result += find_digit(item, dgt)

print(f'В последовательности цифра {dgt} встречается {result} раз')