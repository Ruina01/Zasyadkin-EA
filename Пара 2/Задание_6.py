# -*- coding: utf-8 -*-
print("Столбец первой клетки:")
x1 = int(input())
print("Строка первой клетки:")
y1 = int(input())
print("Стобец второй клетки:")
x2 = int(input())
print("Строка второй клетки:")
y2 = int(input())

if ((x1 % 2 != 0) and (y1 % 2 != 0)) or ((x1 % 2 == 0) and (y1 % 2 == 0)):
    one = str ("Черный")
else:
    one = str ("Белый")
if ((x2 % 2 != 0) and (y2 % 2 != 0)) or ((x2 % 2 == 0) and (y2 % 2 == 0)):
    two = str ("Черный")
else:
    two = str ("Белый")

print("Цвета совпадают?: ")
if one == two:
    print ("Да")
else:
    print ("Нет")   

