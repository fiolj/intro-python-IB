"""Programa para contar e imprimir las palabras capicúa de una longitud dada
Además, imprimimos en qué línea del archivo original se encuentran
"""

fname = '../data/names.txt'
minlen = 3                      # longitud mínima
maxlen = 12                     # longitud máxima
capicua = []

print('\n')
fi = open(fname, 'r')
for line in fi:
  p = line.strip().lower()
  if minlen <= len(p) <= maxlen and p[::-1] == p:
    capicua.append(p)

if minlen == maxlen:
  mensaje = ('Encontramos {} palabras capicúa que tienen {} letras'.
             format(len(capicua), minlen))
else:
  mensaje = 'Encontramos {0} palabras capicúa que tienen entre {1} y {2} letras'.format(
      len(capicua), minlen, maxlen)

print(mensaje)

fo = open('../data/capicua.txt', 'w'); fo.write('\n'.join(capicua)); fo.close()
