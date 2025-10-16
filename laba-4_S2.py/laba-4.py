#Дана строка в виде случайной последовательности чисел от 0 до 9.
#Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.




periodicity = {}
sequence = input('Строка (без пробелов):')

for n in sequence.strip():
    if n in periodicity:
        periodicity[n] += 1
    else:
        periodicity[n] = 1

sequence = {n: periodicity[n] for n in list(sorted(periodicity, key=periodicity.get, reverse=True))[:3]}

print(sequence)