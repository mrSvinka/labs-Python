import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

t = np.linspace(0, 2*np.pi, 1000)

fig = plt.figure(figsize=(10, 8))
plt.subplots_adjust(bottom=0.4)

ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.set_title('Волна 1')
ax2.set_title('Волна 2')
ax3.set_title('Сумма волн')

wave1, = ax1.plot(t, np.sin(t))
wave2, = ax2.plot(t, np.sin(t))
sum_wave, = ax3.plot(t, np.sin(t) + np.sin(t))

slider_ax1 = plt.axes([0.2, 0.25, 0.6, 0.03])
slider_ax2 = plt.axes([0.2, 0.2, 0.6, 0.03])
slider_amp1 = Slider(slider_ax1, 'Амплитуда 1', 0.1, 2.0, valinit=1)
slider_amp2 = Slider(slider_ax2, 'Амплитуда 2', 0.1, 2.0, valinit=1)

def update(val):
    wave1.set_ydata(slider_amp1.val * np.sin(t))
    wave2.set_ydata(slider_amp2.val * np.sin(t))
    sum_wave.set_ydata(wave1.get_ydata() + wave2.get_ydata())
    fig.canvas.draw_idle()

slider_amp1.on_changed(update)
slider_amp2.on_changed(update)
plt.show()