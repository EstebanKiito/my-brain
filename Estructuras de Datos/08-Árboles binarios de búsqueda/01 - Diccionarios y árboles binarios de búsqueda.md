---
ramo: "Estructuras de Datos"
tema: "Árboles binarios de búsqueda"
tags:
  - edd
  - diccionarios
  - abb
  - arbol-binario
  - origen/complemento
prerrequisitos:
  - "[[02 - Heap binario y su representación en arreglo]]"
  - "[[04 - Búsqueda binaria y dividir para conquistar]]"
---

# Diccionarios y árboles binarios de búsqueda

Un **diccionario** asocia **llaves** con **valores**. Por ejemplo, a cada RUT, que es único, se le asocian un nombre, una edad y un número de alumno. Debe permitir saber de forma **eficiente** si una llave está o no, obtener y actualizar su valor y, en algunos casos, eliminar el par. Se asume que las llaves son **únicas**.

## Por qué no alcanzan arreglos, listas ni heaps

| Estructura | Buscar una llave | Insertar |
|---|---|---|
| Lista ligada | $O(n)$ | $O(1)$ |
| Arreglo ordenado | $O(\log n)$ (búsqueda binaria) | $O(n)$ (correr datos) |
| [[02 - Heap binario y su representación en arreglo\|Heap]] | $O(n)$: solo conoce el máximo | $O(\log n)$ |
| **ABB balanceado** | $O(\log n)$ | $O(\log n)$ |

El **árbol binario de búsqueda** (ABB) combina lo mejor de ambos mundos. Lleva la **búsqueda binaria montada en la estructura**: es dividir para conquistar sobre los datos. Gasta algo de trabajo al insertar (mantener el orden) para que buscar sea logarítmico.

> [!tip] Propiedad de ABB
> Para todo nodo $x$: todas las llaves de su subárbol **izquierdo** son **menores** que `x.key`, y todas las de su subárbol **derecho** son **mayores**. A diferencia del heap, aquí sí hay orden entre los hijos: izquierda < padre < derecha.

## Anatomía

![Atributos de un nodo de ABB](adjuntos/Atributos%20de%20un%20nodo%20de%20ABB.png)

> [!example]- Transcripción de la imagen
> Atributos de un nodo $x$ en un ABB: `x.key` es la llave; `x.value`, su valor; `x.left`, el puntero a su hijo izquierdo; `x.right`, el puntero a su hijo derecho; `x.p`, el puntero al padre. "En general no incluiremos `x.value` en los algoritmos. Solo será un espacio de almacenamiento".

El puntero al **padre** no es imprescindible, pero facilita insertar y eliminar, y es una buena práctica de implementación.

![Anatomía de un árbol binario](adjuntos/Anatom%C3%ADa%20de%20un%20%C3%A1rbol%20binario%20-%20ra%C3%ADz%2C%20niveles%20y%20altura.png)

> [!example]- Transcripción de la imagen
> Árbol con raíz M en el nivel 0; I y T en el nivel 1; D, K, Q y Z en el nivel 2; A y G (hijos de D) en el nivel 3. Una llave al costado indica "Altura = 4": aquí la altura se cuenta como número de niveles.

## La forma depende del orden de llegada

![Dos árboles binarios de 6 nodos](adjuntos/Dos%20%C3%A1rboles%20binarios%20de%206%20nodos.png)

> [!example]- Transcripción de la imagen
> "Dos ejemplos de árboles binarios con 6 nodos": uno ancho y bajo (3 niveles) y otro alargado hacia la derecha (4 niveles). No todos los nodos tienen la misma cantidad de hijos.

Las operaciones cuestan $O(h)$, con $h$ la **altura**. Un árbol bien balanceado tiene $h \approx \log_2 n$, como un heap. Pero si los datos llegan **ordenados**, cada nodo nuevo cuelga del anterior hacia el mismo lado y el ABB degenera en una **lista**: $h = n$ y las operaciones pasan a ser $O(n)$. Insertar 1, 2, …, 7 en ese orden da altura 7, y en un orden mezclado, como 6, 3, 8, 1, 5, 7, 9, da altura 3.

> [!warning] Promedio frente a peor caso
> En promedio (llaves que llegan al azar), un ABB tiene altura $O(\log n)$. En el peor caso, $O(n)$. Para **garantizar** $O(\log n)$ hacen falta árboles que se rebalancean: AVL, 2-3 o rojo-negro.

Si al diccionario no le interesa el **orden** de las llaves (por ejemplo, listar todo ordenado), se puede renunciar al árbol y ganar velocidad con una **tabla de hash**.

## Preguntas de repaso

> [!question]- ¿Qué operaciones debe soportar un diccionario?
> Asociar un valor a una llave, actualizar el valor de una llave, obtener el valor asociado a una llave y, en algunos casos, eliminar un par llave-valor.

> [!question]- ¿En qué se diferencia la propiedad de ABB de la propiedad de heap?
> El heap solo exige que el padre sea mayor que sus hijos, sin orden entre hermanos. El ABB exige que todo el subárbol izquierdo sea menor y todo el derecho mayor, lo que permite buscar cualquier llave descartando un lado.

> [!question]- ¿Qué secuencia de inserciones produce el peor caso de un ABB y cuánto cuesta buscar ahí?
> Insertar llaves ya ordenadas, crecientes o decrecientes: cada una queda como hijo del anterior y el árbol es una lista. Buscar cuesta $O(n)$.

> [!question]- ¿Por qué todas las operaciones de un ABB cuestan $O(h)$?
> Porque todas parten con una búsqueda que baja un nivel por comparación desde la raíz, como máximo hasta la hoja más profunda.
