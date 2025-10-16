#Напишите программу, которая принимает 2 списка чисел и определяет количество общих чисел из первого и второго списка.

list1 = list(map(int, input('Элементы списка 1: ').split()))
list2 = list(map(int, input('Элементы списка 2: ').split()))

common = set(list1) & set(list2)

print(len(common))