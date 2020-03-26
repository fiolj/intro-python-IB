# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import imageio
from matplotlib.widgets import Cursor

img = imageio.imread('../figuras/imagen_flujo.png', as_gray=True)
ymax = img.max()


def seleccionar(event):
  """Secuencia:
  1. Encuentro el punto donde el mouse hizo 'click'
  2. Le doy valores a la línea vertical
  3. Le doy valores a la curva en el grafico de la derecha
  4. y 5. Grafico los nuevos valores
  """
  x0 = event.xdata
  n0 = int(x0)
  l1.set_data([[n0, n0], [0., 1.]])
  l2.set_data(range(img.shape[0]), img[:, n0])
  l1.figure.canvas.draw()
  l2.figure.canvas.draw()


# Defino la figura
fig, (ax1, ax2) = plt.subplots(figsize=(12, 4), ncols=2)

# Mostramos la imagen como un mapa de grises
ax1.imshow(img, cmap='gray', interpolation='nearest')
ax1.axis('off')

# Agrego la línea inicial en un valor inicial
x0 = 100
l1 = ax1.axvline(x0, color='r', ls='--', lw=3)

# Grafico de la derecha
l2, = ax2.plot(img[:, x0], 'r-', lw=2, label='corte')
ax2.set_ylim((0, ymax))
ax2.set_xlabel(u'posición en eje $y$ (pixels)')
ax2.set_ylabel('Intensidad')
ax2.legend(loc='best')

fig.tight_layout()

# Agrego el cursor y conecto la accion de presionar a la funcion click
cursor = Cursor(ax1, horizOn=False, vertOn=True, useblit=True,
                color='blue', linewidth=1)
fig.canvas.mpl_connect('button_press_event', seleccionar)

plt.show()
