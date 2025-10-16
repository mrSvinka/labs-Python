import numpy as np

# Сохранение матрицы в файл
matrix = """3,4,17,-3
5,11,-1,6
0,2,-5,8"""
with open('matrix.txt', 'w') as f:
    f.write(matrix)

# Чтение матрицы
data = np.genfromtxt('matrix.txt', delimiter=',')
print("Матрица:\n", data)

# Вычисления
print(f"Сумма: {data.sum()}")
print(f"Максимум: {data.max()}")
print(f"Минимум: {data.min()}")