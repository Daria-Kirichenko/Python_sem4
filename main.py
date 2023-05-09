# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random
first_list = []
second_list = []
n = int(input("Введите количество чисел в первом списке: "))
m = int(input("Введите количество элементов во втором списке: "))
for _ in range(n):
    number = random.randint(1, 10)
    first_list.append(number)
for _ in range(m):
    number = random.randint(1, 10)
    second_list.append(number)

first_list.sort()
second_list.sort()
# print(first_list)
# print(second_list)
first_set = set(first_list)
print(first_set)
second_set = set(second_list)
print(second_set)

common_set = first_set.intersection(second_set)
print(common_set)
