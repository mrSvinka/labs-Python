import numpy as np

arr = np.random.normal(size=(10, 4))
print("Статистики:")
print(f"Min: {arr.min()}, Max: {arr.max()}")
print(f"Mean: {arr.mean()}, Std: {arr.std()}")

first5 = arr[:5]
print("\nПервые 5 строк:\n", first5)