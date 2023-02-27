Control de versiones y biblioteca standard
==========================================

.. role:: strike
   :class: strike
	   
.. note::
  Esta clase está :strike:`copiada` (muy fuertemente) inspirada en las siguientes fuentes:
  
  * `Lecciones de Software Carpentry <http://swcarpentry.github.io/git-novice>`__, y la `versión en castellano <https://swcarpentry.github.io/git-novice-es/>`__).
  * El libro `Pro Git <https://git-scm.com/book/en/v2>`__ de Scott Chacon y Ben Straub, y la `versión en castellano <https://git-scm.com/book/es/>`__. Ambos disponibles libremente.
  * El libro `Mastering git <http://www.packtpub.com/>`__ escrito por Jakub Narębski.


¿Qué es y para qué sirve el control de versiones?
-------------------------------------------------

El control de versiones permite ir grabando puntos en la historia de la evolución de un proyecto. Esta capacidad nos permite:

  - Acceder a versiones anteriores de nuestro trabajo ("undo ilimitado")
  - Trabajar en forma paralela con otras personas sobre un mismo documento.

Habitualmente, nos podemos encontrar con situaciones como esta:

.. figure:: figuras/alternativa.png
   :alt: 


o, más gracioso pero igualmente común, esta otra:

.. figure:: figuras/phd101212s.png
   :alt: “Piled Higher and Deeper” por Jorge Cham, http://www.phdcomics.com

Todos hemos estado en esta situación alguna vez: parece ridículo tener varias versiones casi idénticas del mismo documento. Algunos procesadores de texto nos permiten lidiar con esto un poco mejor, como por ejemplo el `Track Changes de Microsoft Word <https://support.office.com/en-us/article/Track-changes-in-Word-197ba630-0f5f-4a8e-9a77-3712475e806a>`__, el `historial de versiones de Google <https://support.google.com/docs/answer/190843?hl=en>`__, o el `Track-changes de LibreOffice <https://help.libreoffice.org/Common/Recording_and_Displaying_Changes>`__.

Estas herramientas permiten solucionar el problema del trabajo en colaboración. Si tenemos una versión de un archivo (documento, programa, etc) podemos compartirlo con los otros autores para modificar, y luego ir aceptando o rechazando los cambios propuestos.

Algunos problemas aún aparecen cuando se trabaja intensivamente en un documento, porque al aceptar o rechazar los cambios no queda registro de cuáles eran las alternativas. Además, estos sistemas actúan sólo sobre los documentos; en nuestro caso puede haber datos, gráficos, etc que cambien (o que queremos estar seguros que no cambiaron y estamos usando la versión correcta).



En el fondo, la manera de evitar esto es manteniendo una buena organización. Una posible buena manera es designar una persona responsable, que vaya llevando la contabilidad de quién hizo qué correcciones, las integre en un único documento, y vaya guardando copias de todas los documentos que recibe en un lugar separado. Cuando hay varios autores (cuatro o cinco) éste es un trabajo bastante arduo y con buenas posibilidades de pequeños errores. Los sistemas de control de versiones tratan de automatizar la mayor parte del trabajo para hacer más fácil la colaboración, manteniendo registro de los cambios que se hicieron desde que se inició el documento, y produciendo poca interferencia, permitiendo al mismo tiempo trabajar de manera similar a como lo hacemos habitualmente.

Consideremos un proyecto con varios archivos y autores.
En este esquema de trabajo, podemos compartir una versión de todos los archivos del proyecto

Cambios en paralelo
~~~~~~~~~~~~~~~~~~~

Una de las ventajas de los sistemas de control de versiones es que cada autor hace su aporte en su propia copia (en paralelo) 

.. figure:: figuras/versions.png
   :alt: versiones corregidas en paralelo

y después estos son compatibilizados e incorporados en un único documento.

.. figure:: figuras/merge.png
   :alt: Compaginando versiones corregidas en paralelo

En casos en que los autores trabajen en zonas distintas la compaginación se puede hacer en forma automática. Por otro lado, si dos personas cambian la misma frase obviamente se necesita tomar una decisión y la compaginación no puede (ni quiere) hacerse automáticamente.

Historia completa
~~~~~~~~~~~~~~~~~

