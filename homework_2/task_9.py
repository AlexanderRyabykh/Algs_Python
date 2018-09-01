# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def find_sum(num):
    result = 0

    while num != 0:
        result += num % 10
        num /= 10
        num = int(num)

    return result


def get_key(d, value):
    list_of_keys = []

    for key, unit in d.items():
        if unit == value:
            list_of_keys.append(key)

    return list_of_keys


print('Введите последовательность натуральных чисел, разделяя пробелом: ')
nums = list(map(int, input().split(' ')))

sum_of_digits = {}

for item in nums:
    sum_of_digits[item] = find_sum(item)

max_value = max(sum_of_digits.values())

for keys in get_key(sum_of_digits, max_value):
    print(f'Число {keys} - сумма цифр {max_value}')
