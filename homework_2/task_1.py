# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при
# вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать
# пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    num1 = float(input('Введите первое число: '))
    sign = input('Введите знак операции +, -, * или /. Для выхода 0: ').strip(' ')
    if sign == '0':
        print('До свидания')
        break

    num2 = float(input('Введите второе число: '))

    if sign == '+':
        print('Результат: ', num1 + num2)
    elif sign == '-':
        print('Результат: ', num1 - num2)
    elif sign == '*':
        print('Результат: ', num1 * num2)
    elif sign == '/':
        if num2 != 0:
            print('Результат: ', num1 / num2)
        else:
            print('Нельзя делить на ноль')
    else:
        print('Не могу вычислить. Введите правильный знак операции. ')
