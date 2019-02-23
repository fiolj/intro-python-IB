def integrate_simps(f, a, b, N=10):
  """Calcula numéricamente la integral de la función en el intervalo dado
  utilizando la regla de Simpson

  Keyword Arguments:
  f -- Función a integrar
  a -- Límite inferior
  b -- Límite superior
  N -- El intervalo se separa en 2*N intervalos
  """
  h = (b - a) / (2 * N)
  I = f(a) - f(b)
  for j in range(1, N + 1):
    x2j = a + 2 * j * h
    x2jm1 = a + (2 * j - 1) * h
    I += 2 * f(x2j) + 4 * f(x2jm1)
  return I * h / 3
