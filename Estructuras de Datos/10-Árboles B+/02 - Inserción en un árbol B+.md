---
ramo: "Estructuras de Datos"
tema: "Árboles B+"
tags:
  - edd
  - arbol-b-plus
  - insercion
  - split
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructura de un árbol B+]]"
---

# Inserción en un árbol B+

Insertar en un árbol B+ es la misma idea que en un [[03 - Árboles 2-3|árbol 2-3]]: se inserta en una hoja y, si esta se desborda, se hace **split** y se sube un separador. La diferencia es que los nodos aceptan hasta $2d$ llaves y que las hojas además se mantienen ligadas. Se asume que las llaves son únicas.

```
Insertar(k):
    P <- BusquedaEnArbol(k, raiz)          // hoja donde debería ir k
    if |P| < 2d:
        insertar k en P (en su posición ordenada)
    else:
        insertar k en P y hacer SPLIT de [P + k]   // ahora tiene 2d + 1 llaves
```

## Split

![Algoritmo de split](adjuntos/Algoritmo%20de%20split.png)

> [!example]- Transcripción de la imagen
> Para hacer **split** del nodo $[P + k]$ de tamaño $2d + 1$: 1. asumir $[P + k] = k_1^* k_2^* \dots k_{2d}^* k_{2d+1}^*$ con $k_i < k_{i+1}$; 2. **dividir** $[P + k]$ en $P_1 = k_1^* \dots k_d^*$ y $P_2 = k_{d+1}^* \dots k_{2d+1}^*$, y reemplazar $P$ por $P_1, P_2$ en la lista doblemente ligada de los datos; 3. seleccionar $k_{d+1}$ como **divisor** de $P_1$ y $P_2$; 4. reemplazar el puntero $p$ en el nodo $P'$ que apuntaba a $P$ por $p_1\, k_{d+1}\, p_2$, donde $p_1$ apunta a $P_1$ y $p_2$ a $P_2$; 5. iterar sobre el nodo directorio $P'$ (split de $P'$).

> [!tip] Split de hoja frente a split de directorio
> En una **hoja**, el divisor $k_{d+1}$ se **copia** hacia arriba y también se queda en $P_2$, porque los datos solo viven en las hojas. En un nodo **directorio**, la llave del medio **sube** y desaparece del nodo, igual que en un 2-3.

## Ejemplo: insertar 8 con $d = 2$ (máximo 4 llaves por nodo)

![Inserción de 8 - árbol inicial](adjuntos/Inserci%C3%B3n%20de%208%20-%20%C3%A1rbol%20inicial.png)

> [!example]- Transcripción de la imagen
> Raíz (directorio) 13, 17, 24, 30. Hojas: 2* 3* 5* 7* | 14* 16* | 19* 20* 22* | 24* 27* 29* | 33* 34* 38* 39*.

El 8 va a la primera hoja, que ya tiene 4 llaves: queda 2, 3, 5, 7, 8 y hay que hacer split.

![Inserción de 8 - split de la hoja](adjuntos/Inserci%C3%B3n%20de%208%20-%20split%20de%20la%20hoja.png)

> [!example]- Transcripción de la imagen
> La hoja se divide en 2* 3* y 5* 7* 8* (ambas resaltadas), que siguen ligadas al resto.

![Inserción de 8 - el directorio se desborda](adjuntos/Inserci%C3%B3n%20de%208%20-%20el%20directorio%20se%20desborda.png)

> [!example]- Transcripción de la imagen
> El divisor 5 se copia a la raíz, que queda 5, 13, 17, 24, 30 (cinco llaves, resaltada): se desbordó.

![Inserción de 8 - 17 sube como divisor](adjuntos/Inserci%C3%B3n%20de%208%20-%2017%20sube%20como%20divisor.png)

> [!example]- Transcripción de la imagen
> En el directorio desbordado se elige la llave del medio, 17 (resaltada), para subir.

![Inserción de 8 - árbol resultante](adjuntos/Inserci%C3%B3n%20de%208%20-%20%C3%A1rbol%20resultante.png)

> [!example]- Transcripción de la imagen
> Árbol final: raíz 17; directorios 5, 13 (a la izquierda) y 24, 30 (a la derecha); hojas 2* 3* | 5* 7* 8* | 14* 16* | 19* 20* 22* | 24* 27* 29* | 33* 34* 38* 39*. El árbol creció un nivel.

La **altura solo crece cuando se llena la raíz**, y entonces todo el árbol baja un nivel a la vez. Por eso la raíz es el único nodo al que se le permite estar a menos del 50 %.

> [!example] Optimización: redistribuir antes de partir
> Si una hoja se llena pero un **hermano** tiene espacio, se puede pasar una llave al hermano y ajustar el separador del padre en vez de hacer split. Se ahorran splits en cascada y el árbol queda más lleno.

## Preguntas de repaso

> [!question]- ¿Cuándo hay que hacer split al insertar en un árbol B+ de orden $d$?
> Cuando la hoja donde corresponde la llave ya tiene $2d$ llaves: al insertar queda con $2d + 1$ y se divide en dos nodos de $d$ y $d + 1$ llaves.

> [!question]- ¿Por qué en el split de una hoja el divisor se copia y no se mueve?
> Porque las hojas son las únicas que guardan los datos. La llave $k_{d+1}$ tiene que seguir en la hoja $P_2$ con su valor; al directorio solo sube una copia que sirve de separador.

> [!question]- En el ejemplo de insertar 8, ¿por qué sube 17 a una raíz nueva?
> Porque al copiar 5 al directorio, este quedó con 5 llaves (más de $2d = 4$). Se hizo split del directorio: la llave del medio, 17, subió y formó la nueva raíz.

> [!question]- ¿Cuándo aumenta la altura de un árbol B+?
> Solo cuando la raíz se desborda y hace split. Es la única forma de agregar un nivel, y por eso todas las hojas siguen a la misma profundidad.
