---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Complejidad algorítmica"
tags:
  - algoritmos/complejidad
  - algoritmos/analisis
  - origen/complemento
prerrequisitos:
  - "[[05 - Asignación de bloques en disco|Asignación de bloques en disco]]"
---

# Contar operaciones

Para comparar dos algoritmos no basta con mirar el reloj: el tiempo real depende del computador, del lenguaje y de lo que esté corriendo. La idea de la **complejidad algorítmica** es medir el trabajo contando operaciones básicas en función del tamaño de la entrada, y estudiar cómo crece ese trabajo cuando la entrada se hace más grande.

## Qué se cuenta

Se llaman **operaciones básicas** a las acciones que el algoritmo repite: comparaciones, sumas, asignaciones, accesos a una posición de una lista. El **tamaño de la entrada** $n$ es la cantidad de datos que recibe el algoritmo, por ejemplo el largo de una lista.

La pregunta no es "¿cuántos segundos tarda?", sino "¿cuántas operaciones hace cuando la entrada tiene tamaño $n$?".

## Ejemplos

Un algoritmo con operaciones fijas:

```python
def f(a):
    b = a * 42
    c = a // 50
    d = b + c
    return d
```

Hace siempre la misma cantidad de operaciones, sin importar el valor de `a`. Su costo es **constante**: $O(1)$.

Un ciclo con una cantidad fija de vueltas:

```python
def g():
    s = 0
    for i in range(10):
        s += i
    return s
```

Hace 10 iteraciones siempre. Aunque sea un ciclo, el costo sigue siendo constante: $O(1)$.

Un ciclo que depende de la entrada:

```python
def h(n):
    s = 0
    for i in range(n):
        s += i
    return s
```

Hace $n$ iteraciones. Su costo es **lineal**: $O(n)$.

Lo mismo pasa con una búsqueda:

```python
def buscar(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False
```

En el peor caso recorre toda la lista: $n$ comparaciones, $O(n)$.

> [!tip] La idea central
> Lo que importa es cómo crece el número de operaciones cuando crece $n$. Un ciclo de 10 vueltas es constante; un ciclo de $n$ vueltas es lineal.

> [!warning] Un ciclo no siempre es lineal
> `for i in range(10)` es constante porque siempre son 10 vueltas. `for i in range(n)` es lineal porque las vueltas dependen de la entrada.

## Preguntas de repaso

> [!question]- ¿Por qué no se mide el tiempo en segundos?
> Porque depende del computador, del lenguaje y de la carga de la máquina. Contar operaciones en función de $n$ permite comparar algoritmos de forma independiente del hardware.

> [!question]- ¿Cuál es el costo de un algoritmo que hace 10 operaciones sin importar la entrada?
> $O(1)$, constante. El número de operaciones no crece con $n$.

> [!question]- ¿Cuál es el costo de recorrer una lista de largo $n$ una vez?
> $O(n)$, lineal: el trabajo crece proporcionalmente al tamaño de la lista.

> [!question]- Si un algoritmo hace dos ciclos separados de $n$ vueltas, ¿su costo es $O(2n)$ o $O(n)$?
> Es $O(n)$. Las constantes se ignoran en la notación asintótica; lo que importa es que crece de forma lineal.
