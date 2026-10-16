---
ramo: "Estructuras de Datos"
tema: "Árboles B+"
tags:
  - edd
  - arbol-b-plus
  - indices
  - bases-de-datos
  - origen/complemento
prerrequisitos:
  - "[[03 - Árboles 2-3]]"
---

# Estructura de un árbol B+

Cuando los datos viven en **disco**, el costo que importa es cuántas veces se lee un bloque, no cuántas comparaciones se hacen en memoria. Un árbol binario necesita $\log_2 n$ lecturas. Un árbol con nodos que guardan **muchas llaves** (como un 2-3, pero con cientos de llaves) baja muy pocos niveles. El **árbol B+** es esa idea llevada a la práctica: *"B+-trees are by far the most important access path structure in databases and file systems"* (Gray y Reuter, 1993).

> [!tip] Definición: árbol B+ de orden $d$
> Es un árbol de búsqueda que almacena pares (llave, valor) y cumple:
> - Los **nodos internos** (directorio) solo guardan **llaves**, que sirven para navegar.
> - La **raíz** tiene entre 1 y $2d$ llaves.
> - Los **nodos internos** tienen entre $d$ y $2d$ llaves: siempre están **al menos a la mitad**.
> - Las **hojas** están todas **a la misma altura** y guardan a lo más $2d$ pares (llave, valor), ordenados por llave.
> - Las hojas están conectadas en una **lista doblemente ligada**.

## Directorio y datos

![Nodos directorio y nodos de datos](adjuntos/Nodos%20directorio%20y%20nodos%20de%20datos.png)

> [!example]- Transcripción de la imagen
> "Distinguimos entre nodos que solo permiten navegar (directorios) y aquellos que contienen los pares (datos)". Arriba, varios niveles de nodos directorio con punteros hacia abajo; abajo, la fila de nodos de datos (hojas), conectados entre sí con flechas dobles.

![Anatomía de un nodo directorio](adjuntos/Anatom%C3%ADa%20de%20un%20nodo%20directorio.png)

> [!example]- Transcripción de la imagen
> "Nodo directorio": $p_0, k_1, p_1, k_2, p_2, \dots, k_{2d}, p_{2d}$. Cada $p_i$ es un **puntero** a un hijo, cada $k_i$ es un **separador**, y un par $k_i\,p_i$ forma una **index entry**.

Un **índice** es un método de acceso que optimiza la búsqueda de datos para cierto tipo de consultas, como el índice alfabético de un libro o las secciones de un diario. En el directorio, cada separador $k_i$ indica si hay que bajar por la izquierda (llaves menores) o por la derecha (mayores o iguales).

![Árbol B+ de orden 2 con hojas ligadas](adjuntos/%C3%81rbol%20B%2B%20de%20orden%202%20con%20hojas%20ligadas.png)

> [!example]- Transcripción de la imagen
> Árbol B+ de orden $d = 2$. Raíz con la llave 17; hijos con 5 y 13, y con 20, 22 y 30. Hojas: 2* 3* | 5* 7* 8* | 14* 16* | 17* 18* | 20* 21* | 22* 27* 29* | 33* 34* 38* 39*, unidas con flechas dobles. "La lista ligada permite moverse desde un punto de interés". El asterisco indica que la hoja guarda la llave junto con su valor (o un puntero a él).

> [!warning] Lo que suele confundir
> - Una llave puede aparecer en el directorio y **no** estar en las hojas (por ejemplo, si se eliminó el dato), y casi todas las llaves de las hojas no aparecen en el directorio. El directorio solo **separa**.
> - Los nodos internos deben tener **entre $d$ y $2d$** llaves. Solo la raíz puede tener menos.
> - Para revisar si un árbol dibujado es B+ hay que comprobar la ocupación de cada nodo, que las hojas estén al mismo nivel y doblemente ligadas, y que los separadores estén bien ordenados respecto de sus hijos.

## Por qué funciona

- **Siempre balanceado:** como en el 2-3, crece solo desde la raíz, y todas las hojas quedan al mismo nivel.
- **Búsqueda en $O(\log_{2d} n)$** lecturas: con $d$ grande, la base del logaritmo es enorme. Con nodos de cientos de llaves, millones de datos caben en 3 o 4 niveles. Buscar dentro de un nodo cuesta $O(d)$ en memoria, que es despreciable frente a leer del disco.
- **Ocupación mínima del 50 %** (salvo la raíz): no se desperdicia espacio en disco.
- **Búsquedas por rango:** se baja una vez hasta la primera llave del rango y después se recorre la **lista de hojas**, sin volver a subir.

Este tema se ve desde el punto de vista de las bases de datos en [[11 - Índice árbol B+|Índice árbol B+ (Bases de Datos)]].

## Preguntas de repaso

> [!question]- ¿Qué guarda un nodo directorio y qué guarda una hoja en un árbol B+?
> El directorio guarda solo llaves separadoras y punteros a hijos, para navegar. Las hojas guardan los pares (llave, valor) ordenados y están ligadas entre sí.

> [!question]- ¿Para qué sirve que las hojas formen una lista doblemente ligada?
> Para responder consultas por rango. Se baja una vez a la primera llave del rango y después se recorren las hojas vecinas, sin volver a pasar por el directorio.

> [!question]- ¿Por qué un árbol B+ con $d$ grande es mejor para disco que un ABB balanceado?
> Porque su altura es $\log_{2d} n$ en vez de $\log_2 n$. Cada nivel es una lectura de disco, que es carísima, y con $d$ grande el árbol tiene muy pocos niveles.

> [!question]- ¿Puede una llave del directorio no estar en ninguna hoja?
> Sí. El directorio solo separa rangos; si se elimina el dato de una hoja, el separador puede seguir sirviendo para navegar.
