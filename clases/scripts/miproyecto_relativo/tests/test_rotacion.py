import numpy as np


## Importamos la función que vamos a testear mediante path relativo
## Correr desde el directorio raíz del proyecto con
## python -m miproyecto_relativo.tests.test_rotacion
# from ..lib.rotacion import rotate

## Modificamos `sys.path` para poder importar el módulo
## desde cualquier directorio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from lib.rotacion import rotate

def test_rotacion():
  v = np.array([1, 0, 0])
  angle = np.array([0, 0, np.pi/2])
  assert np.allclose(rotate(angle, v), np.array([0, -1, 0]))


if __name__ == "__main__":
  test_rotacion()
  print("All tests passed")  