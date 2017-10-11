import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, np.pi, 25)
data = np.c_[x, np.sin(x)].T


def update_line(num, data, line):
  line.set_data(data[..., :num])
  # En este caso equivalente a:  line.set_data(data[:, :num])
  return line,

fig1 = plt.figure()
l, = plt.plot([], [], 'r-o', animated='True')

plt.xlim(0, np.pi)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
                                   interval=100, blit=True)


plt.show()
