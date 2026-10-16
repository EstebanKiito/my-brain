---
ramo: "Estructuras de Datos"
tema: "Tablas de hash"
tags:
  - edd
  - hash
  - diccionarios
  - origen/complemento
prerrequisitos:
  - "[[01 - Diccionarios y árboles binarios de búsqueda]]"
  - "[[01 - Arreglos frente a listas ligadas]]"
---

# Función de hash y tablas de hash

Los [[01 - Diccionarios y árboles binarios de búsqueda|árboles de búsqueda]] implementan diccionarios en $O(\log n)$ y, de regalo, mantienen las llaves **ordenadas**. Pero muchos problemas no necesitan orden: solo guardar, encontrar y borrar. Si se **sacrifica el orden**, se puede llegar a $O(1)$ en promedio.

## La idea: usar la llave como índice

![Arreglo indexado directamente por la llave](adjuntos/Arreglo%20indexado%20directamente%20por%20la%20llave.png)

> [!example]- Transcripción de la imagen
> Arreglo $A[0 \dots 11]$ donde la celda $k$ guarda un puntero a la información asociada a la llave $k$: las celdas 2, 5, 7 y 11 tienen punteros ("Info asociada a k = 2", "= 5", "= 7", "= 11"), y las demás tienen $\varnothing$.

Si la llave fuera directamente un índice del arreglo, insertar, buscar y eliminar serían $O(1)$: basta con ir a la celda. El problema es el **rango**. Un RUT va de 0 a unos 25 millones, y no tiene sentido un arreglo de ese tamaño para 7000 alumnos.

## Función de hash

![Definición de tabla de hash](adjuntos/Definici%C3%B3n%20de%20tabla%20de%20hash.png)

> [!example]- Transcripción de la imagen
> "Definición": dado $m > 0$ y un conjunto de llaves $K$, una **tabla de hash** $A$ es una EDD que asocia valores a llaves indexadas usando una función de hash $h: K \to \{0, \dots, m-1\}$. Se dice que $A$ es de tamaño $m$. En el dibujo, la llave $k$ pasa por $h(k)$ y llega a la celda 1, que apunta a "Info asociada a llave $k$ con $h(k) = 1$"; otra llave $k'$ llega a la celda $m-2$.

La **función de hash** transforma una llave de un espacio enorme en una posición de un arreglo pequeño. Si las llaves no son números (strings, por ejemplo), primero se convierten a números.

La más simple es el **hashing modular**: $h(k) = k \bmod m$. Como el dominio de llaves es mucho más grande que $m$, la función **no puede ser inyectiva**: habrá llaves distintas con el mismo hash, es decir, **colisiones**.

![Colisiones del hashing modular](adjuntos/Colisiones%20del%20hashing%20modular.png)

> [!example]- Transcripción de la imagen
> "Ejemplo": con $m = 100$ y $K = \{0, \dots, 999\}$, el hashing modular cumple $h(12) = h(112) = \dots = h(912) = 12$ y $h(18) = \dots = h(918) = 18$.

> [!tip] Una buena función de hash
> Reparte las llaves de forma **homogénea** entre las $m$ celdas. Con $h(k) = k \bmod m$ conviene que $m$ sea **primo** (y no cercano a una potencia de 2), porque si muchas llaves comparten un patrón (por ejemplo, todas múltiplos de 10), un $m$ compuesto las amontona en pocas celdas.

| | Árbol balanceado | Tabla de hash |
|---|---|---|
| Buscar, insertar, eliminar | $O(\log n)$ garantizado | $O(1)$ **en promedio** |
| Recorrer en orden | Sí, in-order en $O(n)$ | No: el hash destruye el orden |
| Peor caso | $O(\log n)$ | $O(n)$, si todo colisiona |

> [!warning] Si el problema pide orden, no es hash
> Listar las llaves ordenadas, buscar el sucesor o consultar un rango requieren un árbol. La tabla de hash solo responde "¿está la llave $k$?" y "¿qué valor tiene?".

Las tablas de hash también se usan como índices de bases de datos: ver [[08 - Tablas de hash|Tablas de hash (Bases de Datos)]].

## Preguntas de repaso

> [!question]- ¿Qué se sacrifica al usar una tabla de hash en vez de un árbol de búsqueda, y qué se gana?
> Se sacrifica el orden de las llaves (no se pueden listar ordenadas ni consultar rangos) y se gana acceso en $O(1)$ promedio, en vez de $O(\log n)$.

> [!question]- ¿Por qué las colisiones son inevitables?
> Porque la función de hash lleva un dominio de llaves mucho más grande que $m$ a solo $m$ posiciones, así que no puede ser inyectiva. Por el principio del palomar, alguna celda recibe más de una llave.

> [!question]- ¿Por qué se recomienda que $m$ sea primo con hashing modular?
> Porque un primo no comparte factores con los patrones típicos de las llaves (múltiplos de 10, de 2, etc.), y eso reparte mejor los restos entre todas las celdas.

> [!question]- Con $m = 7$, ¿en qué celdas quedan 15 y 16?
> $15 \bmod 7 = 1$ y $16 \bmod 7 = 2$: en las celdas 1 y 2.
