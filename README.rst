==================================================================
 Introducción al lenguaje Python orientado a ingenierías y física
==================================================================

Material de clase para el Curso dictado, por primera vez en 2017, en el IB.


- Una versión en formato HTML puede encontrarse `aquí <https://fiolj.github.io/intro-python-IB/>`_

- Aquí en `formato pdf <https://fiolj.github.io/data/ClasesdePython.pdf>`_


Autor
-----

Juan Fiol

Version
-------

IB - 2024


Licencia
--------

|Licencia Creative Commons|
Esta obra está bajo una `Licencia Creative Commons
Atribución-CompartirIgual 4.0
Internacional <http://creativecommons.org/licenses/by-sa/4.0/>`__.

.. |Licencia Creative Commons| image:: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
   :target: http://creativecommons.org/licenses/by-sa/4.0/


Bibliografía
------------


Accesible en línea
~~~~~~~~~~~~~~~~~~

-  La documentación oficial de Python (https://docs.python.org/3/)
-  El Tutorial de Python (https://docs.python.org/3/tutorial/), también
   en español (http://docs.python.org.ar/tutorial/3/)
-  Documentación de Numpy (http://docs.scipy.org/doc/numpy/user/)
-  Documentación de Scipy (https://docs.scipy.org/doc/scipy/reference/)
-  Documentación de Matplotlib (http://matplotlib.org), en particular la
   Galería (http://matplotlib.org/gallery.html)
-  Introduction to Python for Science
   (http://www.physics.nyu.edu/pine/pymanual/html/pymanMaster.html)
-  El curso de Python científico
   (https://github.com/mgaitan/curso-python-cientifico)
-  Las clases de Scipy Scipy Lectures (http://scipy-lectures.org)
-  Scipy Cookbook (http://scipy-cookbook.readthedocs.io/index.html)
-  Computational Statistics in Python
   (http://people.duke.edu/~ccc14/sta-663-2017/index.html)

Libros
~~~~~~

-  The Python Standard Library by Example
   (https://doughellmann.com/blog/the-python-3-standard-library-by-example/)
   de Doug Hellman, Addison-Wesley, 2017
-  Python Cookbook
   (https://www.amazon.com/Python-Cookbook-Third-David-Beazley/dp/1449340377)
   de David Beazley, Brian K. Jones, O'Reilly Pub., 2013.
-  Elegant Scipy
   (https://www.oreilly.com/library/view/elegant-scipy/9781491922927/)
   de Harriet Dashnow, Stéfan van der Walt, Juan Nunez-Iglesias,
   O'Reilly Pub., 2017.
-  Scientific Computing with Python 3
   (https://www.packtpub.com/big-data-and-business-intelligence/scientific-computing-python-3)
   de Claus Führer, Jan Erik Solem, Olivier Verdier, Packt Pub., 2016.
-  Interactive Applications Using Matplotlib
   (https://www.packtpub.com/application-development/interactive-applications-using-matplotlib)
   de Benjamin V Root, Packt Pub., 2015.
-  Mastering Python Regular Expressions
   (https://www.packtpub.com/application-development/mastering-python-regular-expressions)
   de Félix López, Víctor Romero, Packt Pub., 2014,


Otras referencias de interés
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Otras bibliotecas útiles:       
     - `Pandas <http://pandas.pydata.org/pandas-docs/stable/>`__
     - `Sympy <http://docs.sympy.org/latest/index.html>`__

- Información para usuarios de Matlab:

    - `Numpy para usuarios de Matlab <https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html>`__
    - `<http://mathesaurus.sourceforge.net/matlab-numpy.html>`__
    

*Blogs* y otras publicaciones
~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - `The Glowing Python <http://glowingpython.blogspot.com.ar/>`__
 - `Python for Signal Processing <http://python-for-signal-processing.blogspot.com.ar/>`__
 - `Ejercicios en Numpy <http://www.labri.fr/perso/nrougier/teaching/numpy.100/>`__
 - `Videos de Curso para Científicos e Ingenieros <https://www.youtube.com/playlist?list=PLoGFizEtm_6iheDXw2-8onKClyxgstBO1>`__ 


   




.. _prog-detalle:

Programa Detallado
==================

:Autor: Juan Fiol
:Version: Revision: 2023
:Copyright: Libre

  
Clase 1: Introducción al lenguaje
---------------------------------------------------

   * Cómo empezar: Instalación y uso

     * Instalación
     * Documentación y ayudas
     * Uso de Python: Interactivo o no
     * Notebooks de Jupyter

   * Comandos de Ipython

     * Comandos de Navegación
     * Algunos de los comandos mágicos
     * Comandos de Shell

   * Conceptos básicos de Python

     * Características generales del lenguaje
     * Tipos de variables

Clase 2: Tipos de datos y control 
----------------------------------------------------

   * Tipos simples: Números
   * Tipos compuestos
   * Strings: Secuencias de caracteres

     * Operaciones
     * Iteración y Métodos de Strings
     * Formato de strings

   * Conversión de tipos
   * Tipos contenedores: Listas

     * Operaciones sobre listas
     * Tuplas
     * Rangos
     * Comprensión de Listas

   * Módulos

     * Módulo math
     * Módulo ``cmath``
     * Adicionales

Clase 3: Tipos complejos y control de flujo
-------------------------------------------------------------

   * Diccionarios

     * Creación
     * Selección de elementos
     * Acceso a claves y valores
     * Modificación o adición de campos

   * Conjuntos

     * Operaciones entre conjuntos
     * Modificar conjuntos

   * Control de flujo

     * if/elif/else
     * Iteraciones

   * Técnicas de iteración

     * Iteración sobre conjuntos (*set*)
     * Iteración sobre elementos de dos listas
     * Iteraciones sobre diccionarios

Clase 4: Funciones
------------------------------------

   * Las funciones son objetos
   * Definición básica de funciones
   * Argumentos de las funciones

     * Ámbito de las variables en los argumentos
     * Funciones con argumentos opcionales
     * Tipos mutables en argumentos opcionales
     * Número variable de argumentos y argumentos *keywords*

   * Empacar y desempacar secuencias o diccionarios
   * Funciones que devuelven funciones
   * Funciones que toman como argumento una función
   * Aplicacion 1: Ordenamiento de listas
   * Funciones anónimas
   * Ejemplo 1: Integración numérica

     * Uso de funciones anónimas

   * Ejemplo 2: Polinomio interpolador

Clase 5: Entrada y salida, decoradores, y errores
-------------------------------------------------------------------

   * Funciones que aceptan y devuelven funciones (Decoradores)

     * Notación para decoradores
     * Algunos usos de decoradores

   * Atrapar y administrar errores

     * Administración de excepciones
     * “Crear” excepciones

   * Escritura y lectura a archivos

     * Ejemplos

   * Archivos comprimidos

Clase 6: Programación Orientada a Objetos 
------------------------------------------------------------

   * Breve introducción a Programación Orientada a Objetos
   * Clases y Objetos

     * Métodos especiales

   * Herencia
   * Atributos de clases y de instancias
   * Algunos métodos “especiales”

     * Método ``__del__()``
     * Métodos ``__str__`` y ``__repr__``
     * Método ``__call__``
     * Métodos ``__add__``, ``__mul__``

Clase 7: Control de versiones y biblioteca standard
---------------------------------------------------------------------

   * ¿Qué es y para qué sirve el control de versiones?

     * Cambios en paralelo
     * Historia completa

   * Instalación y uso: Una versión breve

     * Instalación
     * Interfaces gráficas
     * Documentación
     * Configuración básica
     * Creación de un nuevo repositorio
     * Clonación de un repositorio existente
     * Ver el estado actual
     * Creación de nuevos archivos y modificación de existentes
     * Actualización de un repositorio remoto
     * Puntos importantes

   * Algunos módulos (biblioteca standard) 

     * Módulo sys
     * Módulo ``os``
     * Módulo ``subprocess``
     * Módulo ``glob``
     * Módulo pathlib
     * Módulo ``Argparse``
     * Módulo ``re``

Clase 8: Introducción a Numpy 
------------------------------------------------

   * Algunos ejemplos

     * Graficación de datos de archivos
     * Comparación de listas y *arrays*
     * Generación de datos equiespaciados

   * Características de *arrays* en **Numpy**

     * Uso de memoria de listas y arrays
     * Velocidad de **Numpy**

   * Creación de *arrays* en **Numpy**

     * Creación de *Arrays* unidimensionales
     * Arrays multidimensionales
     * Otras formas de creación

   * Acceso a los elementos
   * Propiedades de **Numpy** arrays

     * Propiedades básicas
     * Otras propiedades y métodos de los *array*

   * Operaciones sobre arrays

     * Operaciones básicas
     * Comparaciones
     * Funciones definidas en **Numpy**
     * Lectura y escritura de datos a archivos

Clase 9: Visualización 
-----------------------------------------

   * Interactividad

     * Trabajo con ventanas emergentes
     * Trabajo sobre notebooks

   * Gráficos simples
   * Formato de las curvas

     * Líneas, símbolos y colores
     * Nombres de ejes y leyendas

   * Escalas y límites de graficación (vista)
   * Exportar las figuras
   * Dos gráficos en la misma figura
   * Personalizando el modo de visualización

     * Archivo de configuración
     * Hojas de estilo
     * Modificación de parámetros dentro de programas

Clase 10: Más información sobre **Numpy** 
------------------------------------------------------------

   * Creación y operación sobre **Numpy** arrays

     * Funciones para crear arrays
     * Funciones que actúan sobre arrays
     * Productos entre arrays y productos vectoriales
     * Comparaciones entre arrays

   * Atributos de *arrays*

     * reshape
     * transpose
     * min, max
     * argmin, argmax
     * sum, prod, mean, std
     * cumsum, cumprod, trapz
     * nonzero

   * Conveniencias con arrays

     * Convertir un array a unidimensional (ravel)
     * Enumerate para ``ndarrays``
     * Vectorización de funciones escalares

   * Copias de arrays y vistas
   * Indexado avanzado

     * Indexado con secuencias de índices
     * Índices de arrays multidimensionales
     * Indexado con condiciones
     * Función where

   * Extensión de las dimensiones (*Broadcasting*)
   * Unir (o concatenar) *arrays*

     * Apilamiento vertical
     * Apilamiento horizontal

   * Generación de números aleatorios

     * Distribución uniforme
     * Distribución normal (Gaussiana)
     * Histogramas
     * Distribución binomial

Clase 11: Introducción al paquete Scipy 
----------------------------------------------------------

   * Una mirada rápida a Scipy
   * Funciones especiales

     * Funciones de Bessel
     * Función Error
     * Evaluación de polinomios ortogonales
     * Factorial, permutaciones y combinaciones

   * Integración numérica

     * Ejemplo de función fuertemente oscilatoria
     * Funciones de más de una variable

   * Álgebra lineal

     * Productos y normas
     * Aplicación a la resolución de sistemas de ecuaciones
     * Descomposición de matrices
     * Autovalores y autovectores
     * Rutinas de resolución de ecuaciones lineales

   * Entrada y salida de datos

     * Entrada/salida con *Numpy*
     * Ejemplo de análisis de palabras
     * Entrada y salida en Scipy

Clase 12: Un poco de graficación 3D
-----------------------------------------------------

   * Gráficos y procesamiento sencillo en 2D

     * Histogramas en 2D
     * Gráficos de contornos
     * Superficies y contornos

Clase 13: Interpolación y ajuste de curvas (fiteo) 
---------------------------------------------------------------------

   * Interpolación

     * Interpolación con polinomios
     * Splines
     * B-Splines
     * Lines are guides to the eyes
     * Cantidades derivadas de *splines*

   * Interpolación en dos dimensiones
   * Interpolación sobre datos no estructurados
   * Fiteos de datos

     * Ajuste con polinomios

   * Fiteos con funciones arbitrarias

     * Ejemplo: Fiteo de picos

Clase 14: Animaciones e interactividad 
---------------------------------------------------------

   * Animaciones con **Matploblib**

     * Una animación simple en pocos pasos
     * Segundo ejemplo simple: Quiver
     * Tercer ejemplo

   * Trabajo simple con imágenes

     * Análisis de la imagen

   * Gráficos interactivos (“widgets”)

     * Cursor
     * Manejo de eventos
     * Ejemplos integrados

Clase 15: Interfaces con otros lenguajes
----------------------------------------------------------

   * Interface con lenguaje C

     * Ejemplo 1: Problema a resolver
     * Interfaces con C

   * Interface con lenguaje Fortran

     * Ejemplo 1: Problema a resolver
     * Interfaces con Fortran

Clase 16: Programación funcional con Python
-------------------------------------------------------------

   * Los errores al programar
   * Los errores en notebooks
   * Mutabilidad
   * Funciones

     * Funciones puras
     * Funciones de primer orden o primera clase
     * Funciones de orden superior

   * Inmutabilidad
   * No más loops


