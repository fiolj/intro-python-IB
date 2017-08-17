fname = '../data/names.txt'
n = 0                           # contador
minlen = 3                      # longitud mínima
maxlen = 3                      # longitud máxima

fi = open(fname, 'r')
lines = fi.readlines()          # El resultado es una lista
fi.close()
for line in lines:
  if minlen <= len(line.strip()) <= maxlen:
    n += 1
    print(line.strip(), end=', ')  # No Newline


print('\n')
if minlen == maxlen:
  mensaje = 'Encontramos {} palabras que tienen {} letras'.format(n, minlen)
else:
  mensaje = 'Encontramos {0} palabras que tienen entre {1} y {2} letras'\
      .format(n, minlen, maxlen)

print(mensaje)
