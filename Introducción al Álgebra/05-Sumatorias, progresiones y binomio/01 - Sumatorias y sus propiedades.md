---
ramo: "Introducción al Álgebra"
tema: "Sumatorias, progresiones y binomio"
tags:
  - intro-algebra/sumatorias-binomio
  - origen/complemento
prerrequisitos:
  - "[[05 - Definiciones por inducción]]"
---

# Sumatorias y sus propiedades

La sumatoria $\sum_{k=1}^{n} a_k = a_1 + a_2 + \dots + a_n$ se definió por recurrencia: $\sum_{k=1}^{1} a_k = a_1$ y $\sum_{k=1}^{n+1} a_k = \sum_{k=1}^{n} a_k + a_{n+1}$. Con esa definición, y por inducción, se prueban unas pocas reglas que permiten **calcular** sumas sin sumar término a término: separar, sacar constantes, cambiar el índice y usar unas cuantas sumas conocidas.

## Reglas básicas

> [!tip] Propiedades de la sumatoria
> Para sucesiones $(a_k)$, $(b_k)$ y una constante $r$:
> - $\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k$.
> - $\sum_{k=1}^{n} r\,a_k = r \sum_{k=1}^{n} a_k$.
> - $\sum_{k=1}^{n} r = n\,r$ (sumar $n$ veces la constante).
> - El índice es **mudo**: $\sum_{k=1}^{n} a_k = \sum_{i=1}^{n} a_i$.

> [!warning] Lo que no se puede hacer
> La sumatoria **no** se distribuye sobre productos ni cocientes: $\sum a_k b_k \neq \left(\sum a_k\right)\left(\sum b_k\right)$ y $\sum \frac{1}{a_k} \neq \frac{1}{\sum a_k}$. Tampoco $\sum r = r$: la constante se suma $n$ veces.

## Sumas conocidas

Estas se prueban por inducción y se usan como "tabla":

> [!tip] Sumas que hay que saber
> $$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}, \qquad \sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}, \qquad \sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2,$$
> $$\sum_{k=0}^{n} r^k = \frac{1 - r^{n+1}}{1 - r} \quad (r \neq 1).$$

**Ejemplo.** $\sum_{k=1}^{10} 2k(k+1) = 2\sum_{k=1}^{10} k^2 + 2\sum_{k=1}^{10} k = 2 \cdot \frac{10 \cdot 11 \cdot 21}{6} + 2 \cdot \frac{10 \cdot 11}{2} = 770 + 110 = 880$.

## Sumas que no parten en 1

Si la suma empieza en $m > 1$, se escribe como diferencia de dos sumas que parten en 1:
$$\sum_{k=m}^{n} a_k = \sum_{k=1}^{n} a_k - \sum_{k=1}^{m-1} a_k.$$

**Ejemplo.** $\sum_{k=5}^{25} k(k-5) = \sum_{k=1}^{25} (k^2 - 5k) - \sum_{k=1}^{4} (k^2 - 5k) = (5525 - 1625) - (30 - 50) = 3920$.

## Traslación del índice

Sumar $p$ al índice y restarlo en los límites no cambia la suma:
$$\sum_{k=m}^{n} a_k = \sum_{k=m+p}^{n+p} a_{k-p}.$$
Sirve para dejar el término general en una forma conocida. Por ejemplo, con $j = k - 2$:
$$\sum_{k=23}^{111} (k-2)^2 = \sum_{j=21}^{109} j^2 = \sum_{j=1}^{109} j^2 - \sum_{j=1}^{20} j^2.$$

> [!warning] Al trasladar, cambian los dos límites
> Si el término pasa de $(k-2)$ a $j$, los límites pasan de $23$ y $111$ a $21$ y $109$. Cambiar solo uno de los dos es el error más común.

## Preguntas de repaso

> [!question]- Calcule $\sum_{k=1}^{20} 3$.
> $20 \cdot 3 = 60$. La constante se suma una vez por cada valor del índice.

> [!question]- ¿Cuánto vale $\sum_{k=1}^{n} (2k - 1)$?
> $2 \cdot \frac{n(n+1)}{2} - n = n^2$: la suma de los $n$ primeros impares es $n^2$.

> [!question]- ¿Cuántos términos tiene $\sum_{k=m}^{n} a_k$?
> $n - m + 1$. Por ejemplo, $\sum_{k=23}^{111}$ tiene $89$ términos.

> [!question]- Reescriba $\sum_{k=3}^{12} (k+1)^2$ con un índice que parta en $4$.
> Con $j = k + 1$: $\sum_{j=4}^{13} j^2$.
