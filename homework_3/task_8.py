# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

print('Введите элементы матрицы, разделяя пробелом')
matrix = [list(map(int, input().split())) for i in range(4)]
for line in matrix:
    line.append(sum(line))
    print(*line)



