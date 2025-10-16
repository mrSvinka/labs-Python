import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, -1]
unique, counts = np.unique(species, return_counts=True)

print("Уникальные виды:", unique)
print("Количество:", counts)