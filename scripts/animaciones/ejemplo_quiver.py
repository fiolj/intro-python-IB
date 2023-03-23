import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('ggplot')

plt.ioff()

# ############################################################
# Creación de datos
x = np.linspace(-3, 3, 91)
t = np.linspace(0, 25, 30)
y = np.linspace(-3, 3, 91)
X3, Y3, T3 = np.meshgrid(x, y, t)
sinT3 = np.sin(2*np.pi*T3 /
               T3.max(axis=2)[..., np.newaxis])

G = (X3**2 + Y3**2)*sinT3
# Graficar una flecha cada step puntos
step = 10
x_q, y_q = x[::step], y[::step]
 
# Create U and V vectors to plot
U = G[::step, ::step, :-1].copy()
V = np.roll(U, shift=3, axis=2)

# ############################################################
# Figura y ejes. 
fig1, ax = plt.subplots(figsize=(12,8))

ax.set_aspect('equal')
 
ax.set(xlim=(-4, 4), ylim=(-4, 4))

 
qax = ax.quiver(x_q, y_q, U[..., 0], V[..., 0],
                scale=100)
 
def animate(i):
  qax.set_UVC(U[..., i], V[..., i])

anim = animation.FuncAnimation(fig1, animate, interval=100, frames=len(t)-1, repeat=True)

# anim.save('quiver.gif', writer='imagemagick')
# anim.save('quiver.mp4')
anim.save('quiver.gif')
plt.show()