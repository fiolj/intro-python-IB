import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('../data/ejemplo_plot_07_1.dat', unpack=True)
plt.plot(x, y)
