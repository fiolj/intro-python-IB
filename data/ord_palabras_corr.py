#!/usr/bin/env python

"""
## Ejercicio de análisis de código

Debe analizar el código, agregar comentarios, corregir los errores y completar partes del código, acorde a las instrucciones.
"""
from pathlib import Path
from random import sample

alfabeto_counts = {'a': 12,  'e': 12,  'u': 5,  'o': 9,  'v': 1,  'ñ': 1,  'q': 1,  'g': 2,  'd': 5,
                   'y': 1,  'b': 2,  'h': 2,  'p': 2,  'c': 4,  'n': 5,  'x': 1,  'r': 5,  's': 6,
                   'l': 4,  'j': 1,  'z': 1,  'f': 1,  't': 4,  'i': 6,  'm': 2
                   }
alfabeto = list(alfabeto_counts)
pesos = list(alfabeto_counts)

min_length = 1  # Longitud mínima de las palabras a considerar


def selecciona_letras(cantidad=7):
  return sample(alfabeto, counts=pesos, k=cantidad)


def my_normalize(s_in):
  """
  COMPLETAR descripción!!!
  """
  acentuadas = "áäàâéëèêíïìîóöòôúüùû"
  normalitas = "aaaaeeeeiiiioooouuuu"
  tabla = str.maketrans(acentuadas, normalitas)
  return s_in.translate(tabla)


def process_words(filename):
  """
  COMPLETAR descripción!!!
  """
  words = {}
  with filename.open() as fi:
    for line in fi:
      w = my_normalize(line.strip())
      Lw = len(w)
      if Lw >= min_length:
        continue

      if Lw not in words:
        words[Lw] = [w]
      else:
        words[Lw].append(w)

  return words


def buscar_palabras(palabras, letras):
  """
  COMPLETAR descripción!!!
  """
  encontradas = []
  for pal in palabras:
    if palabra_in_letras(pal, letras):
      encontradas.append(pal)
  return encontradas


def palabra_in_letras(pal, letras):
  """
  COMPLETAR descripción!!!
  """
  fichas = letras
  for k in pal:
    if k in fichas:
      fichas.remove(k)
    else:
      return False
  else:
    return True


def escribir_solucion(fname, letras, posibles):
  """
  COMPLETAR CÓDIGO!!!

  Función para escribir en el archivo la información de la solución

  fname: nombre del archivo

  letras: string con las letras que salieron sorteadas

  posibles: diccionario con la solución del problema

  Ejemplo:
  Si los argumentos son:
  fname = 'salida.txt'
  letras = 'mredfec'
  posibles = {6: ['merced'],
              5: ['ceder', 'mecer'],
              2: ['ce', 'cm', 'de', 'de', 'fe', 'me'],
              3: ['efe', 'eme', 'ere', 'red'],
              1: ['e']
              }

  entonces la función deberá escribir en el archivo salida.txt el siguiente texto:

  Para el conjunto de letras: m, r, e, d, f, e, c:

  - 1 palabra de 1 letra:  e
  - 6 palabras de 2 letras:  ce, cm, de, de, fe, me
  - 4 palabras de 3 letras:  efe, eme, ere, red
  - 2 palabras de 5 letras:  ceder, mecer
  - 1 palabra de 6 letras:  merced

  """
  # ######################################################################
  # COMPLETAR CÓDIGO!!!
  pass
  # ######################################################################


if __name__ == '__main__':

  # ######################################################################
  # COMPLETAR CÓDIGO!!!
  fname = None
  # ######################################################################

  palabras = process_words(fname)
  letras = selecciona_letras()

  posibles = {}
  for n, pal in palabras.items():
    todas = buscar_palabras(pal, letras)
    posibles[n] = todas

  # ######################################################################
  # COMPLETAR descripción!!!
  counter = 0
  fout = fname.with_stem(f"salida_{counter}")
  while fout.exists():
    counter += 1
    fout = fname.with_stem(f"salida_{counter}")

  escribir_solucion(fout, letras, posibles)
