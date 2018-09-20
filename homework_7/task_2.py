# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 20
numbers = [random.randint(0, 50) for i in range(SIZE)]
print('To sort: ', numbers)


def other_merge(parent, left, right):
    """
    2ой вариант функции слияния, без перебора по индексам
    Комментарии внутри ф-ции для визуализации рекурсии
    """
    # print('Merging launched')
    while left != [] and right != []:
        if left[0] <= right[0]:
            parent.remove(parent[0])
            parent.append(left.pop(0))
        else:
            parent.remove(parent[0])
            parent.append(right.pop(0))

    while left != []:
        parent.remove(parent[0])
        parent.append(left.pop(0))

    while right != []:
        parent.remove(parent[0])
        parent.append(right.pop(0))
    # print('Merged ', parent)


def merge(parent, left, right):
    """
    1ый вариант функции слияния
    Комментарии внутри ф-ции для визуализации рекурсии
    """
    # print('Merging launched')
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            parent[k] = left[i]
            i = i + 1
        else:
            parent[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        parent[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        parent[k] = right[j]
        j = j + 1
        k = k + 1
    # print('Merged ', parent)


def merge_sort(array):
    """
    Рекурентное разбиение входящего массива array
    на составные части-массивы длиной в 1 элемент +
    запуск алгоритма слияния
    """
    if len(array) not in (0, 1):

        # print('To split ', array)
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)
        # print('To merge ', left)
        # print('To merge ', right)

        # merge(array, left, right) # Альтернативная реализация слияния
        other_merge(array, left, right)


merge_sort(numbers)
print('Sorted: ', numbers)

