---
ramo: "Estructuras de Datos"
tema: "Análisis de algoritmos"
tags:
  - edd
  - induccion
  - demostraciones
  - recursion
  - origen/complemento
prerrequisitos: []
---

# Inducción simple, fuerte y estructural

Casi todas las demostraciones del curso, sobre todo las de correctitud de algoritmos, son por **inducción**. La razón es que los algoritmos avanzan paso a paso o se llaman a sí mismos, y la inducción es justamente la herramienta para probar que algo vale "en cada paso". Por eso todo lo que se demuestra por inducción se puede programar de forma recursiva, y al revés.

## El principio y su receta práctica

> [!tip] Principio de inducción simple
> Si $P(0)$ es verdadera y, para todo $n$, $P(n)$ implica $P(n+1)$, entonces $P(n)$ es verdadera para todo $n \in \mathbb{N}$.

En la práctica, una demostración tiene tres partes:

1. **Caso base (CB):** se identifica el primer valor $n_0$ y se verifica que cumple $P$.
2. **Hipótesis inductiva (HI):** se supone que $P(n)$ es cierta para un $n$ cualquiera.
3. **Tesis o paso inductivo (TI):** se demuestra $P(n+1)$ *usando* $P(n)$.

Si las tres partes se completan, $P$ es cierta para todo $n \ge n_0$. El caso base suele ser trivial; el trabajo real está en el paso inductivo, que es donde hay que usar la hipótesis.

> [!warning] Detalles que hacen caer una demostración
> - La propiedad puede valer recién desde un $n_0 \neq 0$; en algoritmos el caso base típico es "un arreglo de 1 elemento".
> - Puede haber **varios casos base**. Si el paso inductivo necesita mirar dos valores anteriores (por ejemplo, un algoritmo que trabaja con dos listas), un solo caso base no alcanza. Conviene elegir el caso base más intuitivo y verificar que efectivamente se cumple.

## Tres variantes

| Variante | Se asume | Se demuestra | Uso típico |
|---|---|---|---|
| **Simple** | $P(n)$ | $P(n+1)$ | Algoritmos iterativos que avanzan de a un elemento |
| **Fuerte** | $P(k)$ para **todo** $k < m$ | $P(m)$ | Dividir para conquistar: la mitad de un problema es "algún $k$ menor", no necesariamente $m-1$ |
| **Estructural** | $P$ para los elementos base y para las partes de una estructura | $P$ para lo que construye la regla de avance | Listas ligadas, árboles: definiciones recursivas |

La inducción estructural no recorre números sino **estructuras definidas recursivamente**. Una lista ligada es la lista vacía o un nodo que apunta a otra lista. Para probar algo sobre todas las listas, se prueba para la vacía y se muestra que, si vale para la lista $k$, también vale para el nodo que apunta a $k$.

## Inducción y recursión son lo mismo

El caso base de la inducción es el caso base de la recursión: tiene que existir para que el algoritmo se detenga. El paso inductivo es la llamada recursiva, que confía en que el problema más chico ya está resuelto.

```python
def suma(n):
    """Suma 1 + 2 + ... + n. La recursión calca la inducción."""
    if n == 1:                 # caso base: P(1)
        return 1
    return suma(n - 1) + n     # usa P(n-1) para obtener P(n)

class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor, self.siguiente = valor, siguiente

def largo(lista):
    """Inducción estructural: lista vacía (None) o un nodo seguido de otra lista."""
    if lista is None:          # elemento base
        return 0
    return 1 + largo(lista.siguiente)   # regla de construcción

print(all(suma(n) == n * (n + 1) // 2 for n in range(1, 500)))  # True
print(largo(Nodo(1, Nodo(5, Nodo(3, Nodo(10))))))               # 4
```

La fórmula $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ se prueba exactamente como corre `suma`. El CB es $1 = \frac{1 \cdot 2}{2}$. En el TI, $\frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}$, y ahí se usa la HI en el primer sumando.

> [!warning] Una recursión sin caso base no es gratis
> Hay un caso documentado ("The story of how one little recursive function took down an entire business") de una función recursiva sin caso base que corrió dos horas en Google Cloud y costó US$ 71.383,86. El caso base no es un trámite de la demostración: es lo que hace que el programa termine.

## Preguntas de repaso

> [!question]- ¿Por qué en el paso inductivo hay que usar la hipótesis inductiva?
> Porque la HI es lo único que conecta $P(n)$ con $P(n+1)$. Si la demostración de $P(n+1)$ no la usa, o se demostró $P(n+1)$ directamente (y la inducción sobraba) o hay un error en el razonamiento.

> [!question]- ¿Cuándo conviene la inducción fuerte en vez de la simple?
> Cuando el paso para $m$ depende de un caso menor que no es necesariamente $m-1$. Pasa en dividir para conquistar: para justificar un problema de tamaño $m$ se usan subproblemas de tamaño $m/2$, y la HI fuerte cubre cualquier $k < m$.

> [!question]- ¿Qué se demuestra en el caso base y en el paso de una inducción estructural sobre listas ligadas?
> En el caso base, que la propiedad vale para la lista vacía (o un solo nodo). En el paso, que si vale para una lista $k$, también vale para la lista que se forma agregando un nodo que apunta a $k$.

> [!question]- ¿Qué relación hay entre el caso base de una inducción y el de una función recursiva?
> Son el mismo concepto. En la demostración, el caso base ancla la cadena de implicancias; en el programa, es la condición que detiene las llamadas. Sin él, la recursión no termina.
