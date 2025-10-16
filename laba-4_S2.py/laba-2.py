#Напишите программу, которая будет выполнять действие, обратное заданию 1.
# Программа должна производить поиск по значению и выдавать ключ.



data = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}
value = input().strip()
key = [k for k, v in data.items() if str(v) == value]
if key:
    print(key[0])