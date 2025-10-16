#Напишите программу,  которая выводит 3 наиболее часто встречающихся символа (без учета пробелов) с указанием их количества, в введенной пользователем строке

input_string = input("Введите строку: ")

from collections import Counter

stripped_string = input_string.replace(" ", "")

counter = Counter(stripped_string)

sorted_chars = sorted(
    counter.items(),
    key=lambda x: (-x[1], x[0])
    )

for char, count in sorted_chars[:3]:
    print(f"Символ '{char}' — {count}")