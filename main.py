# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# import random
# first_list = []
# second_list = []
# n = int(input("Введите количество чисел в первом списке: "))
# m = int(input("Введите количество элементов во втором списке: "))
# for _ in range(n):
#     number = random.randint(1, 10)
#     first_list.append(number)
# for _ in range(m):
#     number = random.randint(1, 10)
#     second_list.append(number)
#
# first_list.sort()
# second_list.sort()
# # print(first_list)
# # print(second_list)
# first_set = set(first_list)
# print(first_set)
# second_set = set(second_list)
# print(second_set)
#
# common_set = first_set.intersection(second_set)
# print(common_set)
#
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
n = int(input("Введите количество кустов: "))
some_list = list()
for i in range(n):
    number = random.randint(1, 20)
    some_list.append(number)

some_list_count = list()
for i in range(len(some_list) - 1):
    some_list_count.append(some_list[i - 1] + some_list[i] + some_list[i + 1])
    some_list_count.append(some_list[-2] + some_list[-1] + some_list[0])
print(max(some_list_count))