Otra característica importante de los sistemas de control de versiones es que guardan la historia completa de todos los archivos que componen el proyecto. Imaginen, por ejemplo, que escribieron una función para resolver parte de un problema. La función no sólo hace su trabajo sino que está muy bien escrita, es elegante y funciona rápidamente. Unos días después encuentran que toda esa belleza era innecesaria, porque el problema que resuelve la función no aparece en su proyecto, y por supuesto la borra. La version oficial no tiene esa parte del código. 

Dos semanas, y varias líneas de código, después aparece un problema parecido y querríamos tener la función que borramos ...

Los sistemas de control de versiones guardan toda la información de la historia de cada archivo, con un comentario del autor. Este modo de trabajar nos permite recuperar (casi) toda la información previa, incluso aquella que en algún momento decidimos descartar.


Instalación y uso: Una versión breve
------------------------------------

Instalación
~~~~~~~~~~~

Vamos a describir uno de los posibles sistemas de control de versiones, llamado *git*

En Linux, usando el administrador de programas, algo así como:

en Ubuntu::

  $ sudo apt-get install git

o usando `dnf` en Fedora::

  $ sudo dnf install git
  
En Windows, se puede descargar `Git for Windows <https://gitforwindows.org/>`__ desde `este enlace <https://github.com/git-for-windows/git/releases/latest>`__,  ejecutar el instalador 
y seguir las instrucciones. Viene con una terminal y una interfaz gráfica.


Interfaces gráficas
~~~~~~~~~~~~~~~~~~~


Existen muchas interfaces gráficas, para todos los sistemas operativos.

Ver por ejemplo `Git Extensions <https://gitextensions.github.io/>`__,  `git-cola <https://git-cola.github.io/>`__, `Code Review <https://github.com/FabriceSalvaire/CodeReview/>`__,  o cualquiera de esta larga lista de `interfaces gráficas a Git <https://git-scm.com/downloads/guis>`__.

Documentación
~~~~~~~~~~~~~

Buscando en internet el término `git` se encuentra mucha documentación. En particular el libro Pro Git tiene información muy accesible y completa.

El programa se usa en la forma:

.. code-block:: shell
		
  $ git <comando> [opciones]

Por ejemplo, para obtener ayuda directamente desde el programa, se puede utilizar cualquiera de las opciones:

.. code-block:: bash
		
  $ git help
  $ git --help

que nos da información sobre su uso, y cuáles son los comandos disponibles.
Si queremos obtener información sobre un comando en particular, agregamos el comando de interés. Para el comando de configuración sería:

.. code-block:: bash
		
  $ git config --help
  $ git help config

  

Configuración básica
~~~~~~~~~~~~~~~~~~~~

Una vez que está instalado, es conveniente configurarlo desde una terminal, con los comandos:

.. code-block:: bash

  $ git config --global user.name "Juan Fiol"
  $ git config --global user.email "fiol@cab.cnea.gov.ar"		

Si necesitamos usar un proxy para acceder fuera del lugar de trabajo:

.. code-block:: bash

  $ git config --global http.proxy proxy-url
  $ git config --global https.proxy proxy-url


Acá hemos usado la opción `--global` para que las variables configuradas se apliquen a todos los repositorios con los que trabajamos.

Si necesitamos desabilitar una variable, por ejemplo el proxy, podemos hacer:

.. code-block:: bash

  $ git config --global unset http.proxy
  $ git config --global unset https.proxy 



Creación de un nuevo repositorio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Si ya estamos trabajando en un proyecto, tenemos algunos archivos de trabajo, sin control de versiones, y queremos empezar a controlarlo, inicializamos el repositorio local con:

.. code-block:: bash

  $ git init

Este comando sólo inicializa el repositorio, no pone ningún archivo bajo control de versiones.


Clonación de un repositorio existente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Otra situación bastante común ocurre cuando queremos tener una copia local de un proyecto (grupo de archivos) que ya existe y está siendo controlado por git. En este caso utilizamos el comando `clone` en la forma:

.. code-block:: bash

  $ git clone <url-del-repositorio> [nombre-local]

donde el argumento `nombre-local` es opcional, si queremos darle a nuestra copia un nombre diferente al que tiene en el repositorio

Ejemplos:

