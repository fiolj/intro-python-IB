# Primero importamos módulos built-in 
import sys, os 

# Después los módulos de terceros
import numpy as np

# Finalmente nuestros propios módulos 

from graficos.simple import plot_data
from graficos.complejo import plot_data_complejo as plot_complejo 
from graficos.tresd.vector import *
from lib.rotacion import rotate


def mi_main(N):
    # Ángulos de Euler
    angle = np.random.random(3)
    # Definimos N vectores tridimensionales
    v = np.random.random((3, N))
    y = rotate(angle,v)
    return y 



if __name__ == "__main__":
    N = 100
    y = mi_main(N)

    print(y[0:5])

    # plot_data(y) 
    # plot_complejo(y)
    print(y[:,0])
    plot_vector(y[:,0])

    print("Fin del programa")


    


