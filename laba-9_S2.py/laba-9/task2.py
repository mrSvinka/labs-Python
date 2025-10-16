import numpy as np

def rle(x):
    indices = np.where(np.diff(x) != 0)[0] + 1
    values = np.split(x, indices)
    return (np.array([v[0] for v in values]),
            np.array([len(v) for v in values]))

x = np.array([2, 2, 2, 3, 3, 3, 5])
print(rle(x))