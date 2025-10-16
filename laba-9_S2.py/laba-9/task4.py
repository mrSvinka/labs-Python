import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
zero_positions = np.where(x[:-1] == 0)[0]
if zero_positions.size > 0:
    print(x[zero_positions + 1].max())
else:
    print("Нет нулевых элементов")