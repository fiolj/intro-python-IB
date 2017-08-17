"""Programa para contar e imprimir las palabras capicúa de una longitud dada"""

fname = '../data/names.txt'

n = 0                           # contador
minlen = 1                      # longitud mínima
maxlen = 9                      # longitud máxima

fi = open(fname, 'r')

for line in (fi):
  p = line.strip().lower()
  if minlen <= len(p) <= maxlen and p[::-1] == p:
    n += 1
    print('({:02d}) {}'.format(n, p))  # Vamos numerando las coincidencias

if minlen == maxlen:
  mensaje = ('Encontramos un total de {} palabras capicúa que tienen {} letras'.
             format(n, minlen))
else:
  mensaje = 'Encontramos un total de {} palabras capicúa que tienen\
 entre {} y {} letras'.format(n, minlen, maxlen)

print(mensaje)
