---
ramo: "Estructuras de Datos"
tema: "Algoritmos codiciosos"
tags:
  - edd
  - greedy
  - mochila
  - contraejemplos
  - origen/complemento
prerrequisitos:
  - "[[01 - Estrategia codiciosa]]"
---

# Mochila fraccional y contraejemplos

El ejemplo central de la [[01 - Estrategia codiciosa|estrategia codiciosa]] es la **mochila con objetos fraccionables**. Sirve para ver que distintos criterios de selección dan resultados distintos y que solo uno llega al óptimo. La otra cara del tema es saber **demostrar que un criterio no funciona**, y para eso basta con un contraejemplo pequeño.

## El problema

![Problema de la mochila fraccional](adjuntos/Problema%20de%20la%20mochila%20fraccional.png)

> [!example]- Transcripción de la imagen
> "Considere el **problema de la mochila con objetos fraccionables**". Hay $n$ objetos y una mochila. Los objetos tienen pesos $\{w_1, \dots, w_n\}$ y ganancias por unidad de peso $\{p_1, \dots, p_n\}$; la mochila tiene una capacidad $m$, en peso; incluir una fracción $x_k$ del objeto $k$ proporciona ganancia $p_k x_k$.

![Mochila - función objetivo y restricciones](adjuntos/Mochila%20-%20funci%C3%B3n%20objetivo%20y%20restricciones.png)

> [!example]- Transcripción de la imagen
> Interesa llenar la mochila cumpliendo tres condiciones: maximizar la ganancia total $\sum_{k=1}^{n} p_k x_k$ (la **función objetivo**); no exceder la capacidad, $\sum_{k=1}^{n} w_k x_k \le m$; y que las fracciones cumplan $0 \le x_k \le 1$ para $1 \le k \le n$.

![Solución factible y solución óptima](adjuntos/Soluci%C3%B3n%20factible%20y%20soluci%C3%B3n%20%C3%B3ptima.png)

> [!example]- Transcripción de la imagen
> Las mismas tres condiciones en forma compacta. Una **solución factible** es $\{x_1, \dots, x_n\}$ que cumple las dos últimas condiciones. Una **solución óptima** es una solución factible que maximiza la función objetivo.

Como $p_k x_k$ es la ganancia de llevar la fracción $x_k$, en el ejemplo $p_k$ funciona como la ganancia del objeto **completo**.

## Tres criterios, tres resultados

![Estrategias codiciosas para la mochila](adjuntos/Estrategias%20codiciosas%20para%20la%20mochila.png)

> [!example]- Transcripción de la imagen
> Para el problema de la mochila se pueden considerar las siguientes estrategias codiciosas *para la etapa actual del algoritmo*: incluir el objeto con mayor ganancia, incluir el de menor peso, o incluir el que tenga mayor cociente ganancia/peso. "Normalmente, la mayoría de las estrategias no producen soluciones óptimas".

![Comparación de estrategias en una instancia](adjuntos/Comparaci%C3%B3n%20de%20estrategias%20en%20una%20instancia.png)

> [!example]- Transcripción de la imagen
> Instancia con $m = 20$ y $n = 3$: pesos $w_1 = 18$, $w_2 = 15$, $w_3 = 10$; ganancias $p_1 = 25$, $p_2 = 24$, $p_3 = 15$. Soluciones factibles: **mayor ganancia** $x = (1, 2/15, 0)$, peso 20, ganancia 28,2; **menor peso** $x = (0, 2/3, 1)$, peso 20, ganancia 31; **mayor ganancia/peso** $x = (0, 1, 1/2)$, peso 20, ganancia 31,5. "En este problema, el óptimo se encuentra privilegiando ganancia/peso".

```python
from fractions import Fraction as F

def mochila_fraccional(w, p, m, criterio):
    orden = sorted(range(len(w)), key=criterio, reverse=True)   # Select
    x, libre = [F(0)] * len(w), F(m)
    for k in orden:
        x[k] = min(F(1), libre / w[k])      # Feasible: lo que quepa del objeto
        libre -= x[k] * w[k]
    return x, sum(xk * pk for xk, pk in zip(x, p))

w, p = [18, 15, 10], [25, 24, 15]
print(mochila_fraccional(w, p, 20, lambda k: F(p[k], w[k])))   # x = (0, 1, 1/2), ganancia 63/2 = 31.5
```

Ordenar por **ganancia/peso** es óptimo en la mochila **fraccional**: cada unidad de capacidad se usa en el objeto que más rinde por unidad, y lo que no cabe se fracciona. En la mochila **0/1** (objetos enteros) el mismo criterio ya no garantiza el óptimo.

## Demostrar que un criterio falla

> [!tip] Contraejemplo mínimo
> Para mostrar que una estrategia codiciosa **no** es óptima basta con **una** instancia en que pierda contra otra solución. Conviene buscarla con $n$ chico (3 a 5 elementos) y pensando en el caso que confunde al criterio: lo más valioso o grande al principio o al final, o un primer paso que bloquea los siguientes.

**Vuelto con monedas.** El criterio "usar la moneda más grande posible" funciona con los valores chilenos {100, 50, 10, 1}, pero falla con {6, 4, 1}: para dar 8 elige 6 + 1 + 1 (3 monedas), cuando el óptimo es 4 + 4 (2 monedas). El mismo problema puede tener o no estrategia codiciosa según los **datos**.

**Selección de charlas.** Para asistir a la mayor **cantidad** de charlas que no se topen, elegir siempre la que **termina primero** es óptimo. Pero si cada charla tiene un **valor** y se quiere maximizar la suma, ese criterio puede fallar, y hace falta programación dinámica.

```python
def charlas(intervalos):
    elegidas, fin = [], float("-inf")
    for ini, f in sorted(intervalos, key=lambda t: t[1]):   # la que termina primero
        if ini >= fin: elegidas.append((ini, f)); fin = f
    return elegidas
```

## Preguntas de repaso

> [!question]- En la instancia del ejemplo, ¿por qué "mayor ganancia" obtiene solo 28,2?
> Porque mete entero el objeto 1 (ganancia 25), que pesa 18 y casi llena la mochila. Solo cabe 2/15 del objeto 2, aunque este rinde más por unidad de peso.

> [!question]- ¿Por qué ganancia/peso es el criterio óptimo en la mochila fraccional?
> Porque la capacidad es el recurso escaso, y ese criterio asigna cada unidad de peso al objeto que más ganancia da por unidad. Como se puede fraccionar, nunca queda espacio desperdiciado.

> [!question]- Mostrar que "la moneda más grande" no es óptimo para el vuelto con monedas {6, 4, 1}.
> Para $S = 8$ el criterio da 6 + 1 + 1 = 3 monedas, pero 4 + 4 = 2 monedas es mejor. Un contraejemplo basta.

> [!question]- ¿Cuál es la estrategia para encontrar un contraejemplo a un algoritmo codicioso?
> Entender qué privilegia el criterio y construir una instancia pequeña donde esa elección temprana impida algo mejor (por ejemplo, poner el elemento más valioso al final o hacer que el primer elegido bloquee a los demás).
