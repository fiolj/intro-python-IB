# -*- coding: utf-8 -*-

# import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from matplotlib.widgets import Cursor

img = misc.imread('../figuras/imagen_flujo.png', flatten=True)
ymax = img.max()


def click(event):
  """Secuencia:
  1. Encuentro el punto donde el mouse hizo 'click'
  2. Le doy valores a la línea vertical
  3. Le doy valores a la curva en el grafico de la derecha
  4. y 5. Grafico los nuevos valores
  """
  x0 = event.xdata
  l1.set_data([[x0, x0], [0., 1.]])
  l2.set_data(range(img.shape[0]), img[:, x0])
  l1.figure.canvas.draw()
  l2.figure.canvas.draw()


# Defino la figura
fig = plt.figure(figsize=(12, 4))

# Agrego el primer grafico y le dibujo la imagen
ax = fig.add_subplot(121, axisbg='#FFFFCC')
plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')

# Agrego la línea inicial en un valor inicial
x0 = 100
l1 = ax.axvline(x0, color='r', ls='--', lw=3)

# Grafico de la derecha
ax2 = plt.subplot(122)
l2, = ax2.plot(img[:, x0], 'r-', lw=2, label='corte')
ax2.set_ylim((0, ymax))
ax2.set_xlabel(u'posición en eje $y$ (pixels)')
ax2.set_ylabel('Intensidad')
ax2.legend(loc='best')

plt.tight_layout()

# Agrego el cursor y conecto la accion de presionar a la funcion click
cursor = Cursor(ax, horizOn=False, vertOn=True, useblit=True, color='blue', linewidth=1)
fig.canvas.mpl_connect('button_press_event', click)


plt.show()
