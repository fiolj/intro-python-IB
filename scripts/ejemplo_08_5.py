#! /usr/bin/ipython3

""" Script realizado durante la clase 8. Dos figuras """
from os.path import join

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# Levantamos los datos
pardir = '/home/fiol/trabajo/clases/pythons/clases-python/'
datfile = join(pardir, 'data/ejemplo_plot_08_1.dat')

x1, y1, y2 = np.loadtxt(datfile, unpack=True)
# Vamos a graficar sólo algunos valores (uno de cada 5)
x = x1[3:-10:5]
y = y1[3:-10:5]
yexp = y2[3:-10:5]

# Ejemplo de barras de error que dependen del eje x
error = 0.05 + 0.3 * y

fig, (ax0, ax1) = plt.subplots(num='subplots', nrows=2, sharex=True)
ax0.errorbar(x, yexp, yerr=error, fmt='-o')
ax1.plot(x, 2 * (yexp - y) / (yexp + y), 'or', markersize=8)

# Límites de graficación y títulos
ax0.set_title('Datos con error variable')
ax1.set_title('Error relativo')
ax0.set_ylabel('Voltaje (mV)', fontsize='x-large')
ax1.set_xlabel('Tiempo ($\mu$-seg)', fontsize='x-large')
ax1.set_ylabel('Error relativo', fontsize='x-large')
ax1.set_xlim((0, 3))

# Guardamos el resultado
plt.savefig('ejemplo_plot_08_5.png', dpi=72)
