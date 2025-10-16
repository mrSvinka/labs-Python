#Задан список с числами. Напишите программу, которая меняет местами наибольший и наименьший элемент и выводит новый список.


num = list(map(int, input('Элементы списка: ').split()))

if len(num) > 0:
    min_val = min(num)
    max_val = max(num)
    min_index = num.index(min_val)
    max_index = num.index(max_val)
    num[min_index], num[max_index] = max_val, min_val

print(num)