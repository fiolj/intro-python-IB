"""Programa para contar e imprimir las palabras capicúa de una longitud dada"""

fname = '../data/names.txt'

n = 0                           # contador
minlen = 3                      # longitud mínima
maxlen = 3                      # longitud máxima

fi = open(fname, 'r')

for line in fi:
  p = line.strip()
  if minlen <= len(p) <= maxlen and p[::-1] == p:
    n += 1
    print('{}'.format(p), end=', ')

print('\n')

if minlen == maxlen:
  mensaje = ('Encontramos un total de {} palabras capicúa que tienen {} letras'.
             format(n, minlen))
else:
  mensaje = 'Encontramos un total de {} palabras capicúa que tienen\
 entre {} y {} letras'.format(n, minlen, maxlen)

print(mensaje)
