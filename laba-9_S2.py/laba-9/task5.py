import numpy as np
from scipy.stats import multivariate_normal

def logpdf(X, m, C):
    D = len(m)
    det = np.linalg.det(C)
    inv = np.linalg.inv(C)
    norm = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det)
    return norm - 0.5 * np.sum((X - m) @ inv * (X - m), axis=1)

# Тестирование
X = np.random.randn(100, 3)
m = np.array([0, 0, 0])
C = np.eye(3)

print("Собственная реализация:", logpdf(X, m, C)[:3])
print("SciPy:", multivariate_normal(m, C).logpdf(X)[:3])