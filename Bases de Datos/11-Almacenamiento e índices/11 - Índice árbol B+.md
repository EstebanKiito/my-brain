---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/indices, origen/complemento]
prerrequisitos: ["[[09 - Índices en bases de datos|Índices en bases de datos]]"]
---
# Índice árbol B+

El árbol B+ es el índice más usado: un árbol balanceado cuyos nodos son páginas, con los datos en las hojas y las hojas **encadenadas en orden**. Busca en tiempo logarítmico y sirve tanto para igualdades como para **rangos**.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 9: Almacenamiento y Índices")
> *"B+ Trees are by far the most important access path structure in database and file systems"* (Gray y Reuter, 1993).
> - Las **páginas del disco** son los nodos del árbol.
> - Las tuplas están en las **hojas**.
> - Tiempo de búsqueda **logarítmico**.
> - Se comporta bien en **consultas de rango**.
> - Es el índice que usa Postgres (y en general todos los sistemas) sobre las llaves primarias.
>
> **Nodo del directorio:** una secuencia `p0, k1, p1, k2, p2, …, k2d, p2d`, con *separadores* (search keys) y *punteros*. Cada separador tiene un puntero antes y otro después: a la izquierda de $k_i$ van los valores menores y a la derecha, los mayores o iguales.

**Búsqueda por valor** (aid = 21): desde la raíz, se sigue en cada nodo el puntero del intervalo que contiene a 21.

> [!tip] Complemento (slides "Clase 9")
> ![Slide - B+ tree búsqueda de aid 21](adjuntos/Slide%20-%20B+%20tree%20búsqueda%20de%20aid%2021.png)
>
> ![Slide - B+ tree consulta de rango](adjuntos/Slide%20-%20B+%20tree%20consulta%20de%20rango.png)

> [!note]- Transcripción de las imágenes
> Raíz [17]. Hijo izquierdo [5, 13] con hojas 2* 3* | 5* 7* 8* | 14* 16*. Hijo derecho [20, 22, 30] con hojas 17* 18* | 20* 21* | 22* 27* 29* | 33* 34* 38* 39*. Las hojas están enlazadas entre sí (↔).
> - **aid = 21:** 21 ≥ 17 → derecha. En [20, 22, 30], 20 ≤ 21 < 22 → hoja 20* 21*.
> - **Rango 5 ≤ aid ≤ 26:** se baja hasta la hoja de 5 (**costo O(h)**, h = altura del árbol) y se avanza por las hojas encadenadas 5* 7* 8* → 14* 16* → 17* 18* → 20* 21* → 22* 27* (**costo O(B_m)**, $B_m$ = n.º de bloques con records que calzan con la búsqueda).

> [!tip] Complemento — costos (slides "Clase 9")
> - Búsqueda por valor: costo $\sim \log(|R|)$. Si B es el tamaño de una página en tuplas, el costo es $O(\log_B(\lceil |R|/B \rceil))$, es decir, la **altura h** del árbol.
> - Consulta de rango: $h + B_m$.
> - "¿Qué pasa si el índice lo mantenemos en memoria RAM?" Los nodos internos son pocos y suelen caber en el buffer, así que en la práctica solo se pagan las hojas. Con fanout alto (cientos de punteros por página), un árbol de altura 3 o 4 indexa miles de millones de tuplas.
> - **Ocupación:** para facilitar la inserción de datos nuevos, los B+ trees **no tienen nodos completamente llenos**. Se dice que las hojas están ocupadas a un porcentaje; por ejemplo, 60%: donde caben 100 tuplas, hay 60.
> - Al insertar en una hoja llena, esta se **divide** en dos y el separador sube al padre. Así el árbol se mantiene **balanceado**: todas las hojas a la misma profundidad.

## Preguntas de repaso

1. ¿Dónde están los datos en un árbol B+ y qué contienen los nodos internos?
> [!question]- Respuesta
> Los datos están en las hojas. Los nodos internos (directorio) tienen separadores (search keys) y punteros a los hijos.

2. ¿Por qué un árbol B+ sirve para consultas de rango y un hash no?
> [!question]- Respuesta
> Porque las hojas están ordenadas y encadenadas: se encuentra el inicio del rango y se recorren las hojas siguientes. El hash no preserva el orden.

3. ¿Cuál es el costo de una consulta de rango con un árbol B+?
> [!question]- Respuesta
> La altura h, para bajar hasta el inicio del rango, más $B_m$, el número de bloques de hojas con resultados.

4. ¿Por qué las hojas no se llenan al 100%?
> [!question]- Respuesta
> Para dejar espacio a inserciones futuras sin tener que dividir nodos tan seguido.
