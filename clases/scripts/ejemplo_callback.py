import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(np.random.rand(10), 'o-', lw=3)


def onclick(event):
  print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        (event.button, event.x, event.y, event.xdata, event.ydata))


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
