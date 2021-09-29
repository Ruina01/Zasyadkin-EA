# -*- coding: utf-8 -*-
print("Введите количество минут:")
n = int(input())
h = n//60
o = n%60
hh = (h%24)
print("Часов:", hh%24, "Минут:", o)

