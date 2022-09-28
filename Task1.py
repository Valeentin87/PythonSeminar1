# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day_number = int(input('введите порядковый день недели '))
while day_number > 7 or day_number < 1:
      day_number = int(input('введите порядковый день недели '))
if day_number == 6 or day_number == 7:
    print('выходной')
else:
    print('рабочий')