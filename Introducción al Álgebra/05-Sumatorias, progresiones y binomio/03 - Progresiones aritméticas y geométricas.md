---
ramo: "Introducción al Álgebra"
tema: "Sumatorias, progresiones y binomio"
tags:
  - intro-algebra/sumatorias-binomio
  - origen/complemento
prerrequisitos:
  - "[[01 - Sumatorias y sus propiedades]]"
  - "[[02 - Sumas telescópicas]]"
---

# Progresiones aritméticas y geométricas

Son las dos sucesiones más simples: en una se **suma** siempre lo mismo para pasar al término siguiente, en la otra se **multiplica** siempre por lo mismo. Ambas tienen fórmula para el término general y para la suma de sus primeros $n$ términos.

## Progresión aritmética (PA)

Una sucesión es aritmética si $a_{k+1} - a_k = d$ es constante; $d$ es la **diferencia**.

> [!tip] Progresión aritmética
> $$a_n = a_1 + (n-1)d, \qquad \sum_{k=1}^{n} a_k = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}\big(2a_1 + (n-1)d\big).$$

La suma es "número de términos por el promedio del primero y el último". Sale de separar: $\sum_{k=1}^{n} [a_1 + (k-1)d] = n a_1 + d \cdot \frac{(n-1)n}{2}$.

**Ejemplo.** Si los dos primeros términos son $-7$ y $-3$, entonces $d = 4$ y $a_{101} = -7 + 100 \cdot 4 = 393$.

## Progresión geométrica (PG)

Una sucesión es geométrica si $\frac{a_{k+1}}{a_k} = r$ es constante; $r$ es la **razón**.

> [!tip] Progresión geométrica
> $$a_n = a_1\, r^{n-1}, \qquad \sum_{k=1}^{n} a_k = a_1 \cdot \frac{1 - r^n}{1 - r} \quad (r \neq 1).$$

La suma se obtiene restando: si $S_n = a_1 + a_1 r + \dots + a_1 r^{n-1}$, entonces $r S_n - S_n = a_1 r^n - a_1$, porque todos los términos intermedios se cancelan (es una telescópica).

**Ejemplo.** Si $a_2 = -24$ y $a_5 = 81$, dividir elimina $a_1$: $\frac{a_1 r^4}{a_1 r} = r^3 = -\frac{27}{8}$, así que $r = -\frac{3}{2}$ y $a_1 = \frac{-24}{r} = 16$. Luego $a_n = 16\left(-\frac{3}{2}\right)^{n-1}$.

> [!warning] Fórmulas con distinto punto de partida
> $\sum_{k=0}^{n} r^k = \frac{1 - r^{n+1}}{1 - r}$ tiene $n + 1$ términos, mientras que $\sum_{k=1}^{n} a_1 r^{k-1}$ tiene $n$. Antes de usar la fórmula hay que contar los términos y ver cuál es el primero. Para una suma desde $k = m$: $\sum_{k=m}^{n} r^k = \frac{r^m - r^{n+1}}{1 - r}$.

## Recuperar la sucesión desde sus sumas

Si se conoce $S_n = \sum_{k=1}^{n} a_k$ para todo $n$, cada término sale de una resta:
$$a_1 = S_1, \qquad a_n = S_n - S_{n-1} \quad (n \ge 2).$$

**Ejemplo.** Si $S_n = \frac{n(13 - 3n)}{2}$, entonces $a_1 = 5$ y, para $n \ge 2$, $a_n = S_n - S_{n-1} = 8 - 3n$, que también vale en $n = 1$. Como $a_{n+1} - a_n = -3$, la sucesión es aritmética de diferencia $-3$.

## Recurrencias que esconden una PG

Una recurrencia como $X_n = \frac{X_{n-1}}{2} + 100$ no es geométrica, pero al desarrollarla aparece una suma geométrica:
$$X_n = \frac{X_0}{2^n} + 100\left(1 + \frac{1}{2} + \dots + \frac{1}{2^{n-1}}\right) = \frac{X_0}{2^n} + 200\left(1 - \frac{1}{2^n}\right) = \frac{X_0 - 200}{2^n} + 200.$$

## Preguntas de repaso

> [!question]- ¿Cuánto vale $1 + 2 + 4 + \dots + 2^{9}$?
> PG con $a_1 = 1$, $r = 2$ y $10$ términos: $\frac{1 - 2^{10}}{1 - 2} = 1023$.

> [!question]- Si $a_5 = 17$ y $a_{12} = 45$ en una PA, ¿cuánto vale $d$?
> $a_{12} - a_5 = 7d = 28$, así que $d = 4$.

> [!question]- ¿Por qué la fórmula de la suma geométrica exige $r \neq 1$?
> Porque divide por $1 - r$. Si $r = 1$, todos los términos son $a_1$ y la suma es $n a_1$.

> [!question]- ¿Cómo se prueba que una sucesión es aritmética?
> Mostrando que $a_{n+1} - a_n$ es la misma constante para **todo** $n$, no solo para los primeros términos.
