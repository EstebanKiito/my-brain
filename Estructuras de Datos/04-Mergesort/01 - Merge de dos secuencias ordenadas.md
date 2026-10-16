---
ramo: "Estructuras de Datos"
tema: "Mergesort"
tags:
  - edd
  - ordenamiento
  - merge
  - correctitud
  - origen/complemento
prerrequisitos:
  - "[[02 - Correctitud de algoritmos]]"
  - "[[04 - Búsqueda binaria y dividir para conquistar]]"
---

# Merge de dos secuencias ordenadas

**Merge** (mezcla) resuelve un problema mucho más fácil que ordenar: juntar **dos secuencias que ya están ordenadas** en una sola ordenada. Basta con comparar sus **cabezas** y sacar siempre la menor. Es la pieza de "combinar" que hace funcionar a mergesort.

## Algoritmo

```
input : secuencias ORDENADAS A y B
output: nueva secuencia ordenada C          // no es in place
Merge(A, B):
1   C <- secuencia vacía
2   sean a y b los primeros elementos de A y B
3   extraer de su secuencia el menor entre a y b
4   insertarlo al FINAL de C
5   si quedan elementos en A y en B, volver a la línea 2
6   concatenar a C la secuencia que aún tenga elementos
7   return C
```

```python
def merge(A, B):
    C, i, j = [], 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:            # <= : ante empate sale primero el de A (estable)
            C.append(A[i]); i += 1
        else:
            C.append(B[j]); j += 1
    return C + A[i:] + B[j:]        # lo que sobra ya está ordenado

print(merge([8, 20, 29, 40, 50, 60, 70, 82], [15, 32, 41, 65]))
# [8, 15, 20, 29, 32, 40, 41, 50, 60, 65, 70, 82]
```

![Merge tras la segunda y tercera iteración](adjuntos/Merge%20tras%20la%20segunda%20y%20tercera%20iteraci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Dos estados de merge entre $A$ = 8, 20, 29, 40, 50, 60, 70, 82 (lila) y $B$ = 15, 32, 41, 65 (amarillo), con la secuencia de salida $C$ a la derecha. "Estado luego de la segunda iteración": $C$ tiene 8 (de $A$) y 15 (de $B$); $a$ apunta a 20 y $b$ a 32. "Estado luego de la tercera iteración": como $20 < 32$, $C$ = 8, 15, 20 y $a$ avanzó a 29.

## Correctitud

**Termina.** En cada iteración se extrae un elemento de $A$ o de $B$ y se inserta en $C$, y cuando una se vacía se concatena la otra. Hay exactamente $n = |A| + |B|$ inserciones y menos de $n$ comparaciones.

**Cumple su propósito.** Se demuestra por inducción con la propiedad $P(n)$: *después de insertar el $n$-ésimo elemento en $C$, las secuencias $A$, $B$ y $C$ están ordenadas*.

- **CB:** tras la primera inserción, $C$ tiene un elemento (está ordenada), y $A$ y $B$ siguen ordenadas porque se les sacó su primer elemento.
- **TI:** el elemento $c_{n+1}$ es el menor entre las cabezas de $A$ y $B$ (o la cabeza de la única que queda).

![Demostración del propósito de merge](adjuntos/Demostraci%C3%B3n%20del%20prop%C3%B3sito%20de%20merge.png)

> [!example]- Transcripción de la imagen
> "Demostración (propósito)". Por H.I., la secuencia de origen de $c_{n+1}$ estaba ordenada antes de sacarlo; como $c_{n+1}$ era su mínimo (el primer elemento), sacarlo preserva el orden, y si la secuencia queda vacía también está ordenada. Por H.I., $c_1 \le \dots \le c_n$. Si $c_{n+1}$ fuera estrictamente menor que alguno de ellos, habría una contradicción: o $A$ o $B$ no estaban ordenadas (ya se probó que sí), o $c_{n+1}$ se habría extraído antes por el criterio de selección. Se concluye que $c_1 \le \dots \le c_n \le c_{n+1}$.

## Complejidad: memoria frente a tiempo

![Complejidad de merge con memoria adicional](adjuntos/Complejidad%20de%20merge%20con%20memoria%20adicional.png)

> [!example]- Transcripción de la imagen
> Implementación con una secuencia **adicional**, en dos fases. 1. Extracción desde $A$ y $B$: decidir quién sale comparando los menores, $\mathcal{O}(1)$, e insertar en $C$, $\mathcal{O}(1)$; se repite $\mathcal{O}(n)$ veces. 2. Reubicar la secuencia no vacía restante: sacar e insertar en $C$, $\mathcal{O}(1)$ cada uno, $\mathcal{O}(n)$ veces. "Usando $\mathcal{O}(n)$ memoria adicional, Merge es $\mathcal{O}(n)$".

![Complejidad de merge in place](adjuntos/Complejidad%20de%20merge%20in%20place.png)

> [!example]- Transcripción de la imagen
> Usando el espacio reservado para $A$ y $B$. 1. Extracción: comparar los menores, $\mathcal{O}(1)$, pero insertar el dato al comienzo cuesta $\mathcal{O}(n)$ (hay que correr los demás); se repite $\mathcal{O}(n)$ veces, total $\mathcal{O}(n^2)$. 2. Reubicar el resto: no hace falta, porque ya está en su posición. "Usando $\mathcal{O}(1)$ memoria adicional, Merge es $\mathcal{O}(n^2)$".

| Versión | Memoria adicional | Tiempo |
|---|---|---|
| Con secuencia auxiliar $C$ | $O(n)$ | $O(n)$ |
| In place (sobre el espacio de $A$ y $B$) | $O(1)$ | $O(n^2)$ |

> [!tip] El compromiso
> Merge es eficiente justamente porque **no** es in place: escribir en una secuencia nueva evita mover datos. La versión in place ahorra memoria, pero paga con tiempo cuadrático. Por eso mergesort usa la versión con memoria extra.

## Preguntas de repaso

> [!question]- ¿Por qué basta comparar las cabezas de A y B para saber cuál es el menor de todos los que quedan?
> Porque ambas están ordenadas: la cabeza de cada una es su mínimo, así que el menor de todos es el menor de las dos cabezas.

> [!question]- ¿Cuántas comparaciones hace merge como máximo con $|A| + |B| = n$?
> Menos de $n$ ($n - 1$ como máximo), porque cada comparación saca un elemento, y cuando una secuencia se vacía el resto se concatena sin comparar.

> [!question]- ¿Por qué el merge in place es $O(n^2)$?
> Porque insertar cada elemento en su lugar dentro del mismo arreglo obliga a correr los demás ($O(n)$), y eso ocurre $O(n)$ veces.

> [!question]- ¿Qué tiene que ver el `<=` del código con la estabilidad?
> Ante dos elementos iguales, saca primero el de $A$, que venía antes en la entrada. Así se conserva su orden relativo y mergesort resulta estable.
