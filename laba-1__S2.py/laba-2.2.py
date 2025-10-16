n = int(input("число n: "))
d = 1
u = 0
r = 0
y = 1
h = 0

#нашли число для целочисленного деления
while u <= n:
    if n // d >= 10:
        d *= 10
    else:
        if 0 < n // d < 10:
            u = d
            break

# нашли кол-во нулей в числе (для послед. прибавления пропуска)
while u>=y:
    if u // y >= 10:
        y *= 10
        r += 1
    else:
        if 0 < u // y < 10:
            break

#формеруем отступы
for i in range(n, 0, -1):
    if 0 >= i // u:
        u /= 10
        h += r
        r -= 1
        print((' ' * ((n + h) - i)), end='')
    else:
        if 0 < i // u < 10:
            h += r
            print((' ' * ( (n+h) - i)), end='')

# Формирование первой части - от i до 1
    for j in range(i, 0, -1):
        print(j, end='')

# Формирование второй части - от 2 до i
    for j in range(2, i + 1):
        print(j, end='')

# Переход на следующую строку
    print()
