# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
number_quarter = int(input("введите номер четверти "))
if number_quarter == 1:
    print("x>0 , y>0")
elif number_quarter == 2:
    print("x<0 , y>0")
elif number_quarter == 3:
    print("x<0 , y<0")
else:
    print("x>0 , y>0")
