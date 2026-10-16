---
ramo: "Estructuras de Datos"
tema: "Programación dinámica"
tags:
  - edd
  - programacion-dinamica
  - cambio-de-monedas
  - origen/complemento
prerrequisitos:
  - "[[02 - Memoización y versión iterativa]]"
---

# Problema del vuelto con programación dinámica

Hay que dar $S$ pesos de vuelto con el **menor número de monedas**, con valores $\{v_1, \dots, v_n\}$ y una cantidad **ilimitada** de cada uno. El criterio codicioso ("la moneda más grande posible") funciona con {10, 5, 2, 1}, pero [[02 - Mochila fraccional y contraejemplos|falla con {6, 4, 1}]]: para 8 da 6 + 1 + 1 en vez de 4 + 4. La programación dinámica lo resuelve para **cualquier** conjunto de valores.

> [!warning] Qué se optimiza
> Aquí se minimiza la **cantidad de monedas**, no su valor; el valor total es fijo ($S$). En las charlas se maximizaba una **suma de valores**. Las recurrencias se parecen, pero no hay que confundir qué cuenta la función.

## La recurrencia

Sea $Z(T, k)$ el menor número de monedas para totalizar $T$ usando solo las primeras $k$ denominaciones. Respecto de la moneda $v_k$ hay dos opciones:

- **Se usa** al menos una moneda de valor $v_k$: queda por pagar $T - v_k$, y como hay monedas ilimitadas, todavía se pueden usar las $k$ denominaciones: $Z(T - v_k, k) + 1$.
- **No se usa:** $Z(T, k - 1)$.

$$Z(T, k) = \min\{\,Z(T - v_k,\ k) + 1,\ \ Z(T,\ k-1)\,\}$$

con casos base $Z(0, k) = 0$ (vuelto cero, cero monedas) y $Z(T, 0) = +\infty$ si $T > 0$ (sin monedas no se puede pagar).

> [!tip] Monedas ilimitadas frente a limitadas
> En la opción "se usa" la recurrencia se queda en $k$ y no pasa a $k-1$: eso permite repetir la moneda. Si cada moneda pudiera usarse **una sola vez**, ese término sería $Z(T - v_k, k - 1) + 1$, y se obtendría la recurrencia de una mochila 0/1.

## Algoritmo iterativo

![Algoritmo iterativo Change](adjuntos/Algoritmo%20iterativo%20Change.png)

> [!example]- Transcripción de la imagen
> "Ejercicio. Con esto, podemos plantear el siguiente algoritmo iterativo". `Change(S)`: `for T = 1, …, S: Z[T][0] ← +∞`; `for k = 0, …, n: Z[0][k] ← 0`; `for k = 1, …, n: for T = 1, …, S: Z[T][k] ← Z[T][k − 1]; if T − v_k ≥ 0: Z[T][k] ← min{Z[T][k], Z[T − v_k, k]}`.

En la última línea falta sumar la moneda usada: debe ser $\min\{Z[T][k],\ Z[T - v_k][k] + 1\}$, consistente con la recurrencia.

```python
def vuelto(S, monedas):
    INF, n = float("inf"), len(monedas)
    Z = [[0] * (n + 1) for _ in range(S + 1)]          # Z[0][k] = 0
    for T in range(1, S + 1):
        Z[T][0] = INF                                  # sin monedas no se puede
    for k in range(1, n + 1):
        for T in range(1, S + 1):
            Z[T][k] = Z[T][k - 1]                      # sin usar la moneda k
            if T - monedas[k - 1] >= 0:                # usando una moneda k más
                Z[T][k] = min(Z[T][k], Z[T - monedas[k - 1]][k] + 1)
    return Z[S][n]

print(vuelto(8, [6, 4, 1]))          # 2  (4 + 4)
print(vuelto(68, [100, 50, 10, 1]))  # 10 (50 + 10 + 8 x 1)
```

La tabla tiene $(S + 1) \times (n + 1)$ celdas y cada una se llena en $O(1)$: el costo es $O(S \cdot n)$ en tiempo y memoria.

> [!example] Variantes para practicar
> - Cantidad **limitada** de monedas de cada valor: hay que llevar en el estado cuántas se usaron, o tratar cada moneda física como un ítem distinto (0/1).
> - Dar el **mejor vuelto posible** cuando faltan denominaciones y no se puede llegar exacto a $S$.

## Preguntas de repaso

> [!question]- ¿Por qué en la recurrencia el término "se usa $v_k$" es $Z(T - v_k, k) + 1$ y no $Z(T - v_k, k - 1) + 1$?
> Porque las monedas son ilimitadas: después de usar una de valor $v_k$ se puede volver a usar otra igual, así que la denominación $k$ sigue disponible.

> [!question]- ¿Qué significan los casos base $Z(0, k) = 0$ y $Z(T, 0) = +\infty$?
> Que un vuelto de 0 no necesita monedas, y que sin denominaciones disponibles no se puede pagar un monto positivo (infinito marca imposible para el `min`).

> [!question]- ¿Cuál es la complejidad del algoritmo Change?
> $O(S \cdot n)$, porque llena una tabla de $S + 1$ por $n + 1$ con trabajo constante por celda.

> [!question]- ¿Qué cambia si cada moneda se puede usar una sola vez?
> El término de uso pasa a $Z(T - v_k, k - 1) + 1$: después de usar la moneda $k$, ya no está disponible. Es la estructura de la mochila 0/1.
