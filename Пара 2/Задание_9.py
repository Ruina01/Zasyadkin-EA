# -*- coding: utf-8 -*-
print("Введите первую сторону шоколадки:")
n = int(input())
print("Введите вторую сторону шоколадки:")
m = int(input())
print("Введите оставшуюся часть:")
k = int(input())
print("Можно ли отломить от шоколадки часть?:")
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да')
else:
    print('Нет')
