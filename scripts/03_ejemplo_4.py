"""Programa para contar e imprimir las palabras capicúa de una longitud dada
Además, imprimimos en qué línea del archivo original se encuentran
"""

fname = '../data/names.txt'

n = 0                           # contador
minlen = 1                      # longitud mínima
maxlen = 9                      # longitud máxima

print('\n')
fi = open(fname, 'r')
for j, line in enumerate(fi):
  p = line.strip().lower()
  if minlen <= len(p) <= maxlen and p[::-1] == p:
    n += 1
    print('línea: {:4d} - {}'.format(j, line.strip()))  # Vamos numerando las coincidencias

if minlen == maxlen:
  mensaje = ('Encontramos {} palabras capicúa que tienen {} letras \
             de un total de {} palabras'.format(n, minlen, j))
else:
  mensaje = 'De un total de {3} palabras, encontramos {0}\
 palabras capicúa que tienen entre {1} y {2} letras'.format(n, minlen, maxlen, j)

print(mensaje)
