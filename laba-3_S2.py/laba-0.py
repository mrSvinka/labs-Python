#Задан список с числами. Напишите программу, которая выводит все элементы списка, которые больше предыдущего, в виде отдельного списка.
num = list(map(int, input('Элементы списка: ').split()))

result = []

for i in range(1, len(num)):
    if num[i] > num[i-1]:
        result.append(num[i])

print(result)