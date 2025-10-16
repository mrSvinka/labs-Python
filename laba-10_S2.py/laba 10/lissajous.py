import numpy as np
import matplotlib.pyplot as plt

ratios = [(3,2), (3,4), (5,4), (5,6)]
t = np.linspace(0, 2*np.pi, 1000)

fig, axs = plt.subplots(1, 4, figsize=(20, 5))
fig.suptitle('Фигуры Лисажу')

for i, (a, b) in enumerate(ratios):
    x = np.sin(a * t)
    y = np.sin(b * t)
    axs[i].plot(x, y)
    axs[i].set_title(f'{a}:{b}')

plt.tight_layout()
plt.show()