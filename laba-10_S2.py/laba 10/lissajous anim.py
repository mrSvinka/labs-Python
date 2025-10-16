import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-')

def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    return ln,

def update(frame):
    t = np.linspace(0, 2*np.pi, 1000)
    ratio = frame / 100
    x = np.sin(ratio * t)
    y = np.sin(t)
    ln.set_data(x, y)
    ax.set_title(f'Соотношение частот: {ratio:.2f}:1')
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(0, 100),
                    init_func=init, blit=True, interval=50)
plt.show()