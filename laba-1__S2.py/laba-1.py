#Задание 1
#Напишите программу, которая принимает 3 числа,
#сравнивает между собой и возвращает максимальное и минимальное числа.
#Программа должна также корректно обрабатывать различные варианты равенств чисел.
#Функции min и мах не использовать. Только условный оператор.



a = int(input('число №1:  '))
b = int(input('число №2:  '))
c = int(input('число №3:  '))

maxi = (abs(a) + abs(b) + abs(c)) * -1
mini = abs(a) + abs(b) + abs(c)

if a >= maxi:
    maxi = a
if b >= maxi:
    maxi = b
if c >= maxi:
    maxi = c

if a <= mini:
    mini = a
if b <= mini:
    mini = b
if c <= mini:
    mini = c

print('max: ', maxi, '  ', 'min: ', mini)

