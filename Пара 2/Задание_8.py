# -*- coding: utf-8 -*-
print("Введите первое число:")
a = int(input())
print("Введите второе число:")
b = int(input())
print("Введите третье число:")
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
