# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')
num_1 = ord(letter_1)
num_2 = ord(letter_2)

print(f'{letter_1} в алфавите под номером {num_1 - 96}')
print(f'{letter_2} в алфавите под номером {num_2 - 96}')
if num_1 == num_2:
    print('Между ними нет букв')
elif num_1 < num_2:
    print(f'Между ними букв - {num_2 - num_1 - 1}')
else:
    print(f'Между ними букв - {num_1 - num_2 - 1}')
