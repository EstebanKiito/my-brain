---
ramo: "Estructuras de Datos"
tema: "Tablas de hash"
tags:
  - edd
  - hash
  - colisiones
  - encadenamiento
  - sondeo
  - origen/complemento
prerrequisitos:
  - "[[01 - Función de hash y tablas de hash]]"
  - "[[02 - Implementación de una lista ligada en C]]"
---

# Resolución de colisiones

Dos llaves con el mismo hash no pueden ocupar la misma celda. Hay dos familias de soluciones: guardar las llaves que colisionan **fuera** de la tabla, en listas (**encadenamiento**), o buscarles **otra celda dentro** de la misma tabla (**direccionamiento abierto**, también llamado sondeo).

## Encadenamiento

Cada celda guarda una **lista ligada** con todas las llaves que caen ahí. Insertar se hace en la **cabeza** de la lista, en $O(1)$.

```
ChainedHashSearch(A, k):     buscar la llave k en la lista A[h(k)]
ChainedHashInsert(A, k, v):  insertar (k, v) como cabeza de A[h(k)]
ChainedHashDelete(A, k):     eliminar la llave k de A[h(k)]
```

![Encadenamiento - inserción de 58 como cabeza](adjuntos/Encadenamiento%20-%20inserci%C3%B3n%20de%2058%20como%20cabeza.png)

> [!example]- Transcripción de la imagen
> Tabla de $m = 7$ con encadenamiento: la celda 1 tiene la lista 29 → 15 y la celda 2 la lista 51 → 37. Al insertar 58 ($58 \bmod 7 = 2$), se calcula la celda 2 (resaltada) y el 58 queda como cabeza: 58 → 51 → 37.

```python
class HashEncadenado:
    def __init__(self, m=7):
        self.m, self.A = m, [[] for _ in range(m)]
    def insert(self, k, v=None):
        lista = self.A[k % self.m]
        for i, (kk, _) in enumerate(lista):
            if kk == k: lista[i] = (k, v); return   # ya estaba: actualiza
        lista.insert(0, (k, v))                    # como cabeza
    def search(self, k):
        return next((v for kk, v in self.A[k % self.m] if kk == k), None)
# insertando 15, 37, 29, 51 y luego 58 con m = 7: celda 1 = [29, 15], celda 2 = [58, 51, 37]
```

El costo de buscar y eliminar depende del **largo de las listas**. Con una función de hash que reparte bien, son cortas y todo es $O(1)$ en promedio. Si todas las llaves cayeran en la misma celda, sería una sola lista y buscar costaría $O(n)$.

## Direccionamiento abierto: sondeo

Sirve cuando **no se puede usar memoria extra**: todo vive en la misma tabla. Si la celda $h(k)$ está ocupada, se prueba una secuencia de celdas alternativas.

**Sondeo lineal:** se prueban $h(k), h(k)+1, h(k)+2, \dots$ (módulo $m$) hasta encontrar una libre. Es como una "lista ligada sin punteros".

![Sondeo lineal - inserción de 29](adjuntos/Sondeo%20lineal%20-%20inserci%C3%B3n%20de%2029.png)

> [!example]- Transcripción de la imagen
> "Al insertar la llave 29 seguimos la misma idea del sondeo lineal": su valor de hash es $h(29) = 29 \bmod 7 = 1$. La tabla tiene 15 en la celda 1, 37 en la 2 y 51 en la 3. Se prueba la celda 1 (ocupada), la 2 (ocupada) y la 3 (ocupada), y el 29 queda en la 4, la primera libre.

Sus problemas son dos. Las llaves se **amontonan** en bloques contiguos, y cuanto más llena está la tabla, más largas son las búsquedas. Además, **eliminar** es delicado: si se vacía una celda en medio de un bloque, las búsquedas que pasaban por ella se cortan antes de tiempo. Se puede resolver (con marcas de "borrado", por ejemplo), pero agrega casos. Por eso el sondeo lineal **no se recomienda si hay que eliminar**.

**Variantes que reducen el amontonamiento:**

- **Sondeo cuadrático:** se prueban $H, H+1, H+4, H+9, \dots$ (saltos $j^2$).
- **Doble hashing:** se usa una segunda función de hash para el tamaño del salto: $h_1(k),\ h_1(k) + h_2(k),\ h_1(k) + 2h_2(k), \dots$ Dos llaves que colisionan en $h_1$ siguen secuencias distintas. **No hay que confundirlo con rehashing.**

```python
def doble_hashing(llaves, m=7):
    T = [None] * m
    for k in llaves:
        h1, h2 = k % m, 1 + k % (m - 1)      # h2 nunca es 0
        j = 0
        while T[(h1 + j * h2) % m] is not None: j += 1
        T[(h1 + j * h2) % m] = k
    return T

print(doble_hashing([15, 37, 51, 29]))     # [29, 15, 37, None, None, None, 51]
```

Con sondeo lineal, las mismas llaves quedan seguidas en las celdas 1 a 4. Con doble hashing quedan repartidas.

## Preguntas de repaso

> [!question]- ¿Por qué en encadenamiento se inserta en la cabeza de la lista?
> Porque insertar en la cabeza es $O(1)$ sin recorrer la lista. Comprobar si la llave ya existía sí obliga a recorrerla, pero se espera que las listas sean cortas.

> [!question]- ¿Por qué eliminar es problemático en el sondeo lineal?
> Porque las búsquedas avanzan hasta encontrar una celda vacía. Si se vacía una celda en medio de un bloque, una búsqueda posterior se detendría ahí y no encontraría llaves que están más adelante.

> [!question]- ¿Qué ventaja tiene el doble hashing sobre el sondeo lineal?
> Que dos llaves con el mismo $h_1$ normalmente tienen distinto $h_2$, así que siguen secuencias de prueba distintas y no se forman bloques contiguos.

> [!question]- Con $m = 7$ y sondeo lineal, insertando 15, 37, 51 y 29, ¿dónde queda el 29?
> $h(29) = 1$, pero las celdas 1, 2 y 3 ya tienen 15, 37 y 51, así que queda en la 4.
