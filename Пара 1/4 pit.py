# -*- coding: utf-8 -*-
seconds = int(input("Введите количество секунд:"))
days = seconds//(3600*24)
hours = seconds//3600
minutes = seconds//60
print(days, hours, minutes, seconds)
