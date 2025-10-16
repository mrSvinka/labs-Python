import numpy as np

a = np.arange(16).reshape(4, 4)
print("Исходная матрица:\n", a)

a[[1, 3]] = a[[3, 1]]
print("\nПосле замены:\n", a)