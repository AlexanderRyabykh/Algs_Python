# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#     При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def generate_hex(number):
    number = list(number)
    for i in range(len(number)):
        if number[i].isalpha():
            number[i] = number[i].upper()
        if number[i].isdigit():
            number[i] = int(number[i])
    return number


def sixteen_to_ten(numbers):
    _LETTERS = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    numbers.reverse()
    result = 0
    for i, item in enumerate(numbers):
        if item in _LETTERS:
            result += _LETTERS[item] * 16 ** i
        else:
            result += item * 16 ** i
    return result


def ten_to_sixteen(number):
    _LETTERS = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = []
    while number != 0:
        if number % 16 <= 9:
            result.append(number % 16)
        else:
            result.append(_LETTERS[number % 16])
        number //= 16
    result.reverse()
    return result


num_1 = generate_hex(input('Введите 1ое число в 16й системе счисления: '))
print(num_1)
num_2 = generate_hex(input('Введите 2ое число в 16й системе счисления: '))
print(num_2)

num_1 = sixteen_to_ten(num_1)
num_2 = sixteen_to_ten(num_2)
result = num_1 + num_2
print(f'Сумма чисел {ten_to_sixteen(result)}')
result = num_1 * num_2
print(f'Произведение чисел {ten_to_sixteen(result)}')
