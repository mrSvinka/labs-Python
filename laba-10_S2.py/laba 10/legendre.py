import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

x = np.linspace(-1, 1, 400)
degrees = range(1, 8)
colors = plt.cm.viridis(np.linspace(0, 1, len(degrees)))

plt.figure(figsize=(10, 6))
for n, color in zip(degrees, colors):
    y = eval_legendre(n, x)
    plt.plot(x, y, color=color, label=f'n = {n}')
    plt.annotate(f'n={n}', xy=(x[-1], y[-1]), xytext=(5, 0),
                 textcoords='offset points', color=color)

plt.title('Полиномы Лежандра')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.grid(True)
plt.legend()
plt.show()