.. code-block:: bash

  $ git clone /home/fiol/my-path/programa
  $ git clone /home/fiol/my-path/programa programa-de-calculo 
  $ git clone https://github.com/fiolj/intro-python-IB.git
  $ git clone https://github.com/fiolj/intro-python-IB.git clase-ib

Los dos primeros ejemplos realizan una copia de trabajo de un proyecto alojado también localmente. En el segundo y cuarto casos les estamos dando un nuevo nombre a la copia local de trabajo.

En los últimos tres ejemplos estamos copiando proyectos alojados en repositorios remotos, cuyo uso es bastante popular: 
`bitbucket <https://bitbucket.org/>`__, `gitlab <https://gitlab.com/>`__, y `github <https://github.com>`__.

Lo que estamos haciendo con estos comandos es copiar no sólo la versión actual del proyecto sino toda su historia. 
Después de ejecutar este comando tendremos en nuestra computadora cada versión de cada uno de los archivos del proyecto, con la información de quién hizo los cambios y cuándo se hicieron.


Una vez que ya tenemos una copia local de un proyecto vamos a querer trabajar: modificar los archivos, agregar nuevos, borrar alguno, etc.


Ver el estado actual
~~~~~~~~~~~~~~~~~~~~

Para determinar qué archivos se cambiaron utilizamos el comando `status`:

.. code-block:: bash
		
  $ cd my-directorio
  $ git status

Creación de nuevos archivos y modificación de existentes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Después de trabajar en un archivo existente, o crear un nuevo archivo que queremos controlar, debemos agregarlo al registro de control:

.. code-block:: bash

  $ git add <nuevo-archivo>
  $ git add <archivo-modificado>

Esto sólo agrega la versión actual del archivo al listado a controlar. Para incluir una copia en la base de datos del repositorio debemos realizar lo que se llama un "commit"

.. code-block:: bash

  $ git commit -m "Mensaje para recordar que hice con estos archivos"

La opción `-m` y su argumento (el *string* entre comillas) es un mensaje que dejamos grabado, asociado a los cambios realizados. Puede realizarse el `commit` sin esta opción, y entonces `git` abrirá un editor de texto para que escribamos el mensaje (que no puede estar vacío).

Actualización de un repositorio remoto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una vez que se añaden o modifican los archivos, y se agregan al repositorio local, podemos enviar los cambios a un repositorio remoto. Para ello utilizamos el comando:

.. code-block:: bash

  $ git push

De la misma manera, si queremos obtener una actualización del repositorio remoto (poque alguien más la modificó), utilizamos el (los) comando(s):

.. code-block:: bash

  $ git fetch

Este comando sólo actualiza el repositorio, pero no modifica los archivos locales. Esto se puede hacer, cuando uno quiera, luego con el comando:

.. code-block:: bash

  $ git merge

Estos dos comandos, pueden generalmente reemplazarse por un único comando:

.. code-block:: bash

  $ git pull

que realizará la descarga desde el repositorio remoto y la actualización de los archivos locales en un sólo paso.



Puntos importantes
~~~~~~~~~~~~~~~~~~

+--------------------------+---------------------------------------------+
| Control de versiones     | Historia de cambios y "undo" ilimitado      |
+--------------------------+---------------------------------------------+
| Configuración            | `git config`, con la opción `–global`       |
+--------------------------+---------------------------------------------+
| Creación                 | `git init` inicializa el repositorio        |
+--------------------------+---------------------------------------------+
|                          | `git clone` copia un repositorio            |
+--------------------------+---------------------------------------------+
| Modificación             | `git status` muestra el estado actual       |
+--------------------------+---------------------------------------------+
|                          | `git add` pone archivos bajo control        |
+--------------------------+---------------------------------------------+
|                          | `git commit` graba la versión actual        |
+--------------------------+---------------------------------------------+
| Explorar las versiones   | `git log` muestra la historia de cambios    |
+--------------------------+---------------------------------------------+
|                          | `git diff` compara versiones                |
+--------------------------+---------------------------------------------+
|                          | `git checkout` recupera versiones previas   |
+--------------------------+---------------------------------------------+
| Comunicación con remotos | `git push` Envía los cambios al remoto      |
+--------------------------+---------------------------------------------+
|                          | `git pull` copia los cambios desde remoto   |
+--------------------------+---------------------------------------------+
