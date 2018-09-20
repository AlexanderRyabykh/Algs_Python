# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array):
    n = 1

    while n < len(array):

        for i in range(len(array) - 1):

            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        n += 1

    print(array)


SIZE = 20
numbers = [random.randint(-100, 100) for i in range(SIZE)]

print(numbers)
bubble_sort(numbers)