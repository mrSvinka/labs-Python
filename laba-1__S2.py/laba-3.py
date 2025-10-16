#Задание 3.
#Напишите программу, которая выводит n строк треугольника Паскаля. https://ru.wikipedia.org/wiki/Треугольник_Паскаля

def p_t(n):
    t = [] #список
    for i in range(n):
        # первая цифра
        r = [1]
        #строки дальше
        if t:
            l_r = t[-1]
            r.extend([l_r[j] + l_r[j + 1] for j in range(len(l_r) - 1)])
            r.append(1)
        t.append(r)

    for r in t:
        print(' '.join(map(str, r)))

n = int(input('введите n: '))
p_t(n)